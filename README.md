# Todolist

Created api for a todolist
1)Endpoint: /list/
[
{
"title": "bills"
},
{
"title": "shoppinglist"
}
]
2)Endpoint : list/1
[
{
"id": 1,
"title": "apple",
"description": "1 kg",
"created_date": "2022-06-01T09:07:26.073504Z",
"due_date": "2022-06-04T09:06:47Z",
"todolist": "shoppinglist"
}
]

## Run

1. Clone the repository

```shell
git clone https://github.com/mathewsaju23/todolist.git
```

2. Move into the repo

```shell
cd todolist
```

3. Install the dependencies

```shell
bash commands.sh
```

4. Run the file

```shell
python3 manage.py runserver
```
