from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

# HOME PAGE
@app.route('/')
def home():
    return render_template('home.html', tasks=tasks)

# ADD TASK
@app.route('/add', methods=['POST'])
def add_task():

    task = request.form.get('task')

    if task:
        tasks.append(task)

    return redirect('/')

# UPDATE PAGE
@app.route('/update/<int:index>', methods=['GET', 'POST'])
def update(index):

    if request.method == 'POST':

        updated_task = request.form.get('task')

        tasks[index] = updated_task

        return redirect('/')

    return render_template('update.html',
                           task=tasks[index],
                           index=index)

# DELETE PAGE
@app.route('/delete/<int:index>')
def delete(index):

    deleted_task = tasks[index]

    tasks.pop(index)

    return render_template('delete.html',
                           task=deleted_task)

if __name__ == '__main__':
    app.run(debug=True)