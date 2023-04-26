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