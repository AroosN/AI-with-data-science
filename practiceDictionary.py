BookDic = {"title" : 'Aroos\'s dictionary', 'author' : 'hania amir', 'number of pages' : 200, 'price' : 200.5}
print(BookDic)
print(type(BookDic))

for x in BookDic:
    print(x)

for x in BookDic:
    print(BookDic[x])
for x in BookDic:
    print(BookDic['title'])

BookDic['city'] = 'LA'
BookDic['isOnSale'] = True
print(BookDic)

BookDic['city'] = 'NY'
print(BookDic)

BookDic.pop('city')
print(BookDic)

BookDic.clear()
print(BookDic)