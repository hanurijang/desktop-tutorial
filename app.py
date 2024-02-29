from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    try:
        user_input = int(request.form.get('user_input'))  # Assuming a form input field with name 'user_input'
        if 1 <= user_input <= 9:
            result = "Hello, World! " * user_input
        else:
            result = "Please enter a number between 1 and 9."
    except ValueError:
        result = "Invalid input. Please enter a valid number."

    return render_template('return.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
