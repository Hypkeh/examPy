#класс Pizza нужен чтобы был как меню для класса Restaurant
class Pizza:
    def __init__(self, name, composition, price, tag):
        self.name = name
        self.composition = composition
        self.price = price
        self.tag = tag
        
#tag это как айди, чтобы делать заказ по нему

pizzas = [Pizza('Pepperoni', 'Тесто, пепперони, сыр', 1300, '01'), Pizza('BBQ','Тесто, сыр, барбекю(наверное)', 1000, '02'), Pizza('Дары моря','Тесто, сыр, крабовые палочки, рыба(наверное)', 1200, '03')]
#список из пицц

class Restaurant:
    def __init__(self, pizza_from_menu):
        self.menu = pizza_from_menu
        self.__bill = 0
#принимает пиццы как меню
        

    def getMenu(self):
        for pizza in self.menu:
           print(f"Name: {pizza.name}({pizza.composition}). Price: {pizza.price}. Tag: {pizza.tag})")
#выводит меню, но используется print() потому, что return выводит только один раз в цикле


    def order(self, tag):
        for pizza in self.menu:
            if tag == pizza:
                self.__bill += pizza.price
                return 'Вы сделали заказ'
#Заказ и одновременно сохраняется счет
    def getBill(self):
        print(f"Bаш счет:{self.__bill}тг")       

    def setMenu(self, newMenu):
        self.menu = newMenu
#функция выбора заказа и рекурсия при желании повторить заказ


rest = Restaurant(pizzas)

rest.getMenu()

tag = int(input('Введите тег заказа: '))
rest.order(tag)

more = input('Хотите сделать еще заказ: ')
if more == "Yes":
    tag = int(input('Введите тег заказа: '))
    rest.order(tag)
    rest.getBill()
else:
    rest.getBill()











