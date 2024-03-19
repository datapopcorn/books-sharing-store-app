from database import db


class ShareLog(db.Model):
    __tablename__ = 'share_log'
    share_id = db.Column(db.Integer, primary_key=True)
    borrow_log = db.relationship('BorrowLog', back_populates='share_log',
                                 uselist=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'),
                            nullable=False)
    customer = db.relationship('Customer', backref='share_log', lazy=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'),
                        nullable=False)
    book = db.relationship('Book', backref='share_log', lazy=True)
    share_time = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now())

    def __repr__(self):
        return f"""
        ShareLog('{self.customer_id}', '{self.book_id}',
        '{self.share_time}')
        """
