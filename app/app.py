from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route('/')
def todo():
    _items = db.todos.find()
    items = [item for item in _items]
    # Render default page template
    return render_template('index.html', items=items)

@app.route('/new', methods=['POST'])
def new():

    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    # Save items to database
    db.todos.insert_one(item_doc)

    return redirect(url_for('todo'))


if __name__ == '__main__':
    app.run(debug=True)
