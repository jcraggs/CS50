#----FIRST STAGE: Getting user inputs
word = input("> Enter the message you want encrypted: ")
entered_word = list(str(word)) #converts message to a list
password_input = input("> Enter a password (case sensitive) for your message: ")

#----Used to set the scrambling of the message and catch any user errors
globvar = 0
def set_globvar_to_one():
		global globvar
		globvar += 1

while globvar == 0:
	scrambler = input("> Enter a number between 1 and 26 to scramble your message: ") #Used to set the scramble offset (Noe this value will be converted to -1 to -26, as outside this range the asciii does not output well)
	try:
		while int(scrambler) > 26 or int(scrambler) < 1:
			print("Error_1: Number must be between 1 and 26 \n")
			scrambler = input("> Enter a number between 1 and 26 to scramble your message: ")
		if 1 <= int(scrambler) <= 26:
			pass
			set_globvar_to_one()
	except ValueError:
		print("Error_2: Input must be a number between 1 and 26 \n")

int_scrambler = int(scrambler)*-1 # used to convert the user input from postive to negative intergers


#---- SECOND STAGE: Ciphering the user message

#Converting the entered_word list to ascii data array#
ord_input = []
for item in entered_word:
	ord_input.append(ord(item))

#Applying the scrambler variable to the unicode numbers to cipher the data
cipher_data = []
for item in ord_input:
	cipher_data.append(item + int_scrambler)

#Printing the scrambled message
cipher_msg = []
for item in cipher_data:
	cipher_msg.append(chr(item))
rev_cipher_msg = cipher_msg[::-1] #this reverses the cipher message to add an extra level of scrambling

print("\nYour ciphered message is displayed below: \n")
for item in rev_cipher_msg:
    print(item, end="")
print()

print("\n-------------------------------------------------------")

#---- THIRD STAGE: Asking the user for a password to unlock the message
t_f_val = 0
def pass_check():
	t_f_val = 0
	x = 3
	def set_t_f_val_to_1():
		global t_f_val
		t_f_val += 1

	password_check = input("\n> Enter the password (case sensitive) to access this message: ")
	while password_input != password_check and x >= 1:
			print("Password is incorrect: " + str(x) + " more retry(s) left \n")
			x -= 1
			password_check = input("> Enter the password (case sensitive) to access this message: ")

	if password_input == password_check:
			pass
			print("Correct password entered, here is the deciphered message: \n")
			set_t_f_val_to_1()

	if x == 0:
		print("\nERROR: Too many password attempts made, exiting program.")
		exit()
pass_check()

#---- FOURTH STAGE: Deciphering and displaying the user the message (if password has been correctly entered)

#Converting the ciphered message to unicode and undo-ing the scambling function + reversal
decipher_data = []
for item in rev_cipher_msg:
	decipher_data.append(ord(item) - int_scrambler)
rerev_decipher_data = decipher_data[::-1]#reverses the data back to normal

#converts re-reversed deciphered data from unicode to ascii characters
chr_decipher = []
for item in rerev_decipher_data:
	chr_decipher.append(chr(item))

for item in chr_decipher:
    print(item, end="")
