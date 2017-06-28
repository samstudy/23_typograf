from flask import Flask, render_template, request, Response
from typograf import typograph

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/typograf', methods=['POST'])
def typograf():
    text = typograph(request.form['text'])
    return Response(json.dumps(text, indent=4),
                    content_type='application/json; charset=utf-8')
    

if __name__ == "__main__":
    app.run(debug=True)