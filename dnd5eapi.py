import requests


fiveE_url = 'https://www.dnd5eapi.co/api/'

shortHand = {
    "ability-scores": "https://www.dnd5eapi.co/api/ability-scores",
    "alignments": "https://www.dnd5eapi.co/api/alignments",
    "backgrounds": "https://www.dnd5eapi.co/api/backgrounds",
    "classes": "https://www.dnd5eapi.co/api/classes",
    "conditions": "https://www.dnd5eapi.co/api/conditions",
    "damage-types": "https://www.dnd5eapi.co/api/damage-types",
    "equipment": "https://www.dnd5eapi.co/api/equipment",
    "equipment-categories": "https://www.dnd5eapi.co/api/equipment-categories",
    "feats": "https://www.dnd5eapi.co/api/feats",
    "features": "https://www.dnd5eapi.co/api/features",
    "languages": "https://www.dnd5eapi.co/api/languages",
    "magic-items": "https://www.dnd5eapi.co/api/magic-items",
    "magic-schools": "https://www.dnd5eapi.co/api/magic-schools",
    "monsters": "https://www.dnd5eapi.co/api/monsters",
    "proficiencies": "https://www.dnd5eapi.co/api/proficiencies",
    "races": "https://www.dnd5eapi.co/api/races",
    "rule-sections": "https://www.dnd5eapi.co/api/rule-sections",
    "rules": "https://www.dnd5eapi.co/api/rules",
    "skills": "https://www.dnd5eapi.co/api/skills",
    "spells": "https://www.dnd5eapi.co/api/spells",
    "subclasses": "https://www.dnd5eapi.co/api/subclasses",
    "subraces": "https://www.dnd5eapi.co/api/subraces",
    "traits": "https://www.dnd5eapi.co/api/traits",
    "weapon-properties": "https://www.dnd5eapi.co/api/weapon-properties"
}

# get a spell
def get_spell(spell_name):
  endpoint = fiveE_url + 'spells/' + spell_name
  response = requests.get(endpoint)
  return response.json()

def get_class(class_name):
  endpoint = fiveE_url + 'classes/' + class_name
  response = requests.get(endpoint)
  return response.json()

def get_race(race_name):
  endpoint = fiveE_url + 'races/' + race_name
  response = requests.get(endpoint)
  return response.json()

def get_background(background_name):
  endpoint = fiveE_url + 'backgrounds/' + background_name
  response = requests.get(endpoint)
  return response.json()

def get_subraces(race_name):
  endpoint = fiveE_url + 'races/' + race_name + '/subraces'
  response = requests.get(endpoint)
  return response.json()

def get_features(feature_name):
  endpoint = fiveE_url + 'features/' + feature_name
  response = requests.get(endpoint)
  return response.json()

def get_monster(monster_name):
  endpoint = fiveE_url + 'monsters/' + monster_name
  response = requests.get(endpoint)
  return response.json()

def get_magic_school(school):
  endpoint = fiveE_url + 'magic-schools/' + school
  response = requests.get(endpoint)
  return response.json()

def get_damage_type(school):
  endpoint = fiveE_url + 'damage-types/' + school
  response = requests.get(endpoint)
  return response.json()

def get_all_monsters():
  endpoint = shortHand.get('monsters')
  response = requests.get(endpoint)
  

  names = []
  res = response.json()['results']
  for o in res:
    names.append(o['name'])
    
  return {"results":names}

  