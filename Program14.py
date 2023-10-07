num = int(input("Enter a number: "))
newnum = 0

for each in range(1,num+1):
    newnum = newnum+(each/(each+1))

print("computed value : ",format(round(newnum,2)))