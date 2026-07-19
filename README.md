# CRM-система

Веб-приложение для управления бизнес-процессами компании, предоставляющей маркетинговые услуги. Система охватывает полный цикл работы с клиентом: от рекламной кампании и привлечения лида до заключения контракта и перевода в активного клиента.

## Технологии

| Категория | Технология |
|-----------|------------|
| Язык | Python 3.14+ |
| Фреймворк | Django 6.0 |
| База данных | PostgreSQL 15+ |
| Шаблоны | Django Templates + Bootstrap 5 |
| Тестирование | pytest + pytest-django |
| Статический анализ | mypy + django-stubs, pylint + pylint-django |
| Управление зависимостями | pip + venv |

## Архитектура

```
crm_system/
├── config/                 # Настройки проекта Django
│   ├── settings.py         # Конфигурация (БД, static, media, logging)
│   ├── urls.py             # Корневые URL-маршруты
│   └── wsgi.py             # Точка входа WSGI
├── apps/                   # Приложения проекта
│   ├── products/           # Услуги компании
│   ├── ads/                # Рекламные кампании
│   ├── leads/              # Потенциальные клиенты (лиды)
│   ├── contracts/          # Контракты
│   ├── customers/          # Активные клиенты
│   └── common/             # Общие утилиты и management-команды
├── templates/              # HTML-шаблоны
│   ├── _base.html          # Базовый шаблон (sidebar, navbar)
│   ├── users/              # Главная страница
│   ├── registration/       # Login / Logout
│   ├── products/           # CRUD-шаблоны услуг
│   ├── ads/                # CRUD + статистика РК
│   ├── leads/              # CRUD-шаблоны лидов
│   ├── contracts/          # CRUD-шаблоны контрактов
│   └── customers/          # CRUD-шаблоны активных клиентов
├── static/                 # CSS
├── media/                  # Загруженные файлы (документы контрактов)
├── logs/                   # Файлы логов
├── conftest.py             # Фикстуры pytest
├── manage.py               # Управляющий скрипт Django
└── pyproject.toml          # Конфигурация инструментов (mypy, pylint, pytest)
```

## Модели и связи

```
Product ─────────────────────┐
  │                          │
  │ (FK)                     │ (FK)
  ▼                          ▼
AdCampaign                 Contract
  │                          │
  │ (FK)                     │ (FK)
  ▼                          ▼
Lead ──── (OneToOne) ────▶ Customer
```

### Описание моделей

| Модель | Назначение | Ключевые поля |
|--------|-----------|---------------|
| **Product** | Услуга компании | `name`, `description`, `price` |
| **AdCampaign** | Рекламная кампания | `name`, `product` (FK), `channel`, `budget` |
| **Lead** | Потенциальный клиент | `full_name`, `phone`, `email`, `ad_campaign` (FK) |
| **Contract** | Контракт с клиентом | `name`, `product` (FK), `document` (FileField), `conclusion_date`, `duration`, `amount` |
| **Customer** | Активный клиент | `lead` (OneToOne), `contract` (FK) |

### Бизнес-логика

- Лид (`Lead`) приходит из рекламной кампании (`AdCampaign`)
- Лид конвертируется в активного клиента (`Customer`) через заключение контракта (`Contract`)
- Связь `OneToOne` между `Lead` и `Customer` гарантирует, что каждый лид может быть конвертирован только один раз
- В списке лидов отображаются только те, кто ещё не стал активным клиентом (фильтр `customer__isnull=True`)

## Роли и права доступа

Система использует ролевую модель доступа через `Group` и `Permission` Django.

| Роль | Доступные модули | Действия                                               |
|------|-----------------|--------------------------------------------------------|
| **Оператор** | Лиды, Рекламные кампании | Просмотр РК; создание, просмотр, редактирование лидов  |
| **Маркетолог** | Услуги, Рекламные кампании | Просмотр, создание, редактирование услуг и РК                         |
| **Менеджер** | Контракты, Лиды, Клиенты, РК | Проссмотр, создание, редактирование  контрактов и клиентов; просмотр лидов и РК |

## URL-маршруты

