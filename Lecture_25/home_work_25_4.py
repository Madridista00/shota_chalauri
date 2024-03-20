# TODO შეცვალეთ იმპლემენტაცია, რადგან ყველა მოთამაშეს არ აქვს აუდიოს ან ვიდეოს მხარდაჭერა
# Interface Segregation Principle
# class MultimediaPlayer:
#     def play_audio(self):
#         pass
#     def play_video(self):
#         pass

from abc import ABC, abstractmethod

class PlayAudio(ABC):
    @abstractmethod
    def play_audio(self):
        pass

class PlayVideo(ABC):
    @abstractmethod
    def play_video(self):
        pass

class MultimediaPlayer1(PlayAudio):
    def play_audio(self):
        print("Can play audio only...")

class MultimediaPlayer2(PlayVideo):
    def play_video(self):
        print("Can play video only...")

class MultimediaPlayer3(PlayAudio, PlayVideo):
    def play_audio(self):
        print("Can play audio...")
    
    def play_video(self):
        print("Can play video...")

#=========================
multimedia_player_3 = MultimediaPlayer3()
multimedia_player_3.play_audio()
multimedia_player_3.play_video()