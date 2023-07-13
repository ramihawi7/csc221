from random import randint

def playgame():
    answer= randint(1,1000)
    intro = print("OK, I've thought of a number between 1 and 1000")
    guess_count = 0
    guess = None
    while answer != guess:
        guess = input('Make a guess:')
        guess = int(guess)
        guess_count += 1
        if(guess > answer):
            print("That's too high")
        elif(guess < answer):
            print("That's too low")     
        else:
            print('That was my number. Well done!')
    print( "You took,",guess_count, 'guesses.')
playgame()

while True:
    anothergame = input('Would you like another game?')
    if(anothergame == 'yes'):
        playgame()
    elif(anothergame == 'no'):
        print('OK. Bye!')
        break       
    else:
        print('Invalid input. Enter Yes or No')
