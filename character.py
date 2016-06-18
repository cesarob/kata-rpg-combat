class Character:
    MAX_HEALTH = 1000
    MIN_LEVEL = 1
    MIN_HEALTH = 0

    def __init__(self, level=MIN_LEVEL):
        self.health = self.MAX_HEALTH
        self.level = level

    def alive(self):
        return self.health > self.MIN_HEALTH

    def deal_damage(self, amount):
        if amount > self.health:
            self.health = self.MIN_HEALTH
        else:
            self.health -= amount

    def heal_damage(self, amount):
        if not self.alive():
            return

        if self.health + amount > self.MAX_HEALTH:
            self.health = self.MAX_HEALTH
        else:
            self.health += amount
