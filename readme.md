#### .venv
```shell
python -m venv .venv  
source .venv/bin/activate
pip freeze > requirements.txt
pip install -r requirements.txt
```

#### pre req for dev
```shell
npm install -g @angular/cli
```

#### Docker
```shell
docker build . -t fui
docker run --rm --name=fui -P fui python app.py
```

