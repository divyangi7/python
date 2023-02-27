
'''Create one class named “location” with members “name”, “code”.'''
'''Create one class named “movement” with members “from_location”, “to_location”, “product”, “quantity”.'''
'''Create one static method named “movements_by_product” inside the “movement” class with one argument named “product”.
 This method will return all “movement” objects which belong to the passed “product” as an argument.'''
'''Add new members inside the product “stock_at_locations”. This new member is a type of Dictionary and it contains 
“location” as key and actual stock of that product on that location as value.'''
'''Create 4 different location objects.'''
'''Create 5 different product objects.'''
'''Move those 5 products from one location to another location using movement. Manage exceptions if product stock goes
 in -ve. '''
'''Display movements of each product using the “movement_by_product” method.'''
'''Display product details with its stock at various locations using “stock_at_locations”.'''
'''Display product list by location ( group by location).'''

#create class name location with members name and code
class location:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def show_location(self):
        print("name:", self.name)
        print("code:", self.code)

class product:

    def __init__(self, name, code, price,stock_at_location):
        self.name = name
        self.code = code
        self.price = price
        self.stock_at_location = {}

    def update_stock(self,location, stock):
        self.stock_at_location[location] = stock

    def product_details(self):
        print("name:", self.name)
        print("code:", self.code)
        print("price:", self.price)
        print("stock location:", self.stock_at_location)


#create class name movement with members from_location , to_location and product , quantity
class movement:
    movement = []

    def __init__(self,from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity

    def movement_details(self):
        print("from_location :", self.from_location)
        print("to_location :", self.to_location)
        print("product :", self.product)
        print("quantity:", self.quantity)

    @staticmethod
    def movements_by_product(product):
      return [movement for movement in m
            if movement.product ==product]

    @staticmethod
    def move_product(from_location, to_location, product, quantity):
        if from_location.stock_at_location[product] < quantity:
            raise ValueError("Not stock to move")
        from_location.stock_at_location[product] -= quantity
        to_location.stock_at_location[product] += quantity
        movement = Movement(from_location, to_loction, product, quantity)
        return movements

#create 4 different location object
l1 = location("rajkot","020")
l2 = location("junagadh", "030")
l3 = location("ahmedabad", "040")
l4 = location("vadodara", "010")
l = [l1, l2, l3, l4]

#create 5 different product objects
p1 = product("mobile", "001", 5000, {l1:1000})
p2 = product("TV", "002", 10000, {l2: 500})
p3 = product("laptop", "003", 14000, {l3:300})
p4 = product("oven", "004", 2500, {l4:200})
p5 = product("shoes", "005", 250, {l1:100})
p = [p1, p2, p3, p4, p5]


m1 = movement("rajkot","ahmedabad", "mobile", 100)
m2 = movement("vadodara", "rajkot","TV", 20)
m3 = movement("junagadh", "rajkot", "laptop", 30)
m4 = movement("ahmedabad", "vadodara", "oven", 15)
m5 = movement("rajkot", "junagadh", "shoes", 40)

m = [m1, m2, m3, m4, m5]

#display movement for each product
print(" -------Movement_by_product------- ")
for product in p:
    movements = movement.movements_by_product(product.name)
    if len(movements) == 0:
        print("No movements found for this product.")
    else:
        for movement in movements:
            movement.movement_details()
    print()


#'Display product details with its stock at various locations using “stock_at_locations
print("------- show product--------")
for product in p:
    print(f"product=>  name: {product.name} | price: {product.price} | code: {product.code} | stock_at_location : {product.stock_at_location}")
print()


#Display product list by location ( group by location).
print("------- Product List by Location -------")
for loc in l:
    print(f"Location: {loc.name} ")

