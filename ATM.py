import time

print("Please insert Your CARD")

time.sleep(1)

password = 1234

pin = int(input("Enter Your ATM PIN : "))

balance = 5000
if pin == password:
	while True:

		print("""
			1 == Balance
			2 == Withdraw Balance
			3 == Deposite Balance
			4 == EXIT
			"""
			)

		try:
			option = int(input("Please Enter Your Choice : "))
		except:
			print("Please enter valid option")


		if option == 1:
			print(f"Your Current Balance is : {balance}")

		if option == 2:

			withdraw_amount = int(input("Please Enter Withdraw Amount : "))

			balance = balance - withdraw_amount

			print(f"{withdraw_amount} is debited from your account ")

			print(f"Your Updated Balance is {balance}")

		if option == 3:

			deposite_amount = int(input("Please Enter Deposite Amount : "))

			balance = balance + deposite_amount

			print(f"{deposite_amount} Is Credited To Your Account")
			print(f"Your Updated Balance is {balance}")

		if option == 4:
			print(f"Thank you for Banking..!")

			break
else:
	print("Wrong pin Please try again")