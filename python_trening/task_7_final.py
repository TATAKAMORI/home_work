#def task1(a):
#    a.append(28)
#    return a
#
#print (task1([1, 2, 3]))
#
#
#def task2(a = [1, 2, 3]):
#    sum = a[0] + a[1] + a[2]
#    return sum
#
#print(task2())

def task3(a: list) -> int:
    result = 0
    for elem in a:
        result = result + elem
    return result

print(task3([1, 5, 9]))