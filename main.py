#!/usr/bin/env python3
def main():                                                                                                               
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
              "Italian":{                                                                                                   
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
        if(food == "American"):
            if(protein == "beef"):
                print(menu["American"]["beef"])
            elif(protein == "pork"):
                print(menu["American"]["pork"])
            elif(protein == "chicken"):
                print(menu["American"]["chicken"])
            elif(protein == "seafood"):
                print(menu["American"]["seafood"])
            elif(protein == "plant"):
                print(menu["American"]["plant"])
            else:
                print("Enter valid protein")
        elif(food == "Thai"):
            if(protein == "beef"):
                print(menu["Thai"]["beef"])
            elif(protein == "pork"):
                print(menu["Thai"]["pork"])
            elif(protein == "chicken"):
                print(menu["Thai"]["chicken"])
            elif(protein == "seafood"):
                print(menu["Thai"]["seafood"])
            else:
                print("Enter valid protein")
        elif(food == "Italian"):
            if(protein == "beef"):
                print(menu["Italian"]["beef"])
            elif(protein == "pork"):
                print(menu["Italian"]["pork"])
            elif(protein == "chicken"):
                print(menu["Italian"]["chicken"])
            elif(protein == "seafood"):
                print(menu["Italian"]["seafood"])
            else:
                print("Enter valid protein")
        else:
            print("Enter a food category")
  
        isHungry = 0
 
main()  
