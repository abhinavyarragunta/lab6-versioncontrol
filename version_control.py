def main():
    password = list(input('Enter password: '))
    for i in range(len(password)):
        password[i] = int(password[i])
        password[i] += 3
        password[i] = str(password[i])
    password = ''.join(password)
    print(password)


if __name__ == '__main__':
    main()