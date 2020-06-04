class AbstractCook:
    def __init__(self):
        self.food = ""
        self.drink = ""
        self.i = 0 
        self.j = 0 
    def add_food(self, numbers_f, price_f):
        self.i += numbers_f * price_f
    def add_drink(self, numbers_d, price_d):
        self.j += numbers_d * price_d
    def total(self):
        return self.food + ": " + str(self.i) + ", " + self.drink + ": " + str(self.j) + ", " + "Total" + ": " + str(self.i+self.j)

class JapaneseCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.food = "Sushi"
        self.drink = "Tea"

class RussianCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.food = "Dumplings"
        self.drink = "Compote"

class ItalianCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.food = "Pizza"
        self.drink = "Juice"

client_1 = JapaneseCook()
client_1.add_food(2, 30)
client_1.add_food(3, 15)
client_1.add_drink(2, 10)
assert type(client_1) == JapaneseCook



# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing

#     client_1 = JapaneseCook()
#     client_1.add_food(2, 30)
#     client_1.add_food(3, 15)
#     client_1.add_drink(2, 10)

#     client_2 = RussianCook()
#     client_2.add_food(1, 40)
#     client_2.add_food(2, 25)
#     client_2.add_drink(5, 20)

#     client_3 = ItalianCook()
#     client_3.add_food(2, 20)
#     client_3.add_food(2, 30)
#     client_3.add_drink(2, 10)

#     assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
#     assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
#     assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
#     print("Coding complete? Let's try tests!")