class Magazin:

    def __init__(self):
        self.prod = [{'name': 'Молоко','price': 20, 'count': 5},{'name': 'Хлеб','price': 30, 'count': 2}]
        self.kol = 0
        self.sum_pok = 0

    def buy(self, name):
        for nam in self.prod:
            if name == nam['name']:
                summa = nam['price']
                if nam['count'] <= 0:
                    print('Товар закончился')

                else:
                    nam['count'] -= 1
                    self.kol +=1
                    self.sum_pok += summa
                    print(f'Вы купили {name}, сумма покупки = {summa}')
                break
        else:
            print('Такого товара нет')

    def add(self, name, price, count):
        add = {'name': name, 'price': price, 'count': count}
        self.prod.append(add)

    def get_info(self):
        print(f'Общая сумма покупок {self.sum_pok}, количество покупок = {self.kol}')

    def  delete_product(self, name):
        for i, d in enumerate(self.prod):
            if d.get('name') == name:
                del self.prod[i]
                break

    def  add_product_count(self, name, count):
        for nam in self.prod:
            if name == nam['name']:
                nam['count'] += count
            else:
                print('Такого товара нет')




mag = Magazin()

mag.add('Груша', 50,3)
mag.add('Яблоко', 30,2)
mag.buy('Яблоко')
mag.buy('Груша')
mag.buy('Молоко')
mag.buy('Хлеб')
mag.delete_product('Хлеб')
mag.add_product_count('Яблоко', 10)
print(mag.prod)

mag.get_info()


