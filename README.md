# MindBox_Test
Тестовое задание на должность Intern Data Engineer


## Задание 1.
Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. Дополнительно к работоспособности оценим:

- Юнит-тесты
- Легкость добавления других фигур
- Вычисление площади фигуры без знания типа фигуры в compile-time
- Проверку на то, является ли треугольник прямоугольным


## Задание 2.
В PySpark приложении датафреймами (pyspark.sql.DataFrame) заданы продукты, категории и их связи. Каждому продукту может соответствовать несколько категорий или ни одной. А каждой категории может соответствовать несколько продуктов или ни одного. Напишите метод на PySpark, который в одном датафрейме вернет все пары «Имя продукта – Имя категории» и имена всех продуктов, у которых нет категорий.

# Содержание репозитория
Папка **test_task** имеет:
- папку **calculate_figures** c кодом `calculate.py`
- код для тестов `tests.py`
- папку **data_frame** с блокнотом Jupyter кодом `task_2.ipynb`



# Установка Pyspark локально из pip

## Предварительные требования

  1. Python 3.9+
  2. Установленный Java/OpenJDK версии 11 или выше.
     Проверить установку из терминала (Windows/Linux/macOS):
     
     `java -version`
     
     `openjdk version "21.0.2" 2024-01-16 LTS`
     
     `OpenJDK Runtime Environment Microsoft-8905927 (build 21.0.2+13-LTS)`
     
     `OpenJDK 64-Bit Server VM Microsoft-8905927 (build 21.0.2+13-LTS, mixed mode, sharing)`


## Установка Apache Spark
  1. Делаем виртуальное окружение Python:
     
     `python -m venv venv`
     
     `source venv/bin/activate`
     
  3. Активируем окружение
     
     `# Linux, macOS`
     
     `source venv/bin/activate`

     `# Windows`
     
     `venv/Scripts/activate.bat`
     
     [Официальная инструкция](https://docs.python.org/3/library/venv.html) по активации окружения

  5. Ставим pyspark из **pip**:
     `(venv) pip install pyspark` 
