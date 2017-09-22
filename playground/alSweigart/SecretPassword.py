
passwordFile = open('secretPasswordFile.txt')
secretPassword = passwordFile.read()
print('Enter password.')
typedPassword = input()
if typedPassword == secretPassword:
	print('Access granted.')
elif typedPassword == '1234':
	print('It\'s a common password.')
else:
	print('Access denied.')
	