from django_seed import Seed
from prototype.models import Finishing, PropertyType, Equipment, Segment, Material
from project.models import Amenity, Developer, Project
from location.models import State, Corridor, Municipality, Colony
import pandas as pd
import random

# exec(open('core/seeder.py').read())

seeder = Seed.seeder()
#no dependencies
amenities = ['Acceso Controlado', 'Areas Verdes/Jardinadas', 'Alberca', 'Carril de Nado', 'Chapoteadero', 'Jacuzzi', 'Gimnasio', 'Aparatos de Ejercicio al aire libre', 'Cancha Deportiva', 'Juegos Infantiles', 'Area para mascotas', 'Asador', 'Fogatero', 'Cowork', 'Ludoteca', 'Sauna', 'Vapor', 'Terraza Comun', 'Ciclopista', 'Vitapista(Jogging)', 'Salon de usos multiples', 'Salon de eventos', 'Salon de juegos', 'Cine', 'Spa']

for amenity in amenities:
    seeder.add_entity(Amenity, 1, {
        'name': amenity,
        'description': 'Areas comunes',
    })
#no dependencies
property_types = ['Loft', 'Casa', 'Duplex', 'Departamento','No existe']

for property_type in property_types:
    seeder.add_entity(PropertyType, 1, {
        'name': property_type,
        'description': 'Tipo de propiedad',
        
    })
#no dependencies
states = ['Queretaro', 'Quintana Roo']

for state in states:
    seeder.add_entity(State, 1, {
        'name': state    
    })

#no dependencies
corridors = ['Norte', 'Junipero', 'Sur-Poniente', 'Oriente', 'Zibatá', 'Centro', 'Sur-Oriente']

for corridor in corridors:
    seeder.add_entity(Corridor, 1, {
        'name': corridor,
    })
#no dependencies
segment_names = ['Residencial', 'Residencial Plus', 'Medio Residencial', 'Social', 'Media', 'No existe']

for segment_name in segment_names:
    seeder.add_entity(Segment, 1, {
        'name': segment_name,
        'description': 'Tipo de Segmento'
    })
#no dependencies
df = pd.read_csv('devs')
developers = df['Devs'].to_list()

for developer in developers:
    seeder.add_entity(Developer, 1, {
        'name': developer,
        'description': 'aqui se describen la desarroladoras',
        'social_networks': 'www.youtube.com',
    })
#no dependencies
equipment_names = ['Baños', 'Estacionamiento', 'Habitación', 'Medios Baños', 'Cuarto de Servicio', 'Roof Garden', 'Penthouse', 'Pentgarden']
equipment_type = ['Interior', 'Exterior']

for equipment_name in equipment_names:
    seeder.add_entity(Equipment, 1, {
        'name': equipment_name,
        'type': lambda x: random.choice(equipment_type)
    })

#no dependencies
finishings = ['Sistema Constructivo', 'Pisos', 'Muros', 'Canceleria Ventanas', 'Cubierta Cocina', 'Carpinteria']

for finishing in finishings:
    seeder.add_entity(Finishing, 1, {
        'name': finishing,
    })

#no depencendies
material_name = ['Madera','Panel Fibra','Granito','Aluminio','Pasta','Yeso','Cerámico','Porcelanato','Tabique','Block','No existe']

for material in material_name:
    seeder.add_entity(Material, 1, {
        'name': material,
    })

municipalities = ['Queretaro', 'Marques', 'Corregidora']

for municipality in municipalities:
    seeder.add_entity(Municipality, 1, {
        'name': municipality,
    })

colonies = ['Juriquilla', 'Zibata', 'Milenio III', 'Cañadas del Lago', 'Balcones Coloniales', 'Vista', 'Punta Esmeralda', 'La Porta ', 'Refugio', 'Loma Dorada', 'San José El Alto', 'Salitre', 'Cumbres del Lago, Juriquilla', 'Centro Sur', 'Mercurio', 'San Jerónimo', 'Campanario', 'Lomas del Campanario Norte', 'Jardines de la Hacienda', 'Miradores', 'Vista Hermosa', 'Mirador', 'Vista Real', 'Bellavista', 'Lomas de Juriquilla', 'Venceremos', 'Cruz de Fuego', 'Real del Bosque']

for colony in colonies:
    seeder.add_entity(Colony, 1, {
        'name': colony,
    })

proyects = ['Inspira L&A (T1-T3)', 'Paseo Pitahaya (T1)', 'Amuralle - Aragón', 'Argu IV', 'Zaniah II', 'Paseo San Junípero', 'Massaro II', 'Sabbia']

for proyect in proyects:
    seeder.add_entity(Project, 1, {
        'name': proyect,
    })

inserted_pks = seeder.execute()