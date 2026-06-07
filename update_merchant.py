import json

import requests
import traceback
import notify

admin_bark = 'https://api.day.app/jgNgRjp5e2oKqrtWa8Ev3g'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36'
}

with open('public/json/merchant-current.json', 'r', encoding='utf-8') as f:
    old_current = json.load(f)

current = {}

requests.get(f'{admin_bark}/远行商人/我被执行了')

try:
    r = requests.get('https://www.taptap.cn/ug-apis/roco/v1/merchant/current', headers=headers)
    print(r.text)
    current = r.json()
except Exception as e:
    print(f'current err: {e}')
    traceback.print_exc()
    requests.get(f'{admin_bark}/远行商人/更新当前商品出错:{e}')
    raise e

with open('public/json/merchant-history.json', 'r', encoding='utf-8') as f:
    old_history = json.load(f)

history = {}

try:
    r = requests.get('https://www.taptap.cn/ug-apis/roco/v1/merchant/history', headers=headers)
    print(r.text)
    history = r.json()
except Exception as e:
    print(f'history err: {e}')
    traceback.print_exc()
    requests.get(f'{admin_bark}/远行商人/更新历史商品出错:{e}')

    raise e

try:
    if current['round']['round_id'] != old_current['round']['round_id']:
        print('班次已经改变')
        with open('public/json/merchant-current.json', 'w', encoding='utf-8') as current_json_f:
            json.dump(current, current_json_f)
        with open('public/json/merchant-history.json', 'w', encoding='utf-8') as history_json_f:
            json.dump(history, history_json_f)
        notify.notify()
except Exception as e:
    requests.get(f'{admin_bark}/远行商人/更新商品出错:{e}')
    raise e
