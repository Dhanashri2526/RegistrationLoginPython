import csv
import re

print("Registration/Login")

def readFile():
	file = open('Users.csv')
	csvreader = csv.reader(file)
	header = []
	header = next(csvreader)
	print(header)
	users = []
	for user in csvreader:
	    users.append(user)
	# print(users)
	file.close()
	return users

def writeFile(email,password):
	# open the file in the write mode
	f = open('Users.csv', 'a')

	# create the csv writer
	writer = csv.writer(f)
	row = [email,password]
	# write a row to the csv file
	writer.writerow(row)

	# close the file
	f.close()

def createFile():
	# open the file in the write mode
	f = open('Users.csv', 'a')
	# create the csv writer
	writer = csv.writer(f)
	row = ['Email','Password']
	# write a row to the csv file
	writer.writerow(row)

	# close the file
	f.close()

def checkLogin(email,password):
	# Check validation
	regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
	if(re.fullmatch(regex, email) is None):
		print("Invalid Email")
		return False
	elif(len(password)<5 or len(password)>16):
		print("Invalid Password")
		return False
	else:
		return True


def showMenu():
	print("\n\nSelect Any")
	print("1.Registration")
	print("2.Login")
	print("3:Forgot Password")
	c = int(input())

	if c==1:
		print("Registration")
		register()
	elif c==2:
		print("Login")
		login()
	elif c==3:
		print("Forgot Password")
		forgotPassword()
	else:
		print("Invalid Choice")
		showMenu()

def register():
	print("Register")    
	email = input("Enter Email:")
	password = input("Enter Password:")
	if(checkLogin(email,password)):
		writeFile(email,password)
		print("Registred Successfully")
	else:
		print("Invalid")

	showMenu()

# writeFile("test@gmail.com","123456")
def login():
	print("Login")    
	email = input("Enter Email:")
	password = input("Enter Password:")
	if(checkLogin(email,password)):
		users = readFile()
		for user in users:
			if(user[0] == email and user[1] == password):
				print("Login Successfully")
				return
		print("Username or password is invalid")
	else:
		print("Invalid")
	showMenu()

def forgotPassword():
	print("Login")    
	email = input("Enter Email:")
	# if(checkLogin(email,password)):
	users = readFile()
	for user in users:
		if(user[0] == email):
			print("Your password is "+user[1])
			return
	print("Username is not present")
	# else:
	# 	print("Invalid")
	showMenu()

showMenu()