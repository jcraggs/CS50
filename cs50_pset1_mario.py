globvar = 0

def mario_world_builder():
	user_input = input("How tall do you want Mario's Pyramid? (Enter a number between 1 - 8): ") 
	rolling_number = 0
	rolling_reverse = 0
	space_var = " "
	hash_var = "#"

	def set_globvar_to_one():
		global globvar
		globvar += 1

	try:
		val = int(user_input)
		while val > 8 or val < 1:
			print("Error_1: Number must be between 1-8 \n")
			user_input = input("How tall do you want Mario's Pyramid? (Enter a number between 1 - 8): ")
			val = int(user_input)
		if 1 <= val <= 9:
			pass
			set_globvar_to_one()
			rolling_reverse= int(user_input)
			while rolling_number < val+1:
				print(" "+(rolling_reverse)*space_var + (1*hash_var)*rolling_number)
				rolling_number += 1
				rolling_reverse -= 1
			print()
	except ValueError:
		print("Error_2: Input must be a number between 1-8 \n")

while globvar ==0:
	mario_world_builder()
