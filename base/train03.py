import json
import re

import requests

import cmath


def read_file(name='train02.py', encoding='utf-8'):
    f = None
    try:
        f = open(name, 'r', encoding=encoding)
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    except Exception:
        print('Exception')
    finally:
        if f:
            f.close()


def copy(sourfile, targetfile):
    try:
        with open(sourfile, 'rb') as fs1:
            data = fs1.read()
        with open(targetfile, 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')


def write(filename='newfile.txt', mode='a', encoding='utf-8'):
    try:
        f = open(filename, mode, encoding=encoding)
        f.write('成功写文件\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        f.close()


def writeMulti():
    filenames = ('a-<100.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成!')


def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(cmath.sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def readjson():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')

def api_weather():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


def test20():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', sentence, flags=re.IGNORECASE)
    print(purified)

    username = input('请输入用户名: ')
    qq = input('请输入QQ号: ')
    # match函数的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('请输入有效的用户名.')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你输入的信息是有效的!')


if __name__ == '__main__':
    # read_file('致橡树.txt')
    # copy('致橡树.txt','copy之西欧昂书.txt')
    # write('haha.txt', 'a')
    # read_file('haha.txt')
    # copy('haha.txt', 'haha2.txt')
    # readjson()
    # api_weather()
    test20()
