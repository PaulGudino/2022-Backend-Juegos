# Requirements

* asgiref               3.5.2
* backports.zoneinfo    0.2.1
* Django                4.1
* django-cors-headers   3.13.0
* django-simple-history 3.1.1
* djangorestframework   3.13.1
* MarkupSafe            2.1.1
* mysqlclient           2.1.1
* pip                   20.2.3
* PyJWT                 2.4.0
* pytz                  2022.2.1
* setuptools            49.2.1
* sqlparse              0.4.2
* tzdata                2022.2
* Werkzeug              2.2.2

## Requierements

### Create the mysql database or Deleted if exist

Enter mysql-server from Window cmd or Linux bash

```
mysql -u root -p
```

enter your root password and press enter.

Run this commands

```mysql

DROP DATABASE juegos;
CREATE DATABASE juegos;
USE juegos;
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'Root@123';
GRANT ALL PRIVILEGES ON juegos.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;

```

### Create the python virtual environment

Windows

```cmd
python -m venv venv
venv\Scripts\activate
```

Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Run the server

```python
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```

### Create a django super user

```python
py manage.py createsuperuser
```
Recomended
- username: admin
- email: email@example.com
- password: Root@123



# Install requirements

### Create the python virtual environment

Windows

```cmd
python -m venv venv
venv\Scripts\activate
```

Linux

```bash
python3 -m venv venv
source venv/bin/activate
```
# Install packages
```python
pip install Django django-cors-headers djangorestframework mysqlclient PyJWT pytz tzdata Werkzeug 
```

