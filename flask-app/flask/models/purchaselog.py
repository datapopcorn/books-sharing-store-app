from database import db


class PurchaseLog(db.Model):
    __tablename__ = 'purchase_log'
    purchase_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'),
                            nullable=False)
    customer = db.relationship('Customer', backref='purchase_log', lazy=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'),
                        nullable=False)
    book = db.relationship('Book', backref='purchase_log', lazy=True)
    purchase_time = db.Column(db.DateTime, nullable=False,
                              server_default=db.func.now())
    purchase_price = db.Column(db.Float)

    def __repr__(self):
        return f"""
        PurchaseLog('{self.customer_id}', '{self.book_id}',
        '{self.purchase_time}', '{self.purchase_price}')
        """
