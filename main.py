from flask import Flask, render_template, request, redirect, url_for, flash
from pyshorteners import Shortener

app = Flask('__main__')
app.secret_key = 'ssshhh'


@app.route('/', methods=['get', 'post'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        if len(url) < 5:
            flash('Введите корректный url!', category='message')
            return render_template('home.html')
        url = Shortener().clckru.short(url)
        return redirect(url_for('index', url=url))
    return render_template('home.html', url=request.args.get('url'))


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
