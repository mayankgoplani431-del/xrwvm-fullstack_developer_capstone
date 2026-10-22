from .models import CarMake, CarModel

CARS = {
    "Nissan": [("Pathfinder", "SUV"), ("Qashqai", "SUV"), ("XTRAIL", "SUV")],
    "Mercedes": [("A-Class", "SUV"), ("C-Class", "SUV"), ("E-Class", "Sedan")],
    "Audi": [("A4", "Sedan"), ("A5", "Sedan"), ("A6", "Sedan")],
    "Kia": [("Sorrento", "SUV"), ("Carnival", "SUV"), ("Cerato", "Sedan")],
    "Toyota": [("Camry", "Sedan"), ("Corolla", "Sedan"), ("Kluger", "SUV")],
}


def initiate():
    for make_name, models in CARS.items():
        make = CarMake.objects.create(
            name=make_name, description="Great cars by " + make_name)
        for model_name, car_type in models:
            CarModel.objects.create(
                car_make=make, name=model_name, type=car_type, year=2023)
