#number rhombus patters
def rhombus_pttrn(n):
    sp = n//2
    st = 1
    num = 1
    for i in range(1, n+1):
        #num = i
        for j in range(sp):
            print(" ", end=" ")
        for k in range(st):
            print(num, end=" ")
            if k < st//2:
                num-=1
            else:
                num+=1
        print()
        if i < n//2+1:
            sp-=1
            st+=2
        else:
            num-=1
            sp+=1
            st-=2

rhombus_pttrn(int(input("n= ")))

#star pattern pyramid
def pyramid_star(n):
    sp=n-1
    st=1
    for i in range(n):
        for j in range(sp):
            print(" ", end=" ")
        for k in range(st):
            print("*", end=" ")
        print()
        sp-=1
        st+=2

pyramid_star(int(input("n= ")))

#another star pattern
def pttrn(n):
    sp=n-1
    st=1
    for i in range(n):
        for j in range(st):
            print("*", end=" ")
        for k in range(sp):
            print(" ", end=" ")
            print("*", end=" ")
        for m in range(st-1):
            print("*", end=" ")
        print()
        sp-=1
        st+=1

pttrn(int(input("n= ")))