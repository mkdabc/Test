from copy import deepcopy

# L =[]
# def test(n):
#     if (n/2)<5000:
#         L.append(n)
#         return test(n*2)
#     else:
#         a = deepcopy(L)
#         a.reverse()
#         L.extend(a)
#         print(L)
# test(20)



# def move(n,a,b,c):
#     if n==1:
#         print(a,'-->',c)
#     else:
#         move(n-1,a,c,b)   #将前n-1个盘子从a移动到b上
#         move(1,a,b,c)     #将最底下的最后一个盘子从a移动到c上
#         move(n-1,b,a,c)   #将b上的n-1个盘子移动到c上
#
# move(3,'A','B','C')

# l = [1,1,2,2,3,4,5,8,6,5]
# # print(set(l))
# li = []
# for i in l:
#     if i not in li:
#         li.append(i)
# print(li)

# class A:
#     list_display = [1, 2, 3]
#     def __init__(self):
#         self.list_display = []
#     def get_list(self):
#         self.list_display.insert(0, 33)
#         return self.list_display
#
# s1 = A()
# print(s1.get_list())

# 如何用一行代码生成[1,4,9,16,25,36,49,64,81,100]
# l = [i*i for i in range(1,11)]
# print(l)

# 用Python实现一个二分查找的函数

# def search(list,num):
#     left = 0
#     right = len(list)-1
#     while left<right:
#         mid = (left+right)//2
#         if mid>num:
#             right = mid-1
#         elif mid<num:
#             left = mid+1
#         else:
#             print(mid)
#             return mid
#     return None
#
# li = [1,2,3,4,5,6,7,8,9,0]
# search(li,2)
#
# for x in range(1,10):
#     for y in range(1,x+1):
#         print(('%s*%s=%s')%(y,x,x*y),end='\t')
#     print('\n')

# a = '1,2,3'
# b = a.split(',')
# print(b)
