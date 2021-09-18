from threading import Thread, Lock


class SingletonMeta(type):
    _instances = {}
    _lock = Lock()  # Lock object for synchronizing threads during the 1st access to singleton.

    def __call__(cls, *args, **kwargs):
        # Threads must reach here in the same time. The 1st one will acquire lock and proceed further,
        # while the rest will wait here.
        with cls._lock:
            # The 1st thread comes here, reaches the condition, goes inside and create singleton instance.
            # Once it leaves, another thread waiting for the lock to release may enter this section. But
            # singleton instance is already initialized, the thread won't create new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class LoggingSingleton(metaclass=SingletonMeta):
    """
    Logging class
    """
    pass


def test():
    logging_singleton = LoggingSingleton()  # Create a logging object
    print(logging_singleton)
    print(id(logging_singleton))


if __name__ == "__main__":
    p1 = Thread(target=test)  # Thread 1
    p2 = Thread(target=test)  # Thread 2
    p1.start()  # Start thread 1
    p2.start()  # Start thread 2
