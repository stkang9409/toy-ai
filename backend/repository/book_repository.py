from common.util.dbModule import get_conn


def save_book(hero, summary):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO books (hero, summary) VALUES (%s, %s)",
                   (str(hero), str(summary), ))
    conn.commit()
    book_id = cursor.lastrowid
    cursor.close()
    return book_id


def save_book_detail(book_id, seq, content, image_url):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO books_details (book_id, seq, content, image_url) VALUES (%s, %s, %s, %s)",
                   (book_id, seq, content, str(image_url)))
    conn.commit()
    cursor.close()


def save_book_histories(book_id, seq, content_list):
    print(content_list)
    if (len(content_list) != 4):
        raise Exception("content_list size is not 4")
    for i in range(4):
        save_book_history(book_id, seq, i+1, content_list[i])


def save_book_history(book_id, seq, candidate_num, content):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO books_histories (book_id, seq, candidate_num, content) VALUES (%s, %s, %s, %s)",
                   (book_id, seq, candidate_num, content))
    conn.commit()
    cursor.close()


def get_book(book_id):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT hero, summary FROM books WHERE id = %s", (book_id,))
    hero, summary = cursor.fetchone()
    cursor.close()
    return hero, summary


def get_book_history(book_id, seq, candidate_num):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT content FROM books_histories WHERE book_id = %s AND seq = %s AND candidate_num = %s",
                   (book_id, seq, candidate_num))
    content = cursor.fetchone()
    cursor.close()
    return content[0]


def get_book_histories(book_id, seq):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT candidate_num, content FROM books_histories WHERE book_id = %s AND seq = %s",
                   (book_id, seq))
    content_list = cursor.fetchall()
    cursor.close()
    return content_list


def get_book_detail(book_id, seq):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT content, image_url FROM books_details WHERE book_id = %s AND seq = %s",
                   (book_id, seq))
    content, image_url = cursor.fetchone()
    cursor.close()
    return content, image_url


def get_book_details_by_book_id(book_id):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT seq, content FROM books_details WHERE book_id = %s ORDER BY seq",
                   (book_id,))
    content_list = cursor.fetchall()
    cursor.close()
    return content_list
