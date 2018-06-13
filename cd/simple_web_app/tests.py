# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from simple_web_app.models import MountainAnimal

# Create your tests here.
class MountainAnimalTestCase(TestCase):
    def setUp(self):
        MountainAnimal.objects.create(name="mountain_lion", visitation_frequency=1)

    def test_animal_visitation_frequency(self):
        """Test that mountain animal visitation frequencies are correctly identified"""
        mountain_lion = MountainAnimal.objects.get(name='mountain_lion')
        self.assertEqual(mountain_lion.visitation_frequency, 1)
