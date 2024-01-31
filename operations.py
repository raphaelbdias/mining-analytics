from app import db
from models import Personnel, Equipment, Vehicles, Materials, MineSections

class PersonnelCRUD:
    @staticmethod
    def create_personnel(employee_id, name, position, shift, hours_worked, productivity_metrics, equipment_id, vehicle_id):
        personnel = Personnel(
            employee_id=employee_id,
            name=name,
            position=position,
            shift=shift,
            hours_worked=hours_worked,
            productivity_metrics=productivity_metrics,
            equipment_id=equipment_id,
            vehicle_id=vehicle_id
        )
        db.session.add(personnel)
        db.session.commit()
        return personnel

    @staticmethod
    def get_personnel_by_id(personnel_id):
        return Personnel.query.get(personnel_id)

    @staticmethod
    def update_personnel(personnel_id, **kwargs):
        personnel = Personnel.query.get(personnel_id)
        if personnel:
            for key, value in kwargs.items():
                setattr(personnel, key, value)
            db.session.commit()
        return personnel

    @staticmethod
    def delete_personnel(personnel_id):
        personnel = Personnel.query.get(personnel_id)
        if personnel:
            db.session.delete(personnel)
            db.session.commit()
        return personnel

    @staticmethod
    def get_all_personnel():
        return Personnel.query.all()

class EquipmentCRUD:
    @staticmethod
    def create_equipment(equipment_id, type_of_systems, status, maintenance_schedule, usage_statistics, overhaul_history):
        equipment = Equipment(
            equipment_id=equipment_id,
            type_of_systems=type_of_systems,
            status=status,
            maintenance_schedule=maintenance_schedule,
            usage_statistics=usage_statistics,
            overhaul_history=overhaul_history
        )
        db.session.add(equipment)
        db.session.commit()
        return equipment

    @staticmethod
    def get_equipment_by_id(equipment_id):
        return Equipment.query.get(equipment_id)

    @staticmethod
    def update_equipment(equipment_id, **kwargs):
        equipment = Equipment.query.get(equipment_id)
        if equipment:
            for key, value in kwargs.items():
                setattr(equipment, key, value)
            db.session.commit()
        return equipment

    @staticmethod
    def delete_equipment(equipment_id):
        equipment = Equipment.query.get(equipment_id)
        if equipment:
            db.session.delete(equipment)
            db.session.commit()
        return equipment

    @staticmethod
    def get_all_equipment():
        return Equipment.query.all()


class VehiclesCRUD:
    @staticmethod
    def create_vehicle(vehicle_id, vehicle_type, fuel_consumption, distance_traveled, maintenance_history, type_of_systems, overhaul_history, vehicle_renewal_and_sale):
        vehicle = Vehicles(
            vehicle_id=vehicle_id,
            vehicle_type=vehicle_type,
            fuel_consumption=fuel_consumption,
            distance_traveled=distance_traveled,
            maintenance_history=maintenance_history,
            type_of_systems=type_of_systems,
            overhaul_history=overhaul_history,
            vehicle_renewal_and_sale=vehicle_renewal_and_sale
        )
        db.session.add(vehicle)
        db.session.commit()
        return vehicle

    @staticmethod
    def get_vehicle_by_id(vehicle_id):
        return Vehicles.query.get(vehicle_id)

    @staticmethod
    def update_vehicle(vehicle_id, **kwargs):
        vehicle = Vehicles.query.get(vehicle_id)
        if vehicle:
            for key, value in kwargs.items():
                setattr(vehicle, key, value)
            db.session.commit()
        return vehicle

    @staticmethod
    def delete_vehicle(vehicle_id):
        vehicle = Vehicles.query.get(vehicle_id)
        if vehicle:
            db.session.delete(vehicle)
            db.session.commit()
        return vehicle

    @staticmethod
    def get_all_vehicles():
        return Vehicles.query.all()


class MaterialsCRUD:
    @staticmethod
    def create_material(material_id, material_type, mining_law, quantity_mined, quality_metrics, production_rates):
        material = Materials(
            material_id=material_id,
            material_type=material_type,
            mining_law=mining_law,
            quantity_mined=quantity_mined,
            quality_metrics=quality_metrics,
            production_rates=production_rates
        )
        db.session.add(material)
        db.session.commit()
        return material

    @staticmethod
    def get_material_by_id(material_id):
        return Materials.query.get(material_id)

    @staticmethod
    def update_material(material_id, **kwargs):
        material = Materials.query.get(material_id)
        if material:
            for key, value in kwargs.items():
                setattr(material, key, value)
            db.session.commit()
        return material

    @staticmethod
    def delete_material(material_id):
        material = Materials.query.get(material_id)
        if material:
            db.session.delete(material)
            db.session.commit()
        return material

    @staticmethod
    def get_all_materials():
        return Materials.query.all()


class MineSectionsCRUD:
    @staticmethod
    def create_mine_section(section_name, section_description):
        mine_section = MineSections(
            section_name=section_name,
            section_description=section_description
        )
        db.session.add(mine_section)
        db.session.commit()
        return mine_section

    @staticmethod
    def get_mine_section_by_id(section_id):
        return MineSections.query.get(section_id)

    @staticmethod
    def update_mine_section(section_id, **kwargs):
        mine_section = MineSections.query.get(section_id)
        if mine_section:
            for key, value in kwargs.items():
                setattr(mine_section, key, value)
            db.session.commit()
        return mine_section

    @staticmethod
    def delete_mine_section(section_id):
        mine_section = MineSections.query.get(section_id)
        if mine_section:
            db.session.delete(mine_section)
            db.session.commit()
        return mine_section

    @staticmethod
    def get_all_mine_sections():
        return MineSections.query.all()