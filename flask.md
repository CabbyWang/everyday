***
# Flask

## Debug Mode
```python
$ export FLASK_DEBUG=1
$ flask run
```
(On Windows use `set` instead of `export`)

```python
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'
```

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
```