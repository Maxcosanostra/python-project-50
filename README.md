<h1 align="center" style="font-size: 3em;">Вычислитель отличий / Generate Difference</h1>

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Maxcosanostra/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Maxcosanostra/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/2e4a74f501af8c1ccd04/maintainability)](https://codeclimate.com/github/Maxcosanostra/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/2e4a74f501af8c1ccd04/test_coverage)](https://codeclimate.com/github/Maxcosanostra/python-project-50/test_coverage)

---

### Описание 
Вычислитель отличий - это универсальная программа, которая принимает на вход путь до конфигурационных файлов и возвращает описание различий между структурами данных файлов. 
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

### Ссылки

| Инструменты | Описание |
|----------|----------|
| [Poetry](https://python-poetry.org/) | Инструмент для управления зависимостями и создания виртуальных окружений в проектах на Python. |
| [Py.Test](https://docs.pytest.org/en/latest/) | Фреймворк для тестирования, который позволяет легко писать и запускать тесты. |
| [Flake8](https://flake8.pycqa.org/en/latest/) | Инструмент для проверки стиля кода согласно стандартам PEP 8. |

---

### Установка

1. Клонируйте репозиторий по ссылке:
    ```sh
    git clone https://github.com/Maxcosanostra/python-project-50
    ```

2. Перейдите в директорию проекта:
    ```sh
    cd python-project-50
    ```

3. Установите пакет:
    ```sh
    make package-install
    ```
---

### Опции сравнения файлов
Пользователям доступны два способа сравнения файлов — из корневой директории проекта или непосредственно из директории, где находятся сравниваемые файлы. Выбор способа зависит от того, 
где Вы находитесь в файловой системе:
1. Из корневой директории проекта:
Укажите относительный путь от корневой директории до файлов. Например, если Вы находитесь в корне вашего проекта и файлы расположены в поддиректории tests/fixtures, используйте следующую 
команду:
```sh
gendiff tests/fixtures/file1.json tests/fixtures/file2.json
```  
2. Из директории с файлами:
Если вы находитесь в той же директории, где расположены сравниваемые файлы, можно запустить gendiff, указывая только имена файлов. Например:
```sh
gendiff file1.json file2.json
```
Ниже приведены команды запуска сравнения файлов из директории  расположения самих файлов.

---

### Сравнение плоских файлов (JSON):
Сравнение строится на основе того, как изменилось содержимое во втором файле относительно первого, позволяющее быстро определить изменения в структуре данных JSON-файлов.
Для сранения двух файлов используйте команду:
```sh
gendiff flat_file1.json flat_file2.json
```

[![asciicast](https://asciinema.org/a/MJPjs1zTfxIxW4aDTQXFntI8T.svg)](https://asciinema.org/a/MJPjs1zTfxIxW4aDTQXFntI8T)

---

### Сравнение плоских файлов (YAML):
Поиск различий между двумя простыми, одноуровневыми YAML-файлами без вложенных структур. Легкочитаемый синтаксис помогает быстро ориентироваться в разнице между файлами. 

Для сранения двух файлов используйте команду:
```sh
gendiff flat_file1.yml flat_file2.yml
```

[![asciicast](https://asciinema.org/a/ti2HW6koM4Uq3gITXJTIEZFZz.svg)](https://asciinema.org/a/ti2HW6koM4Uq3gITXJTIEZFZz)

---

### Рекурсивное сравнение:
Данным примером diff описывает то, что произошло с каждым ключом в diff. Например, был ли он добавлен, изменен или удален.

Для сранения двух файлов используйте команду:
```sh 
gendiff file1.json file2.json
```

[![asciicast](https://asciinema.org/a/VsptnAtA6tyjaleMM9nm0mwef.svg)](https://asciinema.org/a/VsptnAtA6tyjaleMM9nm0mwef)

---

### Плоский формат:
Plain формат представляет данные в линейном виде. 
Это идеальный вариант для визуального ознакомления относительно различий между файлами, а также для простых текстовых отчетов, если нет необходимости в дополнительном парсинге. 

Для сранения двух файлов используйте команду:
```sh
gendiff --format plain file1.json file2.json
```

[![asciicast](https://asciinema.org/a/tFREpk5fq1ehMygKq8iciX7yx.svg)](https://asciinema.org/a/tFREpk5fq1ehMygKq8iciX7yx)

---

### Вывод в JSON:
Данный вывод удобен для широкого применения, так как JSON формат поддерживается всеми современными языками программирования.
Его легко парсить и обрабатывать данные с помощью множества доступных библиотек и инструментов.
JSON поддерживает сложные структуры данных, такие как вложенные объекты и массивы, что позволяет точно и полно представлять данные.

Для сранения двух файлов используйте команду:
```sh
gendiff --format json file1.json file2.json
```

[![asciicast](https://asciinema.org/a/pC4g0avqpWzOMq7r5XrpzOQeg.svg)](https://asciinema.org/a/pC4g0avqpWzOMq7r5XrpzOQeg)

---

Проект выполнен благодаря прохождению практики в Hexlet.io под руководством Рафаэля Мухаметшина

С Уважением, MaxCosaNostra
