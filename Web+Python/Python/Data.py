import os, sys, pythonFile, re, shutil, random, Convert
sys.path.insert(0, 'txt')
sys.path.insert(0, "png")


def style1():
	row1 = "-" * 25
	print(row1)
def style2():
	row1 = "*" * 10
	print(row1)	
def test():
	print("\033[1;32;40m Bright Green  \n")
	
def main():
		
	print("Valikko")
	style1()
	print("(1).Luo tiedosto")
	print("(2).Etsi tiedostosta")	
	print("(3).Kirjoita tiedostoon")
	print("(4).Poista tiedosto")
	print("(5).Kopioi tiedosto")
	print("(6).Konvertoi kuvat")
	print("(7).test zip")
	style1()
	myInput = input("Valitse numero: ")	
	if len(myInput) <= 0:
		pass
	elif len(myInput) >= 30:
		print("liika")
	elif myInput == "1":
		luoTiedosto()
	elif myInput == "2":
		SeachFile()		
	elif myInput == "3":
		tiedostot()
	elif myInput == "4":
		pythonFile.poistaTiedosto()
	elif myInput == "5":
		copyFile()
	elif myInput == "6":
		Convert.ConvertImages()
	elif myInput == "7":
		testMe.zip() 

def copyFile():
	os.system("clear")
	files = ["txt/A"]
	
	AFol = "txt/A/."
	CopyFiles = "txt/A-B-CopyFiles/" #Jos kansio ei ole olemassa toimii
	
	BFol = "txt/B/."	
	Afiles = [AFol]
	Bfiles = [BFol]
	print("(1).Kopioi A kansion tiedostot")
	print("(2).Kopioi B kansion tiedostot")
	print("(3).Takaisin")
	print("(4).Lopeta")
	im = input("Valitse numero: ")
	os.system("clear")
	
	if im == "1":
		# JOS KANSIO JO LÖYTYY
		# ~ if os.path.exists(ADes):
			# ~ shutil.rmtree(ADes)
			# ~ shutil.copytree(AFol, ADes)
		
		# ~ else:
			# ~ shutil.copytree(AFol, ADes)
			
		# ~ print (os.listdir(ADes))		
		for f in Afiles:
			os.system("cp -r "+f+" "+CopyFiles)
			
        
	elif im == "2":
		# ~ shutil.copytree(BFol, BDes)
		# ~ print (os.listdir(BDes))
		
		#AFol --> listaksi
		
		for f in Bfiles:
			os.system("cp -r "+f+" "+CopyFiles)
			print(os.system("cp -r "+f+" "+CopyFiles))
			#os.system("cp -r "+f+" "+ADes)		
def KillorLive():
	os.system("clear")
	print("(1).Valikko")
	print("(2).Lopeta")
	m = int(input("Valitse numero: "))
	if m == 1:
		valikko()
	elif m == 2:
		exit()
	else:		
		KillorLive()	
		
def SeachFile():	
	os.system("clear")
	AvaaTiedosto = open("txt/"+"data", "r")
	KatsoTiedosto = open("txt/"+"data", "r")
	print("\033[1;32;20m"+KatsoTiedosto.read())	
	style1()	
	Etsi = input("Etsi tiedostosta: ")	
	os.system("clear")
	style1()
	for line in AvaaTiedosto:
		if line.find(Etsi) != -1:
			print (line)
	AvaaTiedosto.close() 
	KatsoTiedosto.close()
	style1()
	print("(1).Etsi uudelleen?")
	print("(2).Lopeta")
	a = int(input("Valitse numero: "))
	if a == 1:
		SeachFile()
	elif a == 2:
		exit()
		
def openPythonFile():
	os.system("clear")
	pythonFile.functio1()
	
def tiedostot():
	os.system("clear")
	
	print("Valitse:")
	style1()
	print("(1).A-kamsio")
	print("(2).B-kansio")
	print("(3).Takaisin")
	style1()
	myInput = int(input("Valitse numero: "))
	if myInput == 1:	
		os.system("clear")		
		pythonFile.Alista()			
	elif myInput == 2:		
		pythonFile.Blista()		
	elif myInput == 3:
		os.system("clear")
		valikko()
def luoTiedosto():
	os.system("clear")	
	print("Luo tiedosto")
	style1()
	myInput = input("Kirjoita tiedoston nimi:")
	os.system("clear")
	print("Tiedoston nimi on:",myInput)
	style1()
	print("Mihin halua tallentaa tiedostoa?")
	style1()
	print("(1).A Folder")
	print("(2).B Folder")
	print("(3).Takaisin")
	style1()
	myInput2 = input("Valitse numero:")
	
	if myInput2 == "1":		
		os.system("clear")	
		Result = myInput
		txtFile = open("txt/"+"A/"+Result, "a+")		
		style1()
		print("Kirjoita tiedostoon:" + '"' + myInput+ '"')
		myInput2 = input("Kirjoita teksti: ")
		Result2 = myInput2
		print(txtFile.write(Result2))		
		os.system("clear")
		style1()
		txtFile.close()		
		KillorLive()		
			
	elif myInput2 == "2":
		os.system("clear")	
		Result = myInput
		txtFile = open("txt/"+"B/"+Result, "a+")		
		style1()
		print("Kirjoita tiedostoon:" + '"' + myInput+ '"')
		myInput2 = input("Kirjoita teksti: ")
		Result2 = myInput2
		print(txtFile.write(Result2))		
		os.system("clear")
		style1()
		txtFile.close()		
		KillorLive()	
			
	elif myInput2 == "3":
		valikko()
		
	
def tiedostotKaikki():
	print("Valitse tiedosto minkä haluat muokata")
	myInput = input("Kirjoita tiedoston nimi: ")
	

if __name__ == "__main__":
	main()

