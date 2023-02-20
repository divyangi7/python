''' create one class named "category" with members "name", "code", "no_of_products".'''
''' create one class named "product" with members "name", "code", "category", "name", "code", "category", "price".'''
''' create three objects of category.'''
''' create 10 different products.'''
''' code must be unique.'''
''' print category info with its no_of_product.'''
''' sort and print products based on price ( price high to low and low to high ) with all details. '''
''' search product using its code.'''



class category :
    def __init__(self, name, code, no_of_product):
        self.name = name
        self.code = code
        self.no_of_product = no_of_product

    def show_details(self):
        print("name  :", self.name)
        print("code  :", self.code)
        print("no of product :", self.no_of_product)

    def product_details_in_row(self):
        print("%-12s  %-12s %-10s %6d" % (self.name, self.code, self.category.name, self.price))

class product(category):
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        category.no_of_product = category.no_of_product + 1
        self.price = price



    def product_details(self):
        print("Product name is :", self.name)
        print("product code is :", self.code)
        print("product category is :", self.category.name)
        print("product price is :", self.price)





    def show_product_code():
        for i in p:
            if (search_code == i.code):
                i.product_details()

    def price_print_low_to_high():
        for i in range(len(p) - 1):
            for j in range(len(p) - 1 - i):
                if (p[j].price > p[j + 1].price):
                    t = p[j]
                    p[j] = p[j + 1]
                    p[j + 1] = t
        for i in range(len(p)):
            p[i].product_details_in_row()


    def price_print_high_to_low():
        for i in range(len(p) - 1):
            for j in range(len(p) - 1 - i):
                if (p[j].price > p[j + 1].price):
                    t = p[j]
                    p[j] = p[j + 1]
                    p[j + 1] = t

        for i in reversed(range(len(p))):
            p[i].product_details_in_row()

c1 = category('soap', '020', 0)
c2 = category('shampoo', '010', 0)
c3 = category('handwash','050', 0)

c_list = [c1, c2, c3]

p1 = product('dove',20,c1,60)
p2 = product('santoor',10,c1,50)
p3 = product('cinthol',30,c1,120)
p4 = product('pears',50,c1,65)
p5 = product('lux',90,c1,45)
p6 = product('tresemme',70,c2,250)
p7 = product('sunsilk',100,c2,200)
p8 = product('loreal',80,c2,350)
p9 = product('detol',40,c3,150)
p10 = product('santoor',60,c3,130)

p = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]



#print category info with its no_of_product
c1.show_details()
c2.show_details()
c3.show_details()





#sort and print products based on price
  #price high to low
print("--------------------------------------------")
print(" Sorting Price => high to low")
print(" Name          code         category    Price ")
print("----------------------------------------------")
print(product.price_print_high_to_low())


print(" Sorting Price => low to high")
print("----------------------------------------------")
print(" Name          code         category    Price ")
print("----------------------------------------------")
print(product.price_print_low_to_high())



#search product using its code
search_code = int(input("enter the code :"))
print(product.show_product_code())








