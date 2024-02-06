#Print diviser of user input

inp=int(input("please enter a number"))
lists=list(range(1,inp+1))

divisor=[]
for num in lists:
    if inp % num==0:
        divisor.append(num)
print(divisor)