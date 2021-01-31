from bottle import route, run, template

"""
# サンプル１
# /helloパスをhello()関数（コールバック関数）にリンク
@route("/hello")
def hello():
    return "Hello World!"

run(host="localhost", port=8080, debug=True)
"""


"""
# サンプル２
1つのコールバックに複数のルートをバインドすることができること
URLにワイルドカードを追加してキーワード引数を介してアクセスすることができる

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

run(host="localhost", port=8080, debug=True)
# vaioは固定IPとしたので、外部のクライアントから問い合わせる場合はこちらでrunする
#run(host="192.168.10.201", port=8080, debug=True)
"""

"""
# サンプル３
静的ルーティング
"""
@route('/hello')
def hello():
    return template("view/index.tpl")

run(host="localhost", port=8080, debug=True)