| URL | Имя | Описание |
|-----|-----|----------|
| `/` | `home` | Главная страница |
| `/login/` | `login` | Вход в систему |
| `/logout/` | `logout` | Выход из системы |
| `/admin/` | — | Админ-панель Django |
| `/products/` | `products:products-list` | Список услуг |
| `/products/create/` | `products:products-create` | Создание услуги |
| `/products/<pk>/` | `products:products-detail` | Детали услуги |
| `/products/<pk>/edit/` | `products:products-edit` | Редактирование услуги |
| `/products/<pk>/delete/` | `products:products-delete` | Удаление услуги |
| `/ads/` | `ads:ads-list` | Список рекламных кампаний |
| `/ads/create/` | `ads:ads-create` | Создание РК |
| `/ads/statistic/` | `ads:ads-statistic` | Статистика РК |
| `/ads/<pk>/` | `ads:ads-detail` | Детали РК |
| `/ads/<pk>/edit/` | `ads:ads-edit` | Редактирование РК |
| `/ads/<pk>/delete/` | `ads:ads-delete` | Удаление РК |
| `/leads/` | `leads:leads-list` | Список лидов |
| `/leads/create/` | `leads:leads-create` | Создание лида |
| `/leads/<pk>/` | `leads:leads-detail` | Детали лида |
| `/leads/<pk>/edit/` | `leads:leads-edit` | Редактирование лида |
| `/leads/<pk>/delete/` | `leads:leads-delete` | Удаление лида |
| `/contracts/` | `contracts:contracts-list` | Список контрактов |
| `/contracts/create/` | `contracts:contracts-create` | Создание контракта |
| `/contracts/<pk>/` | `contracts:contracts-detail` | Детали контракта |
| `/contracts/<pk>/edit/` | `contracts:contracts-edit` | Редактирование контракта |
| `/contracts/<pk>/delete/` | `contracts:contracts-delete` | Удаление контракта |
| `/customers/` | `customers:customers-list` | Список активных клиентов |
| `/customers/create/` | `customers:customers-create` | Создание клиента |
| `/customers/<pk>/` | `customers:customers-detail` | Детали клиента |
| `/customers/<pk>/edit/` | `customers:customers-edit` | Редактирование клиента |
| `/customers/<pk>/delete/` | `customers:customers-delete` | Удаление клиента |

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd skillbox_crm_system
```

### 2. Создание виртуального окружения

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения

Скопируйте `.env.example` в `.env` и заполните значения:

```bash
cp crm_system/.env.example crm_system/.env
```

### 5. Настройка PostgreSQL

Создайте базу данных и пользователя:

```sql
CREATE DATABASE crm_db;
CREATE USER crm_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE crm_db TO crm_user;
GRANT ALL ON SCHEMA public TO crm_user;
ALTER USER crm_user CREATEDB;
```

### 6. Применение миграций

```bash
cd crm_system
python manage.py migrate
```

### 7. Создание суперпользователя

```bash
python manage.py createsuperuser
```

### 8. Инициализация ролей

```bash
python manage.py init_roles
```

Создаёт три группы пользователей: **Оператор**, **Маркетолог**, **Менеджер** — с преднастроенными разрешениями.

### 9. Заполнение БД демо-данными (опционально)

```bash
python manage.py seed_demo
```

Создаёт моковые данные. Команда идемпотентна — повторный запуск не создаёт дубликаты.

### 10. Запуск сервера разработки

```bash
python manage.py runserver
```

Приложение будет доступно по адресу: http://127.0.0.1:8000/

## Тестирование

```bash
cd crm_system
pytest -v
```

Или для конкретного приложения:

```bash
pytest -v apps/ads/
pytest -v apps/contracts/
pytest -v apps/customers/
pytest -v apps/leads/
pytest -v apps/products/
```

### Фикстуры

Общие фикстуры определены в `conftest.py`:

## Статический анализ

### mypy

```bash
cd crm_system
mypy apps/
```

Конфигурация: `pyproject.toml` → `[tool.mypy]`. Использует `django-stubs` для типизации Django-моделей и ORM.

### pylint

```bash
cd crm_system
pylint apps/
```

Конфигурация: `pyproject.toml` → `[tool.pylint.main]`. Использует `pylint-django` для проверки Django-специфичного кода.

> **Важно:** pylint и mypy необходимо запускать из каталога `crm_system/` (где находится `manage.py`), чтобы корректно разрешались импорты.

## Статистика рекламных кампаний

Страница `/ads/statistic/` отображает агрегированные данные по каждой рекламной кампании:

- **Количество лидов** — сколько потенциальных клиентов пришло из РК
- **Количество активных клиентов** — сколько лидов конвертировано в клиентов
- **Суммарный доход** — сумма контрактов активных клиентов

Данные вычисляются в одном SQL-запросе с использованием аннотаций Django ORM (`Count`, `Sum`).

## Логирование

Логи записываются в файл `logs/project.log` с ротацией (1 МБ, 3 backup-файла). Уровень логирования — `INFO`.

## Структура проекта

- **Views**: Class-Based Views (`ListView`, `CreateView`, `DetailView`, `UpdateView`, `DeleteView`) с `LoginRequiredMixin` и `PermissionRequiredMixin`
- **Templates**: наследование от `_base.html` (боковое меню, навбар), Bootstrap 5 для стилизации
- **Admin**: расширенная конфигурация для всех моделей (`list_display`, `search_fields`, `list_filter`, `autocomplete_fields`)
- **Документирование**: все модули, классы и методы содержат docstrings в стиле reStructuredText (reST)