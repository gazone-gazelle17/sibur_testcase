from events.event import Event
from typing import List
import os


class Aggregator:
    """
    Класс для работы с событиями.
    Включает в себя агрегирование событий и их отправку в хранилище.
    """
    def __init__(self, aggregation_interval: int):
        self.aggregation_interval = aggregation_interval
        # Загрузка параметров хранилища (postgres)
        self.postgres_db = os.getenv('POSTGRES_DB')
        self.postgres_user = os.getenv('POSTGRES_USER')
        self.postgres_password = os.getenv('POSTGRES_PASSWORD')
        self.postgres_host = os.getenv('POSTGRES_HOST')
        self.postgres_port = os.getenv('POSTGRES_PORT')
        # Загрузка параметров хранилища (kafka)
        self.kafka_broker_url = os.getenv('KAFKA_BROKER_URL')
        self.kafka_topic = os.getenv('KAFKA_TOPIC')

    def aggregate(self, events: List[Event]) -> List[Event]:
        """
        Агрегирует события на основе функции или времени.
        """
        pass

    def send_to_storage(self, aggregated_events: List[Event], storage: str):
        """
        Отправляет события в определенное хранилище
        (PostgreSQL или Kafka).
        """
        if storage == 'postgres':
            self._send_to_postgres(aggregated_events)
        elif storage == 'kafka':
            self._send_to_kafka(aggregated_events)

    def _send_to_postgres(self, aggregated_events: List[Event]):
        """
        Отправляет события в PostgreSQL.
        """
        print(f"Sending to PostgreSQL: {aggregated_events}")

    def _send_to_kafka(self, aggregated_events: List[Event]):
        """
        Отправляет события в Kafka.
        """
        print(f"Sending to Kafka: {aggregated_events}")
