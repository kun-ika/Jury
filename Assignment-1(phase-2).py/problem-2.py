brands = ['adidas', 'nike', 'puma', 'reebok', 'bata', 'red chief']
available_sizes = ['28', '30', '32', '34']

def get_user_name():    
    return input("Enter your name: ")

def check_brand_availability(brand_name):    
    return brand_name.lower() in brands       

def display_brand_availability(brand_name):   
    if check_brand_availability(brand_name):
        print(f"The brand you are looking for is available in our store.")
    else:
        print(f"Unfortunately the brand you are looking is not available in our store.")

def get_tshirt(brand_name, n, size=None):  
    if size and size in available_sizes:
        print(f"Welcome to our store {n}")
    else:
        print(f"Invalid size. Available sizes are: {', '.join(available_sizes)}")
        return
    
    display_brand_availability(brand_name)

name = get_user_name()
brand_name = input('Enter a brand name: ')
tshirt_size = input('Enter the size of the t-shirt (28,30,32 & 34): ')
get_tshirt(brand_name, name, size=tshirt_size if tshirt_size else None)