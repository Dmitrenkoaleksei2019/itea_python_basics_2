from random import randint

max_card = int('21')
first_card = randint(2,11)
second_card = randint(2,11)
current_score = int(first_card + second_card)
y = str('yes')
n = str('no')
i = 0

start = input('Hello. Lets play?: yes/no: ')
while start == y:
    print('You have got two cards:')
    print(int(first_card))
    print(int(second_card))
    print(str('Your current score:') + str(current_score))
    break
    if start == str('no'):
        print('Have a Good Day. See you Soon')
    break
    if start and choise != y or n:
        print('Have a Good Day. See you Soon')
    break

choise = input('Do you want to pick a new card: yes/no: ')
while choise == y and start == y:
    new_card = randint(2,11)
    print('Your new card:', new_card)
    current_score = current_score + new_card
    print(str('Your current score:') + str(int(current_score)))
    if choise == str('no'):
        print('Have a Good Day. See you Soon')
        break
    if current_score > max_card:
        print('User lost.')
        break
    choise = input('Do you want to pick a new card: yes/no: ')
    if choise == n:
        print(str('Your game is over! Your score:') + str(int(current_score)))
        
while i < 2:
    first_bot_card = randint(2,11)
    second_bot_card = randint(2,11)
    current_bot_score = int(first_bot_card + second_bot_card)
    new_bot_card = randint(2,11)
    current_bot_score = current_bot_score + new_bot_card
    print(str('Bot current score:') + str(int(current_bot_score)))
    if current_bot_score <= max_card and current_bot_score > current_score:
        print('BOT WON. His score: ' + str(current_bot_score))
        break
    if current_score <= max_card and current_score > current_bot_score:  
        print('User WON. His score: ' + str(current_score))
        break
    elif current_bot_score <= max_card and current_bot_score > current_score:  
        print('BOT WON. His score: ' + str(current_bot_score))
        break
    elif current_bot_score > max_card and current_score > max_card:
        print('All of the players lost')
        break

