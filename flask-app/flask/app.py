# TODO: finish many to many relationship 
from flask import Flask, request, jsonify, redirect, url_for
from database import db
from flask_migrate import Migrate
from models.book import Book
from models.borrowlog import BorrowLog
from models.credential import Credential
from models.customer import Customer
from models.loginlog import LoginLog
from models.purchaselog import PurchaseLog
from models.returnlog import ReturnLog
from models.sharelog import ShareLog
from dotenv import load_dotenv
import os

base_url = 'booksharingstore'

# 載入 .env 檔案
load_dotenv()

DB_URI = os.getenv('DB_URI')

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate = Migrate(app, db)

    return app


def init_db(app):
    app = app
    from models.book import init_book_data
    from models.customer import init_customer_data
    from models.credential import init_credential_data

    with app.app_context():
        db.drop_all()
        db.create_all()
        for i in range(len(init_book_data)):
            book = Book(book_title=init_book_data[i]["book_title"],
                        book_author=init_book_data[i]["book_author"],
                        book_publisher_name=init_book_data[i]["book_publisher_name"],
                        book_publish_date=init_book_data[i]["book_publish_date"],
                        book_genre=init_book_data[i]["book_genre"],
                        book_language=init_book_data[i]["book_language"]
                        )
            db.session.add(book)

        for i in range(len(init_customer_data)):
            customer = Customer(customer_name=init_customer_data[i]["customer_name"],
                                customer_email=init_customer_data[i]["customer_email"],
                                customer_phone=init_customer_data[i]["customer_phone"],
                                customer_signup_time=init_customer_data[i]["customer_signup_time"]
                                )
            db.session.add(customer)

        for i in range(len(init_credential_data)):
            credential = Credential(customer_id=init_credential_data[i]["customer_id"],
                                    credential_password=init_credential_data[i]["credential_password"],
                                    credential_created_time=init_credential_data[i]["credential_created_time"]
                                    )
            db.session.add(credential)

        db.session.commit()


app = create_app()


@app.route(f'/{base_url}', methods=['GET'])
def index():
    return "Welcome to the Book Sharing Store!!!"


# get all customers
@app.route(f'/{base_url}/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    output = []

    for customer in customers:
        customer_data = {}
        customer_data['customer_id'] = customer.customer_id
        customer_data['customer_name'] = customer.customer_name
        customer_data['customer_email'] = customer.customer_email
        customer_data['customer_phone'] = customer.customer_phone
        customer_data['customer_signup_time'] = customer.customer_signup_time
        output.append(customer_data)
    return jsonify({'customers': output})


# get customer by id
@app.route(f'/{base_url}/customers/<int:customer_id>', methods=['GET'])
def get_customer_by_id(customer_id):
    customer = Customer.query.filter_by(customer_id=customer_id).first()
    if not customer:
        return jsonify({'message': 'No customer found!'})
    customer_data = {}
    customer_data['customer_id'] = customer.customer_id
    customer_data['customer_name'] = customer.customer_name
    customer_data['customer_email'] = customer.customer_email
    customer_data['customer_phone'] = customer.customer_phone
    customer_data['customer_signup_time'] = customer.customer_signup_time
    return jsonify({'customer': customer_data})


# get purchase books by customer id
@app.route(f'/{base_url}/customers/<int:customer_id>/purchased_books', methods=['GET'])
def get_purchased_books_by_customer_id(customer_id):
    purchase_logs = PurchaseLog.query.filter_by(customer_id=customer_id).all()
    output = []

    for purchase_log in purchase_logs:
        book = {}
        book["book_id"] = purchase_log.book.book_id
        book["book_title"] = purchase_log.book.book_title
        book["purchase_time"] = purchase_log.purchase_time
        book["purchase_price"] = purchase_log.purchase_price
        output.append(book)

    return jsonify({"purchased_books": output})

# get shared books by customer id
@app.route(f'/{base_url}/customers/<int:customer_id>/shared_books', methods=['GET'])
def get_shared_books_by_customer_id(customer_id):
    share_logs = ShareLog.query.filter_by(customer_id=customer_id).all()
    output = []

    for share_log in share_logs:
        book = {}
        book["book_id"] = share_log.book.book_id
        book["book_title"] = share_log.book.book_title
        book["share_time"] = share_log.share_time
        output.append(book)

    return jsonify({"shared_books": output})

# get borrowed books by customer id
@app.route(f'/{base_url}/customers/<int:customer_id>/borrowed_books', methods=['GET'])
def get_borrowed_books_by_customer_id(customer_id):
    borrow_logs = BorrowLog.query.filter_by(customer_id=customer_id).all()
    output = []

    for borrow_log in borrow_logs:
        book = {}
        book["book_id"] = borrow_log.book.book_id
        book["book_title"] = borrow_log.book.book_title
        book["borrow_time"] = borrow_log.borrow_time
        book["return_time"] = borrow_log.return_log.return_time
        output.append(book)

    return jsonify({"borrowed_books": output})

# get login history by customer id
@app.route(f'/{base_url}/customers/<int:customer_id>/login_history', methods=['GET'])
def get_login_history_by_customer_id(customer_id):
    login_logs = LoginLog.query.filter_by(customer_id=customer_id).all()
    output = []

    for login_log in login_logs:
        log = {}
        log["login_id"] = login_log.login_id
        log["login_time"] = login_log.login_time
        output.append(log)

    return jsonify({"login_history": output})


# get all books
@app.route(f'/{base_url}/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    output = []

    for book in books:
        book_data = {}
        book_data['book_id'] = book.book_id
        book_data['book_title'] = book.book_title
        book_data['book_author'] = book.book_author
        book_data['book_publisher_name'] = book.book_publisher_name
        book_data['book_publish_date'] = book.book_publish_date
        book_data['book_genre'] = book.book_genre
        book_data['book_language'] = book.book_language
        book_data['book_isbn'] = book.book_isbn
        book_data['book_price'] = book.book_price
        output.append(book_data)
    return jsonify({'books': output})

# login route
@app.route(f'/{base_url}/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.json
        email = data['email']
        password = data['password']
        customer = Customer.query.filter_by(customer_email=email).first()
        if customer:
            credential = Credential.query.filter_by(customer_id=customer.customer_id).order_by(Credential.credential_created_time.desc()).first()
            if credential.credential_password == password:
                login_log = LoginLog(customer_id=customer.customer_id)
                db.session.add(login_log)
                db.session.commit()
                return redirect(url_for('get_login_history_by_customer_id', customer_id=customer.customer_id))
            else:
                return jsonify({"message": "Invalid Password"})
        else:
            return jsonify({"message": "Invalid Email"})

# signup route
@app.route(f'/{base_url}/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        data = request.json
        name = data['name']
        email = data['email']
        phone = data['phone']
        password = data['password']
        customer = Customer(customer_name=name, customer_email=email, customer_phone=phone)
        db.session.add(customer)
        customer_id = Customer.query.filter_by(customer_email=email).first().customer_id
        credential = Credential(customer_id=customer_id, credential_password=password)
        db.session.add(credential)
        db.session.commit()
        return redirect(url_for('get_customer_by_id', customer_id=customer_id))
