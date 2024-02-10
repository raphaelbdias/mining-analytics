
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
    for vehicles in Vehicles.query.all():
        dictionary = {"vehicles": vehicles.vehicle_type, 
                      "Fuel": vehicles.fuel_consumption, 
                      "material":"", 
                      "maintenance_history": vehicles.maintenance_history, 
                      "distance_traveled":vehicles.distance_traveled, 
                      "mine_section":""}
        for i in vehicles.personnel:
            dictionary.update({"personnel":i.name})  
        data.append(dictionary)

        for i in vehicles.mine_section:
            dictionary.update({"mine_section":i.section_name})  
        data.append(dictionary)
    print(data)

    # data = []
    # for vehicle in Vehicles.query.all():
    #     dictionary = {
    #         "vehicles": vehicle.vehicle_type,
    #         "Fuel": vehicle.fuel_consumption,
    #         "material": "",
    #         "maintenance_history": vehicle.maintenance_history,
    #         "distance_traveled": vehicle.distance_traveled,
    #     }
        
    #     # Add mine section coordinates
    #     if vehicle.materials:
    #         mine_section = vehicle.materials.mine_section
    #         if mine_section:
    #             dictionary.update({
    #                 "latitude": mine_section.latitude,
    #                 "longitude": mine_section.longitude,
    #             })

    #     # Add personnel names
    #     personnel_names = [person.name for person in vehicle.personnel]
    #     dictionary.update({"personnel": personnel_names})
        
    #     data.append(dictionary)

    # print(data)