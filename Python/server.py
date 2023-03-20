from flask import Flask, request, render_template, redirect
import datetime

app = Flask(__name__)

class Item():
    def __init__(self, name, description, completion_status):
        self.name = name
        self.description = description
        self.completion_status = completion_status

to_do_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    current_year = datetime.datetime.now().year

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        completion_status = False

        item = Item(name, description, completion_status)
        to_do_list.append(item)

    return render_template('index.html', to_do_list=to_do_list, year=current_year)

@app.route('/complete/<int:item_index>')
def complete(item_index):
    to_do_list[item_index].completion_status = True
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
