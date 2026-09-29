import psycopg
import personal

data = {
    'host': "localhost",
    'port': 5432,
    'dbname': "platform",
    'user': "postgres",
    "password": personal.db_pass()
}

connection = psycopg.connect(**data)
cursor = connection.cursor()

cursor.execute("SELECT * FROM users")
result = cursor.fetchall()
print(result)

cursor.execute("SELECT * FROM users WHERE id = 1")
result = cursor.fetchone()
print(result)

# cursor.execute("INSERT INTO users (id, name) VALUES (2, \'John\')")
# cursor.execute("SELECT * FROM users")
# result = cursor.fetchall()
# print(result)

connection.commit()

cursor.close()
connection.close()