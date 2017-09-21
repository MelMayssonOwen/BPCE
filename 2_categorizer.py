count_twitter = 0
count_facebook = 0
count_google = 0
count_blog = 0
count_website = 0 
count_rh = 0
count_prod = 0
count_com = 0 
count_gouv = 0 
count_perf = 0 
count_concur = 0 
count_digital = 0 
count_client = 0 
count_good = 0 
count_average = 0 
count_bad = 0 
pop_twitter = 0
pop_facebook = 0
pop_google = 0
pop_blog = 0
pop_website = 0 
pop_rh = 0
pop_prod = 0
pop_com = 0 
pop_gouv = 0 
pop_perf = 0 
pop_concur = 0 
pop_digital = 0 
pop_client = 0 


#COUNT : POPULARITE BPCE, BP, CE, NATIXIS !!!!!!!!


prod = ["virement", "carte", "epargne", "credit", "pret", "assurance", "livret a", "livret b", "assurance vie", "pea", "ldd", "taux", "placement", "compte", "titre", "frais", "comission", "decouvert", "agios", "visa", "mastercard", "apple pay", "cb", "succession", "doublo", "cheque", "prelevement", "transfert", "retrait", "cnp", "e-commerce", "toxiques", "emprunt"] 

com = ["open innovation", "89C3", "voile", "basket", "jeux olympiques", "team", "opendata", "innovation", "assurance vie", "sponsoring", "sponsor"] 

gouv = ["Michel Grass", "François Pérol", "Marguerite Bérard-Andrieu", "Catherine Halberstadt", "Laurent Mignon", "Jacques Beyssade", "Yves Tyrode", "Laurent Roubin", "Jean-Yves Forel", "Gils Berrous", "Norbert Cron", "Anne Lebel", "Jean-François Lequoy", "André-Jean Olivier", "Jean Raby", "François Riahi", "Marc Vincent", "Pierre-Yves Dréan", "Jean-Pierre Levayer", "Bruno Deletré", "Gwilherm Le Donné", "Thierry Cahn", "Dominique Wein", "Bernard Dupouy", "Dominique Garnier", "Emmanuel Pouliquen", "Olivier de Marignan", "Dominique Martinie", "Daniel Karyotis", "Bruno Duchesne", "Michel Hillmeyer", "Christophe Bosson", "Philippe Hourdain", "Fabrice Bouvier", "André Samier", "Alain Condaminas", "Eric Sauer", "Maurice Bourrigaud", "Jean-Paul Dumortier", "Yves Gevin", "André Joffre", "Pierre Chauvois", "Gérard Bellemont", "Gonzague de Villèle", "Steve Gentili", "Olivier Klein", "Pierre Desvergnes", "Sylvie Garcelon", "Jean-Louis Bancel", "Christine Jacglin", "Serge Matry", "Michel Roux", "Astrid Boos", "Luc Carpentier", "Jean-Charles Boulanger", "Jean-François Paillissé", "Christian Ducher", "Paul Kerangueven", "Antoine-Sylvain Blanc", "Jean-Pierre Deramecourt", "Philippe Seguin", "Jean-Marc Carcélès", "Françoise Lemalle", "Christophe Pinault", "Daniel de Beaurepaire", "Didier Patault", "Pierre Valentin", "Christine Fabresse", "Jean Arondel", "Nicole Etchegoinberry", "Catherine Amin-Garde", "Stéphane Caminati", "Francis Henry", "Benoît Mercier", "Bernard Roux", "Pierre Carli", "Philippe Lamblin", "Alain Denisot", "Nicolas Plantrou", "Joël Chassard", "Yves Hubert", "Bernard Niglio", "Alain Lacroix", "Michel Manent", "Stéphanie Paix", "Bruno Goré", "Forence Raineix", "nomination", "nommer", "fusion"]

rh = ["recrutement", "embauche", "poste", "carriere", "employeur", "mobilite", "remuneration", "plan ", "effectif", "concours", "greve", "campus", "salon", "qualite ", "travail", "attractivite", "candidat", "candidature", "attractif", "CV", "emploi", "profil", "motivation", "talent", "recrute"]

