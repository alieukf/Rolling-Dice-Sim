#random module
import random
print("Welcome to the dice Rolling Simulator!")
#one out of the 4 different dice functions
def diceroll6side():
  while True:
    #the min is one while the max is 6 because a regular dice has 6 sides
    numbers = [1, 2, 3, 4, 5, 6]
    answer = input("How many dice would you like to roll? (1,2,3): ")
    #this is the list that goes 1 through 3 because they have to choose how many dice they want to roll
    if answer in ('1', '2', '3'):
      if answer == '1':
        print ("Rolling Die...")
        #this will choose a random integer that is in between the minimum and maximum of this segment
        print(f"Your result is {(random.choice(numbers))}")
        break

      elif answer == '2':
        print ("Rolling 2 Dice...")
        #this will choose a random integer that is in between the minimum and maximum of this segment
        print(f"Your results are {(random.choice(numbers))} and {(random.choice(numbers))}")
        break

      elif answer == '3':
        print ("Rolling 3 Dice...")
        #this will choose a random integer that is in between the minimum and maximum of this segment
        print(f"Your results are {(random.choice(numbers))} and {(random.choice(numbers))} and {(random.choice(numbers))}")
        break

def diceroll8side():
  while True:
    #the min is one while the max is 6 because an 8 sided dice has 8 sides
    min = 1
    max = 8
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    answer = input("How many dice would you like to roll? (1,2,3): ")
    #this is the list that goes 1 through 3 because they have to choose how many dice they want to roll
    if answer in ('1', '2', '3'):
      if answer == '1':
        print ("Rolling Die...")
        #this will choose a random integer that is in between the minimum and maximum of this segment
        print(f"Your result is {(random.choice(numbers))}")
        break

      elif answer == '2':
        print ("Rolling 2 Dice...")
        #this will choose a random integer that is in between the minimum and maximum of this segment
        print(f"Your results are {(random.choice(numbers))} and {(random.choice(numbers))}")
        break

      elif answer == '3':
        print ("Rolling 3 Dice...")
        #this will choose a random integer that is in between the minimum and maximum of this segment
        print(f"Your results are {(random.choice(numbers))} and {(random.choice(numbers))} and {(random.choice(numbers))}")
        break

def diceroll10side():
  while True:
    #the min is one while the max is 10 because an 10 sided dice has 10 sides
    min = 1
    max = 10
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    answer = input("How many dice would you like to roll? (1,2,3): ")
    #this is the list that goes 1 through 3 because they have to choose how many dice they want to roll
    if answer in ('1', '2', '3'):
      if answer == '1':
        print ("Rolling Die...")
        #this will choose a random integer that is in between the minimum and maximum of this segment
        print(f"Your result is {(random.choice(numbers))}")
        break

      elif answer == '2':
        print ("Rolling 2 Dice...")
        #this will choose a random integer that is in between the minimum and maximum of this segment
        print(f"Your results are {(random.choice(numbers))} and {(random.choice(numbers))}")
        break

      elif answer == '3':
        print ("Rolling 3 Dice...")
        #this will choose a random integer that is in between the minimum and maximum of this segment
        print(f"Your results are {(random.choice(numbers))} and {(random.choice(numbers))} and {(random.choice(numbers))}")
        break

def diceroll12side():
  while True:
   #the min is one while the max is 12 because an 12 sided dice has 12 sides
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    answer = input("How many dice would you like to roll? (1,2,3): ")
    #this is the list that goes 1 through 3 because they have to choose how many dice they want to roll
    if answer in ('1', '2', '3'):
      if answer == '1':
        print ("Rolling Die...")
        #this will choose a random integer that is in between the minimum and maximum of this segment
        print(f"Your result is {(random.choice(numbers))}")
        break

      elif answer == '2':
        print ("Rolling 2 Dice...")
        #this will choose a random integer that is in between the minimum and maximum of this segment
        print(f"Your results are {(random.choice(numbers))} and {(random.choice(numbers))}")
        break

      elif answer == '3':
        print ("Rolling 3 Dice...")
        #this will choose a random integer that is in between the minimum and maximum of this segment
        print(f"Your results are {(random.choice(numbers))} and {(random.choice(numbers))} and {(random.choice(numbers))}")
        break

#this is the finction that will basically combine all the previous ones and ask the user which dice they want to roll and how many of each dice they want.
def whatdice():
  #this is the while true loop which will ask what dice they want
  while True:
    #main menu which shows the users options
    print("=== Choose a type of dice! ===")
    print("Faces/Sides - Shape")
    print("A: 6 - Cube")
    print("B: 8 - Octahedron")
    print("C: 10 - Pentagonal trapezohedron")
    print("D: 12 - Dodecahedron")
    choice = input("Choice >> ")
    #this list shows the options the user has that they can input
    if choice in ('A', 'a', 'B', 'b', 'C', 'c', 'D', 'd'):
      #as you can see dependng on the input that the user chose, it will call one of the previous functions that calls on a certian type of dice and how many of that dice.
      if choice == 'A':
        diceroll6side()
        break

      if choice == 'a':
        diceroll6side()
        break

      elif choice == 'B':
        diceroll8side()
        break

      elif choice == 'b':
        diceroll8side()
        break

      elif choice == 'C':
        diceroll10side()
        break

      elif choice == 'c':
        diceroll10side()
        break

      elif choice == 'D':
        diceroll12side()
        break

      elif choice == 'd':
        diceroll12side()
        break

  #this is the while true loop which will ask if they want to get more dice and roll again
  while True:
    answer2 = input("Would you like to roll again? (yes or no): ")
    if answer2 == "yes":
      whatdice()
      break
    elif answer2 == "no":
      print("Bye!")
      break

    else:
        print("That is not an option. Try Again!")
        continue

whatdice()