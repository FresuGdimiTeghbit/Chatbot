import requests

class APIparser:
	urlBase = "https://edt-api.univ-avignon.fr/app.php/api/"
	headers = {'Authorization' : 'Bearer {YTIwZTZhY2EtZWU4My00NGJjLTgwMzMtYjQxZjMwNzhjMmI2OmMxOTlmOWM4LTA1NDgtNGJlNzk2NTUtN2VmN2Q3YmY5ZDIw}'}

	def getAuth(self):
		url = self.urlBase + 'auth'
		response = requests.get(url, headers=self.headers)
		print(response.json())
		return response.json()

	def printJSonResp(self, s):
		url = self.urlBase + s
		response = requests.get(url, headers=self.headers)
		print(response.json())
		return response.json()
		
	def printJSonRespParam(self, s, param):
		url = self.urlBase + s+"/"+param
		response = requests.get(url=url, headers=self.headers)
		print(response.json())
		return response.json()
		
	def printJSonRespPost(self, s):
		url = self.urlBase + s
		response = requests.post(url=url, headers=self.headers)
		print(response)
		return response.json()

	def getFormations(self):
		formationsJson = self.printJSonResp("elements")

	def getMatieres(self):
		matieresJson = self.printJSonResp("matieres/UE")

	def getUEO(self):
		ueoJson = self.printJSonResp("matieres/UEO")

	def getSalles(self):
		sallesJson = self.printJSonResp("salles")

	def getEnseignants(self):
		ensJson = self.printJSonResp("enseignants")

	def getSallesDiponibles(self, batiment, duree, heure_debut, date):
		s = "salles/disponibilite?site="+ batiment + "&duree=" + duree+ "&debut="+ heure_debut+"&date="+date
		self.printJSonResp(s)

	#printJSonResp("isOpen")

	def getEDTpromotion(self, formation):
		edtJson = self.printJSonRespParam("events_promotion", formation)

	def getEDTpromotionByGroupe(self, formation, groupe):
		groupeUrl = formation +"?TD=" + groupe 
		edtJson = self.printJSonRespParam("events_promotion", groupeUrl)

#printJSonRespParam("exportAgenda/salle","AGR_A002")
#getEDTpromotion("2-M2EN")
#getEDTpromotionByGroupe("2-M2EN", "2-M2EN?TD=M2IL-Cla-GR1")
#api = APIparser()
#api.getAuth()
#api.getSallesDiponibles("CERI", "3", "10.30", "2020-11-13")
#api.getEDTpromotion("2-M2EN")
#api.getSalles()
#api.getFormations()
#NOT WORKING
#printJSonResp("exportAgenda/diplome/{2-M2EN}")
#printJSonRespPost("users/{uapv1803030}/activate")
#printJSonRespPost("auth/login")
#printJSonResp("users")
#printJSonRespParam("events_salle","AGR_A002")
#printJSonResp("events_enseignant/fox%001")

