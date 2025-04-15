# AtomicsHabbits

Django REST API for tracking and managing useful habits inspired by the book Atomic Habits. Users can create, track, and repeat habits, get reminders via Telegram, and optionally share habits with others.

## 🧰 Technologies
Django

Django REST Framework

Celery + Redis

Telegram Bot API

Simple JWT

PostgreSQL 

Pytest + Coverage

Flake8 + Black

## 📦 Installation  (with Poetry)
- git clone https://github.com/Volodymyr-tech/AtomicsHabbits_Git.git

#### Activate virtual environment (optional, but useful for shell)
- poetry shell

#### Install dependencies
- poetry install


#### Create a .env file in the project root with your environment variables:
- SECRET_KEY = Add secrert key from setting here
- NAME= add name of DB
- USER= add users name
- PASSWORD= add password for DB
- HOST= Add host
- PORT= add port
- TELEGRAM_TOKEN = Add telegram token for bot
- TELEGRAM_CHAT_ID = add your telegram chat id

#### Run migrations:
- python manage.py migrate

#### Load test data:
- python manage.py loaddata users_fixture.json
- python manage.py loaddata habbit_fixture.json


### A Celery worker running:
- celery -A config beat -l info -S django
- celery -A config worker -l INFO -P eventlet (for Windows)

## 🚀 Features

✅ User registration and JWT authentication (Simple JWT)

✅ CRUD for habits

✅ Pleasant vs. useful habit logic with validation

✅ Periodicity (times per week) with scheduler logic

✅ Telegram bot integration for reminders

✅ Public habits listing for community sharing

✅ Pagination (5 habits per page)

✅ Admin panel

✅ CORS-ready for frontend integration

## 🧠 Habit Model Explanation
Each habit consists of:

User — who owns it

Action — e.g. "Do pushups"

Place — where the habit is done

Time — when to do it

Periodicity — how many times per week

Reward or Pleasant Habit — but never both at once!

Public — is it shared with others?

Time to do — must be ≤ 120 seconds

## ⚠️ Validation:

Either award or connected_habbit, not both

Pleasant habits can’t have rewards or be connected

Periodicity must be at least 1 per week

## 🛎 Reminder System
A scheduled Celery task checks every 5 minutes:

Finds habits where time <= now

Sends a Telegram message via bot

Recalculates next execution time:
next_time = current_time + (7 / periodicity) days

## 📬 Telegram Integration
Bot sends reminders to users. You’ll need:

A bot token (@BotFather)

Your Telegram chat_id


## 👤 Author
Created by Volodymyr (@Volodymyr-tech)
For learning, portfolio and practical productivity tracking