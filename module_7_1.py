from pathlib import Path
class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        Path(self.__file_name).touch()
        file = open(self.__file_name, 'r')
        string = file.read()
        file.close()
        return string

    def add(self, *products):
        shop_string = self.get_products()
        products_to_add = []
        names_hash = []
        for i in [*products]:
            if \
                    (i.name not in shop_string) and\
                    (hash(i.name) not in names_hash):
                products_to_add.append(i)
                names_hash.append(hash(i.name))
            else:
                print(f'Продукт {i.name} уже есть в магазине')

        file = open(self.__file_name, 'a')
        for i in products_to_add:
            file.write(f'{i.name}, {i.weight}, {i.category}\n')
        file.close()






class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
        return

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())