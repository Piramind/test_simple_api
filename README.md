# test_simple_api

<h3>Задание</h3>

Создать веб-сервис, который будет выводить "Rekruto! Давай дружить!". 
URL с GET запросом, который будет выводиться уже на странице:

url должен быть таким
```
xx.xx.xx.xx./?name=Rekruto&message=Давай дружить!
```
Вывод
```
Hello {name}! {message}!
```

<h3>Инструкция по запуску:</h3>

1. Клонирование проекта
```
git clone https://github.com/Piramind/test_simple_api.git
```
2. Создание виртульного окружения

```
virtualenv venv
```

3. Активация виртульного окружения
```
source env/Scripts/activate (win)

source env/bin/activate (Linux)

```
4. Установка зависимостей

```
pip install -r requirements.txt
```
5. Запуск
```
uvicorn index:app --reload
```