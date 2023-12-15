from enum import Enum

class Volume(Enum):
    DAL = 'DAL'
    L = 'L'
    CL = 'CL'
    ML = 'ML'

class Mass(Enum):
    KG = 'kg'
    HG = 'hg'
    DAG = 'dag'
    G = 'g'
    CG = 'cg'
    MG = 'mg'

VOLUME = ['dal','l', 'cl', 'ml']

MASS = ['kg', 'hg', 'dag', 'g', 'cg', 'mg']