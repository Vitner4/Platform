import psycopg
import personal


class DataBase:
    def __init__(self):
        self.connect = {
            'host': "localhost",
            'port': 5432,
            'dbname': "platform",
            'user': "postgres",
            "password": personal.db_pass()
        }
        self.connection = psycopg.connect(**self.connect)
        self.cursor = self.connection.cursor()

    def get_by_id(self, data_id) -> tuple | None:
        self.cursor.execute("SELECT * FROM users WHERE id = %s", (data_id,))
        return self.cursor.fetchone()
         
    def _commit(self):
        self.connection.commit()

    def _rollback(self):
        self.connection.rollback()

    def close(self):
        self.cursor.close()
        self.connection.close()


class Users(DataBase):
    def get(self) -> list:
        self.cursor.execute("SELECT * FROM users") 
        return self.cursor.fetchall()

    def create(self, id, name) -> None:
        try:
            self.cursor.execute("INSERT INTO users (id, name) VALUES (%s, %s)", (id, name))
            self._commit()
        except Exception:
            self._rollback()
            raise

    def update(self, id, name) -> None:
        try:
            self.cursor.execute("UPDATE users SET name = %s WHERE id = %s", (name, id))
            self._commit()
        except Exception:
            self._rollback()
            raise

    def delete(self, id) -> None:
        try:
            self.cursor.execute("DELETE FROM users WHERE id = %s", (id,))
            self._commit()
        except Exception:
            self._rollback()
            raise


# Class obj
users = Users()

# CRUD
print(users.get_by_id(1))
print(users.get())

users.delete(3)
print(users.get())

users.create(3, "Wolf")
print(users.get())

users.update(3, "Kine")
print(users.get())

# DB close
users.close()





