"""Unit tests of the thing model."""
from django.test import TestCase
from things.models import Thing, User
from django.core.exceptions import ValidationError

class ThinigModelTest(TestCase):
    """Unit tests of the thing model."""
    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.org',
            password='Password123',
            bio='wag1'
        )
        self.thing = Thing.objects.create(
            name='non-materia',
            description='object of type non-material',
            quantity=1
        )

    def test_valid_thing(self):
        self._assert_thing_is_valid()



    def test_things_name_cannot_be_blank(self):
        self.thing.name = ''
        self._assert_thing_is_invalid()

    def test_name_cannot_be_more_than_35_characters_long(self):
        self.thing.name = 'x' * 36
        self._assert_thing_is_invalid()

    def test_thing_name_can_be_35_characters_long(self):
        self.thing.name = 'x' * 35
        self._assert_thing_is_valid()

    def test_thingname_must_be_uniqe(self):
        second_thing = self._create_second_thing()
        self.thing.name = second_thing.name
        self._assert_thing_is_invalid()

    def test_thingname_may_contain_numbers(self):
        self.thing.thingname =  '@j0hndoe2'
        self._assert_thing_is_valid()



    def test_things_description_can_be_blank(self):
        self.thing.description = ''
        self._assert_thing_is_valid()

    def test_description_cannot_be_more_than_120_characters_long(self):
        self.thing.description = 'x' * 121
        self._assert_thing_is_invalid()

    def test_thing_description_can_be_120_characters_long(self):
        self.thing.description = 'x' * 120
        self._assert_thing_is_valid()

    def test_thingdescription_in_not_unique(self):
        second_thing = self._create_second_thing()
        self.thing.description = second_thing.description
        self._assert_thing_is_valid()



    def test_thing_quantity_can_be_0(self):
        self.thing.quantity = 0
        self._assert_thing_is_valid()

    def test_thing_quantity_cannot_be_more_than_50(self):
        self.thing.quantity = 51
        self._assert_thing_is_invalid()

    def test_thingquantity_can_be_not_uniqe(self):
        second_thing = self._create_second_thing()
        self.thing.quantity = second_thing.quantity
        self._assert_thing_is_valid()



    def _create_second_thing(self):
        thing = Thing.objects.create(
            name='material',
            description='materail object',
            quantity=1
        )
        return thing

    def _assert_thing_is_valid(self):
        try:
            self.thing.full_clean()
        except (ValidationError):
            self.fail('Test thing should be valid')

    def _assert_thing_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.thing.full_clean()
