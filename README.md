## WandaVision Quote API
API using Django REST Framework to serve quotes from the Disney+ TV show, 'WandaVision.'

## How to run locally
### Linux
1. `git clone git@github.com:hillaryosei/wandavision-quote-api.git`
2. `apt install python3`
3. `cd wv-api`
4. `python3 -m venv venv`
5. `source venv/bin/activate`
6. `mv sample.config.py config.py`
7. `python3 manage.py migrate`
8. `python3 manage.py runserver`
9. Open local host (127.0.0.1:8000) in preferred browser 

### Windows
1. `git clone git@github.com:hillaryosei/wandavision-quote-api.git`
2. Install python3
3. `cd wv-api`
4. `python -m venv venv`
5. `venv\Scripts\activate`
6. `move sample.config.py config.py`
7. `python manage.py migrate`
8. `python manage.py runserver`
9. Open local host (127.0.0.1:8000) in preferred browser 

## Paths
#### `quotes/`
view entire list of quotes
#### `quotes/<int:id>`
view a specific quote, up to 119 (ex: quotes/72)


## Deployment
The main branch can be viewed on [Heroku](https://wandavision-api.herokuapp.com/quotes/)
