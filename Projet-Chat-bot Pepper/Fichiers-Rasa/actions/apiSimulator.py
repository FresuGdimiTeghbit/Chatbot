#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
class APIsimulator:
	"""Simule l'API des edt"""
	def __init__(self):
		print("simulation de l'api")
		
	def getFormations(self):
		jsonFile = open('formations.json', encoding='utf-8')
		self.formationJsonRes = json(jsonFile)
		jsonFile.close()
		return self.formationJsonRes

	def getEnseignants(self):
		jsonFile = open('enseignants.json', encoding='utf-8')
		self.enseignantJsonRes = jsonFile
		jsonFile.close()
		#print(self.enseignantJsonRes)
		return self.enseignantJsonRes

	

	def getSalles(self):
		jsonFile = open('salles.json', encoding='utf-8')
		self.sallesJsonRes = jsonFile
		jsonFile.close()
		return self.sallesJsonRes

	def getMatieres(self):
		jsonFile = open('matieres.json', encoding='utf-8')
		self.matieresJsonRes = jsonFile
		jsonFile.close()
		return self.matieresJsonRes

	def getUEOs(self):
		jsonFile = open('ueos.json', encoding='utf-8')
		self.ueosJsonRes = jsonFile
		jsonFile.close()
		return self.ueosJsonRes

	def getEDTbyFormation(self):
		jsonFile = open('edt.json', encoding='utf-8')
		self.edtJsonRes = jsonFile
		jsonFile.close()
		return self.edtJsonRes

apiSim = APIsimulator()
#apiSim.getEnseignants()