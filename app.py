from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.youtubeEng


@app.route('/')
def home():
    return render_template('web.html')


## API역할을 하는 부분
### DB에 데이터 가져오기
@app.route('/videoList', methods=['GET'])
def get_videos():
    videos = list(db.youtube.find({}))
    # # 1. 클라이언트로부터 데이터를 받기
    # article_url = request.form['article_give']
    # comment = request.form['comment_give']
    # # 2. meta tag를 스크래핑하기
    # meta = get_meta_data(article_url)
    # # 3. mongoDB에 데이터 넣기
    # db.alonememo.insert_one({
    #     'url': article_url,
    #     'title': meta['title'],
    #     'image_url': meta['image_url'],
    #     'description': meta['description'],
    #     'comment': comment
    # })
    return jsonify({'result': 'success', 'all_video': videos})
    # ex.서버와 정상연결 확인
    # return jsonify({'result': 'success', 'msg': '성공'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
