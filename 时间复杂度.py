#变位词判断
#逐个比较法：时间复杂度为o(n^2)

#排序比较↓  
list1=list(input())
list2=list(input())
list1.sort()
list2.sort()
if list1==list2:
    print('Yes')
