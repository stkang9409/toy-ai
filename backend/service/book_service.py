from repository.book_repository import *
from core.dalle.dalle import fetch_image, translate
from core.chatGPT.chatgpt import *


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
