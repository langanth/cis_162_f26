"""Cat
Let's make a cat! I want you each to do the following

1. Think of a cat in your head

2. Discuss with a neighbor what your cat looks like

3. How are your cats similar?

4. How are your cats different?

5. Think about how you would represent a cat in code and discuss
that with your neighbor

"""

'''cats = {}
cats['Boba'] = {"Fur": 'Fluffy with white/gray coat', 
                "Eyes": 2,
                "Ears": 2,
                "Tail": True,
                "EyeColor": "Blue",
                "Polydactyl": False
}
print(cats)
print()
print(cats["Boba"])
print(cats["Boba"]["EyeColor"])'''


class Cat:

    def __init__(self, name, fur,eye_color, thumbs=False):
        self.name = name
        self.fur = fur
        self.eye_color = eye_color
        self.thumbs = thumbs
        self.legs = 4
        self.ears = 2
        self.tail = 1
        self.eyes = 2

    def get_legs(self):
        return self.legs

    def set_legs(self, val):
        if val < 0:
            return
        self.legs = val

    def pur(self):
        print(f'{self.name} goes brrrrrr')

    def eat(self, target):
        print(f'{self.name} sees {target}')
        print(f'{self.name} goes nom nom nom')
        print(f'{target} has now disappered')

    def __str__(self):
        return f'Name: {self.name}\nFur: {self.fur}\nEye Color:{self.eye_color}'
        #return f'{self.__class__.__name__}({self.name}, {self.fur}, {self.eye_color}, {self.thumbs})'

if __name__ == "__main__":
    marco = Cat("Marco", "Brown, white, gray", "Brown", True)
    print(marco.name)
    print(marco.tail)
    print(marco.legs)
    marco.legs -= 1
    print(marco.legs)
    print(marco.get_legs())
    marco.pur()
    marco.eat('bird')
    print(marco)