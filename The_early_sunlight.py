##########################################################
#Welcome to The early Sunlight! With this script you can order coffee   #
#and keep evil people like Ben and Dean out of your shop with if-else  #
#statements. Enjoy your coffee!        Oskar Craenen  -  RedAsh                #
#########################################################


import time
#import time module for delays

print("Hello and welcome to the Early Sunlight")

time.sleep(2)
#With this we have a delay of 2 sec

name = input("What is your name?\n")

if name == "Ben":
 print("You are NOT welcome her evil Ben!! GET OUT!!!")
 exit()
#Blocking evil Ben

if name == "Dean":
 print("You are NOT welcome her evil Dean!! GET OUT!!!")
 exit()
#Blocking evil Dean

if name == "admin":
  print("Welcome admin, you are in our membership and you get our coffees for FREE!")
 #Membership for true admins(little easteregg)!

menu = "Latte, Black coffee, Espresso, Cappuccino, Americano, Irish coffee or Iced coffee"
#Our menu of coffees

time.sleep(1)

order = input(name + ", What would you like from our menu today? Here is what we are serving.\n" + menu + "\n")

price = 8
#The price of 1 coffee, can be set to your liking

quantity = input("How many coffees would you like?\n")

total = price * int(quantity)
#Calculating our total pricetag

if name == "admin":
    print("Thank you, your total is: €0")
    #free membership
else:
    print("Thank you. Your total is: €" + str(total))

time.sleep(2)

if quantity >=  "0":
    print("\nSounds good " + name + ", we'll have your " + quantity + " " + order + "s  ready for you in a moment")
else:
    print("\nSounds good " + name + ", we'll have your " + quantity + " " + order + "  ready for you in a moment")
#Adding an "s" when quantity of the order is more than 1
    
time.sleep(5)
