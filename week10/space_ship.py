from random import randint
from time import sleep

class SpaceShip:

    def __init__(self, name, health=100, shield=50, speed=50):
        self.name = name
        self.temp_health = health
        self.health = health
        self.shield = shield
        self.temp_shield = shield
        self.speed = speed

    def attack(self, target):
        attack_roll = randint(1, 100)
        if target.speed > attack_roll:
            print(f'The {self.name} attacked the {target.name} and missed')
        else:
            if target.shield > 0:
                atk = randint(10, 25)
                target.shield -= atk
                if target.shield < 0:
                    target.shield = 0
            else:
                atk = randint(10, 25)
                target.health -= atk
                print(f'The {self.name} dealt {atk} damage to the {target.name}')
                if target.health <= 0:
                    print(f'The {self.name} destroyed the {target.name}!')

    def __str__(self):
        st = f'{self.name}\nHealth {self.temp_health}/{self.health}\nShield: {self.temp_shield}/{self.shield}'
        return st

if __name__ == "__main__":
    xwing = SpaceShip('X-Wing', 100, 50)
    tiefighter = SpaceShip('Tie Fighter')
    print(xwing)
    print('***---===X===---***')
    print(tiefighter)
    turn = 0

    '''while True:
        if turn == 0:
            xwing.attack(tiefighter)
            turn += 1
            if tiefighter.health <= 0:
                print('Game Over!')
                break
        else:
            tiefighter.attack(xwing)
            turn -= 1
            if xwing.health <= 0:
                print('Game Over!')
                break
        print(xwing)
        print('***---===X===---***')
        print(tiefighter)
        sleep(randint(1, 3))'''