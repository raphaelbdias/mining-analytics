from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Personnel(db.Model):
    """Defines the table to conatin information about staff and workers

    Args:
        db (_type_): _description_
    """
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    shift = db.Column(db.String(20))
    hours_worked = db.Column(db.Float)
    productivity_metrics = db.Column(db.Float)

    # Relationship with Equipment
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
    equipment = db.relationship('Equipment', back_populates='personnel')

    # Relationship with Vehicles
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    vehicle = db.relationship('Vehicles', back_populates='personnel')

class Equipment(db.Model):
    """Defines the table to conatin information about equipment

    Args:
        db (_type_): _description_
    """
    id = db.Column(db.Integer, primary_key=True)
    equipment_id = db.Column(db.String(20), unique=True, nullable=False)
    type_of_systems = db.Column(db.String(100))
    status = db.Column(db.String(20), nullable=False)
    maintenance_schedule = db.Column(db.String(50))
    usage_statistics = db.Column(db.Float)
    overhaul_history = db.Column(db.String(100))

    # Relationship with Personnel
    personnel = db.relationship('Personnel', back_populates='equipment')

    # Relationship with Materials
    materials_id = db.Column(db.Integer, db.ForeignKey('materials.id'))
    materials = db.relationship('Materials', back_populates='equipment')

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.String(20), unique=True, nullable=False)
    vehicle_type = db.Column(db.String(50), nullable=False)
    fuel_consumption = db.Column(db.Float)
    distance_traveled = db.Column(db.Float)
    maintenance_history = db.Column(db.String(100))
    type_of_systems = db.Column(db.String(100))
    overhaul_history = db.Column(db.String(100))
    vehicle_renewal_and_sale = db.Column(db.String(50))

    # Relationship with Personnel
    personnel = db.relationship('Personnel', back_populates='vehicle')

    # Relationship with Materials
    materials_id = db.Column(db.Integer, db.ForeignKey('materials.id'))
    materials = db.relationship('Materials', back_populates='vehicles')

class Materials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material_id = db.Column(db.String(20), unique=True, nullable=False)
    material_type = db.Column(db.String(50), nullable=False)
    mining_law = db.Column(db.String(100))
    quantity_mined = db.Column(db.Float)
    quality_metrics = db.Column(db.String(50))
    production_rates = db.Column(db.Float)

    # Relationship with Equipment
    equipment = db.relationship('Equipment', back_populates='materials')

    # Relationship with Vehicles
    vehicles = db.relationship('Vehicles', back_populates='materials')

    # Relationship with MineSections
    mine_section_id = db.Column(db.Integer, db.ForeignKey('mine_sections.id'))
    mine_section = db.relationship('MineSections', back_populates='materials')

class MineSections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    section_name = db.Column(db.String(50), nullable=False)
    section_description = db.Column(db.String(255))

    # Relationship with Materials
    materials = db.relationship('Materials', back_populates='mine_section')