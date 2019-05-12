
import pymongo
import charts

client = pymongo.MongoClient('192.168.99.100',32784)
ceshi = client['copy']
item_info = ceshi['item_info']


re_list = []


def gen_data(pre, after, re_list):
    calc = 0
    for i in item_info.find():
        if '����' not in i['price']:
            if '��' not in i['price']:
                if int(i['price']) > pre and int(i['price']) < after:
                    calc += 1
    sub_list = [str(pre) + '-' + str(after), calc]
    re_list.append(sub_list)


key_list = [[0, 100], [100, 500], [500, 1000], [1000, 1500], [1500, 2000], [2000, 2500], [2500, 3000], [3000, 3500],
            [3500, 4000], [4000, 4500], [4500, 5000]]


def final_data(key_list, re_list):
    calc = 0
    for key in key_list:
        gen_data(key[0], key[1], re_list)
        gen_data(5000, 10000, re_list)
    for i in item_info.find():
        if '��' in i['price']:
            calc += 1
    re_list.append(['��Ԫ����', calc])
    calc = 0
    for i in item_info.find():
        if '����' in i['price']:
            calc += 1
    re_list.append(['����', calc])


final_data(key_list, re_list)
print(re_list)

options = {
    'charts': {'zoomType': 'xy'},
    'title': {'text': '58����������Ʒ�۸�Ա�'},
    'subtitle': {'text': '���Է�ƽ�˾�������'}
}
series = [{
    'type': 'pie',
    'name': 'Browser share',
    'data': [data for data in re_list],
}]
charts.plot(series, show='inline', options=options)
