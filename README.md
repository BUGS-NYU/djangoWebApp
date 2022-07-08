# BUGS Open Source Django Web App - NYU Opportunities Forum

## Summary:

A web application that allows NYU students to share and find job opportunities / conferences / events that would be relevant for the NYU community. It’s a platform for students, by students. 

## Requirements / To-Dos:

- [ ] Ability to post opportunities within higher level categories (suggestions for categories!) 
- [ ] Ability to view and search for opportunities (searching by keyword)
- [ ] Notifications on a certain type of opportunity (maybe SMS or Email?) 
- [ ] Messaging feature for the “owner of an opportunity” 
- [ ] Saving opportunities 
- [ ] Asking questions for the owner 
- [ ] Sending opportunities to another user 

## Getting Started

To copy this repo run `git clone https://github.com/BUGS-NYU/djangoWebApp.git` on your command line or terminal.

### Pre-requisites

Make sure you have python 3 and pip installed on your machine. 

### Installing

Get your virtual environment running.

```
virtualenv venv
source venv/bin/activate
```

Install all the packages by running 

```
pip install -r requirements.txt (Python 2)
or 
pip3 install -r requirements.txt
```

Set up database by `python manage.py makemigrations` and `python manage.py migrate`

Create Super user or admin to work with the database `python manage.py createsuperuser`

To make sure that you've properly installed your django app run `python manage.py runserver` 

Open your web browser and visit the following site.

```
http://localhost:8000/
```

Use ``http://localhost:8000/admin`` to visit admin page




