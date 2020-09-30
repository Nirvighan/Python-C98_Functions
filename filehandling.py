def CountWords():
    
    fName = input("Enter the file name")
    totalWords = 0
    file = open(fName,'r')
    
    for line in file:
        words = line.split()

        totalWords = totalWords + len(words)
    print("No. of words")
    print(totalWords)

CountWords()
    

    





