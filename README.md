# <div align="center">CLOTHING STORE 🛍️</div>

<div align="center">
<img src="assets/products.png" align="center" style="width: 100%; height: 40%" />
</div>

<br/>

I made this django project to explore new technologies and libraries, as well as hone my docker containerization skill.
In this project, I have collected the most popular and necessary tools for creating complex and full-fledged projects.

## Description

<div align="center">
<img src="assets/store.gif" align="center" style="width: 80%; height: 40%" />
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

1. Create a .env file and paste the data from the .env.example file into it.
2. The value of the variable ALLOWED_HOST specify '*' or '0.0.0.0'.
3. Generate django secret key on [this site](https://djecrety.ir/) and specify it in the SECRET_KEY variable.
4. Create an email and configure it to send messages. You can learn more about how to do
   this [here](https://youtu.be/dnhEnF7_RyM?t=902).
5. Register in Stripe, copy the Publishable key and Secret key. Insert the values into the variables STRIPE_PUBLIC and
   STRIPE_SECRET_KEY.
6. Run the project by entering following command:

```
docker-compose up --build
```

7. After the project starts, you will see your webhook signing secret at the bottom of the console. Copy it and paste
   the value into the STRIPE_WEBHOOK_SECRET variable. Reload the container:
```
docker-compose up -d
```
8. Perform migration to the database:

```
docker-compose exec web python manage.py migrate
```

9. Create a superuser by entering the following command:

```
docker-compose exec web python manage.py createsuperuser
```

10. You can log in to the [admin panel](http://127.0.0.1:8000/admin) and add new products and categories or upload the
   fixtures I created by entering the command:

```
docker-compose exec web python manage.py loaddata products/fixtures/products.json
```

#### You can use the data of [these](https://stripe.com/docs/testing) bank cards to test the payment in the store.

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