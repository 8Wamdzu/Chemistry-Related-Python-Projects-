from chempy.util import periodic
from chempy import Substance
#aight so this part just asks the user to put in the formula 

formula = input("Please enter a chemical formula")
print(formula)

#This part uses the ChemPy library to find all the stats on the formula 
#entered like atomic number, symbol, mass and allat

formula2 = Substance.from_formula(formula)

#This part prints the mass of the compound in grams per mole
print(f"Molecular Weight: {formula2.mass:.3f} g/mol")

#Thanks for watching make sure to like and subscribe and hit that bell