import asyncio
import os
import time
from typing import List
from dotenv import load_dotenv
from bus.vabus import VaBus
from aggregator.aggregator import Aggregator
from events.event import Event
from metrics.metric import Metric


# Загружает переменные окружения из .env
load_dotenv()


async def main():
    """
    Получает URL шины, интервал агрегации и тип хранилища
    (с данными по умолчанию).
    """
    bus_url = os.getenv('VABUS_URL')
    aggregation_interval = int(os.getenv('AGGREGATION_INTERVAL', 60))
    storage_type = os.getenv('STORAGE_TYPE', 'postgres')

    processed_events = 0  # Счетчик событий
    error_count = 0  # Счетчик ошибок
    start_time = time.time()  # Текущее время для отслеживания интервала

    async with VaBus(bus_url) as bus:
        """
        Создает экземпляр класса VaBus и агрегатор,
        инициализирует список для наполнения событиями.
        """
        aggregator = Aggregator(aggregation_interval)
        events: List[Event] = []

        while True:
            try:
                # Получает событие из шины данных
                event = await bus.get_event()
                events.append(event)
                processed_events += 1

                # Аггрегирует события и отправляет их в хранилище
                if time.time() - events[0].timestamp >= aggregation_interval:
                    aggregated_events = aggregator.aggregate(events)
                    aggregator.send_to_storage(aggregated_events, storage_type)
                    events.clear()

                # Сохраняет общее время для метрик и обнуляем счетчик времени
                current_time = time.time()
                processing_time = current_time - start_time
                start_time = current_time

                # Метрики для отправки в шину данных
                metrics = [
                    # Количество обработанных событий
                    Metric(name='processed_events', value=processed_events),
                    # Общее время, затраченное на обработку событий
                    Metric(name='processing_time', value=processing_time),
                    # Количество возникших при обработке ошибок
                    Metric(name='error_count', value=error_count)
                ]

                # Отправляет метрики в шину
                for metric in metrics:
                    await bus.send_metric(metric)

                # Обнуляет метрики для следующего цикла
                processed_events = 0
                error_count = 0

            except Exception as e:
                # Обрабатывает ошибки и добавляет их количество в метрики
                error_count += 1
                print(f"Error processing event: {e}")

            await asyncio.sleep(1)  # Задержка для экономии ресурсов

if __name__ == "__main__":
    # Запускает функцию
    asyncio.run(main())
