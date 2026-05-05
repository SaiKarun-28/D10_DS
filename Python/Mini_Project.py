class Product :
    def __init__(self,id,name,price,rating):
        self.id = id
        self.name = name
        self.price = price
        self.rating = rating

class User:
    def __init__(self):
        self.products = []
    
    # Functionalites.

    # Add Product.

    def add_product(self):
        id = int(input('Enter the Product ID :'))
        for product in self.products:
            if product.id == id:
               print('Product already exists....!')
               return
        
        name = input('Enter the Product name :')
        price = int(input('Enter the Product price :'))
        rating = float(input('Enter the Product rating :'))
        product = Product(id,name,price,rating)
        self.products.append(product)
        print('Product added sucessfully.....!')

    # Remove Product.

    def remove_product(self):
        if len(self.products) == 0:
           print('Products cannot be removed....!')
           return
    
        id = int(input('Enter the Product ID :'))
        for product in self.products :
            if product.id == id:
               self.products.remove(product)
               print('Product Removed Sucessfully....!')
               return
        print('No Product Avaliable.....!')
        return
    
    # Update Product.

    def update_product(self):
        if len(self.products) == 0:
           print('Cart is Empty....!')
           return
    
        id = int(input('Enter the product ID :'))
        for product in self.products:
            if product.id == id:
               while True :
                    print('Select 1 to Update Product Name')
                    print('Select 2 to Update Product Price')
                    print('Select 3 to Update Product Rating')
                    print('Select 4 to Update All ')
                    print('Select 5 to Update Product Name and Price')
                    print('Select 6 to Update Product Price and Rating')
                    print('Select 7 to Update Product Rating and Name')
                    print('Select 8 to Proceed with changes')
                
                    option = int(input("Enter the Option :"))
                    match option:
                        case 1:
                            new_name = input('Enter the Product Name :')
                            product.name = new_name
                            print('Sucessfully Changed Product Name....!')
                        case 2:
                            new_price = int(input('Enter the Product Price :'))
                            product.price = new_price
                            print('Sucessfully Changed the Product Price....!')
                        case 3:
                            new_rating = float(input('Enter the Product Rating :'))
                            product.rating = new_rating
                            print('Sucessfully Changed the Product Rating....!')
                        case 4:
                            new_name = input('Enter the Product Name :')
                            new_price = int(input('Enter the Product Price :'))
                            new_rating = float(input('Enter the Product Rating :'))
                            product.name,product.price,product.rating = new_name,new_price,new_rating
                            print('All Changes Updated Sucessfully....!')
                        case 5:
                            new_name = input('Enter the Product Name :')
                            new_price = int(input('Enter the Product Price :'))
                            product.name,product.price = new_name,new_price
                            print('Product Name and Price Changed Sucessfully....!')
                        case 6:
                            new_price = int(input('Enter the Product Price :'))
                            new_rating = float(input('Enter the Product Rating :'))
                            product.price,product.rating = new_price,new_rating
                            print('Product Price and Rating Updated Sucessfully....!')
                        case 7:
                            new_rating = float(input('Enter the Product Rating :'))
                            new_name = input('Enter the Product Name:')
                            product.rating,product.name = new_rating,new_name
                            print('Product Rating and Name Updated Sucessfully....!')
                        case 8:
                           print('Changes Saved Sucessfully in your Cart....!')
                           return
                        case _:
                           print('Enter Valid Option :')
        print("ID Doesn't exists....!")

    # Show Cart.

    def show_product(self):
        if len(self.products) == 0:
           print('Cart is Empty....!')
           return
    
        print('-'*40)
        print('|   ID   |   NAME    |    PRICE   |    RATING   |')
        print('-'*40)
        for product in self.products:
            print(f'|  {product.id}  |  {product.name}  |  {product.price}  |  {product.rating}  |')
        print('-'*40)

    # Search Product.

    def search_product(self):
        if len(self.products) == 0:
           print('Cart is Empty....!')
           return
       
        id = int(input('Enter the Product ID :'))
        for product in self.products:
            if product.id == id:
               print('-'*40)
               print('|   ID   |   NAME    |    PRICE   |    RATING   |')
               print('-'*40)
               print(f'|  {product.id}  |  {product.name}  |  {product.price}  |  {product.rating}  |')
               print('-'*40)
               return
        print("ID Doesn't exist....!")

    # Filter Prices.

    def filter_price(self):
        if len(self.products) == 0:
           print('Cannot Filter....!')
           return
        self.products.sort(key = lambda product:product.price,reverse = False)
        print('Products are filtered from Low to High Price....!')


    # Filter Ratings.

    def filter_rating(self):
        if len(self.products) == 0:
           print('Cannot Filter....!')
           return
        self.products.sort(key = lambda product:product.rating,reverse = True)
        print('Products are Filtered from High to Low Ratings....!')


# User interface
print("---------------> PRODUCT MANAGEMENT SYSTEM <--------------------")
user = User()

while True:
    print('Select 1 to Add Product.')
    print('Select 2 to Remove Product.')
    print('Select 3 to Update Product.')
    print('Select 4 to Show Product.')
    print('Select 5 to Search Product.')
    print('Select 6 to Filter Product Price.')
    print('Select 7 to Filter Product Rating.')
    print('Select 8 to Exit.')
    
    option = int(input('Enter the Option :'))
    match option:
        case 1: user.add_product()
        case 2: user.remove_product()
        case 3: user.update_product()
        case 4: user.show_product()
        case 5: user.search_product()
        case 6: user.filter_price()
        case 7: user.filter_rating()
        case 8: 
            print('THANK YOU')
            break
        case _:
            print('Enter Valid Option .')