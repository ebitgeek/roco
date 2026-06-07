import json
import requests
import traceback

admin_bark = 'https://api.day.app/jgNgRjp5e2oKqrtWa8Ev3g'

barks = [
    'https://api.day.app/jgNgRjp5e2oKqrtWa8Ev3g'
]


def notify():
    with open('public/json/merchant-current.json', 'r', encoding='utf-8') as f:
        current = json.load(f)

    print(current)

    try:
        goods = []
        for item in current['round']['items']:
            goods.append(item['name'])

        for bark in barks:
            requests.get(f'{bark}/远行商人 - {current["round"]["date"]} {current["round"]["slot"]}/{" ".join(goods)}')
    except Exception as e:
        requests.get(f'{admin_bark}/远行商人/发送通知出错：{e}')
        traceback.print_exc()
        raise e