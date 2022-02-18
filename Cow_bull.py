import random
print("...welcome to my guessing game....")
list1=[0,1,2,3,4,5,6,7,8,9]
list2=[]
for i in range(5):
    y=random.choice(list1)
    list2.append(y)
print(list2)
i=0
while i<len(list2):
    j=0
    list3=[]
    list4=[]
    while j<5:
        guess=int(input("enter any number......"))
        position=int(input("enter the postion....."))
        if guess in list2:
            list3.append(guess)
            if list2==list3:
                print("...... BULL ......")
        else:
            print("COW")
            list4.append(guess)
            print(list4)