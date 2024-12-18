l=[1,5,9,45,87,97,45,12,100,8788]
print(l)
sum=0
for number in l:
    sum=sum+number
print("sum=",sum)
average=sum/len(l)
print("average=",average)
l.sort()
print("The sorted list is",l)
print("The smallest number in the list is",l[0])
print("The largest number in the list is",l[-1])