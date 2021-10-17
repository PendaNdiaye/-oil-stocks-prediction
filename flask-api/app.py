from flask import Flask, jsonify, make_response, request

import os 


from model.model import predict
from bot.bot import HeadersData



app = Flask(__name__)


@app.route('/score', methods=['POST'])
def score():
    features = request.json['pages']
    pagination_low, pagination_up = features
    headers_data = HeadersData()
    daily_news = headers_data.current_scraper()
    past_news = headers_data.back_scraper(pagination_low, pagination_up)
    news = daily_news + past_news
    preds = predict(news)
    return make_response(jsonify({'score': preds.tolist()}))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)


