# mico-loans-webapi

Backend application for loan management

## Project setup

```
pip install -r requriments.txt
```

### create Admin user

```
export PYTHONPATH=./
python commands/create_super_user.py -f Test -l [USER_NAME]] -e [EMAIL_USER] -p [PHONE_USER] -pa [PASSWORD_USER]
```

### Upgrade migrations

```
alembic revision --autogenerate -m "Initial"
alembic upgrade head
```

### start project

```
uvicorn main:app --reload
```
