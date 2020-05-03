from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class District(db.Model):
    __tablename__ = 'districts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    streets = db.relationship('Street')
    request_help = db.relationship('RequestHelp')


class Street(db.Model):
    __tablename__ = 'streets'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    district_id = db.Column(db.Integer, db.ForeignKey('districts.id'))
    district = db.relationship('District')
    volunteers = db.relationship('Volunteer')
    request_help = db.relationship('RequestHelp')


class Volunteer(db.Model):
    __tablename__ = 'volunteers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    userpic = db.Column(db.String(300))
    phone = db.Column(db.String(20))
    street_id = db.Column(db.Integer, db.ForeignKey('streets.id'))
    street = db.relationship('Street')


class RequestHelp(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    surname = db.Column(db.String(150))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(300))
    text = db.Column(db.Text)
    district_id = db.Column(db.Integer, db.ForeignKey('districts.id'))
    district = db.relationship('District')
    microdistrict_id = db.Column(db.Integer, db.ForeignKey('streets.id'))
    microdistrict = db.relationship('Street')
    status = db.Column(db.String(30))
