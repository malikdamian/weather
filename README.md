# weather

Choose between a normal installation or docker image build.

## Install

1. Clone this repository

```bash
git clone https://github.com/malikdamian/weather
```

2. Create and activate the python virtual environment

```bash
cd weather
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

### Run

```bash
python manage.py migrate
python manage.py makemigrations
python manage.py runserver --noreload
```

## Docker

1. Clone this repository

```bash
git clone https://github.com/malikdamian/weather
```

2. Create and activate the python virtual environment

```bash
cd weather
python3 -m venv venv
source venv/bin/activate
```

### Run

```bash
docker-compose up -d
docker-compose exec web python manage.py migrate 
```