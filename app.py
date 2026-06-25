from flask import Flask, render_template
app = Flask(__name__)#이 파일 위치로 templates, static 파일의 위치를 찾겠다
@app.route("/") #데코레이터 기본 주소"/"로 접속 시 다음과 같은 함수 실행
def index() :
    return render_template("index.html")
if __name__ == "__main__" :
    app.run(debug=True)
    #TODO "수정테스트입니다."
