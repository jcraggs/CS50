globvar_a = 0
globvar_b = 0
cost_int = 1
paid_int = 1
def change_calculator():

	def cost_input():
		def set_globvar_a_to_one():
			global globvar_a
			globvar_a +=1
		try:
			cost = float(input("How much does the item cost (enter value as a number with decimals i.e 3.99 for £3.99)?: ")) 
			global cost_int
			cost_int = float(cost)
			while cost_int < 0 or cost_int == 0:
				print("Error_1: Cost must be entered as a number greater than 0 \n")
				cost = float(input("How much does the item cost (enter value as a number with decimals i.e 3.99 for £3.99)?: ")) 
				cost_int = float(cost)
			if cost_int > 0:
				pass
				set_globvar_a_to_one()
		except ValueError:
			print("Error_3: Cost must be entered as a number \n")
	while globvar_a == 0:
		cost_input()

	def paid_input():
		def set_globvar_b_to_one():
			global globvar_b
			globvar_b +=1
		try:
			paid = float(input("How much has the customer paid (enter value as a number with decimals i.e 3.99 for £3.99)?: ")) 
			global paid_int
			paid_int = float(paid)
			while paid_int < 0 or paid_int == 0:
				print("Error_1: Payment must be entered as a number greater than 0 \n")
				paid = float(input("How much has the customer paid (enter value as a number with decimals i.e 3.99 for £3.99)?: ")) 
				paid_int = float(int(paid))
			while paid_int < cost_int:
				print("Error_2: Payment must be greater than the cost of the item \n")
				paid = float(input("How much has the customer paid (enter value as a number with decimals i.e 3.99 for £3.99)?: ")) 
				paid_int = float(paid)
			if paid_int > 0:
				pass
				set_globvar_b_to_one()
		except ValueError:
			print("Error_3: Payment must be entered as a number \n")
	while globvar_b == 0:
		paid_input()
	change_val = (paid_int - cost_int)
	rounded_change_val = round(change_val, 2)
	if rounded_change_val == 0:
		print("\nThe customer does not require change.")
	if rounded_change_val > 0:
		print("\nThe customer is owed: £" + str(rounded_change_val))
	
	def smallest_change():
		whole_note_50 = 0
		whole_note_20 = 0
		whole_note_10 = 0
		whole_note_5 = 0
		whole_pound_2 = 0
		whole_pound_1 = 0
		whole_pence_50 = 0
		whole_pence_20 = 0
		whole_pence_10 = 0
		whole_pence_5 = 0
		whole_pence_2 = 0
		whole_pence_1 = 0
		rolling_change_val = rounded_change_val
		while rolling_change_val > 50 or rolling_change_val == 50:
			note_50 = (rounded_change_val/50)
			whole_note_50 = int(note_50) #<--- need to call this at the end (tells you how many £50 notes to give them)
			rem_change = round(((note_50-whole_note_50)*50),2)
			rolling_change_val = rem_change
		while rolling_change_val > 20 or rolling_change_val ==20:
			note_20 = (rolling_change_val/20)
			whole_note_20 = int(note_20) #<--- need to call this at the end (tells you how many £20 notes to give them)
			rem_change = round(((note_20-whole_note_20)*20),2)
			rolling_change_val = rem_change
		while rolling_change_val > 10 or rolling_change_val ==10:
			note_10 = (rolling_change_val/10)
			whole_note_10 = int(note_10) #<--- need to call this at the end (tells you how many £10 notes to give them)
			rem_change = round(((note_10-whole_note_10)*10),2)
			rolling_change_val = rem_change
		while rolling_change_val > 5 or rolling_change_val ==5:
			note_5 = (rolling_change_val/5)
			whole_note_5 = int(note_5) #<--- need to call this at the end (tells you how many £5 notes to give them)
			rem_change = round(((note_5-whole_note_5)*5),2)
			rolling_change_val = rem_change
		while rolling_change_val > 2 or rolling_change_val ==2:
			pound_2 = (rolling_change_val/2)
			whole_pound_2 = int(pound_2) #<--- need to call this at the end (tells you how many £2 coins to give them)
			rem_change = round(((pound_2-whole_pound_2)*2),2)
			rolling_change_val = rem_change
		while rolling_change_val > 1 or rolling_change_val ==1:
			pound_1 = (rolling_change_val/1)
			whole_pound_1 = int(pound_1) #<--- need to call this at the end (tells you how many £1 coins to give them)
			rem_change = round(((pound_1-whole_pound_1)*1),2)
			rolling_change_val = rem_change
		while rolling_change_val > 0.5 or rolling_change_val ==0.5:
			pence_50 = (rolling_change_val/0.5)
			whole_pence_50 = int(pence_50) #<--- need to call this at the end (tells you how many 50p coins to give them)
			rem_change = round(((pence_50-whole_pence_50)*0.5),2)
			rolling_change_val = rem_change
		while rolling_change_val > 0.2 or rolling_change_val ==0.2:
			pence_20 = (rolling_change_val/0.2)
			whole_pence_20 = int(pence_20) #<--- need to call this at the end (tells you how many 20p coins to give them)
			rem_change = round(((pence_20-whole_pence_20)*0.2),2)
			rolling_change_val = rem_change
		while rolling_change_val > 0.1 or rolling_change_val ==0.1:
			pence_10 = (rolling_change_val/0.1)
			whole_pence_10 = int(pence_10) #<--- need to call this at the end (tells you how many 10p coins to give them)
			rem_change = round(((pence_10-whole_pence_10)*0.1),2)
			rolling_change_val = rem_change
		while rolling_change_val > 0.05 or rolling_change_val ==0.05:
			pence_5 = (rolling_change_val/0.05)
			whole_pence_5 = int(pence_5) #<--- need to call this at the end (tells you how many 5p coins to give them)
			rem_change = round(((pence_5-whole_pence_5)*0.05),2)
			rolling_change_val = rem_change
		while rolling_change_val > 0.02 or rolling_change_val ==0.02:
			pence_2 = (rolling_change_val/0.02)
			whole_pence_2 = int(pence_2) #<--- need to call this at the end (tells you how many 2p coins to give them)
			rem_change = round(((pence_2-whole_pence_2)*0.02),2)
			rolling_change_val = rem_change
		while rolling_change_val > 0.01 or rolling_change_val ==0.01:
			pence_1 = (rolling_change_val/0.01)
			whole_pence_1 = int(pence_1) #<--- need to call this at the end (tells you how many 1p coins to give them)
			rem_change = round(((pence_1-whole_pence_1)*0.01),2)
			rolling_change_val = rem_change

		print("You need to give the customer the following change denominations: \n")
		if whole_note_50 > 0:
			print("- £50 note x " + str(whole_note_50))
		if whole_note_20 > 0:
			print("- £20 note x " + str(whole_note_20))
		if whole_note_10 > 0:
			print("- £10 note x " + str(whole_note_10))
		if whole_note_5 > 0:
			print("- £5 note x " + str(whole_note_5))
		if whole_pound_2 > 0:
			print("- £2 coin x " + str(whole_pound_2))
		if whole_pound_1 > 0:
			print("- £1 coin x " + str(whole_pound_1))
		if whole_pence_50 > 0:
			print("- 50p coin x " + str(whole_pence_50))
		if whole_pence_20 > 0:
			print("- 20p coin x " + str(whole_pence_20))
		if whole_pence_10 > 0:
			print("- 10p coin x " + str(whole_pence_10))
		if whole_pence_5 > 0:
			print("- 5p coin x " + str(whole_pence_5))
		if whole_pence_2 > 0:
			print("- 2p coin x " + str(whole_pence_2))
		if whole_pence_1 > 0:
			print("- 1p coin x " + str(whole_pence_1))

	if rounded_change_val > 0:
		smallest_change()

change_calculator()


