from django.test import TestCase, Client
from location.models import (
    Municipality,
    State
)
from .models import (
    Colony,
    Developer,
    Project,
)
from .views import filter_view
import json, datetime, random

def get_random_address():
    return [
        "Faro de San Sebastian",
        "El Alamo Country Club",
        "Gran Jardin",
        "Club Campestre",
        "Cañada del Refugio",
        "Alamos del Lago",
        "El Campanario"
    ][random.randint(0, 6)]

def create_states():
    return State.objects.create(name = "Queretaro")

def create_developer(description: str):
    social_networks = json.dumps({
        "fb": "facebook.com/mock",
        "insta": "instagram.com/mock",
        "twitter": "twitter.com/mock"
    })

    return Developer.objects.create(
        description = description,
        social_networks = social_networks
    )

def create_municipalities(state: State):
    Municipality.objects.create(name = "Queretaro", state_field = state)
    Municipality.objects.create(name = "San Juan del Rio", state_field = state)
    Municipality.objects.create(name = "El Marques", state_field = state)
    Municipality.objects.create(name = "El Pueblito", state_field = state)

def create_colony(municipality: Municipality):
    return Colony.objects.create(
        name = get_random_address(),
        municipality_field = municipality
    )

def create_project(description: str, colony: Colony, developer: Developer):
    social_networks = json.dumps({
        "fb": "zucc.com/fb",
        "insta": "insta.com/pics",
        "twitter": "twitt.com/tweets"
    })

    return Project.objects.create(
        # Dependencies
        colony_field = colony,
        description = description,
        developer_field = developer,
        social_networks = social_networks,

        # Normal properties
        initial_date = datetime.datetime.now(),
        latitud = round(random.uniform(-0.6, 0.6), 3),
        longitude = round(random.uniform(-0.6, 0.6), 3),

        address = get_random_address() + f" #{random.randint(1, 150)}",
        phone = f"442-{random.randint(123, 567)}-{random.randint(123, 567)}",
        levels = random.randint(1, 5)
    )

def seed_database():
    # Setup the state of Queretaro
    create_states()

    # Add 4 municipalities [Qro, San Juan del Rio, El Marques, El Pueblito]
    state = State.objects.first()
    create_municipalities(state)

    # Add 3 colonies for each municipality
    municipalities = Municipality.objects.all()
    for municipality in municipalities:
        create_colony(municipality)
        create_colony(municipality)
        create_colony(municipality)

    # Add 3 projects for each colony
    colonies = Colony.objects.all()
    for colony in colonies:
        developer = create_developer(f"Developer INMO-{colony.name}")

        create_project(f"INMO Project 1 - {colony.name}", colony, developer)
        create_project(f"INMO Project 2 - {colony.name}", colony, developer)
        create_project(f"INMO Project 3 - {colony.name}", colony, developer)

class FilterTest(TestCase):
    def setUp(self):
        return seed_database()

    def test_empty_filter_gets_right_query(self):
        # Arrange
        client = Client()

        # Act
        response = client.get("/proyectos/soto")

        # Should get all developers  
        expected_developers = Developer.objects.all().order_by("pk")
        actual_developers = response.context["developers"].order_by("pk")
        
        # Should get all projects
        expected_projects = Project.objects.all().order_by("pk")
        actual_projects = response.context["projects_filter"].qs.order_by("pk")

        # Assert
        self.assertIs(response.status_code, 200, "Response should return status 200")
        self.assertSetEqual(set(actual_projects), set(expected_projects), "Actual projects doesn't match expected projects")
        self.assertSetEqual(set(actual_developers), set(expected_developers), "Actual developers doesn't match expected developers")

    def test_level_filter_gets_right_query(self):
        # Arrange
        client = Client()

        # Act
        response = client.get("/proyectos/soto", {
            "levels": 1
        })

        expected_developers = Developer.objects.all().order_by("pk")
        actual_developers = response.context["developers"].order_by("pk")
        
        expected_projects = Project.objects.filter(levels=1).order_by("pk")
        actual_projects = response.context["projects_filter"].qs.order_by("pk")

        # Assert
        self.assertIs(response.status_code, 200, "Response should return status 200")
        self.assertSetEqual(set(actual_projects), set(expected_projects), "Actual projects doesn't match expected projects")
        self.assertSetEqual(set(actual_developers), set(expected_developers), "Actual developers doesn't match expected developers")     

    def test_latitud_filter_gets_right_query(self):
        # Arrange
        client = Client()

        # Act
        response = client.get("/proyectos/soto", {
            "latitude_min": 0.1,
            "latitude_max":0.4
        })

        expected_developers = Developer.objects.all().order_by("pk")
        actual_developers = response.context["developers"].order_by("pk")
        
        expected_projects = Project.objects.filter(latitud__gte=0.1, latitud__lte=0.4).order_by("pk")
        actual_projects = response.context["projects_filter"].qs.order_by("pk")

        # Assert
        self.assertIs(response.status_code, 200, "Response should return status 200")
        self.assertSetEqual(set(actual_projects), set(expected_projects), "Actual projects doesn't match expected projects")
        self.assertSetEqual(set(actual_developers), set(expected_developers), "Actual developers doesn't match expected developers")     
    
    def test_longitud_filter_gets_right_query(self):
        # Arrange
        client = Client()

        # Act
        response = client.get("/proyectos/soto", {
            "longitude_min": 0.1,
            "longitude_max":0.4
        })

        expected_developers = Developer.objects.all().order_by("pk")
        actual_developers = response.context["developers"].order_by("pk")
        
        expected_projects = Project.objects.filter(longitude__gte=0.1, longitude__lte=0.4).order_by("pk")
        actual_projects = response.context["projects_filter"].qs.order_by("pk")

        # Assert
        self.assertIs(response.status_code, 200, "Response should return status 200")
        self.assertSetEqual(set(actual_projects), set(expected_projects), "Actual projects doesn't match expected projects")
        self.assertSetEqual(set(actual_developers), set(expected_developers), "Actual developers doesn't match expected developers")

# print("------------- ACTUAL ------------")
# # print(actual_projects.query)
# for p in set(actual_projects):
#     print(f"Name: {p.description} - Longitud: {p.longitude}")

# print("------------- EXPECT ------------")
# # print(expected_projects.query)
# for p in set(expected_projects):
#     print(f"Name: {p.description} - Longitud: {p.longitude}")