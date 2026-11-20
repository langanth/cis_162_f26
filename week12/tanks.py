from random import randint
from math import sqrt

class Tank:

    def __init__(self, name, health, atk_range=3, speed=1):
        pass

    def move_up(self, dist=1):
        pass

    def move_down(self, dist=1):
        pass

    def move_left(self, dist=1):
        pass

    def move_right(self, dist=1):
        pass

    def calculate_range(self, target):
        x1, y1 = self.location
        x2, y2 = target.location
        d = sqrt((x2-x1)**2 + (y2 - y1)**2)
        return d <= self.atk_range

    def attack(self, target):
        pass

def generate_tanks(num: int) -> list:
    tanks = []
    i = 0
    while i < num:
        try:
            name = input(f"Please enter player {i + 1}'s name: ")
            tanks.append(Tank(name, 50))
            i += 1
        except:
            continue
    return tanks

def print_locations(tanks):
    for i in tanks:
        print(i.name, i.location)

if __name__ == "__main__":
    ui = int(input("Enter in the number of players playing tank battle: "))
    tanks = generate_tanks(ui)
    print(tanks)
    names = [tank.name for tank in tanks]
    t = 0
    for i in tanks:
        i.location[0] = randint(0, 20)
        i.location[1] = randint(0, 20)
    while True:
        while t < len(tanks):
            done = False
            tidx = 0
            while tanks[t].moves < tanks[t].speed and not done:
                print_locations(tanks)
                choice = input(f"{tanks[t].name} do you want to attack, move, or are you done?(m or a or d)? ")
                if choice == 'a':
                    target = input("Enter the name of the player you want to attack: ")
                    if target in names:
                        tidx = names.index(target)
                        tanks[t].attack(tanks[tidx])
                        if tanks[tidx].temp_health <= 0:
                            print(f'{tanks[tidx].name} has been destroyed!')
                            tanks.pop(tidx)
                    else:
                        continue
                elif choice == 'm':
                    move_choice = input("Enter what direction you wish to move (u, d, l, r or q if you want to stop moving): ")
                    if move_choice.lower() == 'u':
                        distance = int(input(f"How many spaces do you want to move up? (must be less than or equal to {t.speed - t.moves})"))
                        t.move_up(distance)
                    elif move_choice.lower() == 'd':
                        distance = int(input(f"How many spaces do you want to move down? (must be less than or equal to {t.speed - t.moves})"))
                        t.move_down(distance)
                    elif move_choice.lower() == 'l':
                        distance = int(input(f"How many spaces do you want to move left? (must be less than or equal to {t.speed - t.moves})"))
                        t.move_left(distance)
                    elif move_choice.lower() == 'r':
                        distance = int(input(f"How many spaces do you want to move right? (must be less than or equal to {t.speed - t.moves})"))
                        t.move_right(distance)
                    elif move_choice == 'q':
                        break
                    else:
                        continue
                    t.moves += 1

                elif choice == 'd':
                    done = True
            t += 1
        t = 0
        for t in tanks:
            t.moves = 0
