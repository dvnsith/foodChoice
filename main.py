#!/usr/bin/env python3
def foodChoice():                                                                                                               
    menu = {                                                                                                              
            "American" : {                                                                                                
                       "beef": "Hamburger and fries",                                                                        
                       "chicken": "Wings and beer",                                                                          
                       "pork": "Ribs and beans",                                                                             
                       "plant": "no plant-based food found",                                                                 
                       "seafood": "lobster sandwhich and chips"                                                              
                  },                                                                                                        
             "Thai": {                                                                                                     
                      "beef": "Basil Beef",                                                                                 
                      "chicken": "Coconut curry chicken",                                                                   
                      "pork": "Grilled pork skewers",                                                                       
                      "plant": "Stir-fried veggies",                                                                        
                      "seafood": "Garlic prawns"                                                                            
                  },                                                                                                        
             "Italian": {                                                                                                   
                      "beef": "Spaghetti and beef meatballs",                                                               
                      "chicken": "Parmesan chicken alfredo",                                                                
                      "pork": "Porchetta",                                                                                  
                      "plant": "Pizza margherita",                                                                          
                      "seafood": "Cioppino"                                                                                 
                  }                                                                                                         
             }
    isHungry = 0
    hungry = input("Are you hungry? ").strip().capitalize()
  
    if(hungry == "Y" or hungry == "Yes"):
        isHungry = 1
  
    while(isHungry):
        food = input("Choose a food category (American, Thai, or Italian): ").strip().capitalize()
        protein = input("Choose protein - beef, chicken, pork, seafood, or plant: ").strip().lower()
        if(food == "American" or food == "Thai" or food == "Italian"):
            if(protein == "beef" or protein == "pork" or protein == "chicken" or protein == "seafood" or protein == "plant"):
                 print(menu[food][protein])
             else:
                 print("Enter valid protein")
         else:
             print("Enter a food category")
         isHungry = 0
 
def main():
    foodChoice()
main()  
