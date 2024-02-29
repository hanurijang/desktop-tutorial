from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    try:
        user_input = int(request.form.get('user_input'))  # 'user_input'라는 이름의 폼 입력 필드를 가정합니다.
        if 1 <= user_input <= 9:
            result = "Hello, World! " * user_input
        else:
            result = "1부터 9 사이의 숫자를 입력하세요."
    except ValueError:
        result = "유효하지 않은 입력입니다. 올바른 숫자를 입력하세요."
def another_function():
    # Your code here
    return "Another response"

    return render_template('return.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
