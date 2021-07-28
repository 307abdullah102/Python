# Code pieces should be run by removing only a piece of comment lines placed at certain intervals.
# Ignore the title comments 
# For those wondering, the titles are written in Turkish :)


#print("Hello World!")
#print(3 + 1)
#print(2 * 3)
#print(6 / 3)
#print(5 - 2)
#print(5 // 2)
#print("End", "or is it", 3)



# # Input Output Example ############
# greet = "Hello"
# name = input("please enter your name")
# print(greet + name)
# 


# # Konsolda alt satıra yazma  ############
# splitStr = "This string has been\nsplit over\nseveral\ntimes"
# print(splitStr)



# # Konsolda bir tab boşluk ile yazma 
# tabbedStr = "1\t2\t3\t4\t5\t"
# print(tabbedStr)


# # içerisinde "" gerektiren stringleri 
# # konsola yazdırma 
# print ("She said \" No no\" ")



# # Bir başka alt satıra yazma tipi 
# anotherSplitString = """This string has been
# split over 
# several 
# lines """
# print(anotherSplitString)



#print the type of variables 

# 
# greeting = "hello"
# age = 24
# print(type(greeting))
# print (type(age))
# 
# 



# #Numeric Operators
# a = 15
# b = 4
# print(a / b) # 3.75
# print(a // b) #  3 int division
# print (a % b) # 3 remainder after int division

# for i in range(1, a//b):
#     print(i)



 
  
#String Data Type 

# #                   1
# #         01234567890123
# parrot = "Norwegian Blue"
# print (parrot)
# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])
# print(parrot[9])





# #Negative Index
# print(parrot[-11]) # 3 - 14
# print(parrot[-10]) # 4 - 14
# print(parrot[-5])  # 9 - 14
# print(parrot[-11]) # 3 - 14
# print(parrot[-8])  # 6 - 14
# print(parrot[-6])  # 8 - 14






# print (parrot[0:6]) # slicing Norweg 
# print (parrot[:9]) # Norwegian
# print (parrot[10:]) # Blue

# #Using Step in slicing
# print(parrot[0:6:2])# Nre 2lik adımlarla ilk 6 elemanı bastır.
# print(parrot[0:6:3])# Nw 3lük adımlarla ilk 6 elemanı bastır.





# number = "9,223,372,034,584,775"
# seperators = number[1::4]
# print(seperators)
# values = "".join(char if char not in seperators else " " for char in number).split()
# print ([int(val) for val in values])

 
# #Strings 
# print ("Hello" * 3) # Hello Hello Hello

# today = "friday"
# print("day" in today) # True
# print("fri" in today) # True
# print ("thurs" in today) # False

# age = 24
# print ("My age is {0} years".format(age))
# print ("There are {0} days in {1},{2},{3},{4},{5},{6},{7}".format(31,"Jan","Mar","May","Jul","Aug","Oct","Dec"))






# #String Formatting
 
# for i in range(1,12):
#     print ("No.{0:2} squared {1:<3} cubed {2:^4} " .format(i, i**2, i**3))




# # IF - ELIF - ELSE STATEMENTS 
# name = input("Please enter your name:")
# age = int(input("How old are u {0}" .format(name)))
# print(age)

# if age <= 18:
#     print("Come back in {0} years" .format(18 - age))
    
    
# elif age == 900:
#     print("Sorry, Yoda you die in the Return of the JEDI")
    
# else:
#     print("You are old enough to vote")  





# # IF ELSE SECOND GUESS GAME  
# answer = 5
# print("Please guess number between 1 and 10:")
# guess = int(input())

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done!")
#     else:
#         print("Sorry guess is not correct")

# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well Done!")
#     else:
#         print("Sorry guess is not correct")

# else:
#     print("You got it in first guess")
        
  
# age = int(input("How old are you"))
# if 16 <= age <= 65:
#     print("Have a good day at work")
    
# if age < 16 or age > 65:
#     print("Enjoy your free time")
    
# string = "abcdefgğhıijklmnoöprsştuüvyz"
# for i in range(0,29):
#     print(string[i] + "\n")





# IN and NOT IN  

# parrot = "Norwegian Blue"
# letter = input("enter char")
# if letter in parrot:
#     print("{0} is in {1} \n".format(letter,parrot))

# else:
#      print("nothing")






# activity = input("What would you like to do today")

# if "cinema" not in activity.casefold(): # casefold: Büyük harfleri algılayabilme
#     print("but ı want to go to cinema")

# else:
#     print("ok lets go ")
    


