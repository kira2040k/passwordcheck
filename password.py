from fun import *
def s():
	points=0
	password=input('input your passowrd:')
	points=len10(password,points)
	points=len8(password,points)
	points=capital(password,points)
	points=symbols(password,points)
	print("your password have",points,"points")
while True:
	s()
