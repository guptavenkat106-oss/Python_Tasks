def even_generator():
    num = 2
    while True:
        yield num
        num += 2


N = int(input("Enter how many even numbers you want: "))

gen = even_generator()

for i in range(N):
    print(next(gen), end=" ")