# number = "9.223.372;03,854"
# seperators = " "
# for char in number:
#     if not char.isnumeric():
#         seperators = seperators + char
        
# print(seperators)

# values = "".join(char if char not in seperators else " " for char in number).split()
# print([int(val) for val in values])

    



# #CONTINUE ////////////////////////////////////////////////////////////////////////////
# shoppingList = ["milk" , "pasta" , "eggs" , "spam" , "bread" , "rice" ]

# for item in shoppingList:
#     if item == "spam":
#         continue
#     else:
#         print("Buy" + item)

# BREAK //////////////////////////////////////////////////////////////////////////////////////
# shoppingList = ["milk" , "pasta" , "eggs" , "spam" , "bread" , "rice" ]
#
# for item in shoppingList:
#     if item == "spam":
#         break
#     else:
#         print("Buy" + item)

# # WHILE 

# i = 0
# while i<10:
#     print(i)
#     i += 1
#     if i == 5:
#         break
    




# RANDOMM 
# import random 

# answer = random.randint(1,10)

# print(answer)

# # GUESS GAME 

# import random
# highest = 1000
# answer = random.randint(1, highest)
# print(answer)

# guess = 0
# print("please guess number between 1 and {0}" .format(highest))

# while guess != answer:
#     guess = int(input())
#     if guess == 0:
#         break
#     if guess == answer:
#         print("Well Done")
#         break
#     else:
#         if guess < answer:
#             print("please guess higher")
#         else:
#             print("guess lower")
            
# low = 1
# high = 1000

# print("think of a number between {0} and {1}".format(low,high))
# input("enter to start")

# guess = 1

# while True:
#     guess = low + (high - low) // 2
#     highLow = input("My guess is {}. Should I guess higher or lower"
#                     "Enter h or l or c if my guess was correct"
#                     .format(guess)).casefold()
    

#     if highLow == "h":
#         low = guess + 1
        
#     elif highLow == "l":
#         high = guess - 1
#     elif highLow == "c":
#         print ("I got it {}".format(guess))
#         break
#     else:
#         print("please enter h,l,c")
        
#     guess +=1;
    
# # LISTS ////////////////////////////////////////////////////////////////////////////////////////////////

# computerParts = ["computer",
#                   "monitor",
#                   "keyboard",
#                   "mouse",
#                   "mouse mat"]
    
# print(computerParts[2])
# computerParts += ["HDMI"] # [] ile yazılırsa HDMI "HDMI" yazılırsa alt alta H D M I bastırır
# for part in computerParts:
#     print(part)
# a = b = c = d = computerParts
# print(a)

#////////////////////////////////////////////////////////////////////////////////////////////////
# result = True 
# anotherResult = result

# print(id(result))
# print(id(anotherResult))
# result = False
# print(id(result))

# result ="Correct" 
# print(id(result))

#////////////////////////////////////////////////////////////////////////////////////////////////
# Common Sequence Operations
# even = [2,4,6,8]
# odd = [1,3,5,7,9]

# print(min(even))
# print(max(even))

# print(min(odd))                 # max ve min elemanlar
# print(max(odd))

# print(len(even))                # list kaç elemanlı 
# print(len(odd))

# print("mississipi".count("s"))  # a.count(b) a'da b'den kaç tane var
# even.extend(odd)
# print (even)
# even.sort()
# print(even)


#////////////////////////////////////////////////////////////////////////////////////////////////

# currentChoice = "-"
# computerParts = []

# while currentChoice != "0":
#     if currentChoice in "12345":
#         print ("Adding{}".format(currentChoice))
#         if currentChoice == "1":
#             computerParts.append("computer")
#         elif currentChoice == "2":
#             computerParts.append("monitor")
#         elif currentChoice == "3":
#             computerParts.append("keyboard")
#         elif currentChoice == "4":
#             computerParts.append("mouse")

        
#     else:
#         print("Please add options from the list\n"
#               "1: Computer\n"
#               "2: Monitor\n"
#               "3: Keyboard\n"
#               "4: Mouse\n")
        
#     currentChoice = input()
# print(computerParts)   

#//////////////////////////////////////////////////////////////////
## SORTING

# pangram = "The quick brown fox jumps over the lazy dog"

# letters = sorted(pangram)
# print (letters)

# numbers = [2, 3, 5, 9, 18, 25, 4, 28]
# sortedNums = sorted(numbers)
# print (sortedNums)

# numbers.sort()
# print(numbers)

# missingLetter = sorted("The quick", key = str.casefold)
# print(missingLetter)

