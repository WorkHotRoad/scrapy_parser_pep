import time


BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
ROBOTSTXT_OBEY = True
EXPORT_FIELDS = {
    'number' :"Номер",
    'name': "Имя",
    'status': "Статус",
}
FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': False
    }
}
