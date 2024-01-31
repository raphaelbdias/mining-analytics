# populate_db.py
from app import app, db
from operations import PersonnelCRUD, EquipmentCRUD, VehiclesCRUD, MaterialsCRUD, MineSectionsCRUD

def populate_database():
    with app.app_context():
        # Create MineSections
        # section1 = MineSectionsCRUD.create_mine_section(section_name='Section A', section_description='Main mining area')
        # section2 = MineSectionsCRUD.create_mine_section(section_name='Section B', section_description='Secondary mining area')
        # section3 = MineSectionsCRUD.create_mine_section(section_name='Section C', section_description='Exploration area')
        # section4 = MineSectionsCRUD.create_mine_section(section_name='Section D', section_description='Processing plant')
        # section5 = MineSectionsCRUD.create_mine_section(section_name='Section E', section_description='Storage area')

        # # Create Personnel
        # personnel1 = PersonnelCRUD.create_personnel(employee_id='E001', name='John Doe', position='Operator', shift='Day', hours_worked=40, productivity_metrics=0.85, equipment_id=1, vehicle_id=1)
        # personnel2 = PersonnelCRUD.create_personnel(employee_id='E002', name='Jane Smith', position='Supervisor', shift='Night', hours_worked=35, productivity_metrics=0.92, equipment_id=2, vehicle_id=2)
        # personnel3 = PersonnelCRUD.create_personnel(employee_id='E003', name='Bob Johnson', position='Engineer', shift='Day', hours_worked=38, productivity_metrics=0.88, equipment_id=3, vehicle_id=3)
        # personnel4 = PersonnelCRUD.create_personnel(employee_id='E004', name='Alice Brown', position='Technician', shift='Night', hours_worked=42, productivity_metrics=0.95, equipment_id=4, vehicle_id=4)
        # personnel5 = PersonnelCRUD.create_personnel(employee_id='E005', name='Charlie White', position='Mechanic', shift='Day', hours_worked=36, productivity_metrics=0.90, equipment_id=5, vehicle_id=5)

        # Create Equipment
        # equipment1 = EquipmentCRUD.create_equipment(equipment_id='EQ001', type_of_systems='Hydraulic', status='Operational', maintenance_schedule='Monthly', usage_statistics=500, overhaul_history='2019')
        # equipment2 = EquipmentCRUD.create_equipment(equipment_id='EQ002', type_of_systems='Electrical', status='Under Maintenance', maintenance_schedule='Bi-weekly', usage_statistics=300, overhaul_history='2020')
        # equipment3 = EquipmentCRUD.create_equipment(equipment_id='EQ003', type_of_systems='Pneumatic', status='Operational', maintenance_schedule='Weekly', usage_statistics=700, overhaul_history='2021')
        # equipment4 = EquipmentCRUD.create_equipment(equipment_id='EQ004', type_of_systems='Hydraulic', status='Operational', maintenance_schedule='Monthly', usage_statistics=450, overhaul_history='2022')
        # equipment5 = EquipmentCRUD.create_equipment(equipment_id='EQ005', type_of_systems='Electrical', status='Under Maintenance', maintenance_schedule='Bi-weekly', usage_statistics=250, overhaul_history='2023')

        # # Create Vehicles
        # vehicle1 = VehiclesCRUD.create_vehicle(vehicle_id='V001', vehicle_type='Truck', fuel_consumption=15.5, distance_traveled=2000, maintenance_history='2022', type_of_systems='Hydraulic', overhaul_history='2021', vehicle_renewal_and_sale='2023')
        # vehicle2 = VehiclesCRUD.create_vehicle(vehicle_id='V002', vehicle_type='Excavator', fuel_consumption=20.2, distance_traveled=1500, maintenance_history='2021', type_of_systems='Electrical', overhaul_history='2019', vehicle_renewal_and_sale='2024')
        # vehicle3 = VehiclesCRUD.create_vehicle(vehicle_id='V003', vehicle_type='Bulldozer', fuel_consumption=18.7, distance_traveled=1800, maintenance_history='2023', type_of_systems='Hydraulic', overhaul_history='2020', vehicle_renewal_and_sale='2025')
        # vehicle4 = VehiclesCRUD.create_vehicle(vehicle_id='V004', vehicle_type='Loader', fuel_consumption=17.8, distance_traveled=2200, maintenance_history='2020', type_of_systems='Pneumatic', overhaul_history='2022', vehicle_renewal_and_sale='2026')
        # vehicle5 = VehiclesCRUD.create_vehicle(vehicle_id='V005', vehicle_type='Dump Truck', fuel_consumption=22.0, distance_traveled=1700, maintenance_history='2024', type_of_systems='Hydraulic', overhaul_history='2023', vehicle_renewal_and_sale='2027')

        # Create Materials
        # material1 = MaterialsCRUD.create_material(material_id='M001', material_type='Gold', mining_law='Gold Mining Act', quantity_mined=500, quality_metrics='High', production_rates=100)
        # material2 = MaterialsCRUD.create_material(material_id='M002', material_type='Silver', mining_law='Silver Mining Act', quantity_mined=300, quality_metrics='Medium', production_rates=50)
        # material3 = MaterialsCRUD.create_material(material_id='M003', material_type='Copper', mining_law='Copper Mining Act', quantity_mined=700, quality_metrics='High', production_rates=120)
        # material4 = MaterialsCRUD.create_material(material_id='M004', material_type='Iron', mining_law='Iron Mining Act', quantity_mined=450, quality_metrics='Medium', production_rates=80)
        # material5 = MaterialsCRUD.create_material(material_id='M005', material_type='Platinum', mining_law='Platinum Mining Act', quantity_mined=250, quality_metrics='High', production_rates=60)

if __name__ == '__main__':
    populate_database()
    print("Data populated successfully.")
