from common.config.load_config import get_openai_api_key
import openai

#[Image Generate]
def fetch_image(text):
    openai.api_key = get_openai_api_key()
    dalleResponse = openai.Image.create(
      prompt=text,
      n=2,
      size="1024x1024"
    )
    return dalleResponse["data"][0]['url']

#[테스트]
def fetch_image2():
    openai.api_key = get_openai_api_key()
    dalleResponse2 = openai.Image.create(
      prompt='나무꾼이 나무를 매우 세게 치다',
      n=2,
      size="1024x1024"
    )
    return dalleResponse2

#[Korean->English]
def translate(text):
  openai.api_key = get_openai_api_key()
  translatetext = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": f'Can you translate this into english? {text}'}
  ]
  )
  return translatetext.choices[0].message.content