from abc import ABC, abstractmethod


class AudioFormat(ABC):  # existed ABC class (Target)
    @abstractmethod
    def play(self):
        pass


class MP3(AudioFormat):  # existed class (Target concrete)
    def play(self):
        return "I am playing mp3 format"


class ACC(AudioFormat):  # existed class (Target concrete)
    def play(self):
        return "I am playing acc format"


class AdvancedAudioFormat(ABC):  # existed ABC class (Adaptee)
    @abstractmethod
    def play_sound(self):
        pass


class WAV(AdvancedAudioFormat):  # existed class (Adaptee concrete)
    def play_sound(self):
        return "I am playing wav format"


class ALAC(AdvancedAudioFormat):  # existed class (Adaptee concrete)
    def play_sound(self):
        return "I am playing alac format"


class AudioFormatAdapter(AudioFormat):  # create Adapter class which inherits from AudioFormat class (Target)
    def __init__(self, adaptee_):
        self.__adaptee = adaptee_

    def play(self):
        return self.__adaptee.play_sound()


if __name__ == "__main__":
    mp3 = MP3()  # create mp3 audio format
    print(mp3.play())

    acc = ACC()  # create acc audio format
    print(acc.play())

    wav_adaptee = WAV()  # create wav as advanced audio format interface
    wav = AudioFormatAdapter(wav_adaptee)  # transform wav to audio format interface
    print(wav.play())

    alac_adaptee = ALAC()  # create alac as advanced audio format interface
    alac = AudioFormatAdapter(alac_adaptee)  # transform alac to audio format interface
    print(alac.play())
