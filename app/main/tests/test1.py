import json
import requests

BASE_URL = "https://hufflepuffbookstore.herokuapp.com"

response = requests.get(BASE_URL + "/books/3")
print(response)
#print(response.json())
print(json.dumps(response.json(), indent = 4))

all_books = [
    {
        "author": "Neil Gaiman",
        "book_id": 1,
        "name": "Norse Mythology",
        "published_date": "2018-10-24",
        "status": "Borrowed",
        "subject": "Mythology"
    },
    {
        "author": "Pierce Brown",
        "book_id": 3,
        "name": "Red Rising",
        "published_date": "2013-12-31",
        "status": "Borrowed",
        "subject": "Science Fiction"
    },
    {
        "author": "Ernest Cline",
        "book_id": 2,
        "name": "Ready Player One",
        "published_date": "2011-08-16",
        "status": "loaned out",
        "subject": "Science Fiction"
    },
    {
        "author": "Rick Riordan",
        "book_id": 40,
        "name": "The Titan's Curse",
        "published_date": "2007-04-01",
        "status": "Available",
        "subject": "Fantasy Fiction"
    },
    {
        "author": "string",
        "book_id": 41,
        "name": "string",
        "published_date": "2018-12-06",
        "status": "string",
        "subject": "string"
    }
]

print(all_books[1])





