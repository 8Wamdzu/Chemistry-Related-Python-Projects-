#aight so first we got all da imports 
#we only need to balance stoichiometry and print it out 
from chempy import balance_stoichiometry
from pprint import pprint

#This while loop lets da user enter their reactants, and puts
#it into a list
reactant_list = []

while True:
    reactants = input("Enter a reactant (press enter to finish): ")
    if reactants == "": 
     break
    reactant_list.append(reactants) 
#This while loop lets da user enter their products, and puts
#it into a list
product_list = []
while True:
   products = input("Enter a product (press enter to finish): ")
   if products == "":
       break
   product_list.append(products)

 #Now we gotta take both lists and apply the built in
 #balance_stoichiometry function to them
BalancedReactants, BalancedProducts = balance_stoichiometry(reactant_list, product_list)

#then its gonna print out the reactants and products, along with 
#the balanced coefficients
pprint(dict(BalancedReactants))
pprint(dict(BalancedProducts))

#thanks for watching make sure to like and subscribe and to hit that bell! 