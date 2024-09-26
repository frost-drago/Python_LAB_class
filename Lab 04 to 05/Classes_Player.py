class Player:
    def __init__ (self):
        self.inventory = {}
        self.money = 0
        self.health = 100

    def print_status(self):
        print(f"Health\t\t: {self.health}")
        print(f"Money\t\t: {self.money}")
        print("Inventory\t:")
        for item in self.inventory:
            print(f"\t - {item}\t: {self.inventory[item]}")

    def check_alive(self):
        if self.health <= 0:
            print("\nDEAD\n")
            self.money = 0
            self.inventory = []

    def gain_loot(self, gained_money = 0, gained_inventory = []):
        self.money += gained_money
        for item in gained_inventory:
            if item in self.inventory:
                self.inventory[item] += 1
            else:
                self.inventory[item] = 1
'''
Player_A = Player()
Player_A.print_status()
Player_A.health -= 999
Player_A.check_alive()
'''

Player_B = Player()
Player_B.gain_loot(120, ["Apple", "Apple", "Mana potion", "Random twig"])
Player_B.print_status()
Player_B.gain_loot(gained_inventory=["Apple", "Apple", "Apple", "Doctor"])
Player_B.print_status()
