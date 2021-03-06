RPG COMBAT KATA
by @SuuiGD

Description: http://www.slideshare.net/DanielOjedaLoisel/rpg-combat-kata

1. DOMAIN • For the scope of this kata, the player won’t be running around and doing stuff. The features implemented in each iteration will be limited to the framework that the game may use in the future. • It is centered on the characters combat skills which are basically damaging and healing. • You may fix a time limit for each iteration as a constraint.
2. PREPARATION (10 MIN) • Find a pair • Choose a language • Setup your environment
3. ITERATION 1 • Characters have: • Health, starting at 1000. • Level, starting at 1. • Characters are: • Dead or alive. • Characters can: • Deal damage. • Heal. • Conditions: • When the damage received is higher than the actual health, health drops to 0 and the character dies. • When the character is dead, he cannot be healed. • The character cannot be healed over 1000 health.
4. ITERATION 2 • The player can deal damage to his enemies, but not to himself. • The player can heal himself, but not his enemies. • The level now has an effect on the damage applied. • If the target is 5 or more levels above the player, the damage applied will be reduced by 50%. • If the target is 5 or more levels below the player, the damage applied will be boosted by 50%.
5. ITERATION 3 • The player has an attack range. • If he is a melee fighter, his range will be 2 meters. • If he is a ranged fighter, his range will be 20 meters. • When trying to deal damage, the player must be in range.
6. RETROSPECTIVE (10 MIN) • Are you keeping up with the requirements? • Do you feel good about your design, is it scalable and easily adapted to the new requirements that will be introduced in the last iterations? • Is everything tested and are you confident in your tests?
7. ITERATION 4 • We now have factions. • One player may join or leave one or more factions. • Players of the same faction are allies • They can’t damage each other • They can heal each other.
8. ITERATION 5 • Finally, the player can damage other things that are not characters (props). This means that he can attack a house, a tree or anything else that has some health. • Those things cannot heal nor be healed and cannot deal damage. • They belong to no faction, as they are neutral things. • You may setup a house starting with 2000 health.
9. FINAL RETROSPECTIVE • What problems did you encounter? • What have you learned? • Debate on the different ways to possibly solve the kata!

