from replit.ai.modelfarm import ChatModel, ChatSession, ChatMessage
from dnd5eapi import get_all_monsters, get_monster, get_background, get_class, get_race, get_spell


def chat_to_modelFarm(messageHistory):
  model = ChatModel("chat-bison")
  response = model.chat([
    ChatSession(
      context="I want you to take a deep breath and think about the questions you are about to recieve step by step. You are a unique, generative Dungeons and Dragons assistant. Users will ask you to make parts of Dungeons and Dragons character's, and you will fulfill their request - nothing more, nothing less. DO NOT announce your presence as an assistant. Act as if you are an API.",
      examples=[
      ],
      messages=messageHistory,
    )
  ], temperature=0.2)

  responseText = response.responses[0].candidates[0].message.content

  return responseText
  
def generate_backstory(prevReq,messageHistory):
  chatHistory = [ChatMessage(author="USER", content=f"Write a short, 1-2 paragraph backstory for a {prevReq}. Do not include name, race, class, level, or subclass, unless directly mentioned in the backstory you create.")]
  responseText = chat_to_modelFarm(chatHistory)

  return responseText

def generate_encounter_backstory(prevReq,messageHistory):
  chatHistory = [ChatMessage(author="USER", content=f"Write a short, 1-2 paragraph backstory for an encounter with {prevReq}. Do not include name, race, class, level, or subclass, unless directly mentioned in the backstory you create.")]
  responseText = chat_to_modelFarm(chatHistory)

  return responseText

def generate_statBlock(prevReq,messageHistory):
  chatHistory = [ChatMessage(author="USER", content=messageHistory)]
  responseText = chat_to_modelFarm(chatHistory)

  return responseText

def generate_area(prevReq):
  chatHistory = [ChatMessage(author="USER", content=f"Create a description and outline of an area that is {prevReq}. Include potential monsters, treasure, and NPCs someone could meet here. Keep the design of the area modular so it can be used to createa a map or quickly shoe-horned into a story.")]
  responseText = chat_to_modelFarm(chatHistory)

  return responseText

def generate_custom_item(prevReq):
  chatHistory = [ChatMessage(author="USER", content=f"Create a stat block for a {prevReq} in the following format. Name: \n Type: \n Rarity: \n Damage: \n Weight: \n Properties: \n Special Features (if any): \n Description:")]
  responseText = chat_to_modelFarm(chatHistory)

  return responseText


def generate_encounter(prevReq,names):
  names = names['results']
  chatHistory = [ChatMessage(author="USER", content=f"Create an encounter that makes sense in the context of {prevReq} using monsters from the following list: {names}. Include some descriptions and details in the form of a stat block about the encounter.")]
  responseText = chat_to_modelFarm(chatHistory)

  monsters = []
  for o in names:
    if(o.lower() in responseText.lower()):
      monsters.append({"link":f'https://dndbeyond.com/monsters/{o}','name':o})

  return {"result":responseText, "monsters":monsters}
