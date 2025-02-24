from django.test import TestCase
from restaurant.forms import CookYearsOfExperienceCreateForm


class CookCreationFormTest(TestCase):

    def test_cook_create_with_years_of_experience_first_name_last_name(self):

        form_data = {
            "username": "Test",
            "years_of_experience": 12,
            "first_name": "TestFirstName",
            "last_name": "TestLastName",
        }
        form = CookYearsOfExperienceCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
