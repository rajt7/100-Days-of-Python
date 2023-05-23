def prime_checker(number):
    flag = 0

    if(number==0 or number==1):
        print(f'{number} is not a prime number')
    else:
        for i in range(2, int(number/2)):
            if number % i == 0:
                flag = 1
                break
        
    if flag == 0:
        print("It's a prime number")
    elif flag == 1:
        print("It's not a prime number")    


n = int(input('Enter a number: '))
prime_checker(number = n)