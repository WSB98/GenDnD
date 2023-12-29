from flask import Flask, render_template, request
from image_generation import generate_image, generate_map, generate_item_image
from  modelFarmInteraction import generate_backstory, generate_statBlock, generate_area, generate_custom_item, generate_encounter, generate_encounter_backstory
from dnd5eapi import get_all_monsters

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

# does more than get image
@app.route('/api/get_image', methods=['GET','POST'])
def get_image():
  responseText = ''
  backstory = ''
  returnDict = {}

  # take in the request
  print('Step 1')
  requestText = request.json['text']
  requestType = request.json['type']
  print('text: ',requestText,'\ntype: ',requestType)

  match requestType:
    case 'Character':
      # chat to modelFarm
      print('Character')
      # generate the image
      print('Step 2', f'Generating Image of a {requestText}')
      image = generate_image(requestText)
      # generate a stat block
      print('Step 3', f'Generating Description of a {requestText}')
      responseText = generate_statBlock(f'generate a stat block for a {requestText} that looks like: Name \n Race \n Class \n Level \n Alignment \n Hit Points \n Armor Class \n Ability scores \n Skills \n Languages \n Class features \n Actions \n Bonus actions \n Physical Appearance', f'generate a stat block for a {requestText} that looks like: Name \n Race \n Class \n Level \n Alignment \n Hit Points \n Armor Class \n Ability scores \n Skills \n Languages \n Class features \n Actions \n Bonus actions \n Physical Appearance')
      # generate the backstory
      print('Step 4', f'Generating History for a {requestText}')
      backstory = generate_backstory(requestText, requestText)
      # return all of the data
      print('Step 5', f'Building Return Data for a {requestText}')
      returnDict = {
        'statblock': responseText,
        'backstory': backstory,
        'image': image.data[0].url,
        'requestType':requestType
      }
    case 'Encounter':
      print('Step 2', f'Generating Image of a {requestText}')
      image = generate_image(requestText)
      print('Step 3', f'Generating Description of a {requestText}')
      monsterNames = get_all_monsters()
      responseText = generate_encounter(requestText,monsterNames)
      print('Step 4', f'Generating History for {requestText}')
      backstory = generate_encounter_backstory(requestText,requestText)
      # chat to modelFarm# return all of the data
      print('Step 5', f'Building Return Data for a {requestText}')
      returnDict = {
        'statblock': responseText,
        'backstory': backstory,
        'image': image.data[0].url,
        'requestType':requestType
      }
    case 'Area':
      print('Step 2', f'Generating Image of a {requestText}')
      image = generate_map(requestText)
      print('Step 3', f'Generating Description of a {requestText}')
      responseText = generate_area(requestText)
      print('Step 4', f'Generating History for a {requestText}')
      backstory = generate_backstory(requestText,requestText)
      
      # return all of the data
      print('Step 5', f'Building Return Data for a {requestText}')
      returnDict = {
        'statblock': responseText,
        'backstory': backstory,
        'image': image.data[0].url,
        'requestType':requestType
      }
    case 'Item':
      print('Step 2', f'Generating Image of a {requestText}')
      image = generate_item_image(requestText)
      print('Step 3', f'Generating Description of a {requestText}')
      responseText = generate_custom_item(requestText)
      print('Step 4', f'Generating History for a {requestText}')
      backstory = generate_backstory(requestText,requestText)
      
      # return all of the data
      print('Step 5', f'Building Return Data for a {requestText}')
      returnDict = {
        'statblock': responseText,
        'backstory': backstory,
        'image': image.data[0].url,
        'requestType':requestType
      }
    case _:
      print('something went wrong. please refresh and try again.')
      returnDict = {
        'statblock': responseText + 'something went wrong! please wait, refresh, and try again (:',
        'backstory': backstory,
        'image': 'no image',
        'requestType':requestType
      }
      
      
  return returnDict



app.run(host='0.0.0.0', port=82)
