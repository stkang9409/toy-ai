from common.utill.api_key import get_openAI_api_key
import openai

def gpt_response(prompt, messages_before=None):
    openai.api_key = get_openAI_api_key()
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



def set_message_before(bef_message_list, question, answer):
    bef_message_list.append({"role": "user", "content": question, "role": "assistant", "content": answer}) 
    return bef_message_list



def book_create(book):
    message_list = []
    set_message_before(message_list, '내가 책을 5번에 이어서 설명해줄게', '좋아요, 기다리고 있겠습니다.')
    set_message_before(message_list, '첫번째 내용 : 선녀와 나무꾼이 연못에서 만났어', '네, 이해했습니다. 선녀와 나무꾼이 연못에서 만나는 장면은 이야기의 시작입니다. 이들은 서로의 존재를 알게 되고 서로에 대해 궁금해합니다. 이 장면은 새로운 인연이 시작되는 출발점이 되는 중요한 장면입니다.')
    print(message_list)
    
    msg = gpt_response('내가 설명한 책의 첫번째 내용이 뭐야?', message_list)
    return msg
    


def main():
    msg = gpt_response("안녕하세요?")
    return msg