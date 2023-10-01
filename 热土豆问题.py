from Queue import Queue
q=Queue()
namelist=input().split()
for i in namelist:
    q.enqueue(i)
time=int(input('请输入一次想传递的次数：'))
while q.size()>1:
    for i in range(time):
        q.enqueue(q.dequeue())
    q.dequeue()
print(f'幸存者：{q.dequeue()}')