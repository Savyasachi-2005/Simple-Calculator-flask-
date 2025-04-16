from flask import Flask
from calci import calculator  # Import your blueprint

app = Flask(__name__)

# Register your blueprint
app.register_blueprint(calculator)

if __name__ == '__main__':
    app.run(debug=True)
