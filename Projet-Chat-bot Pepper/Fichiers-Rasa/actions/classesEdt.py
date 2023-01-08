#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .apiSimulator import APIsimulator
#from edtAPI import APIparser
import json

sites = ['CERI', 'Agrosciences']

class Formation:
	def __init__(self, nom_f, code_f, search, categ_f):
		self.nom = nom_f
		self.code = code_f
		self.searchString = search
		self.categorie = categ_f
		#print(self.nom)

class Matiere:
	def __init__(self, nom_m, code_m, search):
		self.nom = nom_m
		self.code = code_m
		self.searchString = search
		#print(self.nom)

class UEO(Matiere):
	def __init__(self, nom_m, code_m, search):
		super(self, nom_m, code_m, search)

class Salle:
	def __init__(self, site_s, nom_s, searchString_s, code_s):
		self.site = site_s
		self.nom = nom_s
		self.searchString = searchString_s
		self.code = code_s
		#print(self.nom)

class Enseignant:
	def __init__(self, nom_e, code_e, uapv_e, search, email):
		self.nom = nom_e
		self.code = code_e
		self.uapv = uapv_e
		self.searchString = search
		self.email = email
		#print(self.nom)

class Cours:
	def __init__(self, date, f_code, m_code, enseignant, heure_debut, 
		heure_fin, s_code, type_c, grp):
		self.formationCode = f_code
		self.date = date
		self.matiereCode = m_code
		self.enseignant = enseignant
		self.hDebut = heure_debut
		self.hFin = heure_fin
		self.salleCode = s_code
		self.type_cours = type_c
		self.groupe = grp
		#print(self.matiereCode)

