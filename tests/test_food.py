from multiprocessing.sharedctypes import Value
import unittest

from src.model.food import Food

# Depois adicionar os match das mensagens de erro aosa assertRaises

# Modificar os valores de entrada das comidas para algo mais real

class TestFood(unittest.TestCase):

    def test_measure_unity_is_not_in_the_units_list(self):
        with self.assertRaises(ValueError):
            name = 'banana'
            amount = 1.0
            unity = 't'
            kcal = 1.0
            Food(name, amount, unity, kcal)

    def test_valid_measure_unity(self):
        name = 'banana'
        amount = 1.0
        unity = 'g'
        kcal = 1.0
        food = Food(name, amount, unity, kcal)    
        self.assertEqual(unity, food.unity)

    def test_empty_measure_unity(self):
        params = {
            'name': 'banana',
            'amount': 1.0,
            'unity': '',
            'kcal': 1.0
        }
        with self.assertRaises(ValueError):
            Food(**params)


    def test_constructor(self):
        

        
        
        with self.assertRaises(TypeError):
            Food('banana', 1.0)

        with self.assertRaises(TypeError):
            Food('banana', 1.0, 'g')

        
        Food('banana', 1.0, 'g', 10.0)

    def test_constructor_no_params(self):
        with self.assertRaises(TypeError):
            Food()

    def test_constructor_name_params(self):
        with self.assertRaises(TypeError):
            Food('banana')

    def test_minimal_params_to_constructor(self):
        try:
            Food('banana', 1.0, 'g', 10.0)
        except Exception:
            self.fail('Exceção não esperada')

    def test_constructor_weight_unity(self):
        with self.assertRaises(ValueError):
            params = {
                'name': 'banana',
                'amount': 1.0,
                'unity': 'g',
                'kcal': 1.0,
                'weight_unity': 't'
            }
            Food(**params)
        
    def test_constructor_weight_liquids(self):
        
        params = {
            'name': 'leite',
            'amount': 250.0,
            'unity': 'ml',
            'kcal': 187.0,
            'weight': 100,
            'weight_unity': 'g'
        }
        try:
            Food(**params)
        except Exception:
            self.fail('Exceção não esparada')
            