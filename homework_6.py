class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:
    def live(self):
        return "Я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"


# 🔥 Гибриды

class GlowStreamer(Streamer, Mutant):

    def ultimate_content(self):
        return self.live() + " + " + self.superpower()


class ViralCyborg(TikToker, Mutant):

    def ultimate_content(self):
        return self.live() + " + " + self.superpower()


class DonateMage(Streamer, TikToker):

    def ultimate_content(self):
        return self.live() + " + " + self.viral()


if __name__ == "__main__":
    g = GlowStreamer()
    v = ViralCyborg()
    d = DonateMage()

    print("GlowStreamer MRO:", GlowStreamer.mro())
    print(g.live())
    print(g.ultimate_content())

    print()

    print("ViralCyborg MRO:", ViralCyborg.mro())
    print(v.live())
    print(v.ultimate_content())

    print()

    print("DonateMage MRO:", DonateMage.mro())
    print(d.live())
    print(d.ultimate_content())