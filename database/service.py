import sqlite3

class Database:
    __DATABASE = 'db.sqlite3'
    
    @classmethod
    def create_users_table(cls):
        with sqlite3.connect(cls.__DATABASE) as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY UNIQUE NOT NULL, 
                        first_name TEXT NOT NULL UNIQUE,
                        is_newsletter INTEGER NOT NULL,
                        last_news TEXT
                        )""")
            
    @classmethod
    def set_user(cls, user_id: int, first_name: str):
        with sqlite3.connect(cls.__DATABASE) as conn:
            cur = conn.cursor()
            
            cur.execute("""
                        SELECT * FROM users
                        WHERE user_id=?
                        """, (user_id,))
            user = cur.fetchone()
            
            if not user:
                cur.execute("""
                            INSERT INTO users
                                (user_id, first_name, is_newsletter, last_news)
                            VALUES
                                (?, ?, 0, NULL)
                            """, (user_id, first_name))
            
    @classmethod
    def get_first_name(cls, user_id: int):
        with sqlite3.connect(cls.__DATABASE) as conn:
            cur = conn.cursor()
            cur.execute("""
                        SELECT first_name FROM users
                        WHERE user_id=?
                        """, (user_id,))
            
            first_name = cur.fetchone()
            return first_name[0]
        
    
    @classmethod
    def set_user_newsletter(cls, user_id: int, state: bool):
        with sqlite3.connect(cls.__DATABASE) as conn:
            cur = conn.cursor()
            cur.execute("""
                        UPDATE users
                        SET is_newsletter=?
                        WHERE user_id=?
                        """, (int(state), user_id))
            
    @classmethod
    def get_users_newsletter(cls):
        with sqlite3.connect(cls.__DATABASE) as conn:
            cur = conn.cursor()
            cur.execute("""
                        SELECT user_id FROM users
                        WHERE is_newsletter=1
                        """)
            
            users = cur.fetchall()
            return list(map(lambda x: x[0], users))
    
    @classmethod
    def get_last_news(cls, user_id: int):
        with sqlite3.connect(cls.__DATABASE) as conn:
            cur = conn.cursor()
            cur.execute("""
                        SELECT last_news FROM users
                        WHERE user_id=?
                        """, (user_id,))
            last_news = cur.fetchone()
        
        return last_news[0]
    
    @classmethod
    def set_last_news(cls, user_id: int, link: str):
        with sqlite3.connect(cls.__DATABASE) as conn:
            cur = conn.cursor()
            cur.execute("""
                        UPDATE users
                        SET last_news=?
                        WHERE user_id=?
                        """, (link, user_id))