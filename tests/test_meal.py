import unittest
import math

from src.model.meal import Meal, Food

class TestMeal(unittest.TestCase):

    def test_minimal_params_to_constructor(self):
        params_food = {
            'name': 'banana prata',
            'amount': 100,
            'unity': 'g',
            'kcal': 98
        }

        params_meal = {
            'name': 'breakfast',
            'foods': [Food(**params_food)],
        }

        try:
            Meal(**params_meal)
        except Exception:
            self.fail('Exceção não esperada')
        
    
    def test_calculate_total_protein(self):
        params_food1 = {
                'name': 'banana prata',
                'amount': 100,
                'unity': 'g',
                'kcal': 98,
                'protein': 1.4
        }

        params_food2 = {
            'name': 'aveia',
            'amount': 100,
            'unity': 'g',
            'kcal': 346.67,
            'protein': 14.33
        }

        
        params_meal = {
            'name': 'breakfast',
            'foods': [Food(**params_food1), Food(**params_food2)]
        }

        TOTAL_PROTEIN = params_food1['protein'] + params_food2['protein']

        meal = Meal(**params_meal)

        try:
            meal.calculate_total_protein()
        except Exception:
            self.fail('Exceção não esperada')

        self.assertAlmostEqual(meal.total_protein, TOTAL_PROTEIN, places=6)

    def test_calculate_total_carbohydrate(self):
        params_food1 = {
                'name': 'banana prata',
                'amount': 100,
                'unity': 'g',
                'kcal': 98,
                'carbohydrate': 26.0
        }

        params_food2 = {
            'name': 'aveia',
            'amount': 100,
            'unity': 'g',
            'kcal': 346.67,
            'carbohydrate': 66.27
        }

        
        params_meal = {
            'name': 'breakfast',
            'foods': [Food(**params_food1), Food(**params_food2)]
        }

        TOTAL_CARB = params_food1['carbohydrate'] + params_food2['carbohydrate']

        meal = Meal(**params_meal)

        try:
            meal.calculate_total_carbohydrate()
        except Exception:
            self.fail('Exceção não esperada')

        self.assertAlmostEqual(meal.total_carbohydrate, TOTAL_CARB, places=6)

    def test_calculate_total_fat(self):
        params_food1 = {
                'name': 'banana prata',
                'amount': 100,
                'unity': 'g',
                'kcal': 98,
                'fat': 0.1
        }

        params_food2 = {
            'name': 'aveia',
            'amount': 100,
            'unity': 'g',
            'kcal': 346.67,
            'fat': 6.9
        }

        
        params_meal = {
            'name': 'breakfast',
            'foods': [Food(**params_food1), Food(**params_food2)]
        }

        TOTAL_FAT = params_food1['fat'] + params_food2['fat']

        meal = Meal(**params_meal)

        try:
            meal.calculate_total_fat()
        except Exception:
            self.fail('Exceção não esperada')

        self.assertAlmostEqual(meal.total_fat, TOTAL_FAT, places=6)
        

    def test_calculate_total_kcal(self):


        params_food1 = {
            'name': 'banana prata',
            'amount': 100,
            'unity': 'g',
            'kcal': 98
        }

        params_food2 = {
            'name': 'aveia',
            'amount': 100,
            'unity': 'g',
            'kcal': 346.67
        }

        
        params_meal = {
            'name': 'breakfast',
            'foods': [Food(**params_food1), Food(**params_food2)]
        }

        TOTAL_KCAL = params_food1['kcal'] + params_food2['kcal']

        meal = Meal(**params_meal)

        try:
            meal.calculate_total_kcal()
        except Exception:
            self.fail('Exceção não esperada')

        self.assertAlmostEqual(meal.total_kcal, TOTAL_KCAL, places=6)

    def test_calculate_total(self):

        params_food1 = {
            'name': 'banana prata',
            'amount': 100,
            'unity': 'g',
            'kcal': 98,
            'protein': 1.4,
            'carbohydrate': 26.0,
            'fat': 0.1
        }

        params_food2 = {
            'name': 'aveia',
            'amount': 100,
            'unity': 'g',
            'kcal': 346.67,
            'protein': 14.33,
            'carbohydrate': 66.27,
            'fat': 6.9
        }

        params_meal = {
            'name': 'breakfast',
            'foods': [Food(**params_food1), Food(**params_food2)]
        }

        TOTAL_PROTEIN = params_food1['protein'] + params_food2['protein']
        TOTAL_CARB = params_food1['carbohydrate'] + params_food2['carbohydrate']
        TOTAL_FAT = params_food1['fat'] + params_food2['fat']
        TOTAL_KCAL = params_food1['kcal'] + params_food2['kcal']

        meal = Meal(**params_meal)

        self.assertAlmostEqual(meal.total_protein, TOTAL_PROTEIN, places=6)
        self.assertAlmostEqual(meal.total_carbohydrate, TOTAL_CARB, places=6)
        self.assertAlmostEqual(meal.total_fat, TOTAL_FAT, places=6)
        self.assertAlmostEqual(meal.total_kcal, TOTAL_KCAL, places=6)


    def test_valid_weight_unity(self):
        params_food = {
            'name': 'banana prata',
            'amount': 100,
            'unity': 'g',
            'kcal': 98
        }

        params_meal = {
            'name': 'breakfast',
            'foods': [Food(**params_food)],
            'weight': 100,
            'weight': 'g'
        }

        try:
            Meal(**params_meal)
        except Exception:
            self.fail('Exceção não esperada')


    def test_invalid_weight_unity(self):
        params_food = {
            'name': 'banana prata',
            'amount': 100,
            'unity': 'g',
            'kcal': 98
        }

        params_meal = {
            'name': 'breakfast',
            'foods': [Food(**params_food)],
            'weight': 100,
            'weight_unity': 'tt'
        }

        with self.assertRaises(ValueError):
            Meal(**params_meal)