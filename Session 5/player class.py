class Player:
    def __init__(self, inventory, money : int, health :int):
        self.inventory = inventory 
        self.money = money 
        self.health = health 
    
    def add_inventory(self, item : str, amount : int):
        new_item = {'Item' : item, 'amount': amount}
        for i in self.inventory:
            if i["Item"] == item:
                i['amount'] += amount
                print('Added',amount, item, "to inv")
                return
        
        self.inventory.append(new_item)
    
    def remove_inventory(self, item: str, amount : int ):
        for i in self.inventory:
            if i['Item'] == item:
                i['amount'] -= amount
                print ('Removed', amount, item, 'from Inventory')
                return
            if i["amount"] <= 0:
                self.inventory.remove(i)
                return 
        print('no such item exists in your inv')
    
    def get_money(self, money : int):
        self.money += money 
        print('Added', money, 'coins to your wallet.')
    
    def gain_health(self, health : int):
        self.health += health
        print('Total health:', self.health )
    
    def lose_health(self,health: int):
        self.health -= health
        print('Total health:', self.health)
        if self.health <= 0:
            print('u ded')
    
    




all = Player([{'Item':'Shield(s)', "amount":  3 },{'Item':'Potion(s)','amount': 3}],0,100)

all.add_inventory('Shield(s)', 2)
all.add_inventory('Sword(s)', 2)
print(all.inventory)

all.remove_inventory('Shield(s)',5)
all.remove_inventory('Shovel',2)

print(all.inventory)

all.get_money(500)
print('Money in wallet:', all.money, 'coins')

all.gain_health(23)

all.lose_health(126)