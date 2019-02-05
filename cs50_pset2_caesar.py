"""A program which ciphers a user input message by shifting unicode characters"""
def main():
    """Main program"""
    clear_text, int_scrambler, password_input = user_inputs()
    rev_cipher_msg = cipher_message(clear_text, int_scrambler)
    password_test(password_input)
    decipher_message(rev_cipher_msg, int_scrambler)


def user_inputs():#FIRST STAGE: Getting user inputs
    """This function gets the user inputs"""
    clear_text = input("> Enter the message you want encrypted: ")
    password_input = input("> Enter a password (case sensitive) for your message: ")

    #used to set scramble amount for the message and catch any user errors
    while True:
        scrambler = input("> Enter a number between 1 and 26 to scramble your message: ")
        try:
            if 1 <= int(scrambler) <= 26:
                break
            else:
                print("Error_1: Number must be between 1 and 26 \n")
        except ValueError:
            print("Error_2: Input must be a number between 1 and 26 \n")

    # used to convert the user input from postive to negative intergers
    int_scrambler = int(scrambler)*-1

    return clear_text, int_scrambler, password_input


def cipher_message(clear_text, int_scrambler):
    """This function ciphers the users message"""
    clear_text_list = list(str(clear_text)) #converts clear_text message to a list
    ord_input = []

    for item in clear_text_list:
        ord_input.append(ord(item))

    #Applying the scrambler variable to the unicode numbers to cipher the data
    cipher_data = []
    for item in ord_input:
        cipher_data.append(item + int_scrambler)

    #Printing the scrambled message
    cipher_msg = []
    for item in cipher_data:
        cipher_msg.append(chr(item))

    #this reverses the cipher message to add an extra level of scrambling
    rev_cipher_msg = cipher_msg[::-1]

    print("\nYour ciphered message is displayed below: \n")
    for item in rev_cipher_msg:
        print(item, end="")
    print()
    print("\n-------------------------------------------------------")

    return rev_cipher_msg


def password_test(password_input):
    """This function asks the user for a password to unlock the message"""
    attempts = 3 #allows a max of 3 failed attempts
    while True:
        password_check = input("\n> Enter the password (case sensitive) to access this message: ")
        if password_input != password_check and attempts >= 0:
            print("Password is incorrect: " + str(attempts) + " more retry(s) left \n")
            attempts -= 1
        if password_input == password_check:
            break
        if attempts == 0:
            print("\nERROR: Too many password attempts made, exiting program.")
            exit()


def decipher_message(rev_cipher_msg, int_scrambler):
    """This function diciphers and then displays the user message"""
    print("\nYour deciphered message is displayed below: \n")
    decipher_data = []
    for item in rev_cipher_msg:
        decipher_data.append(ord(item) - int_scrambler) #re-aligns to original unicode
    rerev_decipher_data = decipher_data[::-1]#re-reverses the message back to orignal

    #converts re-reversed deciphered data from unicode to ascii characters
    chr_decipher = []
    for item in rerev_decipher_data:
        chr_decipher.append(chr(item))

    #prints the deciphered message
    for item in chr_decipher:
        print(item, end="")


if __name__ == "__main__":
    main()
