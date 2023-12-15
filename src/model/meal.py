from typing import List
import utils.measurement_units as mu
from model.food import Food


class Meal:
    id: int
    name: str
    foods: List[Food]
    ref_foods: List[Food]
    weight: float
    weight_unity: str
    total_protein: float
    total_carbohydrate: float
    total_fat: float
    total_kcal: float

    def __init__(self, name: str, foods: List, weight: float = 0.0, weight_unity: str = '',
                    total_protein: float=0.0, total_carbohydrate: float=0.0, total_fat: float=0.0,
                    total_kcal: float=0.0
    ):

        if weight_unity and weight_unity not in mu.MASS:
            raise ValueError(weight_unity + ' não pertence a lista de unidades!')

        self.name = name
        self.foods = foods
        self.weight = weight
        self.weight_unity = weight_unity
        self.total_protein = total_protein
        self.total_carbohydrate = total_carbohydrate
        self.total_fat = total_fat
        self.total_kcal = total_kcal
        self.calculate_total() #Mesmo ele dando todos os valores, calcular o total
    
    def calculate_total_protein(self):
        self.total_protein = sum(food.protein for food in self.foods)

    def calculate_total_carbohydrate(self):
        self.total_carbohydrate = sum(food.carbohydrate for food in self.foods)

    def calculate_total_fat(self):
        self.total_fat = sum(food.fat for food in self.foods)

    def calculate_total_kcal(self):
        self.total_kcal = sum(food.kcal for food in self.foods)

    def calculate_total(self):
        
        # Poderia chamar as funções aqui, mas por questão de performance assim é melhor
        # Ou provavelmente tem o mesmo nivel de desempenho
        accumulator_protein = 0.0
        accumulator_carb = 0.0
        accumulator_fat = 0.0
        accumulator_kcal = 0.0

        for food in self.foods:
            accumulator_protein += food.protein
            accumulator_carb += food.carbohydrate
            accumulator_fat += food.fat
            accumulator_kcal += food.kcal

        self.total_protein = accumulator_protein
        self.total_carbohydrate = accumulator_carb
        self.total_fat = accumulator_fat
        self.total_kcal = accumulator_kcal