# names = ["Graham",
#          "John",
#          "terry",
#          "eric",
#          "michael"
#          ]
# names.sort(key = str.casefold)
# print(names)

# str.casefold sayesinde büyük harf küçük
# harf duyarsızlaşıyor ve tam olarak 
# istenen alfabetik sıra elde ediliyor.

# data = [ 4, 5, 100, 102, 18, 25, 28, 
#         37, 98, 254, 185, 487, 254,]

# del data [0:2]
# print (data)
# del data[7:]
# print (data)

#//////////////////////////////////////////////////////////////////
# import numpy as np
# import matplotlib.pyplot as plt
# pi = np.pi
# t = np.arange(-20, -10, 0.5)
# y1 = np.sin(0.1*pi*t) + (1/3) * np.sin(0.3 * pi * t) + (1/5) * np.sin(0.5 * pi * t)
# for i in range(11):
#     print(y1[i])
# plt.scatter(t,y1)
# plt.show

# import matplotlib.pyplot as plt
# import numpy as np
# t = np.arange(-5, 5, 1)
# y = np.heaviside(t+2,1) - np.heaviside(t-2,1)

# plt.stem(t,y)
# plt.show()

## Arange interval of your data as [100-200]
# data = [104, 101, 4, 105, 308, 103, 5,
#         107, 100, 305, 105, 102, 108]
# minValid = 100
# maxValid = 200

# for index in range(len(data)-1, -1, -1):
#     if data[index] < minValid or data[index] > maxValid:
#         print(index, data)
#         del data[index]
        
# print(data)

#//////////////////////////////////////////////////////////////////
## REVERSED FUNCTION
# data = [104, 101, 4, 105, 308, 103, 5,
#         107, 100, 305, 105, 102, 108]
# minValid = 100
# maxValid = 200

# topIndex = len(data) - 1
# for index,value in enumerate(reversed(data)):
#     if value < minValid or value > maxValid:
            
#         print(topIndex - index,value)
#         del data[topIndex - index]
# print(data)

 #/////////////////////////////////////////////////////
##NESTED LISTS##
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# numbers = [even, odd]
# print(numbers)

# for numberList in numbers:
#     print(numberList)
    
#     for value in numberList:
#         print(value)
        
# menu = [
#         ["egg", "bacon"],
#         ["egg", "sausage", "bacon"],
#         ["egg", "spam"],
#         ["egg", "spam", "bacon"],
#         ["egg", "sausage", "bacon", "spam"],
#         ["spam", "sausage", "bacon", "spam"],]
 
# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
        
#         for item in meal:
#             print (item)
            
#     else:
#         print("{0} has a spam score of {1}"
#               .format(meal, meal.count("spam")))


#//////////////////////////////////////////////////////////////////
## FUNCTIONS REVISITATIONS
# name = " Abdullah"
# age = 21
# print (name, age, "Python", 2020)
# print (name, age, "Python", 2020, sep=", ")
# print (name, age, "Python", 2020, end=", ")

   #////////////////////////////////////////////////////////////////// 
# ## JOIN METHOD ##
# flowers = [
#      "Gul",
#      "Papatya",
#      "Karanfil",
#      "Ihlamur",
#      ] 
# seperator = " | "
# output = seperator.join(flowers)
# print(output)
        
# print(" | ".join(flowers))

## SPLIT METHOD ##

#import numpy as np
##import matplotlib.pyplot as plt
#panagram = "My name is Abdullah How are you"
#
#pi = np.pi
#
#words = panagram.split()
#print(words)
#
#numbers = "9,223,251,245,542,512,211"
#print(numbers.split(","))

#//////////////////////////////////////////////////////////////////
#import numpy as np
#import matplotlib.pyplot as plt 
#
##%matplotlib notebook
#pi = np.pi
#
#
#x = np.arange(-12,13,1)
#y = np.zeros(len(x))
#for i in range(len(x)):
#    y[i] = np.exp(((0+1j)*pi*i/6))
#plt.stem(x, y.real,  use_line_collection=True)
#plt.stem(x, y.imag,  use_line_collection=True)
#plt.xticks(np.arange(x[0],x[-1],1))
#plt.show()

#albums = ["SSS", "Alice", 1975,
#          "AAA", "Alic", 1976,
#          "DDD", "Alicee", 1977,
#          "FFF", "Alicc", 1974,
#          "WWW", "Alicec", 1973,]
#
#print (len(albums)) # 15
#
 
 #//////////////////////////////////////////////////////////////////
