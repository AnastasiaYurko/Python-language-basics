class Cloth:
    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    def consumption_cloth_coat(self):
        return self.size / 6.5 + 0.5

    def consumption_cloth_suit(self):
        return self.growth * 2 + 0.3

    def consumption_cloth_together(self):
        return (self.size / 6.5 + 0.5) + (self.growth * 2 + 0.3)


class Coat(Cloth):
    def __init__(self, size, growth):
        super().__init__(size, growth)
        self.consumption_cloth_c = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто: {self.consumption_cloth_c}'


class Suit(Cloth):
    def __init__(self, size, growth):
        super().__init__(size, growth)
        self.consumption_cloth_s = round(self.growth * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм: {self.consumption_cloth_s}'


coat = Coat(46, 165)
suit = Suit(52, 190)
cloth = Cloth(48, 178)

print(coat.consumption_cloth_coat())
print(suit.consumption_cloth_suit())
print(cloth.consumption_cloth_together())




