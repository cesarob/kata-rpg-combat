class Character:
    MAX_HEALTH = 1000
    MIN_LEVEL = 1
    MIN_HEALTH = 0
    MIN_ATTACK_RANGE = 2

    def __init__(self, level=MIN_LEVEL, attack_range=MIN_ATTACK_RANGE):
        self.health = self.MAX_HEALTH
        self.level = level
        self.attack_range = attack_range

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
