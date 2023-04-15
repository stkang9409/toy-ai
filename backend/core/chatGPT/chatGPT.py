from common.utill.api_key import get_openAI_api_key
import openai


def generate_response(prompt, messages_before=None):
    if messages_before is None:
        messages_before = []

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "All the responses should be format of json.",
            },
            *messages_before,
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0]["message"]["content"]


def main():
    generate_response("안녕하세요?")