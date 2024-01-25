#!/bin/python3  

  

   

#Programer: Chase Bennett  
#Program: Variables 
#Date: 1.11.24
  
  
quote = "ALL is fair in love and war."
  
print(quote)
  
print(quote.upper()) #Uppercase
print(quote.lower()) #Lowercase
print(quote.title()) #Title case
print(len(quote))    # length of charcters

name = "Chase" #String
age = 16 #int
gpa = 3.8 #float
print("\n")



print(int(age))
print(int(30.1)) # can only print whole number
print(int(gpa)) # takes a float and casts to an int, will not round


print("\nMy Name is " + name + " and I am " + str(age) + " with a gpa of " + str(gpa) + ".") # Concontenate variables while Casting int to str 





print("\nMy Name is", name, "and I am " + str(age) + " with a gpa of " + str(gpa) + ".")









