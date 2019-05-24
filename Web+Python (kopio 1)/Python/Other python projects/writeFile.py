import os
def write():
	f=open("text", "a+")
	writehere = input("Kirjoita tiedostoon: ")
	total = writehere
	countLetter = len(total)
	printChars = countLetter
	f.write("-"*countLetter)
	f.write("\n")
	f.write(writehere)
	f.write("\n")
	f.write("-"*countLetter)
	f.write("\n\n")
	f.close()
def varoitusTeksti():
	row1 = "*" * 28
	print("\n")	
	print(row1)	
	print("Kirjoita alle 30 kirjainta!*")
	print(row1)	
	print("\n")

def option():
	row2 = "*" * 38
	space1 = " " * 15 
	space2 = " " * 14
	print(row2)
	print("*"+space1+"Valikko"+space2+"*")
	print(row2)
	print("*"+"(1)Kirjoita")
	print("*"+"(2)Lue")
	print("*"+"(3)Pyyhi tiedosto")
	print(row2+"\n")
	choise = input("Valitse: ")
	print("\n")
	
	if choise == "1":
		write()
	elif choise == "2":
		os.system("clear")
		print(r.read())		
	elif choise == "3":
		f=open("text", "w")
	else:		
		os.system("clear")
		option()
	
writehere = ""

while writehere != "close":
	r=open("text", "r+")
	f=open("text", "a+")
	writehere = input("Kirjoita tiedostoon: ")
	clear = writehere
	if len(writehere) <= 0:
		pass
	elif len(writehere) >= 30:
		varoitusTeksti()
		
	elif clear == "clear":
		f=open("text", "w")
	elif writehere == "/help":
		os.system("clear")
		option()	
	
	else:	
		total = writehere
		countLetter = len(total)
		printChars = countLetter
		f.write("-"*countLetter)
		f.write("\n")
		f.write(writehere)
		f.write("\n")
		f.write("-"*countLetter)
		f.write("\n\n")
	

	
