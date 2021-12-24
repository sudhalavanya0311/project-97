#myName = "Sudha"
#print ("myName")

#myAge = 15
#print (myAge)

#MyFriends=["Sudha","Sid","Uday"]
#print (MyFriends[1])


#age = int(input("Enter your age: "))

#if (age>18):
    #print("You are an adult. You can vote!")
#elif (age>12):
    #print("You are a teenager and a rebel!")
#else:
    #print("You are still a kid. There is so much in the world for you to see.")

#myFriendList = ["Ram", "Radha","Nivedita"]
#for friend in myFriendList:
    #print(friend)

#count = 5
#while (count>=0):
    #print(count)
    #count = count - 1


characterCount=0
wordCount=1
introString = input("Enter your introduction:")
print(introString)
for character in introString:
    characterCount=characterCount +1
    #print(characterCount)
    if(character == ' '):
        wordCount=wordCount+1
        print(wordCount)
