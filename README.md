# Асинхроннвый парсер документации Python

# Парсер документов PEP на базе фреймворка Scrapy.

## Описание:

Программа парсит документацию с официального
сайта Python, позволяя оставаться в курсе последних новостей и изменений.
Парсинг производится асинхронным путем при
помощи фреймворка Scrapy, что позволяет значительно уменьшить время
получения информации с сайта.

Парсер выводит собранную информацию в два файла **.csv**:
- В первом файле список всех PEP: номер, название и статус.
- Второй файл содержит сводку по статусам PEP - статус, количество.

---

###Автор - Я

---

## Инструкция по использованию парсера

1. Клонируйте проект на свой компьютер и перейдите в его корневую папку:
```
https://github.com/WorkHotRoad/scrapy_parser_pep.git

```
2. Создайте и активируйте виртуальное окружение:

```
python -m venv venv
активация - /venv/scripts/activate
```

3. Обновите pip и установите зависимости в виртуальное окружение:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Запустите паука 'pep'
```
scrapy crawl pep

```
