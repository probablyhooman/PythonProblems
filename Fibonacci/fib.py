#creating a fibonacci series 

def fib(n):

    a= 0
    b = 1
    print(0)
    print(1)
    for i in range(2,n):
        c = a+b
        a =b
        b =c
        print(c)

fib(11)
