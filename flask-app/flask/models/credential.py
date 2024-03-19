from database import db


class Credential(db.Model):
    __tablename__ = 'credential'
    credential_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'),
                            nullable=False)
    customer = db.relationship('Customer', backref='credential', lazy=True)
    credential_password = db.Column(db.String(100), nullable=False)
    credential_created_time = db.Column(db.DateTime, nullable=False,
                                        server_default=db.func.now())

    def __repr__(self):
        return f"""
        Credential('{self.customer_id}',
        '{self.credential_password}',
        '{self.credential_created_time}')
        """


init_credential_data = [
    {
        "customer_id": 1,
        "credential_password": "password1",
        "credential_created_time": "2020-01-01 00:00:00"
    },
    {
        "customer_id": 2,
        "credential_password": "password2",
        "credential_created_time": "2021-01-01 00:00:00"
    },
    {
        "customer_id": 3,
        "credential_password": "password3",
        "credential_created_time": "2023-01-01 00:00:00"
    }
]
