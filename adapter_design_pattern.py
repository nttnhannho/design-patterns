from abc import ABC, abstractmethod


class AudioFormat(ABC):
    """
    Target: AudioFormat ABC class (Existed)
    """
    @abstractmethod
    def play(self):
        pass


class MP3(AudioFormat):
    """
    Concreted MP3 class from Target (Existed)
    """
    def play(self):
        return "I am playing mp3 format"


class ACC(AudioFormat):
    """
    Concreted ACC class from Target (Existed)
    """
    def play(self):
        return "I am playing acc format"


class AdvancedAudioFormat(ABC):
    """
    Adaptee: AdvancedAudioFormat ABC class (Existed).
    """
    @abstractmethod
    def play_sound(self):
        pass


class WAV(AdvancedAudioFormat):
    """
    Concreted WAV class from Adaptee (Existed)
    """
    def play_sound(self):
        return "I am playing wav format"


class ALAC(AdvancedAudioFormat):
    """
    Concreted ALAC class from Adaptee (Existed)
    """
    def play_sound(self):
        return "I am playing alac format"


class AudioFormatAdapter(AudioFormat):
    """
    Adapter class which inherits from AudioFormat class (Target).
    This class is used to defined which adaptee (AdvancedAudioFormat) will be played by AudioFormat.
    """
    def __init__(self, adaptee_):
        self.__adaptee = adaptee_

    def play(self):
        return self.__adaptee.play_sound()


if __name__ == "__main__":
    mp3 = MP3()  # Create MP3 audio format
    print(mp3.play())

    acc = ACC()  # Create ACC audio format
    print(acc.play())

    wav_adaptee = WAV()  # Create WAV as advanced audio format interface
    wav = AudioFormatAdapter(wav_adaptee)  # Transform WAV to audio format interface
    print(wav.play())

    alac_adaptee = ALAC()  # Create ALAC as advanced audio format interface
    alac = AudioFormatAdapter(alac_adaptee)  # Transform ALAC to audio format interface
    print(alac.play())
