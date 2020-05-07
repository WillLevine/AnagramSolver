import time
import sys
import operator

# User inputs the anagram and then the program puts each letter separately
# into an array and also finds the length of the anagram as a whole

anagram = input("Enter the anagram: ")
anagramSplit = list(anagram)
anagramLength = len(anagram)

# The dictionary .txt file is opened and the file is split so that all of the
# words are in a sort of array

with open("dictionary.txt", "r") as f:
    dictionary = f.read()
    words = dictionary.split()
    #print(words)

# Checking the length of the anagram and then making an array of every 
# word of the same length

    if anagramLength == 2:
        possibleWords = words[0:124]
    elif anagramLength == 3:
        possibleWords = words[124:1435]
    elif anagramLength == 4:
        possibleWords = words[1435:6963]
    elif anagramLength == 5:
        possibleWords = words[6963:19615]
    elif anagramLength == 6:
        possibleWords = words[19615:42030]
    elif anagramLength == 7:
        possibleWords = words[42030:75322]
    elif anagramLength == 8:
        possibleWords = words[75322:115964]
    elif anagramLength == 9:
        possibleWords = words[115964:157190]
    elif anagramLength == 10:
        possibleWords = words[157190:193063]
    elif anagramLength == 11:
        possibleWords = words[193063:221177]
    elif anagramLength == 12:
        possibleWords = words[221177:241631]
    elif anagramLength == 13:
        possibleWords = words[241631:255608]
    elif anagramLength == 14:
        possibleWords = words[255608:264821]
    elif anagramLength == 15:
        possibleWords = words[264821:270633]
    elif anagramLength == 16:
        possibleWords = words[270633:272577]
    elif anagramLength == 17:
        possibleWords = words[272577:273704]
    elif anagramLength == 18:
        possibleWords = words[273704:274299]
    elif anagramLength == 19:
        possibleWords = words[274299:274628]
    elif anagramLength == 20:
        possibleWords = words[274628:274788]
    elif anagramLength == 21:
        possibleWords = words[274788:274850]
    elif anagramLength == 22:
        possibleWords = words[274850:274880]
    elif anagramLength == 23:
        possibleWords = words[274880:274893]
    elif anagramLength == 24:
        possibleWords = words[274893:274902]
    elif anagramLength == 25:
        possibleWords = words[274902:274904]
    elif anagramLength == 26:
        print("No Words Found.")
        sys.exit()
    elif anagramLength == 27:
        possibleWords = words[274904:274906]
    elif anagramLength == 28:
        possibleWords = words[274906:274907]
    # print(possibleWords)
    print(anagramSplit,"\n")
    print ("The anagram is : " + str(anagramSplit),"\n") 
    for word in possibleWords:
        wordList = list(word)
        solved = str(wordList)
        solved = solved.replace("[", "")
        solved = solved.replace("'", "")
        solved = solved.replace("]", "")
        solved = solved.replace(" ", "")
        solved = solved.replace(",", "")
        print ("The real word is : " + solved)
        # sorting both the lists 
        anagramSplit.sort() 
        wordList.sort()
        if anagramSplit == wordList:
            # removing the unwanted symbols in the solved anagram
            solved = solved.replace("[", "")
            solved = solved.replace("'", "")
            solved = solved.replace("]", "")
            solved = solved.replace(" ", "")
            solved = solved.replace(",", "")
            time.sleep(1) 
            print("The lists are identical\n")
            time.sleep(1)
            print("Your anagram has been solved\n\n")
            time.sleep(1)
            print("The SOLVED anagram is: ",solved,"\n\n")
            time.sleep(1)
            print("A copy of the solved anagram has been saved in 'solved.txt' for your reference.""\n\n")
            # writing the solved anagram to a text file
            with open("Solved.txt", "w") as Solved:
                Solved.write("Solved: "+solved)
                Solved.close()
            input('Press ENTER to exit')
            sys.exit()
        elif anagramSplit != wordList: 
            print ("The lists are not identical\n\n")
        else:
            print("Error")
            sys.exit()

input('Press ENTER to exit')
sys.exit()
