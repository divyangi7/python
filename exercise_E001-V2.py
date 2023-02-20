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
    def __init__(self, name, code, no_of_product, parent, display_name, product):
        self.name = name
        self.code = code
        self.no_of_product = no_of_product
        self.parent = parent
        self.display_name = display_name
        self.product = product

    def show_details(self):
        print("name of category is :", self.name)
        print("code of category is :", self.code)
        print("no of product is :", self.no_of_product)
        print("parent is :", self.parent)
        print("display name is :", self.display_name)
        print("product is :", self.product)

    def display_name(self):
        pass


class product(category):
    def __init__(self,name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

c1 = category('vehicle','020',5 ,None,None)
c2 = category('car', '030', 5, None, None)
c3 = category('petrol','010', 5,None, None)
c4 = category('disel', '040', 5 , None, None)
c5 = category('electric', '060', 5 ,None, None)
c_list = [c1, c2, c3, c4, c5]

p1 = product()
p2 = product()
p3 = product()
p4 = product()
p5 = product()
p6 = product()
p7 = product()
p8 = product()
p9 = product()
p10 = product()
p11 = product()
p12 = product()
p13 = product()
p14 = product()
p15 = product()
p = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15]




