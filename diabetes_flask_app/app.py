from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    color = None

    if request.method == 'POST':
        sugar = float(request.form['sugar'])

        if sugar < 100:
            result = "Normal"
            color = "green"
        elif 100 <= sugar < 126:
            result = "Prediabetic"
            color = "orange"
        else:
            result = "Diabetic"
            color = "red"

    return render_template('index.html', result=result, color=color)

if __name__ == '__main__':
    app.run(debug=True)
