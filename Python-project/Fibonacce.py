count = 0
number = int(input("Please enter your number : "))
list1 = [1,1]
while list1[-1] != number:                                  
    list1.append(list1[count] + list1[count + 1])
    count += 1
print(list1)
