from database import db


class Book(db.Model):
    __tablename__ = 'book'
    book_id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(100), nullable=False)
    book_author = db.Column(db.String(100), nullable=False)
    book_publisher_name = db.Column(db.String(100))
    book_publish_date = db.Column(db.Date)
    book_genre = db.Column(db.String(100))
    book_language = db.Column(db.String(100))
    book_isbn = db.Column(db.String(100), unique=True)
    book_price = db.Column(db.Float)

    def __repr__(self):
        return f"""
        Book('{self.book_title}', '{self.book_author}',
        '{self.book_publisher_name}', '{self.book_publish_date}',
        '{self.book_genre}', '{self.book_language}', '{self.book_isbn}',
        '{self.book_price}')
        """


init_book_data = [
    {
        "book_title": "Harry Potter and the Philosopher's Stone",
        "book_author": "J.K. Rowling",
        "book_publisher_name": "Bloomsbury",
        "book_publish_date": "1997-06-26",
        "book_genre": "Fantasy",
        "book_language": "English"
    },
    {
        "book_title": "Harry Potter and the Chamber of Secrets",
        "book_author": "J.K. Rowling",
        "book_publisher_name": "Bloomsbury",
        "book_publish_date": "1998-07-02",
        "book_genre": "Fantasy",
        "book_language": "English"
    },
    {
        "book_title": "Harry Potter and the Prisoner of Azkaban",
        "book_author": "J.K. Rowling",
        "book_publisher_name": "Bloomsbury",
        "book_publish_date": "1999-07-08",
        "book_genre": "Fantasy",
        "book_language": "English"
    },
    {
        "book_title": "Harry Potter and the Goblet of Fire",
        "book_author": "J.K. Rowling",
        "book_publisher_name": "Bloomsbury",
        "book_publish_date": "2000-07-08",
        "book_genre": "Fantasy",
        "book_language": "English"
    },
    {
        "book_title": "Harry Potter and the Order of the Phoenix",
        "book_author": "J.K. Rowling",
        "book_publisher_name": "Bloomsbury",
        "book_publish_date": "2003-06-21",
        "book_genre": "Fantasy",
        "book_language": "English"
    },
    {
        "book_title": "Harry Potter and the Half-Blood Prince",
        "book_author": "J.K. Rowling",
        "book_publisher_name": "Bloomsbury",
        "book_publish_date": "2005-07-16",
        "book_genre": "Fantasy",
        "book_language": "English"
    },
    {
        "book_title": "Harry Potter and the Deathly Hallows",
        "book_author": "J.K. Rowling",
        "book_publisher_name": "Bloomsbury",
        "book_publish_date": "2007-07-21",
        "book_genre": "Fantasy",
        "book_language": "English"
    }
]
