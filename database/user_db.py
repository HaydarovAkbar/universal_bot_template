import datetime
import sqlite3

db = "bot.db"

user_table_name = 'sys_user'
admin_table_name = 'sys_admin'
channel_table_name = "channels"
rek_table_name = "txt_rek"


class DatabaseDB:
    @staticmethod
    def get_user_if_id(user_id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {user_table_name} WHERE chat_id = {user_id}")
            response = cursor.fetchone()
            connection.close()
            return response
        except Exception:
            pass

    @staticmethod
    def get_user_50():
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {user_table_name} ORDER BY -id LIMIT 50")
        response = cursor.fetchall()
        connection.close()
        return response

    @staticmethod
    def get_user_all():
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(f"SELECT chat_id,fullname FROM {user_table_name}")
        response = cursor.fetchall()
        connection.close()
        return response

    @staticmethod
    def get_user_all_count():
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(f"SELECT count(id) FROM {user_table_name}")
        response = cursor.fetchone()
        connection.close()
        return response

    @staticmethod
    def check_admin(chat_id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {admin_table_name} WHERE chat_id = {chat_id}")
            response = cursor.fetchone()
            connection.close()
            return response
        except Exception:
            pass

    @staticmethod
    def get_admin_list():
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {admin_table_name}")
            response = cursor.fetchall()
            connection.close()
            return response
        except Exception:
            pass

    @staticmethod
    def insert_start_user(chat_id, username, joined_date, fullname):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        sql = f"INSERT INTO {user_table_name}(chat_id, username, lang, date_of_created,fullname) VALUES({chat_id}, '{username}','uz', '{joined_date}','{fullname}')"
        cursor.execute(sql)
        connection.commit()
        connection.close()
        return False

    @staticmethod
    def insert_user(chat_id, full_name, username, lang, joined_date, status, phone_number):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            sql = f"INSERT INTO {user_table_name}(chat_id, fullname, username, lang, date_of_created, status, phone_number) VALUES({chat_id}, '{full_name}', '{username}', '{lang}', '{joined_date}', '{status}', '{phone_number}')"
            cursor.execute(sql)
            connection.commit()
            connection.close()
            return True
        except Exception:
            return False

    @staticmethod
    def insert_rek(txt, date):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            sql = f"""INSERT INTO {rek_table_name}(text, date_of_created, status) VALUES(%s,%s, %s)"""
            cursor.execute(sql, (txt, date, 1))
            connection.commit()
            connection.close()
            return True
        except Exception:
            return False

    @staticmethod
    def insert_admin(chat_id, username):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            now = datetime.datetime.now().strftime('%Y-%m-%d')
            sql = f"INSERT INTO {admin_table_name}(chat_id, username, status,date_of_created) VALUES({chat_id}, '{username}', '1','{now}')"
            cursor.execute(sql)
            connection.commit()
            connection.close()
            return True
        except Exception:
            return False

    @staticmethod
    def get_rek_1():
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {rek_table_name} ORDER BY id DESC LIMIT 1 ")
            response = cursor.fetchone()
            connection.close()
            return response
        except Exception:
            pass

    @staticmethod
    def delete_admin(chat_id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM {admin_table_name} WHERE chat_id = {chat_id}")
            connection.commit()
            connection.close()
            return True
        except Exception:
            return False

    @staticmethod
    def insert_text_reklama(text, date, status=1):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            sql = f"""INSERT INTO {rek_table_name}(txt, created_date, status) VALUES("{text}", '{date}', '{status}')"""
            cursor.execute(sql)
            connection.commit()
            connection.close()
            return True
        except Exception:
            return False

    @staticmethod
    def update_reklama(id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            sql = f"""UPDATE {rek_table_name} SET status=0 WHERE id={id}"""
            cursor.execute(sql)
            connection.commit()
            connection.close()
            return True
        except Exception:
            return False

    @staticmethod
    def update_user_firstname(firstname, chat_id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            sql = f"""UPDATE {user_table_name} SET fullname='{firstname}' WHERE chat_id={chat_id}"""
            cursor.execute(sql)
            connection.commit()
            connection.close()
            return True
        except Exception:
            return False

    @staticmethod
    def find_user_with_name(txt):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {user_table_name} WHERE fullname LIKE '%{txt}%' OR username LIKE '%{txt}%'")
            response = cursor.fetchall()
            connection.close()
            return response
        except Exception:
            pass

    ## channels ----------------------------------
    @staticmethod
    def add_channel(channel_id, date_of_created, status, channel_name, url):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(
                f"INSERT INTO {channel_table_name}(channel_id, date_of_created, status, text, channel_url) VALUES('{channel_id}','{date_of_created}','{status}','{channel_name}','{url}')")
            connection.commit()
            connection.close()

            return True
        except Exception:
            return False

    @staticmethod
    def update_channel(channel_id, channel_name, url, channel_number):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(
                f"UPDATE {channel_table_name} SET text = '{channel_name}', channel_url = '{url}',channel_id = '{channel_id}' WHERE id = {channel_number}")
            connection.commit()
            connection.close()

            return True
        except Exception:
            return False

    @staticmethod
    def update_channel_status(channel_id, status):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"UPDATE {channel_table_name} SET status = '{status}' WHERE id = {channel_id}")
            connection.commit()
            connection.close()

            return True
        except Exception:
            return False

    @staticmethod
    def get_channel_where_id(channel_id):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {channel_table_name} where id={channel_id}")
        response = cursor.fetchone()
        connection.close()
        return response

    @staticmethod
    def get_all_channel():
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {channel_table_name} where status = '1'")
        response = cursor.fetchall()
        connection.close()
        return response

    @staticmethod
    def get_all_channel_id():
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(f"SELECT channel_id FROM {channel_table_name} where status = '1'")
        response = cursor.fetchall()
        connection.close()
        return response


if __name__ == '__main__':
    a = DatabaseDB()
