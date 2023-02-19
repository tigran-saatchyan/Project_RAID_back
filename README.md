# RAID 3.0 - SKYRENT
![alt text](https://img.shields.io/badge/Python-v3.10.6-blue?style=for-the-badge&logo=appveyor "Python")
![alt text](https://img.shields.io/badge/Flask-v2.2.3-green?style=for-the-badge&logo=appveyor "Flask")

![alt text](https://img.shields.io/badge/Flask%E2%80%93SQLAlchemy-v3.0.3-yellow?style=for-the-badge&logo=appveyor "Python")
![alt text](https://img.shields.io/badge/flask%E2%80%93restx-v1.0.6-yellow?style=for-the-badge&logo=appveyor "Python")

![alt text](https://img.shields.io/badge/SQLAlchemy-v2.0.4-yellow?style=for-the-badge&logo=appveyor "Python")
![alt text](https://img.shields.io/badge/marshmallow-v3.19.0-yellow?style=for-the-badge&logo=appveyor "Python")

***
Разработать MVP сервиса доски объявлений по 
длительной аренде жилья для релокации. Минимальная версия 
сервиса будет позволять просматривать список, просматривать 
карточку, фильтровать и просматривать контакты арендатора.

### Бэкенд

**База данных**

- [x]  Создайте проект и разверните бойлерплейт
- [x]  Создайте модели для бд и наполните бд

Ключи модели и отдаваемого JSON:

```python
pk: int  # первичный ключ

title: str # название объекта
description: str  # описание объекта

picture_url: str  # путь к картинке

price: int # цена за месяц

country: str # страна
city: str # город

features_on: list[str] # что есть
features_off: list[str] # чего нет
```

Актуальный JSON с данными

[https://drive.google.com/file/d/1tKZVENJkEZDwprhte62iuI1a8rj254W1/view?usp=sharing](https://drive.google.com/file/d/1tKZVENJkEZDwprhte62iuI1a8rj254W1/view?usp=sharing)

**Эндпоинты для списка**

- [x]  Добавьте эндпоинт `GET /places` который возвращает все места
- [ ]  Добавьте к нему фильтрацию по городу `GET /places?city=<city>`
- [ ]  Добавьте к нему фильтрацию по цене `GET /places?from=1,to=1000`

**Эндпоинты для сущности**

- [ ]  Добавьте эндопоинт `GET /places/<pk>` который возвращает подробную информацию

**Обработка ошибок**

- [ ]  Добавьте обработку 404 ошибки на ваше усмотрение

- [ ]  Добавьте обработку 500 ошибки на ваше усмотрение

---
