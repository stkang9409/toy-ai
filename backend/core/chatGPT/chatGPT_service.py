import json

import openai

from common.config.load_config import get_openai_api_key
from core.chatGPT.chatGPT_repository import *
from core.dalle.dalle import fetch_image, translate


def gpt_response(prompt, messages_before=None):
    print(prompt)
    openai.api_key = get_openai_api_key()
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


def set_message_before(bef_message_list, question=None, answer=None):
    if question:
        bef_message_list.append({"role": "user", "content": question})
    if answer:
        bef_message_list.append({"role": "assistant", "content": answer})
    return bef_message_list


def gpt_book_start(book):
    message_list = []

    start_question = '''
    아래와같은 요약으로 책을 만들어줘
    ''' + str(book) + '''
    각 문단당 50자 이내로 해줘
    책은 총 5개의 문단으로 구성되어야해
    
    한 문단씩 요약을 줄테니 너는 요약을 보고 문단을 만들어달라
    문단을 만들고 다음 문단이 될 수 있을 만한 요약도 네개 만들어서 함께달라.

    
    첫번째 문단을 만들어줘
    
    응답 형식:
{
    문단: "문단내용",
    다음문단후보: [요약1, 요약2, 요약3, 요약4]
}
    '''

    """
    한 문단씩 요약을 줄테니 너는 요약을 보고 문단을 만들어달라
    문단을 만들고 다음 문단이 될 수 있을 만한 요약도 세개 만들어서 함께달라.
    첫번째 문단과 이어지는 두번째 문단후보를 3개 만들어줘(행복한분위기의 문단, 무서운분위기의 문단, 불행한분위기의 문단)
    다음문단: [행복한분위기의 문단, 무서운분위기의 문단, 불행한분위기의 문단]
    2-1. 후보1: 행복한 분위기의 문단, 후보2: 행복한 분위기의 문단, 후보3: 무서운 분위기의 문단, 후보4: 불행한 분위기의 문단
    분위기별(행복한분위기1, 행복한분위기2, 무서운분위기, 불행한분위기)로 4개 만들어서 함께달라.
    """

    """
    {
    "book":
    {
    "hero" : [{"name": "햇님", "detail": "뜨거운태양"}, {"name": "달님", "detail": "차가운달"}],
    "summary": "해와 달이 싸우는 내용"
    }
}
    """

    # answer = gpt_response(start_question, message_list)
    # print(answer)

    # answer_dict = json.loads(answer)
    # print(answer_dict)

    #!!TODO 임시
    answer_dict = {'문단': '창훈은 대학 입학을 앞두고 새로운 시작을 약간의 두려움과 함께 기다리고 있었다. 그러던 어느 날 카리나를 만나게 된다.', '다음문단후보': [
        '카리나와의 첫 만남', '카리나에게 반해버린 이유', '창훈과 카리나의 대화', '창훈과 카리나의 운동']}
    print(answer_dict)

    book_id = save_book(book["hero"])
    content = answer_dict['문단']
    next_content_list = answer_dict["다음문단후보"]
    save_book_detail(book_id, 1, content, fetch_image(translate(content)))
    save_book_histories(book_id, 2, next_content_list)

    return book_id


def start_book(book):
    book_id = save_book(book["hero"], book["summary"])
    content, next_content_list = gpt_make_next_content(
        book["hero"], book["summary"])
    save_book_detail(book_id, 1, content, fetch_image(translate(content)))
    save_book_histories(book_id, 2, next_content_list)
    return book_id


def save_next_book_content(book_id, seq, candidate_num):
    next_seq = str(int(seq)+1)
    next_content = get_book_history(book_id, next_seq, candidate_num)
    hero, summary = get_book(book_id)

    next_content_list = gpt_make_next_content(
        hero, summary, {k: v for k, v in get_book_details_by_book_id(book_id)})

    save_book_detail(book_id, next_seq, next_content,
                     fetch_image(translate(next_content)))
    save_book_histories(book_id, str(int(next_seq)+1), next_content_list)


def get_book_content(book_id, seq):
    next_seq = str(int(seq)+1)
    content, image_url = get_book_detail(book_id, seq)
    next_content_list = get_book_histories(book_id, next_seq)
    print(next_content_list)
    return {"content": content, "image_url": image_url, "next_content_list": next_content_list}


def gpt_make_next_content(hero, summary, content_history: dict = None):
    gpt_history = []
    set_message_before(gpt_history,
"""
책을 만들어줘 책은 총 5개의 문단으로 구성되어야해 각 문단당 50자 이내로 해줘
주인공 정보는 다음과 같아
""" + str(hero) +
        """
책 요약은 다음과 같아
""" + str(summary), None)

    if not content_history:
        answer = gpt_response(
            """
문단은 하나씩 만들어줘

첫 문단을 만들고 다음 문단이 될 수 있을 만한 요약도 4개 만들어서 함께달라.

응답형식을 꼭 지켜서 응답해줘

응답 형식:
{
    문단: "문단내용",
    다음문단후보: [요약1, 요약2, 요약3, 요약4]
}""", gpt_history)
        print(answer)
        answer_dict = json.loads(answer)
        return answer_dict["문단"], answer_dict["다음문단후보"]

    else:
        for k, v in content_history.items():
            set_message_before(gpt_history,
                               str(k) + """번째 문단은 다음과 같아
""" + str(v),
                None)
        answer = gpt_response(
            str(len(content_history)) + """번째 문단의 다음 문단이 될 수 있을 만한 요약을 4개 만들어서 함께달라. 

응답형식을 꼭 지켜서 응답해줘

응답 형식:
{
    다음문단후보: [요약1, 요약2, 요약3, 요약4]
}""", gpt_history)

        print(gpt_history)
        print(answer)
        answer_dict = json.loads(answer)
        return answer_dict["다음문단후보"]


def main():
    msg = gpt_make_next_content([{"name": "선녀", "detail": "착하고 이쁘다"}, {
                                "name": "나무꾼", "detail": "도끼를 훔쳤다"}], "선녀와 나무꾼이 우연히 연못에서 만나는 이야기")
    return msg
