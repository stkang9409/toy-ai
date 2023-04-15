
# #[Image Save]
# def insert_image_url(image_url):
#     connection = get_db_connection()
#     cursor = connection.cursor()

#     insert_query = "INSERT INTO images (image_url) VALUES (%s)"
#     data = (str(image_url),)

#     cursor.execute(insert_query, data)
#     connection.commit()

#     cursor.close()
#     connection.close()