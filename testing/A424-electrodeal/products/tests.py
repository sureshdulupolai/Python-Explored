from django.test import TestCase
from .calculator import Calculator
from .models import Category, Product
# Create your tests here.
# class CalculatorTest(TestCase):
    
#     def setUp(self):
#         self.calculator=Calculator()
    
#     def test_add(self):
#         self.assertEqual(self.calculator.add(12,2),14)
#         self.assertEqual(self.calculator.add(2,2),4)
#         self.assertEqual(self.calculator.add(4,4),8)
#         self.assertEqual(self.calculator.add(2,3),5)

#     def test_isEven(self):
#         self.assertTrue(self.calculator.is_even(4))
#         self.assertTrue(self.calculator.is_even(6))
#         self.assertTrue(self.calculator.is_even(14))
#         self.assertTrue(self.calculator.is_even(60))

#         self.assertFalse(self.calculator.is_even(29))
#         self.assertFalse(self.calculator.is_even(63))
#         self.assertFalse(self.calculator.is_even(1))
#         self.assertFalse(self.calculator.is_even(9))

#         with self.assertRaises(TypeError):
#             self.calculator.is_even("")



# class CategoryModel(TestCase):
    
#     def setUp(self):
#         # old slug
#         self.category = Category.objects.create(name='Laptops')

#     def test_category_creation(self):
#         self.assertIsNotNone(self.category)
#         self.assertEqual(self.category.name, 'Laptops')
#         self.assertEqual(self.category.slug, 'laptops')

#     def test_slug_generation(self):
#         # new slug
#         other_category = Category.objects.create(name="Accessories")

#         # creating different slug or not
#         self.assertNotEqual(other_category.slug, self.category.slug)

class ProductModel(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Laptops')
        self.product = Product.objects.create(
            name = 'test-product',
            description = 'testing descriptions',
            price = 2600,
            category = self.category
        )

    
    def test_product_creation(self):
        self.assertIsNotNone(self.product)
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.name, 'test-product')
        
