# Assuming you are using Flask-SQLAlchemy
from models import db, Personnel

with app.app_context():
    personnel_data = db.session.query(Personnel).\
        options(db.joinedload('equipment')).\
        options(db.joinedload('vehicle')).\
        options(db.joinedload('materials')).\
        all()

    for person in personnel_data:
        print(f"Person: {person.name}, Equipment: {person.equipment}, Vehicle: {person.vehicle}, Materials: {person.materials}")
