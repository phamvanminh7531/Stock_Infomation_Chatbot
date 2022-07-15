import difflib
from datetime import datetime

def reply_fl(reply, quet, hit):
    list_flu = {
        'check_times': check_times,
        'check_market': check_market,
        'name_me': name_me,
        'name': name,
    }
    return list_flu[reply](quet, hit)


def reply_hit(quet, hit):
    list_flu = {
        'name_sen': name_sen,
    }
    return list_flu[hit['hit_flu']](quet, hit)


def name(quet, hit):
    hit = hit
    if 'name_me' not in hit.keys():
        return name_me(quet, hit)
    reply = 'tên bạn là '+hit['name_me']
    return [reply, hit]


def name_me(quet, hit):
    hit = hit
    reply = 'tên bạn là gì'
    hit['hit_flu'] = 'name_sen'
    return [reply, hit]


def name_sen(quet, hit):
    quet = quet.lower()
    quet_list=[
        "không nhớ nữa",
        "không sữa nữa",
        "dùng tên củ",
        "xài tên củ",
        "không nói",
        "thoát",
    ]
    reply = ''
    op = True
    for x in quet_list:
        if difflib.SequenceMatcher(None, quet, x).ratio() > 0.7:
            reply = "vân! không hỏi nữa"
            op = False
    quet_ot = [
        "là tên đầy đủ của tôi",
        "tên đầy đủ của tôi là",
        "chính là tên tôi",
        "tên của tôi là",
        "là tên của tôi",
        "tên đầy đủ là",
        "là tên đầy đủ",
        "tên tôi là",
        "là tên tôi",
        "tôi tên là",
        "là tên",
        "tôi là",
        "tên là",
        "tôi là",
    ]
    for x in quet_ot:
        quet = quet.replace(x, '')

    quet = quet.title()
    if op:
        reply = 'đã nhớ. <br> tên bạn là '+quet+'.'
        hit['name_me'] = quet
    del hit['hit_flu']
    return [reply, hit]


def check_times(quet, hit):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S <br> %d/%m/%Y ")
    return [current_time, hit]


def check_market(quet, hit):
    now = datetime.now()
    h = int(now.strftime("%H"))
    w = int(now.strftime("%w"))
    if 8 < h < 16 and 1 >= w >= 5:
        return ["thị trường đang mở. <br> thị trường sẻ mở vào 8h-16h từ thứ hai đến chủ nhật", hit]
    if h < 8 or h > 16:
        return ["thị trường đang đóng. <br> thị trường sẻ mở vào 8h-16h từ thứ hai đến chủ nhật", hit]
    if 8 < h < 16 and (w < 1 or w > 5) :
        return ["thị trường đang đóng. <br> thị trường sẻ mở vào 8h-16h từ thứ hai đến chủ nhật", hit]
