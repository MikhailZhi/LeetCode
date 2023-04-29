# accounts: List[List[int]]
# m == accounts.length
# n == accounts[i].length



# version 1
accounts = [[1,2,3],[3,2,1]]
all = []
for banks in accounts:
    summ = 0
    for money in banks:
        summ += money
    all.append(summ)
print(max(all))


# version 2
accounts = [[1,5],[7,3],[3,5]]
all = []
for banks in accounts:
    summ = 0
    for money in banks:
        summ += money
    all.append(summ)
print(max(all))

# version 3
accounts = [[2,8,7],[7,1,3],[1,9,5]]
all = []
for banks in accounts:
    summ = 0
    for money in banks:
        summ += money
    all.append(summ)
print(max(all))
