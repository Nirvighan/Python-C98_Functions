

f = open("text.txt")


f = open("text.txt")
fileLines = f.readlines()

for line in fileLines:
    print(line)

introString = "My name is Nirvighan Sinha,I am a student,I love coding"
words = introString.split(",")
print(words)

#def functionName():
#    <Block of code


def greet(Name):
    print("Hello , " + Name + " How are you ?")

greet("Nirvighan")