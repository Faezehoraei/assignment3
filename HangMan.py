import random
animals=['Lion','Rabbit','Bear','Elephant','Ant','wolf','Bird','Giraffe']
word=random.choice(animals)
heart=7

while True:  
    user_true_char=[]
    user_char = input('\n Please enter a character: ')
    user_true_char.append(user_char)
    if char in user_true_char:
        print(char,end='')

    for char in word:
        print('_', end='')

    if user_char in word:
        print('✔')
    else:
        heart -=1
        print('❌')

        if heart >0:
            print(' YOU WIN😍')
        if heart==0:
            print('Game over😭')
            break

