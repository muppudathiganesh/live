from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/poll', methods=['GET', 'POST'])
def poll():
    if request.method == 'POST':
        choice = request.form.get('choice')
        return redirect(url_for('summary', choice=choice))
    return render_template('poll.html')

@app.route('/summary')
def summary():
    choice = request.args.get('choice')
    return render_template('summary.html', choice=choice)

if __name__ == '__main__':
    app.run(debug=True)
