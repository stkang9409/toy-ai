import openai
import json

from common.config.load_config import get_openai_api_key


def gpt_response(prompt, messages_before=None):
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


# 책을 만들어주는 GPT코드
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
