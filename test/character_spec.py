from expects import *

from character import Character


with description("Character"):
    with before.each:
        self.character = Character()

    with context("when starting"):

        with it("has maximum health"):
            expect(self.character.health).to(equal(Character.MAX_HEALTH))

        with it("has initial level"):
            expect(self.character.level).to(equal(Character.MIN_LEVEL))

        with it("is alive"):
            expect(self.character.alive()).to(be_true)

    with context("when receiving damage"):
        with it("health decreases"):
            self.character.deal_damage(1)
            expect(self.character.health).to(equal(999))

        with it("loses health when damage greater than health"):
            self.character.deal_damage(Character.MAX_HEALTH + 1)
            expect(self.character.health).to(equal(Character.MIN_HEALTH))

        with it("dies when loses health"):
            self.character.deal_damage(Character.MAX_HEALTH + 1)
            expect(self.character.alive()).to(be_false)

        with it("cannot be healed if already dead"):
            self.character.deal_damage(Character.MAX_HEALTH + 1)

            self.character.heal_damage(Character.MAX_HEALTH)

            expect(self.character.alive()).to(be_false)

    with context("healing"):
        with it("heals damage"):
            self.character.deal_damage(1)
            self.character.heal_damage(1)
            expect(self.character.health).to(equal(Character.MAX_HEALTH))

        with it("cannot be healed over max"):
            self.character.deal_damage(10)

            self.character.heal_damage(20)

            expect(self.character.health).to(equal(Character.MAX_HEALTH))
