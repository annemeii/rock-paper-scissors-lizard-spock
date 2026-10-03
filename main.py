import random

print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================")
print("")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")

player = int(input("Pick a number: "))
computer = random.randint(1, 5)

while player < 1 or player > 5:
  print("You can only choose between 1 and 5 dummy!")
  player = int(input("Pick a number: "))

if computer == 1:
  print("CPU chose :✊")
elif computer == 2:
  print("CPU chose :✋")
elif computer == 3:
  print("CPU chose :✌️")
elif computer == 4:
  print("CPU chose :🦎")
else:
  print("CPU chose :🖖")

if player == 1:
  print("You chose: ✊")
elif player == 2:
  print("You chose :✋")
elif player == 3:
  print("You chose :✌️")
elif player == 4:
  print("You chose :🦎")
else:
  print("You chose :🖖")

if player == 1 and  computer == 3 or player == 1 and computer == 4:
  print("The player won !")
elif player == 2 and computer == 1 or player == 2 and computer == 5:
  print("The player won!")
elif player == 3 and computer == 2 or player ==  3 and computer == 4:
  print("The player won!")
elif player == 4 and computer == 5 or player == 4 and computer == 2:
  print("The player won!")
elif player == 5 and computer == 3 or player == 5 and computer == 1:
  print("The player won!")
elif player == computer:
  print("Draw.")
else :
  print("CPU won!")

# Bonus inside the bonus : a little rematch system !

rematch = input("Play again?")
while rematch == "Yes":
 player = int(input("Pick a number: "))
 computer = random.randint(1, 5)

 while player < 1 or player > 5:
   print("You can only choose between 1 and 5 dummy!")
   player = int(input("Pick a number: "))

 if computer == 1:
   print("CPU chose :✊")
 elif computer == 2:
   print("CPU chose :✋")
 elif computer == 3:
   print("CPU chose :✌️")
 elif computer == 4:
   print("CPU chose :🦎")
 else:
   print("CPU chose :🖖")


 if player == 1:
   print("You chose: ✊")
 elif player == 2:
   print("You chose :✋")
 elif player == 3:
   print("You chose :✌️")
 elif player == 4:
   print("You chose :🦎")
 else:
   print("You chose :🖖")

 if player == 1 and  computer == 3 or player == 1 and computer == 4:
   print("The player won !")
 elif player == 2 and computer == 1 or player == 2 and computer == 5:
   print("The player won!")
 elif player == 3 and computer == 2 or player ==  3 and computer == 4:
   print("The player won!")
 elif player == 4 and computer == 5 or player == 4 and computer == 2:
   print("The player won!")
 elif player == 5 and computer == 3 or player == 5 and computer == 1:
   print("The player won!")
 elif player == computer:
   print("Draw.")
 else :
   print("CPU won!")
 rematch = input("Play again? ")
