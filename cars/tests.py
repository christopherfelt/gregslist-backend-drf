from django.test import TestCase

# Create your tests here.
from .models import Car

class CarsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_car = Car.objects.create(
            make="chevy",
            model="thing",
            description="some stuff",
            imgUrl="an image url",
            price=234,
            year=1999
        )
        test_car.save()

    def test_car_content(self):
        car = Car.objects.get(id=1)
        make = f'{car.make}'
        model = f'{car.model}'
        description = f'{car.description}'
        imgUrl = f'{car.imgUrl}'
        price = car.price
        year = car.year
        self.assertEqual(make, 'chevy')
        self.assertEqual(model, 'thing')
        self.assertEqual(description, 'some stuff')
        self.assertEqual(imgUrl, "an image url")
        self.assertEqual(price, 234)
        self.assertEqual(year, 1999)