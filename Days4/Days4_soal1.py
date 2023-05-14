def caeser_cihper(message, key):
    encription =' '
    alpa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in message:
        if(i == ' '):
            print(' ', end='')
        elif(ord(i)-ord('A')+ key >= 26 ):
            print(chr(ord(i)- 26+ key), end='')
        else:
            print(chr(ord(i)+key), end='')
        return encription    

if __name__ == '__main__':
    message = input("Enter the message: ")
    # message = Meet me by the rose bushes tonight.
    message = str.upper(message)
    key = 4
    encription = caeser_cihper(message, key)
    print(encription)