import unidecode
import time

final = open("outputs/final_output.csv", "w")
accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
 

################ TWITTER ##################

f = open("outputs/twitter_output.csv",'r')
lines  = f.readlines()
f.close()

for line in lines:
	line = unidecode.unidecode(line)
	final.write(line)
print("Scanning Twitter...")
time.sleep(2)

#################  FACEBOOK  ###############

#f = open("Parse_Facebook/out_facebook.csv",'r')
#lines  = f.readlines()
#f.close()

#for line in lines:
#	line = unidecode.unidecode(line)
#	final.write(line)
#print(Scanning Facebook...)

################  GOOGLE  #################

f = open("outputs/google_output.csv",'r')
lines  = f.readlines()
f.close()

for line in lines:
	line = unidecode.unidecode(line)
	final.write(line)
print("Scanning Google...")
time.sleep(1)

################  WEB  ###################

f = open("outputs/web_output.csv",'r')
lines  = f.readlines()
f.close()

for line in lines:
	line = unidecode.unidecode(line)
	final.write(line)
print("Scanning the planet...")
time.sleep(2)

print ("\nDone.")


print ("\n\n     iVenture\n\n   dP88  oP`Yb.\n  dP 88  `' dP'\n d888888   dP'  \n    88  .d8888 .fr \n\n\n")
