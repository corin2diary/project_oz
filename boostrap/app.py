from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 사용자 데이터를 저장할 임시 리스트
user_data = []

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/login' ,methods=['GET'])
def login_page():
    return render_template('boostrap_admin2.html')

@app.route('/main')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # 폼에서 데이터를 추출
        print("Login Request")
        username = request.form['id']
        password = request.form['password']
        print(username, password)
        # 사용자 데이터와 일치하는지 확인
        for user in user_data:
            if user['username'] == username and user['password'] == password:
                print("Login Successful")
                return redirect(url_for('index'))  # 로그인 성공 시 홈페이지로 리다이렉션

        # 일치하는 데이터가 없는 경우
        print("Login Failed")
        return "Login Failed"  # 로그인 실패 메시지 표시

@app.route('/register', methods=['POST'])
def submit():
    if request.method == 'POST':
        # 폼에서 데이터를 추출
        name = request.form['name']
        username = request.form['id']
        password = request.form['password']

        # 추출된 데이터를 리스트에 저장
        user_data.append({'name': name, 'username': username, 'password': password})

        # 저장된 데이터 확인을 위한 콘솔 출력
        print(f"Registered Users: {user_data}")

        # 홈 페이지로 리다이렉션
        return render_template('boostrap_admin2.html')

if __name__ == '__main__':
    app.run(debug=True)