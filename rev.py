#reverse a string using recurssion
def rev(n,s):
    if n == -len(s)-1:
        return ''
    return s[n] + rev(n-1,s)

n = -1
s = 'Sourabh loves python'
result = rev(n,s)
print(result)