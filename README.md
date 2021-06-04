
# Django Newspaper App (Basic)
This project is an extended version of [A Basic Django Blog App](https://github.com/asis2016/django-blog-app) but with basic functionality. The project made on Django framework.


## Tech Stack
Docker 20.10.6, Python 3.8, Django 3.2.3, Whitenoise, Gunicorn, Heroku


## Demo
[https://basic-newspaper-app-amaharjan.herokuapp.com/](https://basic-newspaper-app-amaharjan.herokuapp.com/)

- username: admin
- password: admin

## Environment Variables

To run this project, you will need to add the following environment variables:

`SECRET_KEY` `django-insecure-82fe0_^x$$r33o7$$8n@*lb*t@=k-$$ozmt*4m=6=f5jdrl8xx!m8`

## Run Locally

Clone the project

```bash
  git clone https://github.com/asis2016/django-newspaper-app.git
```

Go to the project directory

```bash
  cd django-newspaper-app
```

Start the project

```bash
  docker build .
```

```bash
  docker-compose up -d
```

## Running Tests

To run tests, run the following command

```bash
  docker-compose exec web python manage.py test
```

## Running the project locally

Goto [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- username: admin
- password: admin

### Running Django Administration

Goto [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
- username: admin
- password: admin
  


  
## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

## Feedback

If you have any feedback, please reach out to us at hello@amaharjan.com

  
## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

  