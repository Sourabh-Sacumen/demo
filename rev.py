#reverse a string using recurssion
def rev(n,s):
    if n == -len(s)-1:
        return ''
    return s[n] + rev(n-1,s)

n = -1
s = 'Sourabh loves python'
result = rev(n,s)
print(result)

print("*"*30)
#reverse a string without using inbuit method
def revStr_1(s):
    x=''
    for i in range(len(s)-1, -1, -1):
        x+=s[i]
    print(x)

revStr_1("Hello Sourabh Welcome to Sacumen")