class APIlauncher:
	def __init__(self):
		self.simulator = APIsimulator()
		print("lancement du launcher")

	'''Renvoie toutes les formations'''
	def getAllFormations(self):
		jsonStr = json.loads(json.dumps(self.simulator.getFormations()))
		formations =[]
		for formation in jsonStr["results"]:
			nom = formation["names"][0]["name"]
			code = formation["names"][0]["code"]
			searchString = formation["names"][0]["searchString"]
			categorie = formation["letter"]
			f = Formation(nom, code, searchString, categorie)
			formations.append(f)
		return formations

	'''Renvoie toutes les matières'''
	def getAllMatieres(self):
		jsonStr = json.loads(json.dumps(self.simulator.getMatieres()))
		matieres =[]
		for matiere in jsonStr["results"]:
			nom = matiere["names"][0]["name"]
			code = matiere["names"][0]["code"]
			searchString = matiere["names"][0]["searchString"]
			m = Matiere(nom, code, searchString)
			matieres.append(m)
		return matieres

	'''Renvoie toutes les UEOs'''
	def getAllUEOs(self):
		jsonStr = json.loads(json.dumps(self.simulator.getUEOs()))
		matieres =[]
		for matiere in jsonStr["results"]:
			nom = matiere["names"][0]["name"]
			code = matiere["names"][0]["code"]
			searchString = matiere["names"][0]["searchString"]
			m = Matiere(nom, code, searchString)
			matieres.append(m)
		return matieres

	'''Renvoie toutes les salles'''
	def getSalles(self):
		jsonStr = json.loads(json.dumps(self.simulator.getSalles()))
		salles =[]
		for salle in jsonStr["results"]:
			json.loads(json.dumps(jsonStr))
			site = salle["letter"]
			for s in salle["names"]:
				json.loads(json.dumps(salle))
				nom = s["name"]
				searchString = s["searchString"]
				code = s["code"]
				s = Salle(site, nom, searchString, code)
				salles.append(s)
		return salles

	'''Renvoie tous les enseignants'''
	def getEnseignants(self):
		jsonStr = self.simulator.getEnseignants()
		ens =[]
		json.loads(json.dumps(jsonStr))
		for e in jsonStr["results"]:
			json.loads(json.dumps(jsonStr))
			try:
				nom = e["names"][0]["name"]
				code = e["names"][0]["code"]
				uapv = e["names"][0]["uapvHarpege"]
				searchString = e["names"][0]["searchString"]
				email = e["names"][0]["email"]
				enseignant = Enseignant(nom, code, uapv, searchString, email)
				ens.append(enseignant)
			except KeyError:
				print("key error")
		return ens

	'''Renvoie les emplois du temps de toutes les promotions'''
	def getEDTpromotions(self):
		jsonStr = json.loads(json.dumps(self.simulator.getEDTbyFormation()))
		matieres =[]
		for matiere in jsonStr["results"]:
			json.loads(json.dumps(jsonStr))
			formation = matiere["formation"]
			date = matiere["date"]
			for cours in matiere["names"]:
				json.loads(json.dumps(matiere))
				matiere = cours["matiereCode"]
				enseignant = cours["enseignant"]
				h1 = cours["heureDebut"]
				h2 = cours["heureFin"]
				salle = cours["salleCode"]
				type_c = cours["type"]
				groupe = cours["groupe"]
				m = Cours(date, formation, matiere, enseignant, h1, h2, salle, type_c, groupe)
				matieres.append(m)
		return matieres

	'''Renvoie l'emploi du temps d'une promotion'''
	def getEDTpromotionByFormation(self, promotion):
		jsonStr = json.loads(json.dumps(self.simulator.getEDTbyFormation()))
		matieres =[]
		for matiere in jsonStr["results"]:
			json.loads(json.dumps(jsonStr))
			formation = matiere["formation"]
			if(formation == promotion):
				date = matiere["date"]
				for cours in matiere["names"]:
					json.loads(json.dumps(matiere))
					groupe = cours["groupe"]
					matiere = cours["matiereCode"]
					enseignant = cours["enseignant"]
					h1 = cours["heureDebut"]
					h2 = cours["heureFin"]
					salle = cours["salleCode"]
					type_c = cours["type"]
					m = Cours(date, formation, matiere, enseignant, h1, h2, salle, type_c, groupe)
					matieres.append(m)
		return matieres

	'''Renvoie l'emploi du temps d'une promotion par groupe'''
	def getEDTpromotionByGroupe(self, promotion, grpe):
		jsonStr = json.loads(json.dumps(self.simulator.getEDTbyFormation()))
		matieres =[]
		for matiere in jsonStr["results"]:
			json.loads(json.dumps(jsonStr))
			formation = matiere["formation"]
			if(formation == promotion):
				date = matiere["date"]
				for cours in matiere["names"]:
					json.loads(json.dumps(matiere))
					groupe = cours["groupe"]
					grps = groupe.split(", ")
					for g in grps:
						if(g == grpe):
							matiere = cours["matiereCode"]
							enseignant = cours["enseignant"]
							h1 = cours["heureDebut"]
							h2 = cours["heureFin"]
							salle = cours["salleCode"]
							type_c = cours["type"]
							m = Cours(date, formation, matiere, enseignant, h1, h2, salle, type_c, groupe)
							matieres.append(m)
		return matieres

	'''Renvoie l'emploi du temps d'un enseignant'''
	def getEDTenseignant(self, e):
		jsonStr = json.loads(json.dumps(self.simulator.getEDTbyFormation()))
		matieres =[]
		for matiere in jsonStr["results"]:
			json.loads(json.dumps(jsonStr))
			formation = matiere["formation"]
			date = matiere["date"]
			for cours in matiere["names"]:
				json.loads(json.dumps(matiere))
				enseignant = cours["enseignant"]
				if enseignant == e:
					groupe = cours["groupe"]
					matiere = cours["matiereCode"]
					h1 = cours["heureDebut"]
					h2 = cours["heureFin"]
					salle = cours["salleCode"]
					type_c = cours["type"]
					m = Cours(date, formation, matiere, enseignant, h1, h2, salle, type_c, groupe)
					matieres.append(m)
		return matieres

	'''Renvoie l'emploi du temps d'une salle'''
	def getEDTsalle(self, s):
		jsonStr = json.loads(json.dumps(self.simulator.getEDTbyFormation()))
		matieres =[]
		for matiere in jsonStr["results"]:
			json.loads(json.dumps(jsonStr))
			formation = matiere["formation"]
			date = matiere["date"]
			for cours in matiere["names"]:
				json.loads(json.dumps(matiere))
				salle = cours["salleCode"]
				if salle == s:
					enseignant = cours["enseignant"]
					groupe = cours["groupe"]
					matiere = cours["matiereCode"]
					h1 = cours["heureDebut"]
					h2 = cours["heureFin"]
					type_c = cours["type"]
					m = Cours(date, formation, matiere, enseignant, h1, h2, salle, type_c, groupe)
					matieres.append(m)
		return matieres

	def isOccupe(self, edt_salle, h1, h2):
		for creneau in edt_salle:
			if creneau.hDebut == h1 and creneau.hFin == h2:
				return True
		return False

	'''Renvoie les salles libres sur un site à une période donnée'''
	def getSallesLibres(self, site, date, h1, h2):
		all_salles = self.getSalles()
		s = []
		for salle in all_salles:
			if salle.site == site:
				edt = self.getEDTsalle(salle.code)
				if not edt:
					s.append(salle)
					print(salle.code)
				for jour in edt:
					if jour.date == date and self.isOccupe(edt, h1, h2) == False:
						s.append(salle)
						print(salle.code)
		return s


apiLauncher = APIlauncher()
#apiLauncher.getEnseignants()
#apiLauncher.getSalles()
#apiLauncher.getAllFormations()
#apiLauncher.getAllMatieres()
#apiLauncher.getAllUEOs()
#apiLauncher.getEDTpromotion()
#apiLauncher.getEDTpromotionByGroupe("2-M2EN", "IA-IL-ALT")
#apiLauncher.getEDTpromotionByFormation("2-M2EN")
#apiLauncher.getEDTenseignant("Fabrice Lefèvre")
#apiLauncher.getEDTsalle("stat1")
#apiLauncher.getSallesLibres("CERI", "5-12-2022", "10:00", "13:00")