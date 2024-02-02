from flask import Flask, render_template
from models import Personnel, Equipment, Vehicles, Materials, MineSections, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

with app.app_context():
    personnel_data = Personnel.query.all()
    equipment_data = Equipment.query.all()
    vehicles_data = Vehicles.query.all()
    materials_data = Materials.query.all()
    mine_sections_data = MineSections.query.all()

@app.route('/')
def home():
    

    # Pass the data to the template
    return render_template('home.html',
                           personnel_data=personnel_data,
                           equipment_data=equipment_data,
                           vehicles_data=vehicles_data,
                           materials_data=materials_data,
                           mine_sections_data=mine_sections_data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
