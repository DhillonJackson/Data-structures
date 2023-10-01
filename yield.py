def fun_yield():
    print("starting fun yield")
    while True:
        res = yield 4
        print("判断yield之后是否继续执行",res)

g = fun_yield() # 调用这个函数只是会得到一个生成器
print("函数结果是一个生成器：",g)

print("对此生成器还是进行调用：")
print("第一次调用")
print("生成器的返回值",next(g))
print("第二次调用")
print("生成器的返回值",next(g))
print("第三次调用")
print("生成器的返回值",next(g))
