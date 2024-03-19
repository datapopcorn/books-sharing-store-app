from database import db


class Customer(db.Model):
    __tablename__ = 'customer'
    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), unique=True, nullable=False)
    customer_phone = db.Column(db.String(20))
    customer_signup_time = db.Column(db.DateTime)

    def __repr__(self):
        return f"""
        Customer('{self.customer_name}', '{self.customer_email}',
        '{self.customer_phone}', '{self.customer_signup_time}')
        """


init_customer_data = [
    {
        "customer_name": "Ian",
        "customer_email": "Ian@mail.com",
        "customer_phone": "389243242",
        "customer_signup_time": "2020-01-01 00:00:00"
    },
    {
        "customer_name": "Joe",
        "customer_email": "Joe@mail.com",
        "customer_phone": "3894545352",
        "customer_signup_time": "2021-01-01 00:00:00"
    },
    {
        "customer_name": "Jack",
        "customer_email": "Jack@mail.com",
        "customer_phone": "37657422",
        "customer_signup_time": "2023-01-01 00:00:00"
    }
]
