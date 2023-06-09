# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
 return pet_shop["admin"]["total_cash"]
 
def add_or_remove_cash(pet_shop, cash):
   pet_shop["admin"]["total_cash"] += cash
   return get_total_cash

def get_pets_sold(pet_shop):
   return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, number):
   pet_shop["admin"]["pets_sold"] += number
   return get_pets_sold 

def get_stock_count(pet_shop):
   return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pets = []
    for pet in pet_shop["pets"]:
      if pet["breed"] == breed:
        pets.append(pet)
    return pets

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
      if pet["name"] == name:
         return pet
       
def remove_pet_by_name(pet_shop, name):
    pets = pet_shop["pets"]
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
           pets.remove(pet)
         
def add_pet_to_stock(pet_shop, new_pet):
    pets = pet_shop["pets"]
    pets.append(new_pet)

def get_customer_cash(customers):
   return (customers["cash"])

def remove_customer_cash(customer, amount):
   customer["cash"] -= amount
   
def get_customer_pet_count(customer):
   return len(customer["pets"])
   
def add_pet_to_customer(customer, new_pet):
   pets = customer["pets"] 
   pets.append(new_pet)
   

   
   
          
          

   
         
         




       

     

   
 
   

    
   
   
   
   



   





