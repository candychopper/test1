import os
import os.path
a = "txt/A/"
items = sorted(os.listdir(a))
b = "txt/B/"
items2 = sorted(os.listdir(b))
def style01():
	a = "*" * 25
	print(a)
	
def Alista():
	os.system("clear")
	num = 0	
	styleRow1 = "\n" + "-" * 15 + "\n"
	print("A kansio")
	style01()
	for names in items:				
		if names.endswith(".txt"):							
			print("(",num,")",names)								
		num += 1
	style01()	
	myInput = input("Valitse tiedosto:")	
	os.system("clear")
	print("Valitsit: ",items[int(myInput)])
	print("(1).Katso")
	print("(2).Muokkaa")	
	test = items[int(myInput)]	
	l = input("Valitse numero: ")
	if l == "1":
		print(test)
	elif l == "2":
		os.system("clear")
		newInput = input("Kirjoita tiedostoon: ")				
		m = open("txt/"+"A/"+test, "w")		
		print(m.write(styleRow1))
		print(m.write(newInput))
		print(m.write(styleRow1))
		m.close()
		
def Blista():
	os.system("clear")
	num = 0	
	styleRow1 = "\n" + "-" * 15 + "\n"
	print("B kansio")
	style01()
	for names in items2:				
		if names.endswith(".txt"):							
			print("(",num,")",names)								
		num += 1
	style01()	
	myInput = input("Valitse tiedosto:")	
	os.system("clear")
	print("Valitsit: ",items2[int(myInput)])
	print("(1).Katso")
	print("(2).Muokkaa")	
	test = items2[int(myInput)]	
	l = input("Valitse numero: ")
	if l == "1":
		print(test)
	elif l == "2":
		os.system("clear")
		newInput = input("Kirjoita tiedostoon: ")				
		m = open("txt/"+"B/"+test, "w")		
		print(m.write(styleRow1))
		print(m.write(newInput))
		print(m.write(styleRow1))
		m.close()
		
def poistaTiedosto():
	os.system("clear")		
	print("Valitse kansio")
	print("(1).A")
	print("(2).B")	
	inp = input("Valitse: ")
	
	if inp == "1":
		os.system("clear")			
		num = 0
		for names in items:
			if names.endswith(".txt"):						
					print("(",num,")",names)
			num += 1
			
		myInput = input("Numero:")
		os.system("clear")
		print("Valitsit tiedosto poistamisee ",items[int(myInput)] +"!")
		print("-------")
		print("(1).Poista")
		print("(2).STOP!!!")		
		newInput = input("Valitse: ")
		
		if newInput == "1":
			os.system("clear")
			delete = items[int(myInput)]
			m = os.remove("txt/"+"A/"+delete)
			print("Poistit tiedostoon",delete)
		elif newInput == "2":
			print("Ei poistetaan!")
			
	elif inp == "2":
		os.system("clear")			
		num = 0
		for names in items2:
			if names.endswith(".txt"):						
					print("(",num,")",names)
			num += 1
			
		myInput = input("Numero:")
		os.system("clear")
		print("Valitsit tiedosto poistamisee ",items2[int(myInput)] +"!")
		print("-------")
		print("(1).Poista")
		print("(2).STOP!!!")		
		newInput = input("Valitse: ")
		
		if newInput == "1":
			os.system("clear")
			delete = items2[int(myInput)]
			m = os.remove("txt/"+"B/"+delete)
			print("Poistit tiedostoon",delete)
		elif newInput == "2":
			print("Ei poistetaan!")

