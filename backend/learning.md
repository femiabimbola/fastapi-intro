# Learning using FastAPI

 ### Activate the virtual environment

```
python -m venv env

source env/Scripts/activate
```

You can then install `uvicorn` to run the server

```
pip install uvicorn

uvicorn main:app --reload
```

#### Installing Postgress driver and SQL query

```bash
pip install sqlalchemy psycopg2
```