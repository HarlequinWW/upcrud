from flask import Flask, render_template, request, redirect, flash
from models import Todo, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://harlequin:0000@192.168.56.101:5432/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "StrengGeheim"

db.init_app(app)


@app.route('/')
def home():
    all_data = Todo.query.all()
    return render_template('index.html', notes=all_data)


@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        data = Todo(title, content)
        db.session.add(data)
        db.session.commit()

        flash("Done!")

        return redirect('/')


@app.route('/update', methods=['POST'])
def update():
    data = Todo.query.get(request.form.get('id'))
    data.title = request.form['title']
    data.content = request.form['content']

    db.session.commit()

    flash("Done!")

    return redirect('/')


@app.route('/delete', methods=['GET'])
def delete():
    data = Todo.query.get(request.form.get('id'))
    db.session.delete(data)
    db.session.commit()

    flash("Done!")

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
