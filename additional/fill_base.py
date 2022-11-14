from random import randint
from sqlite3 import connect
from uuid import uuid4

from additional.constants.data import Data


def clean_base(cursor):
    for name in ["AuthorBooks", "Authors", "Books", "Categories", "Genres", "Reviews", "Users"]:
        cursor.execute(f"delete from {name}")


def fill_base(filename, data):
    con = connect(filename)
    cur = con.cursor()
    clean_base(cur)
    con.commit()

    genres = set()
    users = {}
    authors = {}

    for category in data:
        category_id = str(uuid4())
        cur.execute("insert into Categories values (?, ?)", (category_id, category["name"]))
        for book in category['books']:
            book_id = str(uuid4())
            if book["genre"] not in genres:
                genres.add(book["genre"])
                genre_id = str(uuid4())
                cur.execute("insert into Genres values (?, ?)", (genre_id, book["genre"]))
            cur.execute("insert into Books values (?, ?, ?, ?, ?, ?)", (
                book_id,
                category_id,
                book["name"],
                book["price"],
                book["annotation"],
                genre_id
            ))
            authors_ids = []
            for author in book["authors"]:
                if author not in authors.keys():
                    author_id = str(uuid4())
                    authors_ids.append(author_id)
                    authors[author] = author_id
                    cur.execute("insert into Authors values (?, ?)", (author_id, author))

            for author_id in authors_ids:
                cur.execute("insert into AuthorBooks values (?, ?)", (book_id, author_id))

            for review in book["reviews"]:
                if review['name'] not in users.keys():
                    user_id = str(uuid4())
                    users[review['name']] = user_id
                    cur.execute("insert into Users values (?, ?)", (user_id, review["name"]))

                review_id = str(uuid4())
                cur.execute("insert into Reviews values (?, ?, ?, ?, ?)", (
                    review_id,
                    book_id,
                    users[review['name']],
                    randint(1, 5),
                    review['text']
                ))
    con.commit()


fill_base("../../forReact/base.db", data=Data.data)

