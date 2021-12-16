## Advanced Templates
___
### Table Of Contents
* What you will learn
  * Useful Resources
  * Rendering Templates
  Statements
    * If statement
    * For loops
  * Template Inheritance: Add a placeholder block of code
  * Feedback
___
### What You Will Learn
* More complex Flask Templates
___
### Useful Resources
* **Must See !!** [Video on Creating and Styling Templates + Templates Inheritance](https://www.youtube.com/watch?v=QnDWIZuWYW0 "Video on Creating and Styling Templates + Templates Inheritance")
___
### Rendering Templates
To render a template you can use the render_template() method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments.

Flask will look for templates in the templates folder.

Therefore, you have to create a templates folder in your project folder. The html files should be inside the templates folder
___
**Example without argument**
**app.py**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello():
    return render_template('hello.html')


if __name__ == "__main__":
    app.run(debug=True,port=5000)
```
**templates/hello.html**
```html
<html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h1>Hello Word</h1>
</body>
</html>
```
**Example with argument**
**app.py**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<username>')
def hello(username):
    return render_template('hello.html', name=username)


if __name__ == "__main__":
    app.run(debug=True,port=5000)
```
**templates/hello.html**
```html
<html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h1>Hello {{name}} </h1>
</body>
</html>
```
___
