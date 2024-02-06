from flask import Flask, render_template
from models import Personnel, Equipment, Vehicles, Materials, MineSections, db
import plotly.graph_objects as go
import json
import plotly


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
def index():
    
    # Pass the data to the template
    return render_template('index.html',
                            personnel_data=personnel_data,
                           equipment_data=equipment_data,
                           vehicles_data=vehicles_data,
                           materials_data=materials_data,
                           mine_sections_data=mine_sections_data)

@app.route('/personnel')
def personnel():
    

    # Pass the data to the template
    return render_template('personnel.html',
                           personnel_data=personnel_data)

@app.route('/vehicles')
def vehicles():
    
    # Pass the data to the template
    return render_template('vehicles.html',
                            vehicles_data=vehicles_data)



@app.route('/equipment')
def equipment():
    graphJSON = ''

    data = []
    for equipment in Equipment.query.all():
        personnel_names = [person.name for person in equipment.personnel]
        dictionary = {
            "Equipment": equipment.equipment_id,
            "Status": equipment.status,
            "personnel": ', '.join(personnel_names),
            "system": equipment.type_of_systems,
            "usage_statistics": equipment.usage_statistics
        }
        data.append(dictionary)

    # Create a bar chart
    fig = go.Figure(data=[
        go.Bar(x=[entry['Equipment'] for entry in data],
               y=[entry['usage_statistics'] for entry in data],
               text=[entry['system'] for entry in data],
               marker=dict(color='#305D7D')
        )
    ])

    # Update layout for better visualization
    fig.update_layout(
        font_family="Source Sans Pro",
        title='Equipment Usage Statistics',
        xaxis_title='Equipment',
        yaxis_title='Usage Statistics',
        barmode='group'
    )

    # Convert the figure to JSON for rendering in HTML
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('equipment.html', graphJSON=graphJSON, data = data)

@app.route('/mine')
def mine():
    
    # Pass the data to the template
    return render_template('mine.html',
                            mine_sections_data=mine_sections_data)


@app.route('/materials')
def materials():
    
    # Pass the data to the template
    return render_template('materials.html',
                            materials_data=materials_data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
