upTo = int(input("Masukkan sebuah angka: "))
for number in range (1, upTo +1 ):
    d3 = number % 3
    d5 = number % 5
    if d3 == 0 and d5 == 0:
        print("FizzBuzz", end=" ")
    elif d3 == 0 and d5 != 0:
        print ("Fizz", end=" ")
    elif d3 !=0 and d5 == 0:
        print("Buzz", end=" ")
    else:
        print(number, end=" ")