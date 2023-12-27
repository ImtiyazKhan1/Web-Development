#Intro make a welcome input, welcoming the user and explaning the rules of the game.
rules = """
Welcome to general knowledge quiz game, 10 questions. 
Covering different topics from, geography, computing and more!
At the end of the quiz you'll recieve a score, Good Luck :) ! 

""" 
print(rules)

playing = input("Would you like to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :) ")
score = 0 

answer = input("What's the name of the river that runs through Egypt? ")
if answer.lower() == "river nile":
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')

answer = input("What's the highest mountain in the world? ")
if answer.lower() == "mount everest":
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')

answer = input("What are the names of the five oceans? ")
if answer.lower() == " pacific, atlantic, indian, arctic and southern":
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')

answer = input("The United States consists of how many states? ")
if answer.lower() == "50":
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')

answer = input("What is the most important unit of a computer? ")
if answer.lower() == "central processing unit":
    print('Correct!') 
    score += 1
else: 
    print('Incorrect!')

answer = input("Where is the coldest place on Earth? ")
if answer.lower() == "antarctica":
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')

answer = input("What does CPU mean? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')

answer = input("What does RAM mean? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')

answer = input("What is an array? ")
if answer.lower() == "a data structure which can hold a lot of data":
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')

answer = input("What is a User Interface? ")
if answer.lower() == "user behaviour with a product":
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")


