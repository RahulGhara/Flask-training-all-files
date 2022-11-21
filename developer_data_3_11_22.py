from flask import request
from model_11_11_22 import Developer
from database_11_11_22 import db


class Dev_api:
    @staticmethod
    def add():
        dev_name = request.form['dev_name']
        dept_no = request.form['dept_no']
        location = request.form['location']

        new_dev = Developer(dev_name, dept_no, location)

        db.session.add(new_dev)
        db.session.commit()

        return "inserted"

    @staticmethod
    def view_all():
        dev = Developer.query.all()
        row = []
        for i in dev:
            record = {'name': i.dev_name,
                      'dept_no': i.dept_no,
                      'location': i.location
                      }
            row.append(record)
        return row

    @staticmethod
    def view(dept_no):
        dev = Developer.query.get(dept_no)
        arr1 = [dev.dev_name, dev.dept_no, dev.location]
        return arr1

    @staticmethod
    def update(dept_no):
        dev = Developer.query.get(dept_no)
        dev_name = request.form.get('dev_name')
        location = request.form.get('location')
        if dev_name is None and location is None:
            return 'Nothing updated'
        elif dev_name == '' and location == '':
            return 'No values given'
        elif dev_name is None:
            dev.location = location
            db.session.commit()
            return 'updated'
        elif location is None:
            dev.dev_name = dev_name
            db.session.commit()
            return 'updated'
        else:
            dev.dev_name = dev_name
            dev.location = location
            db.session.commit()
            return "updated"

    @staticmethod
    def delete(dept_no):
        dev = Developer.query.get(dept_no)
        db.session.delete(dev)
        db.session.commit()
        return 'row deleted'



