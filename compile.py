#!/usr/bin/env python
import os
import py_compile
os.system("apt-get install figlet")
os.system("clear")
def menu():
	try:
		while True:
			os.system("figlet COMPILE")
			print(""" 
Welcome To Encrypt
			""")
			compiler = input("Enter the programme name: ")
			py_compile.compile(compiler)
			print("Successful")
			
	except KeyboardInterrupt:
		print(" Exiting...")
if __name__ == "__main__":
	menu()			