perf = ["bourse", "boursier", "cours", "cotation", "resultat", "PNB", "strategie", "strategique", "gestion ", "risque", "fraude", "amende", "blanchiment", "asset ", "dividende", "actionnaire", "solvabilite", "ratio", "prudentiel", "liquidite", "LCR", "NSFR"]

concur = ["BNP", "LCL", "Credit Lyonnais", "Credit Agricole", "Credit Mutuel", "Societe Generale", "SG", "HSBC", "Banque Postale", "CIC", "Boursorama", "Fortuneo", "Monabanq", "Hellobank", "BforBank", "ING", "Carrefour Banque", "PSA Banque", "RCI Banque", "N26", "Revolut", "Nickel", "Arkea", "BCE", "ACPR", "EBA", "FBF", "GIE ", "reglementation", "banque ", "Bale"]

digital = ["application", "app", "banque ", "cyberplus", "cyber", "direct ", "turbo", "portail", "consultation", "consulter"]

client = ["reclamation", "accueil", "conseiller", "agence", "horaire", "service apres vente", "directeur", "mail", "telephone", "service client", "call center", "SAV", "mecontent", "relation", "attente", "competence", "competent", "incompetence", "incompetent", "responsable", "plainte", "cloture", "erreur", "delai", "guichet"]

with open("outputs/final_output.csv", "r") as f:
	lines = f.readlines()
f.close()
for line in lines:
	pop = 0
	if "good" in line: 
		count_good = count_good + 1
		pop = 1
	elif "average" in line: 
		count_average = count_average + 1
	elif "bad" in line: 
		count_bad = count_bad + 1
		pop = -1
	if "website" in line: 
		count_website += 1
		pop_website += pop
	elif "blog" in line: 
		count_blog += 1
		pop_blog += pop
	elif "Twitter" in line: 
		count_twitter += 1
		pop_twitter += pop
	elif "facebook" in line: 
		count_facebook += 1
		pop_facebook += pop
	elif "Google" in line:
		count_google += 1
		pop_google += pop
 


	for keyword in prod:
		if keyword in line:
			count_prod += 1
			pop_prod += pop
			break

	for keyword in com:
		if keyword in line:
			count_com += 1
			pop_com += pop
			break
	for keyword in gouv:
		if keyword in line:
			count_gouv += 1
			pop_gouv += pop
			break
	for keyword in rh:
		if keyword in line:
			count_rh += 1
			pop_rh += pop
			break
	for keyword in perf:
		if keyword in line:
			count_perf += 1
			pop_perf += pop
			break

	for keyword in concur:
		if keyword in line:
			count_concur += 1
			pop_concur += pop
			break
	
	for keyword in digital:
		if keyword in line:
			count_digital += 1
			pop_digital += pop
			break

	for keyword in client:
		if keyword in line:
			count_client += 1
			pop_client += pop
			break

f = open("variables.py", "w")


f.write("count_twitter = %d" % count_twitter + "\n" + "count_facebook = %d" % count_facebook + "\n" + "count_google = %d" % count_google + "\n" + "count_blog = %d" % count_blog + "\n" + "count_website = %d" % count_website + "\n" + "count_prod = %d" % count_prod + "\n" + "count_com = %d" % count_com + "\n" + "count_gouv = %d" % count_gouv + "\n" + "count_perf = %d" % count_perf + "\n" + "count_concur = %d" % count_concur + "\n" + "count_digital = %d" % count_digital + "\n" + "count_client = %d" % count_client + "\n" + "count_good = %d" % count_good + "\n" + "count_average = %d" % count_average + "\n" + "count_bad = %d" % count_bad + "\n" + "pop_twitter = %d" % pop_twitter + "\n" + "pop_facebook = %d" % pop_facebook + "\n" + "pop_google = %d" % pop_google + "\n" + "pop_blog = %d" % pop_blog + "\n" + "pop_website = %d" % pop_website + "\n" + "pop_prod = %d" % pop_prod + "\n" + "pop_com = %d" % pop_com + "\n" + "pop_gouv = %d" % pop_gouv + "\n" + "pop_perf = %d" % pop_perf + "\n" + "pop_concur = %d" % pop_concur + "\n" + "pop_digital = %d" % pop_digital + "\n" + "pop_client = %d" % pop_client + "\n" )
