from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html', name="Dill")

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    if num1.isnumeric() and num2.isnumeric():
        operation = request.form['operation']
    else:
        result = "Please enter a number"
        return render_template('app.html', result=result)
    if operation == 'add':
        result = float(num1) + float(num2)
        return render_template('app.html', result=result)
    elif operation == 'subtract':
        result = float(num1) - float(num2)
        return render_template('app.html', result=result)
    elif operation == 'multiply':
        result = float(num1) * float(num2)
        return render_template('app.html', result=result)
    elif operation == 'divide':
        result = float(num1) / float(num2)
        return render_template('app.html', result=result)
    else:
        return render_template('app.html')

