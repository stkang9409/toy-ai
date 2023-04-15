from common.utill.api_key import get_openAI_api_key
import openai

def fetch_image():
    openai.api_key = get_openAI_api_key()
    image = openai.Image.create(
      prompt="A cute baby sea otter",
      n=2,
      size="1024x1024"
    )
    return image

