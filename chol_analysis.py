def HDL_analysis(HDL_level):
		print(HDL_level)
		if HDL_level >= 60:
				return "Normal"
		elif 40 <= HDL_level < 60:
				return "Borderline low"
		else:
				return "Low"

def LDL_analysis(LDL_level):
						print(LDL_level)
						if LDL_level < 130:
								return "Normal"
						elif 130 <= LDL_level < 159:
								return "Borderline high"
						elif 160 <= LDL_level < 189:
								return "High"
						else:
								return "Very high"

def cholesterol_analysis():
		print("Cholesterol Analysis")
		input_val = input("Enter test result: ")
		test_info = input_val.split("=")
		if test_info[0] == "HDL":
				answer = HDL_analysis(int(test_info[1]))
				print("The {} level is {}".format(test_info[0],answer))
		elif test_info[0] == "LDL":
				answer = LDL_analysis(int(test_info[1]))
				print("The {} level is {}".format(test_info[0],answer))
		else:
    			print("We do not test for this")

def new_feature():
    	pass #says pass over this line

def name_function():
	first_name = "Sabrina"
	last_name = "Ward"
	full_name = [first_name, last_name]

def interface():
		while True:
				print("Cholesterol Calculator")
				print("Options: ")
				print(" 1 - Cholesterol Analysis")
				print(" 9 - Quit")
				choice = input("Enter your option: ")
				if choice == "9":
						return
				elif choice == "1":
						cholesterol_analysis()

if __name__ == "__main__":
		interface()
