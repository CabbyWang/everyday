#coding:utf-8
import requests
from requests import RequestException
import re


def get_one_page(url):
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            html = response.text
            # print(html)
            return html
    except RequestException:
        return


def parse_one_page(html, index):
    print(1111)
    pattern = re.compile('bpic="(.*?)"', re.S)
    pattern2 = re.compile('data-video="(.*?)".*?data-vsrc="(.*?)"', re.S)
    items = re.findall(pattern, html)
    items2 = re.findall(pattern2, html)

    # download pictures
    # for i, item in enumerate(items):
    #     print(i, item)
    #     jpg_res = requests.get(item)
    #     jpg_data = jpg_res.content
    #     with open(r'd:/test/tt/{}_{}.jpg'.format(index, i), 'wb') as f:
    #         f.write(jpg_data)

    # download videos
    for i, item in enumerate(items2):
        print(i, item[0])
        video_res = requests.get(item[0])
        video_data = video_res.content
        with open(r'd:/test/tt/{}_{}.mp4'.format(index, i), 'wb') as f:
            f.write(video_data)


def main():
    for i in range(10):
        html = get_one_page('https://tieba.baidu.com/f?kw=萌妹纸&ie=utf-8&pn={}'.format(i*50))
        parse_one_page(html, i)


if __name__ == '__main__':
    main()
