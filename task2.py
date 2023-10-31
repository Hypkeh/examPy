import random



def rock_paper_scissors(object):
    compObject = random.randint(1,3) 

#С помощью рандома определить будет камень ножницы или бумага
#1 = 'Rock'
#2 = 'Scissors'
#3 = 'Paper'
    acceptedObject = ['Rock','rock','Scissors','scissors','Paper','paper']
#Допустимые значения

    try:
        if object == 'rock' or object == 'Rock' and compObject == 1:
            return f" You: {object}\n Computer: Rock.\n It's draw"

        elif object == 'rock' or object == 'Rock' and compObject == 2:
            return f" You: {object}\n Computer: Scissors.\n You win"

        elif object == 'rock' or object == 'Rock' and compObject == 3:
            return f" You: {object}\n Computer: Paper.\n You lose"

        elif object == 'scissors' or object == 'Scissors' and compObject == 1:
            return f" You: {object}\n Computer: Rock.\n You lose"

        elif object == 'scissors' or object == 'Scissors' and compObject == 2:
            return f" You: {object}\n Computer: Scissors.\n It's draw"

        elif object == 'scissors' or object == 'Scissors' and compObject == 3:
            return f" You: {object}\n Computer: Paper.\n You win"

        elif object == 'Paper' or object == 'paper' and compObject == 1:
            return f" You: {object}\n Computer: Rock.\n You win"

        elif object == 'Paper' or object == 'paper' and compObject == 2:
            return f" You: {object}\n Computer: Scissors.\n You lose"

        elif object == 'Paper' or object == 'paper' and compObject == 3:
            return f" You: {object}\n Computer: Paper.\n It's draw"
        for i in acceptedObject:
            if i != object:
                return 'Нет такого значения'
    except:
        return "Something went wrong"
    

#Если введется не верное значение вывести сообщение
print("Let's start to play rock/paper/scissors")
obj = input('Enter rock/paper/scissors: ')
print(rock_paper_scissors(obj))




