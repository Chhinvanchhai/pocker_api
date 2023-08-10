# Pocker API

## Project setup
```
 python3 -m venv .venv

 . .venv/bin/activate

 pip install -r requirements.txt
```

## Init databse
```
 python3

 from app import db
```

### Compiles and hot-reloads for development
```
 flask --app api run
```

### To data dependency
```
pip freeze > requirements.txt 
```

 docker run --name some-postgres -e POSTGRES_PASSWORD=123456 -d postgres 


### See more
See [Configuration Reference](https://flask.palletsprojects.com/en/2.3.x/installation/#).