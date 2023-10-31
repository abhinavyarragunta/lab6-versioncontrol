def encode(password):
    password = list(password)
    for i in range(len(password)):
        password[i] = int(password[i])
        password[i] += 3
        password[i] %= 10
        password[i] = str(password[i])
    password = ''.join(password)
    return password

#Rich Nguyen 
def decode(password):
    a = ''
    for i in range(len(password)):
        b = int(password[i])
        b += 7
        b %= 10
        a = a + str(b)
    return a


def main():
    global password, encoded_password
    quit_program = False
    while not quit_program:
        menu = 'Menu'
        print(menu)
        print('-' * len(menu))
        print('1. Encode\n2. Decode\n3. Quit')
        menu_option = input('Please enter an option: ')
        if menu_option == '1':
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
        elif menu_option == '2':
            print(f'The encoded password is {encoded_password}, and the original password is {password}.')
        elif menu_option == '3':
            quit_program = True


if __name__ == '__main__':
    main()
