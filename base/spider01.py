import re
import ssl
from urllib.error import URLError
from urllib.request import urlopen

import pymysql
from pymysql import Error


# 通过指定的字符集对页面进行解码(不是每个网站都将字符集设置为utf-8)
def decode_page(page_bytes, charsets=('utf-8',)):
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
            # logging.error('Decode:', error)
    return page_html


# 获取页面的HTML代码(通过递归实现指定次数的重试操作)
def get_page_html(seed_url, *, retry_times=3, charsets='utf-8'):
    page_html = None
    try:
        page_html = decode_page(urlopen(seed_url).read(), charsets)
    except URLError as err:
        print('url err : ', err)
        if retry_times > 0:
            return get_page_html(seed_url, retry_times=retry_times - 1,charsets=charsets)
    return page_html


# 从页面中提取需要的部分(通常是链接也可以通过正则表达式进行指定)
def get_matched_parts(page_html, pattern_str, pattern_ignore_case=re.I):
    pattern_regex = re.compile(pattern_str, pattern_ignore_case)
    return pattern_regex.findall(page_html) if page_html else []


# 开始执行爬虫程序并对指定的数据进行持久化操作
def start_crawl(seed_url, match_pattern,detail_page_reg, *, max_depth=-1 ):
    conn = pymysql.connect(host='192.168.99.100', port=3306,
                           database='school', charset='utf8',
                           user='root', password='root', autocommit=True)
    print(conn)
    try:
        with conn.cursor() as cursor:
            url_list = [seed_url]
            # 通过下面的字典避免重复抓取并控制抓取深度
            visited_url_list = {seed_url: 0}
            while url_list:
                print(url_list)
                current_url = url_list.pop(0)
                depth = visited_url_list[current_url]
                if depth != max_depth:
                    # 尝试用utf-8/gbk/gb2312三种字符集进行页面解码
                    page_html = get_page_html(current_url, charsets=('utf-8', 'gbk', 'gb2312'))
                    links_list = get_matched_parts(page_html, match_pattern)
                    param_list = []
                    for link in links_list:
                        if link not in visited_url_list:
                            visited_url_list[link] = depth + 1
                            page_html = get_page_html(link, charsets=('utf-8', 'gbk', 'gb2312'))
                            headings = get_matched_parts(page_html, detail_page_reg)
                            if headings:
                                print(page_html,headings[0], link)
                                param_list.append((headings[0], link))
                    cursor.executemany('insert into tb_website_link values (%s, %s)', param_list)
                    conn.commit()
    except Error as err:
        pass
        print("sql error : ", err)
        # logging.error('SQL:', error)
    finally:
        conn.close()


def main(regparam):
    ssl._create_default_https_context = ssl._create_unverified_context
    start_crawl('http://sports.sohu.com/nba_a.shtml', regparam, regparam , max_depth=2 )


if __name__ == '__main__':
    reg1 = r'<a (.*)href="(.*)"(.*?)>(.*?)</a>'
    reg2=r'<title>.*</title>'
    reg3=r'href=".*?"'
    main(reg3)
