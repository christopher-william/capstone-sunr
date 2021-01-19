from . import db


class Panel_price(db.Model):
    __tablename__ = "panel_price"
    
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    power = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric, nullable=False)

    simulation = db.relationship('Simulation')

    def __repr__(self):
        return f"<Table name {self.Panel_price.__name__}>"
