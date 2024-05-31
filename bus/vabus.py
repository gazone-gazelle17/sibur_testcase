import time
from aiohttp import ClientSession
from events.event import Event
from metrics.metric import Metric


class VaBus:
    """
    Класс для работы с шиной данных.
    Включает в себя установку соединения, прекращение соединения,
    получение события из шины данных и отправку метрик в шину данных.
    """
    def __init__(self, url: str):
        self.url = url
        self._session = ClientSession(base_url=url)

    async def __aenter__(self) -> 'VaBus':
        """
        Устанавливает соединение с шиной данных.
        """
        await self._session.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Закрывает соединение с шиной данных.
        """
        await self._session.__aexit__(exc_type, exc_val, exc_tb)

    async def get_event(self) -> Event:
        """
        Получает событие из шины данных.
        """
        return Event(
            name="example_event",
            value=42.0,
            timestamp=time.time(),
            agg_func="sum"
        )

    async def send_metric(self, metric: Metric):
        """
        Отправляет метрики в шину данных.
        """
        print(f"Metric sent: {metric}")
