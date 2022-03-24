
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
first = 0
second = 0
love_score_string = ""
names = name1.lower() + name2.lower()


for letter in names:
    first += letter.count("t")
    first += letter.count("r")
    first += letter.count("u")
    first += letter.count("e")

for letter in names:
    second += letter.count("l")
    second += letter.count("o")
    second += letter.count("v")
    second += letter.count("e")

love_score_string = str(first) + str(second)
love_score = int(love_score_string)


if(love_score < 10 or love_score > 90):
    print("Your score is " + love_score_string + ", you go together like coke and mentos.")
elif (40<love_score<50):
    print("Your score is " + love_score_string + ", you are alright together.")
else:
    print("Your score is " + love_score_string + ".")