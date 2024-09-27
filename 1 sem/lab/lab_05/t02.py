num = int(input())

count = 0
if num == 1:
    for i in range(10, 100):
        ody = i % 10
        des = i // 10
        if des > ody:
            count += 1
# for des in range(1, 10):
#     for ody in range(0, 10):
#         if des < ody:
#             counter += 1
#
# print(counter)
elif num == 2:
    for i in range(10, 100):
        ody = i % 10
        des = i // 10
        if des < ody:
            count += 1
print(count)






