from flask import Blueprint, render_template, request
import math

calculator = Blueprint('calculator', __name__)

@calculator.route('/', methods=['GET', 'POST'])
def calculator_page():
    result = None
    error = None  # Initialize error

    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operator = request.form['operator']

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '^':
                result = num1 ** num2
            elif operator == '%':
                result = num1 % num2
            elif operator == '//':
                result = num1 // num2
            elif operator == 'sqrt':
                if num1 >= 0:
                    result = num1 ** 0.5
                else:
                    error = "Square root of negative number is not allowed"
            elif operator == 'log':
                if num1 > 0:
                    result = math.log(num1, num2)
                else:
                    error = "Logarithm of non-positive number is not allowed"
            elif operator == 'exp':
                result = math.exp(num1)
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    error = "Division by zero is not allowed"
            else:
                error = "Invalid operator"
        except ValueError:
            error = "Please enter valid numbers"

        return render_template('index.html', result=result, error=error)

    return render_template('index.html', result=result, error=error)
