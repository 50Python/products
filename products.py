
products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
    	break
    price = input('請輸入商品價格: ')
    #p = []
    #p.append(name)
    #p.append(price)
    #products.append(p)
    #p =[name, proce]
    products.append([name, price])

print('目前商品有: ', products[0][0], products[0][1])
print('目前商品有: ', products[1][0], products[1][1])
print('目前商品有: ', products)

for p in products:
	print(p[0], '的價格是', p[1])

