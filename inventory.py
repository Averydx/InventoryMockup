
class item:
    def __init__(self,weight,length,name): 
        self.weight = weight;
        self.length = length;
        self.name = name;

class inventory:
    def __init__(self):
        self.itemsList = [];

    def addItem(self,item):
        self.itemsList.append(item);

    def readInventory(self):
        for item_ in self.itemsList:
            print(item_.name)

class sword(item):
    def __init__(self, weight, length, name,shinyness,metal):
        super().__init__(weight, length, name)
        self.shinyness = shinyness;
        self.metal = metal;

def main():
    inv = inventory();
    item1 = sword(20,20,"sword of excalibur",12,"bronze");
    item2 = item(20,30,"butt");
    inv.addItem(item1);
    inv.addItem(item2);

    inv.readInventory();
    print(inv.itemsList[0].metal)


main();



