#讀取檔案

products = []

with open('product_list.csv', 'r', encoding = 'utf-8') as f:
    for line in f:
        if '商品,價格' in line: # 如果商品、價格出現在讀取的字串內
            continue # 忽略這一次、跳到下一回再開始
        name, price = line.strip().split(',') #strip()清楚\n , line.spilt 遇到逗點就切割
        products.append([name, price])
print(products)

# 使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
    	break
    price = input('請輸入商品價格: ')
    #p = []
    #p.append(name)
    #p.append(price)
    #products.append(p)
    #p =[name, price]
    products.append([name, price])

#print('目前商品有: ', products[0][0], products[0][1])
#print('目前商品有: ', products[1][0], products[1][1])
#print('目前商品有: ', products)

#印出購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open ('product_list.csv', 'w', encoding = 'utf-8') as f: # with 裡面檔案開啟
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1]+ '\n') # 這個要寫在with裡面