# config:utf-8

from bottle import run, get, post, template, request

def checkLogin(username, password):
    """
    ログイン判定を行う。
    今回はダミー関数として、パスワードがdenzowならログインOKとする
    実際はユーザデータと照合等をする
    """
    if password == "denzow":
        return True
    else:
        return False

@get("/login")
def login():
    """
    GETで/loginにアクセスした際の処理
    """
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post("/login")
def doLogin():
    """
    POSTで/loginにアクセスした際の処理
    """
    # フォームからPOSTされたデータを取得する
    username = request.forms.get('username')
    password = request.forms.get('password')

    # ログイン判定を行う
    if checkLogin(username, password):
        return template("<p>Your login information was correct. welcome {{username}}</p>", username=username)
    else:
        return "<p>Login failed.</p>"

if __name__ == "__main__":
    # テスト用のサーバをlocalhost:8080で起動する
    # reloader=Trueにより、ソースを書き換えると自動的に再起動される
    run(host='localhost', port=8080, reloader=True)
