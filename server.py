from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', type=str)
    return jsonify(a)

if __name__ == "__main__":
    app.run()
