for x in range(100):
    if x % 3 == 0 and x % 5 == 0:
        print(str(x)+" FizzBuzz")
    elif x % 3 == 0:
        print(str(x)+" Fizz")
    elif x % 5 == 0:
        print(str(x)+" Buzz")
    else:
        print(x)
