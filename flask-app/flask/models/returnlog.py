from database import db


class ReturnLog(db.Model):
    __tablename__ = 'return_log'
    return_id = db.Column(db.Integer, primary_key=True)
    borrow_id = db.Column(db.Integer, db.ForeignKey('borrow_log.borrow_id'),
                          nullable=False)
    borrow_log = db.relationship('BorrowLog', back_populates='return_log',
                                 uselist=False)
    return_time = db.Column(db.DateTime, nullable=False,
                            server_default=db.func.now())

    def __repr__(self):
        return f"""
        ReturnLog('{self.borrow_id}', '{self.return_time}')
        """