##TUPLES
#albums = [("SSS", "Alice", 1975,),
#          ("AAA", "Alic", 1976,),
#          ("DDD", "Alicee", 1977,),
#          ("FFF", "Alicc", 1974,),
#          ("WWW", "Alicec", 1973,)]
#print (len(albums)) #5
#
#print (albums[0]) # SSS ALICE 1975
#
#print (albums[0][0]) # SSS

# Tuples as library 
#from nestedData import albums
#
#print(albums)
 
 #//////////////////////////////////////////////////////////////////
 ## FUNCTION WITH NO PARAMETER
#def multiply():
#    result = 10.5*4
#    return result
#
#answer = multiply()
#print(answer)

#//////////////////////////////////////////////////////////////////
##FUNCTION WITH PARAMETERS
#def multiply(x,y):
#    result = x*y
#    return result
#
#answer = multiply(3,5)
#print(answer)

#//////////////////////////////////////////////////////////////////
##PALINDROME

#def isPalindrome(string):
#    
#    #backwards = string[::-1]
#    #return backwards == string
#    # Casefold for big-small letter 
#    return string[::-1].casefold() == string.casefold()
#
##word = input("Give me polindrome")
#word = "ey edip adANADa pide ye"
#word = "İKi"
#word = "Kazak"
#if isPalindrome(word):
#    print("{} is polindrome".format(word))
#else:
#    print("{} is polindrome".format(word))
    
#def isPalindrome(string):
#    
#    #backwards = string[::-1]
#    #return backwards == string
#    # Casefold for big-small letter 
#    return string[::-1].casefold() == string.casefold()
#
#
#
##word = input("Give me polindrome")
#word = "ey edip adANADa pide ye"
#word = "İKi"
#word = "Kazak"
#
#if isPalindrome(word):
#    print("{} is polindrome".format(word))
#else:
#    print("{} is polindrome".format(word))
#

#//////////////////////////////////////////////////////////////////
# PALINDROME SENTENCE 
#sentence = "do geese ! see god '^+="
#
#def palindromeSentence(sentence):
#    string = ""
#    for char in sentence:
#        if char.isalnum():
#            string += char
#    print(string)
#    return string[::-1].casefold() == string.casefold()
#           
#
#
#
#
#if palindromeSentence(sentence):
#    print("{} is polindrome".format(sentence))
#else:
#    print("{} is polindrome".format(sentence))
#
#//////////////////////////////////////////////////////////////////
 
 #FUNCTIONS CALLING FUNCTIONS 
 
#sentence = "do geese ! see god '^+="
#def isPalindrome(string):
#    
#    #backwards = string[::-1]
#    #return backwards == string
#    # Casefold for big-small letter 
#    return string[::-1].casefold() == string.casefold()
#
# 
# 
# 
# 
#def palindromeSentence(sentence):
#    string = ""
#    for char in sentence:
#        if char.isalnum():
#            string += char
#    print(string)
## FUNCTION CALLING ANOTHER FUNCTION
#    isPalindrome(string)
# 
#if palindromeSentence(sentence):
#    print("{} is polindrome".format(sentence))
#else:
#    print("{} is polindrome".format(sentence))
#
# /////////////////////////////////////////////////////////////////
 
#def banner_text (text):
#    screen_width = 80
#    if len(text) > screen_width - 4:
#        print("The text is too long to fit in the specified width")
#    
#    if text == "*":
#        print("*" * screen_width)
#    
#    else:
#        output_string = "**{0}**".format(text.center(screen_width-4))
#        print(output_string)
#        
#banner_text("*")
#banner_text("Always look on the bright side of life...")
#banner_text("If life seems jolly rotten,")
#banner_text("And that's to laugh and smile and dance and sing")
#banner_text("*")
        
#////////////////////////////////////////////////////////////////////////
 
## FIBONACCI & FIBONACCI & FIBONACCI # 
#def multiply(x, y):
#    return x*y
#
#def is_palindrome(string):
#    return string[::-1].casefold() == string.casefold()
#
#def palindrome_sentence(sentence):
#    string = ""
#    for char in sentence:
#        if char.isalnum():
#            string += char
#    return is_palindrome(string)
#
#def fibonacci(n):
#    """Return the n'th Fibonacci number, for positive n"""
#    
#    if 0 <= n <= 1:
#        return n
#    n_minus1, n_minus2 = 1, 0
#    
#    result = None
#    for f in range(n - 1):
#        result = n_minus2 + n_minus1
#        n_minus2 = n_minus1
#        n_minus1 = result
#        
#    return result
#
#for i in range(36):
#    print(i, fibonacci(i))
#////////////////////////////////////////////////////////////////////////







































 
 
 
 
 
 
 
