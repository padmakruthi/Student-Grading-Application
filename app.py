from flask import Flask, render_template, request
from sklearn.svm import SVC

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('grade.html')

@app.route('/predict', methods=['POST'])
def predict():
    num1 = int(request.form.get("num1"))
    num2 = int(request.form.get("num2"))
    inputs = [[33], [36], [70], [80], [100]]
    outputs = ['fail', 'just pass', 'first class', 'good', 'distinction']
    model = SVC()
    model.fit(inputs, outputs)
    result1 = model.predict([[num1]])[0]
    result2 = model.predict([[num2]])[0]
    return render_template('result.html', res1=result1, res2=result2)

if __name__ == "__main__":
    app.run(debug=True)