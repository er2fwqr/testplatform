
import requests
json={'NAME':'疯驴子','TEL':13333333333,'ID':444444444444444444,'product_id':85}
res=requests.post(url='https://1934054mxunji.sjdzp.cn/Miniwx/Index/orders.json',json=json)
print(res.json())