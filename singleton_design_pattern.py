from threading import Thread, Lock


class SingletonMeta(type):
    __instances = {}
    __lock = Lock()  # Lock object for synchronizing threads during the 1st access to singleton.

    def __call__(cls, *args, **kwargs):
        # Threads must reach here in the same time. The 1st one will acquire lock and proceed further,
        # while the rest will wait here.
        with cls.__lock:
            # The 1st thread comes here, reaches the condition, goes inside and create singleton instance.
            # Once it leaves, another thread waiting for the lock to release may enter this section. But
            # singleton instance is already initialized, the thread won't create new object.
            if cls not in cls.__instances:
                instance = super().__call__(*args, **kwargs)
                cls.__instances[cls] = instance
        return cls.__instances[cls]


class RoundRobin(metaclass=SingletonMeta):
    def __init__(self):
        self.servers = []
        self.index = 0

    def add_server(self, server):
        self.servers.append(server)

    def get_next_server(self):
        num_server = len(self.servers)
        if not num_server:
            raise Exception('No available server')
        server = self.servers[self.index]
        self.index = (self.index + 1) % num_server

        return server

    @staticmethod
    def get_instance():
        return RoundRobin()


def main():
    load_balancer_1 = RoundRobin()
    load_balancer_2 = RoundRobin()
    load_balancer_3 = RoundRobin.get_instance()
    print(load_balancer_1 is load_balancer_2)
    print(load_balancer_1 is load_balancer_3)

    load_balancer_1.add_server('Server 1')
    load_balancer_1.add_server('Server 2')
    load_balancer_1.add_server('Server 3')
    print(load_balancer_1.get_next_server())
    print(load_balancer_1.get_next_server())
    print(load_balancer_1.get_next_server())
    print(load_balancer_1.get_next_server())
    print(load_balancer_1.get_next_server())


if __name__ == "__main__":
    p1 = Thread(target=main)
    p2 = Thread(target=main)
    p1.start()
    p2.start()
