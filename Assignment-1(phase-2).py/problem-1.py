brands = ['adidas', 'nike', 'puma', 'reebok', 'bata', 'red chief']

def get_user_name():
    return input("Enter your name: ")

def get_name():
    return get_name

def brand(brand_name=None):
    name = get_user_name()
    
    if brand_name is None:
        brand_name = input('Enter a brand name: ')

    if brand_name.lower() in brands:
        print(f"Hi {name}, the brand you are looking for is available in our store.")
    else:
        print(f"Hi {name}, unfortunately the brand you are looking for is not available in our store.")

def get_tshirt(brand_name):
    print(f"Welcome to our store!")
    brand()

get_tshirt(get_name())