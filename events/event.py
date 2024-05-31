from dataclasses import dataclass
from typing import Literal, Union


@dataclass
class Event:
    """
    Класс события.
    Аттрибуты:
    - name - наименование события
    - value - значение события
    - timestamp - временная метка события
    - agg_func - применяемая функция агрегации
    """
    name: str
    value: Union[int, float]
    timestamp: float
    agg_func: Literal['sum', 'avg', 'min', 'max'] = 'sum'
