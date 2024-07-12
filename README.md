# fastapi-celery

## Встановлення та Запуск

Для запуску цього проекту використовуйте Docker та Docker Compose. Виконайте наступні кроки:

1. Клонуйте цей репозиторій:

    ```bash
    git clone https://github.com/ninaprus/fastapi-celery.git
    cd fastapi-celery
    ```

2. Створіть та налаштуйте файл `.env`за прикладом `.env.example`. Наприклад:
    ```env
    POSTGRES_DB=library_db
    POSTGRES_USER=user_db
    POSTGRES_PASSWORD=password_db
    ```

3. Запустіть Docker Compose:

    ```bash
    docker-compose up -d
    ```

Інтерактивна документація API
Тепер перейдіть до http://127.0.0.1:8000/docs

4. Зупинити Docker Compose:

    ```bash
    docker-compose down
    ```

## Використання

Після запуску контейнерів ви можете використовувати наступні ендпойнти:

- `GET /books` - Отримати список книг
- `GET /celery` - Запустити Celery завдання на REST запит до ендпоінта /books та передати результат запиту в Kafka

## Перевірка статусу контейнерів
1. Щоб перевірити статус ваших Docker-контейнерів, використовуйте команду:

    ```bash
    docker ps
    ```

## Підключення до Kafka-consumer
Щоб підключитися до Kafka-consumer і переглядати повідомлення з теми my-topic з початку, виконайте наступні команди:

1. Знайдіть ID контейнера Kafka:

    ```bash
    docker ps
    ```
2. Підключіться до Kafka-consumer:
    Замість <kafka-container-id> використовуйте фактичний ID вашого Kafka-контейнера.

    ```bash
    docker exec -it <kafka-container-id> /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-topic --from-beginning
    ```


    **Опис команди:**

    ```
    docker exec: Використовується для виконання команди всередині працюючого контейнера Docker.
    -it: Ці два прапорці:
        -i (інтерактивний режим) дозволяє взаємодіяти з процесом всередині контейнера.
        -t (псевдотермінал) створює псевдотермінал, що дозволяє запускати команду так, ніби підключилися до терміналу контейнера.
    <kafka-container-id>: Ідентифікатор контейнера Kafka
    /opt/kafka/bin/kafka-console-consumer.sh: Шлях до виконуваного файлу kafka-console-consumer.sh всередині контейнера Kafka, який запускає консольний споживач Kafka.
    --bootstrap-server localhost:9092: Прапорець --bootstrap-server вказує на адресу і порт сервера Kafka, до якого підключається споживач. У даному випадку це localhost з портом 9092.
    --topic my-topic: Прапорець --topic вказує на назву теми Kafka, з якої буде споживатися повідомлення. У даному випадку це my-topic.
    --from-beginning: Прапорець --from-beginning вказує споживачеві почати читати повідомлення з початку журналу теми, а не тільки нові повідомлення.
    ```