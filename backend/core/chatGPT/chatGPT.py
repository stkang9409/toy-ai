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
    
    start_question = '''
    아래와같은 요약으로 5번 문단으로 나누어 책을 만들어줘
    '''+ str(book) + '''
    각 문단당 50자 이내로 해줘
    근데 내가 문단을 하나씩 물어볼게
    첫번째 문단을 행복한 분위기와 우울한 분위기로 옵션을 2개주세요.
    
    응답형식은 이렇게해줘
    {{1.행복한분위기: "", 2.우울한분위기: ""}}
    '''
    print(start_question)
    # {주인공 : [{이름 : 창훈, 상세설명: 나무꾼}, {이름 : 카리나, 상세설명: 선녀}], 요약 : 둘이사랑에 빠지는 얘기를 만들어줘}

    
    msg = gpt_response(start_question, message_list)
    return msg
    
def main():
    msg = gpt_response("안녕하세요?")
    return msg