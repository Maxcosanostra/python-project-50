### Вычислитель отличий / Generate Difference

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Maxcosanostra/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Maxcosanostra/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/2e4a74f501af8c1ccd04/maintainability)](https://codeclimate.com/github/Maxcosanostra/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/2e4a74f501af8c1ccd04/test_coverage)](https://codeclimate.com/github/Maxcosanostra/python-project-50/test_coverage)

---

### Описание 
Вычислитель отличий - это универсальная программа, которая принимает на вход два пути до конфигурационных файлов и возвращает описание различий между структурами данных файлов. 
Использование инструмента gendiff ликвидирует необходимость в дополнительной и оригинальной копии каталога.

* Поддержка форматов: json/yaml
* Генерация отчетов: plain, stylish, json 

---

### Содержание
* Сравнение плоских файлов (JSON)
* Сравнение плоских файлов (YAML)
* Рекурсивное сравнение
* Плоский формат
* Вывод в JSON

---

### Установка

1. git clone https://github.com/Maxcosanostra/python-project-50
2. cd python-project-50
3. make package-install

---

### Сравнение плоских файлов (JSON):
Сравнение строится на основе того, как изменилось содержимое во втором файле относительно первого, позволяющее быстро определить изменения в структуре данных JSON-файлов.

Для сранения двух файлов используйте команду: __gendiff file1.json file2.json__

https://asciinema.org/a/Yi0ytEZSOk4PYDWIclMiBtNgq

---

### Сравнение плоских файлов (YAML):
Поиск различий между двумя простыми, одноуровневыми YAML-файлами без вложенных структур. Легкочитаемый синтаксис помогает быстро ориентироваться в разнице между файлами. 

Для сранения двух файлов используйте команду: __gendiff file1.yml file2.yml__

https://asciinema.org/a/nIGO5Ws6491yypo2rfmWqx1gu

---

### Рекурсивное сравнение:
Данным примером diff описывает то, что произошло с каждым ключом в diff. Например, был ли он добавлен, изменен или удален.

Для сранения двух файлов используйте команду: __gendiff file1.json file2.json__

https://asciinema.org/a/ywSbxIHLxJpXE5K5lvI4TymSC

---

### Плоский формат:
Plain формат представляет данные в линейном виде. 
Это идеальный вариант для визуального ознакомления относительно различий между файлами, а также для простых текстовых отчетов, если нет необходимости в дополнительном парсинге. 

Для сранения двух файлов используйте команду: __gendiff --format plain file1.json file2.json__

https://asciinema.org/a/qigKRmfcosbsjYyQJCRB9gTjf

### Вывод в JSON:
Данный вывод удобен для широкого применения, так как JSON формат поддерживается всеми современными языками программирования.
Его легко парсить и обрабатывать данные с помощью множества доступных библиотек и инструментов.
JSON поддерживает сложные структуры данных, такие как вложенные объекты и массивы, что позволяет точно и полно представлять данные.

Для сранения двух файлов используйте команду: __gendiff --format json file1.json file2.json__

https://asciinema.org/a/2E7Bmc9ACSo9SzK7829sMuwOG

