data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f :
        data.append(line)
        count += 1
        if count % 100000 == 0 :
            print(len(data))
print('總共',len(data),'資料')

sum_len =0 
for line in data:
    length = len(line)
    sum_len += length
print('留言平均長度',sum_len / len(data))

