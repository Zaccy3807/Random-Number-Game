#Made By Isaac Yeoman
#Random number game
import random
medium = ['M', 'm', 'Medium', 'medium']
hard = ['H', 'h', 'Hard', 'hard']
easy = ['E', 'e', 'Easy', 'easy']
ansch = 1
gues = 0
#credits
print('-------------------------------------')
print('Welcome to the random number game!')
print('Made by Isaac Yeoman')
print('-------------------------------------')
diff = 1
#Difficulty Selection
print('What Difficulty Would you like to play?, (Hard/H), (Easy/E) or (Medium/M)')
while diff < 2:
    difficult = input('Difficulty: ')
    if difficult in medium:
         print('Difficulty set to medium.')
         ans = random.randint(0, 10000)
         print('The answer is between 0 and 10000')
         ansch = 1
         diff = 3

    elif difficult in hard:
         print('Difficulty set to hard.')
         ans = random.randint(0, 100000)
         print('The answer is between 0 and 100000')
         ansch = 1
         diff = 3

    elif difficult in easy:
         print('Difficulty set to easy.')
         ans = random.randint(0, 1000)
         print('The answer is between 0 and 1000')
         ansch = 1
         diff = 3

    elif difficult == 'DevTools:':
        print('DevTools: activated, game skipped')
        ansch = 10
        break

    else:
        print('Please enter a true difficulty option, perhaps you misspelled it?')

print('-------------------------------------')
#Main Game
print('Remember, only use numbers')
while ansch < 2:
    user_input = input('Guess the number: ')
    
    if int(user_input) == ans:
        print('You Guessed It!, The number was',ans)
        ansch = 10
        print('-------------------------------------')
        print('It took you', gues,'guesses to find the answer.')
    
    elif int(user_input) > ans:
        print('Lower')
        gues += 1
        print('---')

    elif int(user_input) < ans:
        print('Higher')
        gues += 1
        print('---')

input('Press enter to exit')