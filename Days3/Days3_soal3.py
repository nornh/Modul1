b = (input("Enter a starting number (greater than 0) or QUIT: "))
if b != "QUIT" :
    b = int(b)
    while b != 1 :
            print (b, end=" ")
            if b % 2 ==0:
                b //= 2
            else:
                b *= 3
                b += 1
    print (b)