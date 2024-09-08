num = int(input())

module = abs(num)
first = module // 100
second = (module // 10) % 10
third = module % 10


print(first,' \n',second,' \n',third, sep = '')
