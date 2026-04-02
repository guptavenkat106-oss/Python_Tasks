def number_genrator(n):
    for i in range(1, n + 1):
        yield i

n = 5
gen = number_genrator(n)

for num in gen:
    print(num)
