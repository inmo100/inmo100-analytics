from django_seed import Seed
from prototype.models import Finishing, PropertyType, Equipment, Segment, Prototype, Transaction
from project.models import Amenity, Developer, Project
from location.models import State, Corridor, Municipality, Colony


seeder = Seed.seeder()

seeder.add_entity(Finishing, 10)
seeder.add_entity(PropertyType, 10)
seeder.add_entity(Segment, 10)
seeder.add_entity(Equipment, 10)
seeder.add_entity(State, 10)
seeder.add_entity(Corridor, 10)
seeder.add_entity(Municipality, 10)
seeder.add_entity(Colony, 10)
seeder.add_entity(Amenity, 10)
seeder.add_entity(Developer, 10)
seeder.add_entity(Project, 10)
seeder.add_entity(Prototype, 10)
seeder.add_entity(Transaction, 10)

inserted_pks = seeder.execute()