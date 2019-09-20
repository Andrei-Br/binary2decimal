class NotBinary(Exception):
    pass
class OutOfBounds(Exception):
    pass

# function handling the user input
def UserInput():
    # asking for user input until valid
    while True:
        try:
            user_num = input('Enter a binary number: ')
            num_list = [digit for digit in user_num]
            # checking if the number has any characters different from 0 and 1
            for digit in num_list:
                if digit == '0' or digit == '1':
                    continue
                else:
                    raise NotBinary
            # checking if the number has more than 8 digits:
            if len(user_num) > 8:
                raise OutOfBounds
            # if the input is valid, break the input loop and return the number
            else:
                return int(user_num)

        # in case of error, print the corresponding message
        except NotBinary:
            print('Your number ( ' + user_num + ' ) is not binary. '
                  'It contains characters other than 0 or 1. '
                  'Try again.\n')
        except OutOfBounds:
            print('Your number ( ' + user_num + ' ) has more than 8 digits. '
                  'Try again.\n')

def bin2dec():
    user_input = UserInput()
    dec_num = 0
    pwr = 0
    for digit in range(len(str(user_input))):
        last_digit = user_input % 10
        if last_digit == 1:
            dec_num += 2 ** pwr
        pwr += 1
        user_input = int(user_input/10)
    print('Your decimal number is:', dec_num)

def main():
    bin2dec()

if __name__ == '__main__':
    main()