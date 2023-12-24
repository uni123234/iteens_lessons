from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# http://127.0.0.1:5000/
menu_items = [
    {"name" : "Маргарита" , "description" : "Традиційна піца з томатним соусом і сиром" , "price" : 10.99} ,
    {"name" : "Пепероні" , "description" : "Піца з пепероні та сиром" , "price" : 12.99} ,
    ]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/menu')
def menu():
    return render_template('menu.html', menu_items=menu_items)


@app.route('/redirect_menu')
def redirect_menu():
    return redirect(url_for('menu'))


if __name__ == '__main__':
    app.run(debug=True)