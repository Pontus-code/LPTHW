# Learning Python3 the Hard Way. Excercise 40. Modules, Classes and Objects.

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

I_love = Song(["I love the mountains",
                "I love the rolling hills",
                "I love the flowers",
                "I love the daffodils",
                "I love the fire side",
                "When the lights are low",])

my_bunny = ["My bunny is over the ocean",
            "My bunny is over the sea",
            "My bunny is over the ocean",
            "Please bring back my bunny to me"]

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

I_love.sing_me_a_song()

Song(my_bunny).sing_me_a_song()


