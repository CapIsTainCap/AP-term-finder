
try:
	def apFinder():		
		a = float(input("Enter the first term of the Arithmetic Progression: "))
		d = float(input("Enter the common difference of the Arithmetic Progression: "))
		n = float(input("Enter which term you want to find: "))

		print(a+(n-1)*d)
		restart = input("Do you want to try again? (yes/no): ")
		if restart.lower() == 'yes':
			apFinder()
		elif restart.lower() == 'no':
			print("Thank you for using this application.")
		else:
			print("Please enter either yes or no")
	apFinder()
  

  	
except ValueError:
	print("You entered an incorrect value. Please try again. ")
	
except ZeroDivisionError:
	print("Please don't divide by zero.")
	
except:
	print("Sorry, there was an error. Please try again.")
	