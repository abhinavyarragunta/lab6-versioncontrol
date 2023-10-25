def encode(password):
    for i in range(len(password)):
        password[i] = int(password[i])
        password[i] += 3
        password[i] = str(password[i])
    password = ''.join(password)
    return password


def main():
    password = list(input('Enter password: '))
    print(encode(password))


if __name__ == '__main__':
    main()
