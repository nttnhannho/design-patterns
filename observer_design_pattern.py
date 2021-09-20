from abc import ABC, abstractmethod


class Subject(ABC):
    """
    Subject for observers.
    Contains 3 default methods: attach, detach and notify observers.
    """
    @abstractmethod
    def attach(self, observer_):
        pass

    @abstractmethod
    def detach(self, observer_):
        pass

    @abstractmethod
    def notify(self):
        pass


class VideoSubject(Subject):
    """
    Video subject
    """
    __observers = []

    def attach(self, observer_):
        self.__observers.append(observer_)

    def detach(self, observer_):
        self.__observers.remove(observer_)

    def notify(self):
        for observer in self.__observers:
            observer.update()


class Observer(ABC):
    """
    Observer has 3 types: email, phone and facebook.
    """
    def __init__(self, subject_):
        self.__subject = subject_
        self.__subject.attach(self)

    @property
    def subject(self):
        return self.__subject

    @abstractmethod
    def update(self):
        pass


class VideoDataEmailNotifier(Observer):
    def update(self):
        if isinstance(self.subject, VideoData):
            print("To email:")
            print(f"{self.subject.title}\n{self.subject.description}")


class VideoDataPhoneNotifier(Observer):
    def update(self):
        if isinstance(self.subject, VideoData):
            print("To Phone:")
            print(f"{self.subject.title}\n{self.subject.description}")


class VideoDataFacebookNotifier(Observer):
    def update(self):
        if isinstance(self.subject, VideoData):
            print("To Facebook:")
            print(f"{self.subject.title}\n{self.subject.description}")


class VideoData(VideoSubject):
    """
    Video data class.
    """
    def __init__(self):
        self.__title = None
        self.__description = None

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value_):
        self.__title = value_

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value_):
        self.__description = value_

    def video_data_changed(self):
        self.notify()


if __name__ == "__main__":
    subject = VideoSubject()  # Create a video subject

    video_data = VideoData()  # Create a video data

    email = VideoDataEmailNotifier(video_data)  # Attach email notifier to video data
    phone = VideoDataPhoneNotifier(video_data)  # Attach phone notifier to video data

    video_data.title = "Video for Observer Design Pattern" # Change title
    video_data.description = "Observer is a good design pattern"  # Change description
    video_data.video_data_changed()  # Call video data changed to notify to all notifiers (email, phone).

    print("*** After detach phone notifier ***")
    subject.detach(phone)  # Detach phone notifier from video data
    video_data.title = "Video for Observer Design Pattern by Nhan"
    video_data.description = "Observer is a good design pattern, medium difficulty level"
    video_data.video_data_changed()  # Call video data changed to notify to all notifiers (email).

    print("*** After attach facebook notifier")
    facebook = VideoDataFacebookNotifier(video_data)  # Attach facebook notifier to video data
    video_data.video_data_changed()  # Call video data changed to notify to all notifiers (email, facebook).
