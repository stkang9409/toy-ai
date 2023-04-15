from common.utill.api_key import get_openAI_api_key
import openai

def fetch_image(text):
    openai.api_key = get_openAI_api_key()
    dalleResponse = openai.Image.create(
      prompt=text,
      n=2,
      size="1024x1024"
    )
    return dalleResponse

def fetch_image2():
    openai.api_key = get_openAI_api_key()
    dalleResponse2 = openai.Image.create(
      prompt='a white cat',
      n=2,
      size="1024x1024"
    )
    return dalleResponse2
