# <div align="center">CLOTHING STORE 🛍️</div>

<div align="center">
<img src="assets/products.png" align="center" style="width: 100%; height: 40%" />
</div>

<br/>

I made this django project to explore new technologies and libraries, as well as hone my docker containerization skill.
In this project, I have collected the most popular and necessary tools for creating complex and full-fledged projects.

## Description

<div align="center">
<img src="assets/store.gif" align="center" style="width: 60%; height: 40%" />
</div>

<br/>

This is one of the most complex Django projects that I have implemented to date. I created an online store where you can
log in through social networks or register, receive email confirmation letters, purchase various products, sort them by
categories, and then pay through the Stripe system. You can also see a list of all your orders and their status. This is
a fully functional and ready-to-use online store.

Since I position myself as a backend developer, I focused on the internal components, not the appearance of the
site.

## Technologies

***Languages***

![Python](https://img.shields.io/badge/-Python-1C1C1C?&style=for-the-badge)
![JavaScript](https://img.shields.io/badge/-JavaScript-1C1C1C?&style=for-the-badge)
![HTML](https://img.shields.io/badge/-HTML-1C1C1C?&style=for-the-badge)
![CSS](https://img.shields.io/badge/-CSS-1C1C1C?&style=for-the-badge)

***Framework***

![Django](https://img.shields.io/badge/-Django-1C1C1C?&style=for-the-badge)

***Databases***

![Postgres](https://img.shields.io/badge/-Postgresql-1C1C1C?&style=for-the-badge)
![Redis](https://img.shields.io/badge/-Redis-1C1C1C?&style=for-the-badge)

***Libraries***

![Django-allauth](https://img.shields.io/badge/-Django--allauth-1C1C1C?&style=for-the-badge)
![Celery](https://img.shields.io/badge/-Celery-1C1C1C?&style=for-the-badge)
![Aiocron](https://img.shields.io/badge/-django--redis-1C1C1C?&style=for-the-badge)
![Asyncpg](https://img.shields.io/badge/-psycopg2-1C1C1C?&style=for-the-badge)
![aioredis](https://img.shields.io/badge/-stripe-1C1C1C?&style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/-Bootstrap-1C1C1C?&style=for-the-badge)
![JQuery](https://img.shields.io/badge/-JQuery-1C1C1C?&style=for-the-badge)

***Other***

![Docker](https://img.shields.io/badge/-Docker-1C1C1C?&style=for-the-badge)
![StripeCLI](https://img.shields.io/badge/-Stripe_CLI-1C1C1C?&style=for-the-badge)

## Project setup

***Method 1: Via docker-compose***

1. Create a .env file and paste the data from the .env.example file into it
2. In REDIS_HOST and POSTGRES_HOST, specify the names of docker-compose services (redis and db)
3. In BOT_TOKEN, specify the token of your telegram bot created earlier via BotFather
4. In the terminal, enter the following command:

```
docker-compose up --build
```

***Method 2: Via virtual environment***

1. Create and activate a python virtual environment
2. In the terminal, enter the following command:

```
pip3 install -r requirements.txt
```

3. Create a .env file and paste the data from the .env.example file into it
4. In REDIS_HOST and POSTGRES_HOST, specify localhost
5. In BOT_TOKEN, specify the token of your telegram bot created earlier via BotFather
6. Run the file bot.py

## <div align="center">Thank you for taking the time to review my project. Enjoy reading!👋</div>