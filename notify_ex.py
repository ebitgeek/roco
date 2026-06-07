import json
import requests
import traceback

admin_bark = 'https://api.day.app/jgNgRjp5e2oKqrtWa8Ev3g'

barks = [
    'https://api.day.app/jgNgRjp5e2oKqrtWa8Ev3g'
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36'
}
try:
    r = requests.get('https://www.taptap.cn/ug-apis/roco/v1/merchant/current', headers=headers)
    print(r.text)
    current = r.json()
except Exception as e:
    print(f'current err: {e}')
    traceback.print_exc()
    requests.get(f'{admin_bark}/远行商人/更新当前商品出错:{e}')
    raise e

print(current)

try:
    goods = []
    for item in current['round']['items']:
        goods.append(item['name'])
except Exception as e:
    requests.get(f'{admin_bark}/远行商人/发送通知出错：{e}')
    traceback.print_exc()
    raise e

trigger = False
trigger_keys = ['棱镜', '祝福']
for g in goods:
    for t in trigger_keys:
        if t in g:
            trigger = True

if trigger:
    for bark in barks:
        for bark in barks:
            requests.get(f'{bark}/远行商人 - {current["round"]["date"]} {current["round"]["slot"]}/{" ".join(goods)}?level=critical&volume=5&call=1')