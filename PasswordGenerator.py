#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
options  = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
hard_password = "" 
for items in range(1,nr_letters + 1):
  choice1 = random.randint(0,51)
  password = password + letters[choice1]
for items in range(1,nr_symbols + 1):
  choice2 = random.randint(0,8)
  password = password + symbols[choice2]
for items in range(1,nr_numbers + 1):
  choice3 = random.randint(0,9)
  password = password + numbers[choice3]
print("Your easy password is: " + password)

#Hard Level - Order of characters randomised:
hard_password = ""
total_size = nr_letters + nr_symbols + nr_numbers
for choice in range(0,total_size):
  random_choice = random.randint(0,2)
  if random_choice == 0:
    hard_password = hard_password + options[random_choice][random.randint(0,53)]
  elif random_choice == 1:
    hard_password = hard_password + options[random_choice][random.randint(0,9)] 
  elif random_choice == 2:
    hard_password = hard_password + options[random_choice][random.randint(0,8)]
print("Your hard password is: " + hard_password)
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P