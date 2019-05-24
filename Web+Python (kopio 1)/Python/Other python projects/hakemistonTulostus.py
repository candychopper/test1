import os
import subprocess

#a = os.listdir()



process = subprocess.Popen(['ls'], stdout=subprocess.PIPE)
stdout = str(process.communicate()[0])

#print(stdout)
#exit()

lista = stdout.split('\\n')

for file in range(0,len(lista)-1):
    print(lista[file])

    
print("")
print("Folder has {} files".format(len(lista)))


