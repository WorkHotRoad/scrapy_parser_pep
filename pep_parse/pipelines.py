import csv
import datetime as dt
from pathlib import Path
from scrapy.exceptions import DropItem

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = dict()

    def process_item(self, item, spider):
        key = item["status"]
        if key:
            self.results[key] = self.results.get(key, 0) + 1
            return item
        raise DropItem(f'Отсутствует статус в {item}')

    def close_spider(self, spider):
        total = sum(self.results.values())
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(
            file_path, mode="w", encoding="utf-8", newline=""
        ) as file:
            writer = csv.writer(file, dialect='unix', delimiter=":")
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.results.items())
            writer.writerow(['Total', total])
