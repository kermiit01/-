from pprint import pprint
class Product:
    name = ''
    weight = 0.0
    category = ''
    def __init__(self,name,weight,category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
       return f" {self.name}, {self.weight} , {self.category}"

class Shop:
    __file_name = 'products.txt'
    products = ''
    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        print(products)
        file.close

    def add(self,*args):
        for arg in args:
            matrix_arg = []
            for i in str(arg).split(','):
                matrix_arg.append(i)
            file = open(self.__file_name, 'r')
            products = file.read()
            if matrix_arg[0] and matrix_arg[2] in products:
                matrix = [row.split(",") for row in products.split("\n")]
                for i in range(len(matrix)):
                    if matrix[i][0] == matrix_arg[0]:
                        matrix[i][1]= f" {float(matrix_arg[1])+float(matrix[i][1])}"
                        products =  '\n'.join(','.join(row) for row in matrix)
                        print(f'Продукт {matrix[i][0]} уже был в магазине, его общий вес теперь равен {matrix[i][1]}')
                file = open(self.__file_name, 'w')
                file.write(products)
            else:
                 file = open(self.__file_name, 'a')
                 file.write(f"{arg}\n")
            file.close




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())