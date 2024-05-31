from dataclasses import dataclass, field
import time
from typing import Union


@dataclass
class Metric:
    """
    Класс метрики.
    Аттрибуты:
    - name - наименование метрики
    - value - значение метрики
    - timestamp - временная метка метрики
    """
    name: str
    value: Union[int, float]
    timestamp: float = field(default_factory=lambda: time.time())
