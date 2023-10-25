def encode(password):
    for i in range(len(password)):
        password[i] = int(password[i])
        password[i] += 3
        password[i] = str(password[i])
    password = ''.join(password)
    return password

def decode(password):
    a = ''
    for i in range(len(password)):
        b = int(password[i])
        b += 7
        b %= 10
        a = a + str(b)
    return a

def main():
    password = list(input('Enter password: '))
    print(encode(password))


if __name__ == '__main__':
    main()
