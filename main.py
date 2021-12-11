#Hangman Game
#Using basic python syntax and coding principles: if/else, lists, strings, range and modules

#Importing from modules to be used in program
import os, platform
import random
from ascii_art import stages, logo
from words import word_list

#Variables and lists
chosen_word = random.choice(word_list) #stores a random word
word_length = len(chosen_word)         #stores length of word

end_of_game = False                          
lives = 6

display = [] #An empty list

#Clears screen
def clear():
  if platform.system() == 'Windows':
    os.system('cls')
  else:
    os.system('clear')

print(logo)  #Prints hangman logo
print("Welcome player! Let's get started.")

#Creates blanks in the list represented by underscores
for _ in range(word_length):
    display.append("_")

#Loops through game until condition becomes not False
while not end_of_game:
  guess = input("Guess a letter: ").lower()

  clear() 

  #Checks to see if the letter was already guessed.
  #Let's user know, but does not deduct from life
  if guess in display:
    print(f"You have already guessed the letter, {guess}.")

  #Checks guessed letter by comparing it to letters in chosen word
  for position in range(word_length):
    letter = chosen_word[position]
    #Assigns letter to display list according to its position
    if letter == guess:
        display[position] = letter
  
  #Checks to see if user is wrong and deducts 1 point from lives.
  if guess not in chosen_word:
      lives -= 1
      print(f"The letter {guess} is not in the word.")
      #Checks to see if lives is 0 and then ends game
      if lives == 0:
          end_of_game = True
          print("You lose.")

  #Joins all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Checks if user has gotten all letters.
  if "_" not in display:
      end_of_game = True
      print("You win.")

  #Prints graphics based on lives
  print(stages[lives])