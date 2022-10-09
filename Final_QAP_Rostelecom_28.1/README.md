Объект тестирования https://b2c.passport.rt.ru/

Ссылка на файл с тест-кейсами https://docs.google.com/spreadsheets/d/1kTZuVYWpsx4BLAReI6CJawvkhRQ_hGe0tIyRhRjlkng/edit?usp=sharing 

В файле settings* собраны значения для автотестирования

*Примечание: звездочками обозначены тестовые данные, которых у меня нет или которые я не могу опубликовать (например номер телефона)

В файле tests собраны автотесты с помощью библиотеки Selenium

Для запуска использовать команду pytest -v --driver Chrome tests.py из терминала

Драйвер для Chrome находится в папке Scripts, поэтому путь к нему нигде не прописан

