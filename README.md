Simple blog application using Django
====================================

Setup
-----

```
pip install -r requirements.txt
```

Configure postgres
^^^^^^^^^^^^^^^^^^

Install postgres using [docker](https://docs.docker.com/samples/library/postgres/) or from the [source](https://www.postgresql.org/download/)

Update settings.py with the correct postgres connection values.

Apply migrations
^^^^^^^^^^^^^^^^

Run `python manage.py migrate` to create appropriate tables in the database.

Testing
-------

Fetch all articles
^^^^^^^^^^^^^^^^^^

```
  curl http://localhost:8000/articles -H "Authorization: Bearer 70kc8b75ca68amj3xwrayqvy9j46yzr" -H 'Content-Type: application/json'
```

```
[
  {
    "title": "Update rows using postgres",
    "description": "Update rows using postgres",
    "author_id": 2,
    "id": 2
  }
]
```

Fetch articles owned by the specific author
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```
  curl  http://localhost:8000/author/articles -H "Authorization: Bearer 70kc8b75ca68amj3xwrayqvy9j46yzrf" -H 'Content-Type: application/json'
```

```
[
  {
    "title": "Insert rows using postgres",
    "description": "This blog post will take you through the steps which needs to be followed to insert rows using postgres",                       
    "author_id": 2,
    "id": 1
  },
  {
    "title": "Update rows using postgres",
    "description": "Update rows using postgres",
    "author_id": 2,
    "id": 2
  }
]
```
