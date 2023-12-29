import openai
import os

api_key = os.environ['openAI_key']
openai.api_key = api_key

def generate_image(text):
    customPrompt = f'Design a circular Dungeons & Dragons character token of a {text}, done in a low poly style with minimal detail. Fit the character art within a circular frame. DO NOT include any words.'
    image = openai.Image.create(
        model="dall-e-2",
        prompt=customPrompt,
        n=1,
        size="512x512"
    )
    return image

def generate_map(text):
    customPrompt = f'Design a top down 3D dungeons and dragons combat map of a {text}. Include low poly texture detail and minimal background. DO NOT include any words.'
    image = openai.Image.create(
        model="dall-e-3",
        prompt=customPrompt,
        n=1,
        size="1792x1024",
        quality='standard'
    )
    return image

def generate_item_image(text):
  customPrompt = f'Design Dungeons & Dragons item art of a {text}, done in a low poly style with minimal detail. Fit the art within a circular frame. DO NOT include any words.'
  image = openai.Image.create(
      model="dall-e-2",
      prompt=customPrompt,
      n=1,
      size="512x512"
  )
  return image
