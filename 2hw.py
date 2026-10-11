####Q1
name = input("Please enter your name: ")

if name == "Bond":
    print("Welcome on board 007.")
else:
    print("Good morning " + name)


####Q2
number = int(input("Please enter a number: "))
if number % 2 == 0:
    print(True)
else:
    print(False)

####Q3
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

####Q4
for i in range(1500, 2701):
    if i % 7 == 0 or i % 5 == 0:
        print(i)

####Q5
word = input("Enter a word: ")
reversed_word = word[::-1]
print(reversed_word)
