from database_11_11_22 import db

#my_model
class Developer(db.Model):
    __tablename__ = "developer"
    dev_name = db.Column(db.String(30))
    dept_no = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(30))

    def __init__(self, dev_name, dept_no, location):
        self.dev_name = dev_name
        self.dept_no = dept_no
        self.location = location
