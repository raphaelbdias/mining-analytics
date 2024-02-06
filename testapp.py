
from flask import Flask, render_template
from models import Personnel, Equipment, Vehicles, Materials, MineSections, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)
# Assuming you are using Flask-SQLAlchemy
from models import db, Personnel


with app.app_context():
    personnel_data = Personnel.query.all()
    equipment_data = Equipment.query.all()
    vehicles_data = Vehicles.query.all()
    materials_data = Materials.query.all()
    mine_sections_data = MineSections.query.all()
    
    
    # for person in personnel_data:
    #     print(f"Person: {person.name}, Equipment: {person.equipment.equipment_id}, Vehicle: {person.vehicle.fuel_consumption}")
        

    # for equipment in equipment_data:
    #     # print(f"Person: {equipment.id}, Equipment: {equipment.type_of_systems}, Vehicle: {equipment.personnel}")
    #     for i in equipment.personnel:
    #         print(i.name)
            
            
            
    data = []
    for equipment in equipment_data:
        dictionary = {"Equipment": {equipment.equipment_id}, "Status": {equipment.status}, "personnel":""}
        for i in equipment.personnel:
            dictionary.update({"personnel":i.name})  
        data.append(dictionary)
print(data)