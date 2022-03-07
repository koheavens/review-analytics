data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f :
        data.append(line)
        count += 1
        if count % 100000 == 0 :
            print(len(data))
print('總共',len(data),'資料')

#計算平均留言長度
sum_len =0 
for line in data:
    length = len(line)
    sum_len += length
print('留言平均長度',sum_len / len(data))

#留言過濾<100筆
new = []
for d in data :
    if len(d) < 100:
        new.append(d)
print('留言長度小於100有',len(new))
print(new[0])


#留言過濾有 'good'
new2 = []
for d in data :
    if 'good' in d :
        new2.append(d)
print('包含good資料共',len(new2))
print(new2[0])