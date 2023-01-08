# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#from larousse_api import larousse
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from googletrans import Translator
from .classesEdt import APIlauncher, Formation, Enseignant, Salle, Matiere, UEO, Cours

import requests
#import pandas as pd
import json
import difflib
from datetime import datetime

url_code = 'https://edt-api.univ-avignon.fr/app.php/api/elements'
url_schedule = 'https://edt-api.univ-avignon.fr/app.php/api/events_promotion/{}'
dict_formation = {"ia":"Intelligence Artificielle","ilsen":"ingénieur logiciel de la societe numerique","sicom":"systemes informatiques communicants"}
dict_language = {'français':'fr','anglais':'en','arabe':'ar','espagnol':'es','korean':'ko'}

edtPromotions = []
edtPromIlsen = []
api = APIlauncher()



def get_code(formation_proximation):
    #elements = json.loads(requests.get(url_code).text)
    enseignants = api.getEnseignants()
    salles = api.getSalles()
    formations = api.getAllFormations()
    matieres = api.getAllMatieres()
    ueos = api.getAllUEOs()
    edtPromotions = api.getEDTpromotion()
    edtPromIlsen = apiLauncher.getEDTpromotionByGroupe("2-M2EN", "IA-IL-ALT")

def get_schedule(code):
        current_date = datetime.now()
        previous_class = edtPromIlsen[0]
        for cours in edtPromIlsen:
                if(datetime.strptime(cours.date, '%d-%m-%y') <= current_datedt.strftime("%d-%m-%Y")):
                        if (current_date.strftime("%H:%M") <= datetime.strptime(cours.hDebut, '%H:%M')):
                                matiere = matiere_code
                                for m in matieres:
                                        if m.code == matiere_code:
                                                matiere = m.nom
                                return(cours.hDebut, matiere, cours.type_cours, "","","")

def get_definition(sentence):
        url = "https://www.wikidata.org/w/api.php"

        params = {
        "action" : "wbsearchentities",
        "language" : "en",
        "format" : "json",
        "search" : sentence }
        data = requests.get(url,params=params)
        definition=data.json()["search"][0]["description"]
        return definition


def get_traduction(sentence):
        translator = Translator()
        translated = translator(source='auto', dest='en').translate(sentence)
        return translated

def get_meteo(cityName):
        langage = "fr"
        clef="d9f9917e0890ef12ae118a0f392ed5df"
        api_lien=f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={clef}&lang={langage}"

        json = requests.get(api_lien).json()
        JSON = json['weather'][0]['description']
        return JSON

class ActionDefinition(Action):
     def name(self) -> Text:
         return "action_definition"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             sentence = tracker.get_slot('word')
             definition = get_definition(sentence)
             message = definition
             dispatcher.utter_message(text=message)	
             return []
	


class ActionTranslation(Action):
     def name(self) -> Text:
         return "action_translation"
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             sentence = tracker.get_slot('trans')
             traduction = get_traduction(sentence)
             translated = traduction
             dispatcher.utter_message(text=translated)	
             return []


class ActionMeteo(Action):
     def name(self) -> Text:
         return "action_meteo"
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             sentence = tracker.get_slot('meteo')
             meteo = get_meteo(sentence)
             message = meteo
             dispatcher.utter_message(text=message)	
             return []
      