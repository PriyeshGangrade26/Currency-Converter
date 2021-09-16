while True:
	try:
		with open('Currency_Data.txt') as f:
			lines = f.readlines()

		currencyDict = {}
		for line in lines:
			parsed = line.split("\t")
			currencyDict[parsed[0]] = parsed[1]
		print("\n")
		print("\n")
		amount = int(input("Enter amount:\n"))
		print("\n")
		print("Enter the name of the currency you want to convert this amount to?\nAvailable Options:\n")
		[print(item) for item in currencyDict.keys()]
		try:
			print("\n")
			currency = input("Please enter one of these values:\n")
			print("\n")
			print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")
		except Exception as e:
			print("\n")
			print("\n")
			print("***  Please Enter A Correct Currency Name  ***")
			print("\n")
			print("\n")
	except Exception as e:
		print("\n")
		print("\n")
		print("***  Please Enter A Integer  ***")
		print("\n")
		print("\n")

		