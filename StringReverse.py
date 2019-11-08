
#StringReverse



test = 1023
while test not in range(0,100):
    test = int(input("Enter the test cases : "))

words = "t"
inputList = []
while len(words) not in range(3,1000) and len(inputList) < test:
    for i in range(0,test):
        words = input("Enter words = ")
        inputList.append(words)
    break


for i in range(0,len(inputList)):
    print(inputList[i][::-1])


