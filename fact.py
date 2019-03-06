def factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s

def fact_recursive(n):
    if(n==1):
        return 1
    else:
        return fact_recursive(n-1)*n

def fibo_loop(n):
    a,b=0,1
    if(n==0):
        return 0
    for i in range(n-1):
        a,b=b,a+b

    return b

def fibo_recursive(n):
    if(n<2):
        return n
    else:
        return fibo_recursive(n-1)+fibo_recursive(n-2)

def power_r(m,n):
    if(n==0):
        return 1
    elif(n==1):
        return m
    elif(n%2 ==0):
        return power_r(m*m,n//2)
    elif(n%2 !=0):
        return power_r(m*m,n//2)*m

