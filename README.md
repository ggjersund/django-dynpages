# Dynpages

A lightweight Dynamic Django flatpage application with i18n support and no sites requirements.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

i18n has to be enabled for this application to work properly.
See the following link for instructions on how to enable [Internationalization](https://docs.djangoproject.com/en/2.0/topics/i18n/).

Dependencies:

```
Django >= 2.0.0
```

### Installing

1. First download or clone the application into your Django Project

```
cd <YOUR DJANGO PROJECT FOLDER> [Mac / Linux]
dir <YOUR DJANGO PROJECT FOLDER> [Windows]
git clone https://github.com/ggjersund/django-dynpages
```

2. Add dynpages to your INSTALLED APPS list

```
INSTALLED_APPS = [
    ...
    'dynpages',
    ...
]
```

3. Make migrations and run migrate

```
python manage.py makemigrations
python manage.py migrate
```

4. Voila! Visit your Django admin to use add/change dynamic pages.

## Built With

* [Django 2.0.0](https://www.djangoproject.com/) - Web Framework

## Authors

* **G. Gjersund** - *Initial work* - [ggjersund](https://github.com/ggjersund/)

See also the list of [contributors](https://github.com/ggjersund/django-dynpages/graphs/contributors) who participated in this project.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details