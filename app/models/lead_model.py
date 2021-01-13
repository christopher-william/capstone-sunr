from . import db


class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    hsp_id = db.Column(db.Integer, db.ForeignKey('hsp.id'))
    energy_id = db.Column(db.Integer, db.ForeignKey('energy_data.id'))
    simulations = db.relationship('Simulation', backref='lead', lazy=True)