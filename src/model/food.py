import utils.measurement_units as mu

class Food:
    id: int
    name: str
    amount: float
    unity: str
    
    kcal: float
    protein: float
    carbohydrate: float
    fat: float


    weight: float # Necessary for liquids
    weight_unity: str # Necessary for liquids

    def __init__(   self, name: str, amount: float, unity: str, kcal: float, 
                    protein: float=0.0, carbohydrate: float=0.0, fat: float=0.0, 
                    weight: float=0.0, weight_unity: str=''
    ):
        if not unity:
            raise ValueError('unity não pode ser uma string vazia!')

        if unity not in mu.MASS + mu.VOLUME:
            raise ValueError(unity + ' não pertence a lista de unidades!')


        if weight_unity:
            if weight_unity not in mu.MASS + mu.VOLUME:
                raise ValueError('Unidade de peso não faz parte da lista de unidades aceitas')

        self.name = name
        self.amount = amount
        self.unity = unity
        
        self.kcal = kcal
        self.protein = protein
        self.carbohydrate = carbohydrate
        self.fat = fat


        if(self.unity in mu.MASS):
            self.weight = self.amount
            self.weight_unity = self.unity
        else: 
            self.weight = weight
            self.weight_unity = weight_unity
