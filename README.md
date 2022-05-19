# Django Restful CRUD API with MongoDB

This code was cloned from :
> [Django & MongoDB CRUD example with Rest Framework](https://bezkoder.com/django-mongodb-crud-rest-framework/)

Note : The author of this repository change several code in the original file after cloned from it's original repository. So this code was not 100% same to the original repository from bezkoder.

## Running the Application

### 1. Install Djongo

```pip install djongo```

For further instruction, read : https://github.com/doableware/djongo

### 2. Make migration file:

1. delete the migrations folder resided inside the `./DjangoRestApi/users` folder [if exist]

2. delete the pycache folder too [if exist]

3. restart the server [if your server is on and you are working from another cli]

4. Run python manage.py makemigrations <app_name> [explicit app_name is important] :

```
python manage.py makemigrations users
```

### 3. Create the DB tables first (Migration):

```
python manage.py migrate
```

#### - Error Migration : No migrations to apply [if happen]

```bash
Operations to perform:
  Apply all migrations: users
Running migrations:
  No migrations to apply.
```

Solution : Change database name in settings.py it works in my case. But the django app will working with different database name.

#### - OperationalError: database is locked 

`django.db.utils.OperationalError: database is locked`

Solution : In my case, It was because I open the database from SQLite Browser [DB Browser]. When I close it from the browser, the problem is gone.

https://docs.djangoproject.com/en/dev/ref/databases/#database-is-locked-errors

If this solution don't work, just switch to another DB such as MySQL, MongoDB or PostgreSQL.

#### - 

### 4. Run the development web server:

```
python manage.py runserver 8080
```

Open the URL http://localhost:8080/ to access the application.