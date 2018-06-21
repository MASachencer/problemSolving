from .queue_ import Queue_


def hot_potato(namelist, num):
    q = Queue_()
    for name in namelist:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()


print(hot_potato(['1', '2', '3', '4', '5', '6'], 7))
