from classes.car import Car
from classes.engine import Engine

eng1 = Engine(140, 2.0)
car1 = Car("Ford", "Mustang", "Red", True, engine = eng1 )
print(car1.brand, car1.model, car1.year, car1.color, car1.is_for_sale, car1.engine.horse_power, car1.engine.vol, car1.engine.fuel_type, car1.engine.material)

car2 = Car("Tesla", "X", "White", engine = Engine(300, 0, "electro"))
print(car2.brand, car2.model, car2.color, car2.engine.horse_power, car2.engine.vol, car2.engine.fuel_type)

car3 = Car(model = "X5", is_for_sale = True, brand = "BMW")
print(car3.brand, car3.model, car3.color)