n, k = (map(int, input().split()))
a = list(map(int, input().split()))
tmp_lst = []
for i, j in enumerate(a):
    if not j % 2:
        tmp_lst.append(i)

count_max = 1
for i in range(len(tmp_lst)):
    tmp_count = 1
    tmp_k = k
    flag = True
    for j in range(i + 1, len(tmp_lst)):
        if tmp_lst[j - 1] + 1 == tmp_lst[j]:
            if flag:
                tmp_count += 1
                if count_max < tmp_count:
                    count_max = tmp_count
            else:
                flag = True
                continue
        elif (j+1)<len(tmp_lst):
            if tmp_lst[j - 1] + 2 == tmp_lst[j]:
                tmp_count += 1
                tmp_k-=1
                flag = False
                if count_max < tmp_count:
                    count_max = tmp_count
        else:
            break
res = (count_max + (len(tmp_lst) - count_max)) if k >= (len(tmp_lst) - count_max) else (count_max + k)
print(res)
