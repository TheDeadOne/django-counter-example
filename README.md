# django-counter-example
Пример счётчика посещений для вопроса https://ru.stackoverflow.com/q/1001468/204271

## Установка
1. [Клонируйте репозиторий](https://help.github.com/en/articles/cloning-a-repository) на свой компьютер
2. Создайте и активируйте [виртуальное окружение](https://virtualenv.pypa.io) в каталоге репозитория
3. [Установите зависимости](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
4. [Примените миграции](https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-migrate)
5. [Загрузите тестовые данные](https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-loaddata)

    ```
    python manage.py loaddata posts
    ```

6. Запустите проект и откройте в браузере адрес http://localhost:8000/blog/

[![Скриншот][1]][1]

  [1]: https://habrastorage.org/webt/67/54/0f/67540f3ff265a865222124.png
