#finding factorial using recurssion
def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

#add elements of list
def addls(l):
    sum=0
    for i in l:
        sum+=i
    return sum

print(addls([1,2,3,4,5]))