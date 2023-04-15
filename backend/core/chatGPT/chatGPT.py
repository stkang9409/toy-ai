from common.config.load_config import get_openai_api_key
from common.util.session_history import set_history, get_history
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



def set_message_before(user_uuid, question, answer):
    user_history = get_history(user_uuid)
    user_history.append({"role": "user", "content": question, "role": "assistant", "content": answer}) 
    set_history(user_uuid, user_history)
    return user_history


def create_book(book, user_uuid):
    message_list = []
    
    start_question = '''
    아래와같은 요약으로 5번 문단으로 나누어 책을 만들어줘
    '''+ str(book) + '''
    각 문단당 50자 이내로 해줘
    한 문단씩 요약을 줄테니 너는 요약을 보고 문단을 만들어달라
    문단을 만들고 다음 문단이 될 수 있을 만한 요약도 세개 만들어서 함께달라.

    
    응답 형식:
{
    문단: "문단내용",
    다음문단: ["요약1", "요약2", "요약3"]
}
    '''
    # print(start_question)
    # {주인공 : [{이름 : 창훈, 상세설명: 나무꾼}, {이름 : 카리나, 상세설명: 선녀}], 요약 : 둘이사랑에 빠지는 얘기를 만들어줘}
    
    answer = gpt_response(start_question, message_list)
    set_message_before(user_uuid, start_question, answer)
    return answer

def get_next_book_content(user_uuid, seq):
    question = str(seq)+"요약을 주세요"
    set_message_before(user_uuid, start_question, answer)
    
    
    
    
def main():
    msg = gpt_response("안녕하세요?")
    return msg