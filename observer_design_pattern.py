from abc import ABC, abstractmethod


class Subject(ABC):
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
    __observers = []

    def attach(self, observer_):
        self.__observers.append(observer_)

    def detach(self, observer_):
        self.__observers.remove(observer_)

    def notify(self):
        for observer in self.__observers:
            observer.update()


class Observer(ABC):
    def __init__(self, subject_):
        self._subject = subject_
        self._subject.attach(self)

    @abstractmethod
    def update(self):
        pass


class VideoDataEmailNotifier(Observer):
    def update(self):
        if isinstance(self._subject, VideoData):
            print("To email:")
            print(f"{self._subject.title}\n{self._subject.description}")


class VideoDataPhoneNotifier(Observer):
    def update(self):
        if isinstance(self._subject, VideoData):
            print("To Phone:")
            print(f"{self._subject.title}\n{self._subject.description}")


class VideoDataFacebookNotifier(Observer):
    def update(self):
        if isinstance(self._subject, VideoData):
            print("To Facebook:")
            print(f"{self._subject.title}\n{self._subject.description}")


class VideoData(VideoSubject):
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
    subject = VideoSubject()

    video_data = VideoData()

    email = VideoDataEmailNotifier(video_data)
    phone = VideoDataPhoneNotifier(video_data)

    video_data.title = "Video for Observer Design Pattern"
    video_data.description = "Observer is a good design pattern"
    video_data.video_data_changed()

    print("*** After detach phone notifier ***")
    subject.detach(phone)
    video_data.title = "Video for Observer Design Pattern by Nhan"
    video_data.description = "Observer is a good design pattern, medium difficulty level"
    video_data.video_data_changed()

    print("*** After attach facebook notifier")
    facebook = VideoDataFacebookNotifier(video_data)
    video_data.video_data_changed()
