# recipe-suggestion

## Create virtual env using below command

```
python3 -m venv venv
```

## Activate virtual environment using below command

```
source venv/bin/activate
```

## Install Requirements using below command

```
pip3 install -r requirements.txt
```

## Run Migrations(Only First time)

```
python3 manage.py makemigrations know_your_food
```

```
python3 manage.py migrate
```

## Run python script using below command

```
python3 manage.py runserver
```

## To upload the nutritional information sheet use the below command(Use only one time)

```
python3 manage.py import_excel
```

## Deactivate virtual environemnt using below command

```
deactivate
```
