from lab7.Exceptions import *


class Flower:
    __height = None
    __size = None
    __color = None
    __price = None
    __quantity = None
    __delivery_rate = None

    def get_height(self):
        return self.__height

    def get_size(self):
        return self.__size

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def get_delivery_rate(self):
        return self.__delivery_rate

    def set_height(self, value):
        self.__height = value

    def set_size(self, value):
        self.__size = value

    def set_color(self, value):
        self.__color = value

    def set_price(self, value):
        self.__price = value

    def set_quantity(self, value):
        self.__quantity = value

    def set_delivery_rate(self, value):
        self.__delivery_rate = value

    def __init__(self, height, size, color, price, quantity, delivery_rate):
        self.__height = height
        self.__size = size
        self.__color = color
        self.__price = price
        self.__quantity = quantity
        self.__delivery_rate = delivery_rate

    def __str__(self):
        return f"Flower: | Height:{self.get_height()} Price:{self.get_price()} Quantity:{self.get_quantity()}|"


class FlowerShop:
    def __init__(self):
        self.list_of_flowers_in_shop = []

    def add_flower_to_shop(self, flower):
        self.list_of_flowers_in_shop.append(flower)

    def top_most_expensive_flowers(self):
        sorted_list = sorted(self.list_of_flowers_in_shop, key=lambda flower: flower.get_price(), reverse=True)
        return sorted_list

    @logged(FlowerNotFoundException,"console")
    def delete_flower_from_shop(self, flower):
        if flower in self.list_of_flowers_in_shop:
            self.list_of_flowers_in_shop.remove(flower)
        else:
            raise FlowerNotFoundException("Flower not found")

    def __str__(self):
        return "\n".join(str(flower_from_flower_shop) for flower_from_flower_shop in self.list_of_flowers_in_shop)

class Bouquet:
    def __init__(self):
        self.flowers = []

    @logged(InvalidQuantityException,"file")
    def add_flower_to_bouquet(self, flower, quantity):
        if quantity <= 0:
            raise InvalidQuantityException("Invalid quantity. Quantity should be greater than zero")
        for _ in range(quantity):
            self.flowers.append(flower)

    def get_total_price(self):
        return sum(flower.get_price() for flower in self.flowers)

    def __str__(self):
        return f"Bouquet - Total Price: {self.get_total_price()}"


if __name__ == "__main__":
    rose = Flower(20, "Medium", "Red", 5.99, 10, 1)
    tulip = Flower(15, "Small", "Yellow", 3.99, 15, 0.5)
    lily = Flower(25, "Large", "White", 6.99, 8, 2)

    flower_shop = FlowerShop()
    flower_shop.add_flower_to_shop(rose)
    flower_shop.add_flower_to_shop(lily)
    flower_shop.delete_flower_from_shop(tulip)


    print("Flower Shop Inventory:")
    print(flower_shop)

    bouquet = Bouquet()
    bouquet.add_flower_to_bouquet(rose, -1)
    bouquet.add_flower_to_bouquet(tulip, 5)

    print(f"Bouquet Details: {bouquet}")

    top_expensive_flowers = flower_shop.top_most_expensive_flowers()
    print("Top Most Expensive Flowers in the Shop:")
    for i, flower in enumerate(top_expensive_flowers, start=1):
        print(f"{i}. {flower}")
