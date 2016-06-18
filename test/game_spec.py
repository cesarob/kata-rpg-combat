from expects import *

from character import Character


class Game:
    def deal_damage(self, attacker, receiver, amount):
        if attacker == receiver:
            return
        receiver.deal_damage(amount)

    def heal_damage(self, healer, patient, amount):
        if healer == patient:
            patient.heal_damage(amount)

with description("Game"):
    with before.each:
        self.a_character = Character()
        self.other_character = Character()
        self.game = Game()

    with context("damaging characters"):

        with it("a character damages another character"):
            actual_health = self.other_character.health
            self.game.deal_damage(self.a_character, self.other_character, 10)

            expect(self.other_character.health).to(be_below(actual_health))

        with it("cannot damage himself"):
            actual_health = self.a_character.health
            self.game.deal_damage(self.a_character, self.a_character, 10)

            expect(self.a_character.health).to(equal(actual_health))

    with context("healing characters"):
        with it("a character cannot heal another characters"):
            self.game.deal_damage(self.a_character, self.other_character, 10)
            actual_health = self.other_character.health

            self.game.heal_damage(self.a_character, self.other_character, 10)

            expect(self.other_character.health).to(equal(actual_health))

        with it("a character can heal himself"):
            actual_health = self.other_character.health
            self.game.deal_damage(self.a_character, self.other_character, 10)

            self.game.heal_damage(self.other_character, self.other_character, 10)

            expect(self.other_character.health).to(equal(actual_health))
