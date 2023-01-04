import random
A = eval(input("Enter the Range from: "))
B = eval(input("Enter the Range to: "))

num = random.randint(A,B)
if num>=1:
    print(num,"is positive number")
    if num%2==0:
         print(num,"is even number")
    else:
        print(num,"is odd number")
    if num > 1:
        for i in range(2,num):
            if num%i==0:
                print(num,"is a composite number")
                break
        else:
            print(num,"is a prime number")
    elif num==0 or num==1:
        print(num,"is neither prime nor composite")
    else:
        print(num,"is a prime number")
elif num==0:
    print(num,"is neither positive nor negative")
    print(num,"is neither even nor odd")
    print(num,"is neither prime nor composite")
else:
    print(num,"is negative number")
