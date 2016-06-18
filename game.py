class Game:
    def deal_damage(self, attacker, receiver, amount, distance):
        if attacker == receiver:
            return
        if receiver.level - attacker.level >= 5:
            amount = amount / 2
        if attacker.level - receiver.level >= 5:
            amount = amount * 1.5
        receiver.deal_damage(amount)

    def heal_damage(self, healer, patient, amount):
        if healer == patient:
            patient.heal_damage(amount)
