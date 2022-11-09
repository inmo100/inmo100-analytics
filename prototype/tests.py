from django.test import TestCase
from .models import Prototype
from .helpers import recreate_prototypes

class HelperTests(TestCase):

    def test_recreate_prototypes():
        prototype_count = Prototype.objects.count()
        all_prototypes = recreate_prototypes()
        proyect_prototypes = recreate_prototypes()
        