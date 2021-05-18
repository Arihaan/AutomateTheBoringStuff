# code (Display inventory function) from previous exercise:
def display_inventory(inventory):
    print("Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))
# ends here


def add_to_inventory(inventory, items_added):
    for item in items_added:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
