***


````python
import requests
response = requests.get()
response.text                  # 可以获取响应的内容(如抓来的网页)
response.encoding = 'utf-8'    # 改变编码为utf-8
response.content               # 获取二进制内容(如抓取登陆时的验证码等非字符资源)
response.cookies               # 可以查看当前保存的cookie情况
response.status_code           # 可以查看HTTP状态码
response.url                   # 可以查看当前请求的网址
````