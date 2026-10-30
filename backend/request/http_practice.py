import requests

# Пример
# response = requests.get(
#     "https://jsonplaceholder.typicode.com/posts/1"
# )

# print(response.status_code)
# print(response.headers["Content-Type"])
# print(response.json())

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "My first post",
    "body": "Learning HTTP with Python",
    "userId": 1
}

# Практика
def func():
    post = requests.post(url, json=data)
    response = requests.get(url, params={"userId": 1})

    print(response.status_code)
    post = response.json()
    print(len(post))
    print(post)

