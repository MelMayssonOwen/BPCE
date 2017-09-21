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
good_twitter = 0
average_twitter = 0
bad_twitter = 0
good_facebook = 0
average_facebook = 0
bad_facebook = 0
good_google = 0
average_google = 0
bad_google = 0
good_blog = 0
average_blog = 0
bad_blog = 0
good_website = 0 
average_website = 0 
bad_website = 0 
good_rh = 0
average_rh = 0
bad_rh = 0
good_prod = 0
average_prod = 0
bad_prod = 0
good_com = 0 
average_com = 0 
bad_com = 0 
good_gouv = 0 
average_gouv = 0 
bad_gouv = 0 
good_perf = 0 
average_perf = 0 
bad_perf = 0 
good_concur = 0 
average_concur = 0 
bad_concur = 0 
good_digital = 0 
average_digital = 0 
bad_digital = 0 
good_client = 0 
average_client = 0 
bad_client = 0 


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
	good = 0
        bad = 0
        average = 0
	if "good" in line: 
		count_good = count_good + 1
		 good = 1
	elif "average" in line: 
		count_average = count_average + 1
                average = 1
	elif "bad" in line: 
		count_bad = count_bad + 1
		bad = 1
	if "website" in line: 
		count_website += 1
		good_website += good
		average_website += average
		bad_website += bad
	elif "blog" in line: 
		count_blog += 1
		good_blog += good
		average_blog += average
		bad_blog += bad
	elif "Twitter" in line: 
		count_twitter += 1
		good_twitter += good
		average_twitter += average
		bad_twitter += bad
	elif "facebook" in line: 
		count_facebook += 1
		good_facebook += good
		average_facebook += average
		bad_facebook += bad
	elif "Google" in line:
		count_google += 1
		good_google += good
		average_google += average
		bad_google += bad
 
        for keyword in prod:
		if keyword in line:
			count_prod += 1
			good_prod += good
			average_prod += average
			bad_prod += bad
			break

	for keyword in com:
		if keyword in line:
			count_com += 1
			good_com += good
			average_com += average
			bad_com += bad
			break
	for keyword in gouv:
		if keyword in line:
			count_gouv += 1
			good_gouv += good
			average_gouv += average
			bad_gouv += bad
			break
	for keyword in rh:
		if keyword in line:
			count_rh += 1
			good_rh += good
			average_rh += average
			bad_rh += bad
			break
	for keyword in perf:
		if keyword in line:
			count_perf += 1
			good_perf += good
			average_perf += average
			bad_perf += bad
			break

	for keyword in concur:
		if keyword in line:
			count_concur += 1
			good_concur += good
			average_concur += average
			bad_concur += bad
			break
	
	for keyword in digital:
		if keyword in line:
			count_digital += 1
			good_digital += good
			average_digital += average
			bad_digital += bad
			break

	for keyword in client:
		if keyword in line:
			count_client += 1
			good_client += good
			average_client += average
			bad_client += bad
			break

f = open("variables.py", "w")

f.write("count_twitter = %d" % count_twitter + "\n" + "count_facebook = %d" % count_facebook + "\n" + "count_google = %d" % count_google + "\n" + "count_blog = %d" % count_blog + "\n" + "count_website = %d" % count_website + "\n" + "count_prod = %d" % count_prod + "\n" + "count_com = %d" % count_com + "\n" + "count_gouv = %d" % count_gouv + "\n" + "count_perf = %d" % count_perf + "\n" + "count_concur = %d" % count_concur + "\n" + "count_digital = %d" % count_digital + "\n" + "count_client = %d" % count_client + "\n" + "count_good = %d" % count_good + "\n" + "count_average = %d" % count_average + "\n" + "count_bad = %d" % count_bad + "\n" + "good_twitter = %d" % good_twitter + "\n" + "average_twitter = %d" % average_twitter + "\n" + "bad_twitter = %d" % bad_twitter + "\n" + "good_facebook = %d" % good_facebook + "\n" + "average_facebook = %d" % average_facebook + "\n" + "bad_facebook = %d" % bad_facebook + "\n" + "good_google = %d" % good_google + "\n" + "average_google = %d" % averaged_google + "\n" + "bad_google = %d" % bad_google + "\n" + "good_blog = %d" % good_blog + "\n" + "average_blog = %d" % average_blog + "\n" + "bad_blog = %d" % bad_blog + "\n" + "good_website = %d" % good_website + "\n" + "average_website = %d" % average_website + "\n" + "bad_website = %d" % bad_website + "\n" + "good_prod = %d" % good_prod + "\n" + "average_prod = %d" % average_prod + "\n" + "bad_prod = %d" % bad_prod + "\n" + "good_com = %d" % good_com + "\n" + "average_com = %d" % average_com + "\n" + "bad_com = %d" % bad_com + "\n" + "good_gouv = %d" % good_gouv + "\n" + "average_gouv = %d" % average_gouv + "\n" + "bad_gouv = %d" % bad_gouv + "\n" + "good_perf = %d" % good_perf + "\n" + "average_perf = %d" % average_perf + "\n" + "bad_perf = %d" % bad_perf + "\n" + "good_concur = %d" % good_concur + "\n" + "average_concur = %d" % average_concur + "\n" + "bad_concur = %d" % bad_concur + "\n" + "good_digital = %d" % good_digital + "\n" + "average_digital = %d" % average_digital + "\n" + "bad_digital = %d" % bad_digital + "\n" + "good_client = %d" % good_client + "\n" + "average_client = %d" % average_client + "\n" + "bad_client = %d" % bad_client + "\n") 
f.close()
