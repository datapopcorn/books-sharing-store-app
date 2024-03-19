from database import db


class BorrowLog(db.Model):
    __tablename__ = 'borrow_log'
    borrow_id = db.Column(db.Integer, primary_key=True)
    return_log = db.relationship('ReturnLog', back_populates='borrow_log',
                                 uselist=False)
    share_id = db.Column(db.Integer, db.ForeignKey('share_log.share_id'),
                         nullable=False)
    share_log = db.relationship('ShareLog', back_populates='borrow_log',
                                uselist=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'),
                            nullable=False)
    customer = db.relationship('Customer', backref='borrow_log', lazy=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'),
                        nullable=False)
    book = db.relationship('Book', backref='borrow_log', lazy=True)
    borrow_time = db.Column(db.DateTime, nullable=False,
                            server_default=db.func.now())

    def __repr__(self):
        return f"""
        BorrowLog('{self.customer_id}', '{self.book_id}',
        '{self.borrow_time}')
        """
