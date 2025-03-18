# KOCHA
#### KOCHA app that allows people to find qualified coaches, 2021
#### By **[CIAN](https://github.com/Cian747)**
## Description
* Kocha is an application that allows users to find qualified and suitable coaches in all disciplines around their area. A coach can also register and advertise their business and show off their skills and experience on their profile. 
* Find sport events and activties near you and get exposed to new people and cultures.
## Setup/Installation Requirements
* git clone the repo to your local desktop
```
git clone https://github.com/Cian747/coach.git
```
* Install the dependencies from the requirements file
```
pip install -r requirements.txt
```
* make and run your app on you local server
```
python manage.py runserver
```
* Create and test the methods for the new features added.
```
python manage.py test <app-name>
```
* Create a .env file to hold your sensitive data like so:
```
SECRET_KEY='your_secret_key'
DEBUG=False 
DB_NAME='db_name'
DB_USER='your_username_postgres'
DB_PASSWORD='password'
DB_HOST='127.0.0.1'
MODE='prod' 
ALLOWED_HOSTS='.localhost','.herokuapp.com','.127.0.0.1'
DISABLE_COLLECTSTATIC=1
EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='your_email'
EMAIL_HOST_PASSWORD='email_password'

```
* commit all your changes and create a pull request
```
git add.
git commit -m "edit that was made"
git push origin <branch-name>
```

* Deployment
```
git add.
git commit -m "deployment"
git push heroku main
```

## Known Bugs
None
## Technologies Used
* Django
* CSS
* Bootstrap
* PostgreSQL
* Python

## Support and contact details
cianomondi@gmail.com
### License

Copyright (c) 2021 **CIAN**