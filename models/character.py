class Character:
    def __init__(self, name, house, strength, intelligence, charisma, defense):
        self.name = name
        self.house = house
        self.strength = max(1, strength)  # Ensure strength is at least 1
        self.intelligence = intelligence
        self.charisma = charisma
        self.defense = max(0, defense)  # Ensure defense is non-negative
        self._health = 100
        self.gold = 100
        self.inventory = Inventory()
        self.position = (0, 0)
        self.defending = False

    @property
    def speak_words(self):
        return f"{self.name} says: {self.house.words}"

    def move(self, direction):
        x, y = self.position
        if direction == 'north':
            self.position = (x-1, y)
        elif direction == 'south':
            self.position = (x+1, y)
        elif direction == 'east':
            self.position = (x, y+1)
        elif direction == 'west':
            self.position = (x, y-1)

    @property
    def total_stats(self):
        return self.strength + self.intelligence + self.charisma + self.defense

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value

    @health.deleter
    def health(self):
        del self._health

    @property
    def inventory_value(self):
        return self.inventory.get_total_value()

    def use_item(self, item_name):
        for item in self.inventory.items:
            if item.name == item_name:
                item.use(self)
                self.inventory.remove_item(item)
                return True
        print(f"{self.name} does not have {item_name}")
        return False


    def take_damage(self, amount):
        self.health = max(0, self.health - amount)


    def is_alive(self):
        return self.health > 0

    def spend_gold(self, amount):
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False

    def earn_gold(self, amount):
        self.gold += amount


class Warrior(Character):

    def __init__(self, name, house, strength, intelligence, charisma, defense):
        super().__init__(name, house, strength, intelligence, charisma, defense)
        self.strength += 10  # Warriors are stronger

    def attack(self):
        return f"{self.name} attacks with strength {self.strength}"


    def move(self, direction):
        super().move(direction)
        print(f"Warrior {self.name} moves {direction}")


class Diplomat(Character):
    def __init__(self, name, house, strength, intelligence, charisma, defense):
        super().__init__(name, house, strength, intelligence, charisma, defense)
        self.charisma += 10  # Diplomat are more intelligent

    def negotiate(self):
        return f"{self.name} negotiates with charisma {self.charisma}"

    def move(self, direction):
        super().move(direction)
        print(f"Diplomat {self.name} moves {direction}")


class Maester(Character):
    def __init__(self, name, house, strength, intelligence, charisma, defense):
        super().__init__(name, house, strength, intelligence, charisma, defense)
        self.intelligence += 10  # Maesters are more intelligent

    def heal(self):
        healing_power = self.intelligence * 0.5  # Healing power is based on intelligence
        return f"{self.name} heals for {healing_power} points."