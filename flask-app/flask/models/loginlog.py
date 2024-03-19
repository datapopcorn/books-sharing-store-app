from database import db


class LoginLog(db.Model):
    __tablename__ = 'login_log'
    login_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'),
                            nullable=False)
    customer = db.relationship('Customer', backref='login_log', lazy=True)
    login_time = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now())

    def __repr__(self):
        return f"""
        LoginLog('{self.customer_id}', '{self.login_time}')
        """
