''' ● Add new data members “parent”, “display_name”, “products” (list of product objects) inside category class.'''
''' ● Add a new member function to generate “display_name”.'''
''' ● “display_name” has text value as below.
     Vehicle category without parent then “Vehicle” 
     Car category with “Vehicle” as parent then “Vehicle > Car”
     Petrol category with “Car” as parent then “Vehicle > Car > Petrol” .'''
'''● Create 5 category objects with parent and child relation.'''
''' ● Create 3 product objects in each category.'''
''' ● Display Category with its Code, Display Name and all product details inside that category.'''
''' ● Display product list by category ( group by category, order by category name).'''


class category :
    def show_display_name(self):

        if not self.parent:
            return self.name
        else:
            parent_display = self.parent.show_display_name()
            return parent_display +" > " + self.name

    def __init__(self, name, code, no_of_product, parent, product, display_name):
        self.name = name
        self.code = code
        self.no_of_product = no_of_product
        self.parent = parent
        self.product = []
        self.display_name = self.show_display_name()


    def show_details(self):
        print("name :", self.name)
        print("code :", self.code)
        print("no of product :", self.no_of_product)
        print("parent :", self.parent and self.parent.name or 'None')
        print("product :", self.product)
        print("display name :", self.display_name)

class product(category):
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        category.no_of_product = category.no_of_product + 1
        category.product.append(self)
        self.price = price


    def __repr__(self):

       return f'{"Product-name :", self.name, " | Price:", self.price, " | Code:" ,self.code, " | Category:" , self.category.name}'


    def sort_categories_by_name():
        for i in range(len(c_list)):
            for j in range(i + 1, len(c_list)):
                if c_list[i].name > c_list[j].name:
                    c_list[i], c_list[j] = c_list[j], c_list[i]
        for i in c_list:
            print("name :", i.name)
            for product in i.product:
                print("- " + product.__repr__())



    def product_details(self):
        print("Product name is :", self.name)
        print("product code is :", self.code)
        print("product category is :", self.category.name)
        print("product price is :", self.price)



c1 = category('vehicle','020',0 ,False,1,None )
c2 = category('car', '030', 0, c1,2, None )
c3 = category('petrol', '010', 0, c2, 3, None)
c4 = category('disel', '040', 0, c2, 4, None )
c5 = category('electric', '060', 0, c3, 5, None )
c_list = [c1, c2, c3, c4, c5]

p1 = product('bus', '100', c1, 6000)
p2 = product('airplane', '200', c1, 5000)
p3 = product('boat', '300', c1, 1200)
p4 = product('toyota', '500', c2, 6500)
p5 = product('audi', '900', c2, 4500)
p6 = product('volvo', '700', c2, 2500)
p7 = product('HP', '400', c3, 2000)
p8 = product('Reliance', '800', c3, 3500)
p9 = product('indian oil', '400', c3, 1500)
p10 = product('nitrogen', '600', c4, 1300)
p11 = product('oxygen', '1000', c4, 4800)
p12 = product('helium', '2000', c4, 6540)
p13 = product('clock', '3000', c5, 1200)
p14 = product('iron', '1200', c5, 4720)
p15 = product('oven', '450', c5, 7510)

p = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15]



print(product.sort_categories_by_name())
for c in c_list:
    c.show_details()





