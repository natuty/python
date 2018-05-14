```
python "F:\Program Files\Python2.7\Scripts\django-admin.py" startproject HelloWorld
python manage.py runserver 0.0.0.0:8000

pip install mysqlclient

python "F:\Program Files\Python2.7\Scripts\django-admin.py" startapp TestModel
python manage.py migrate   # 创建表结构
python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
python manage.py migrate TestModel   # 创建表结构
```