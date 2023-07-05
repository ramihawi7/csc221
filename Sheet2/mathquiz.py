from random import randint
numquestions=10
num_correct=0

for _  in range(numquestions):
    num1=randint(1,10)
    num2=randint(1,10)
    question= 'What is ' +  str(num1)  +  " times "  +  str(num2)+'?'
    print(question)
    numcorrect=0
    useranswer= input('Enter a Number:')
    useranswer= int(useranswer)
    correct= num1*num2
    if useranswer== correct:
        print(" That is right - Well done.")
        num_correct+=1
    else:
        print('No, I am afraid the answer is ' +str(correct) + '.')
    
print('I asked you 10 questions. You got ' + str(num_correct) +' of them correct.')
print('Well done!')