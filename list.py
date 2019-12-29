# # list=[ '','I', 'xffhc', 'efy']
# # list1=['1', '2']
# # list.extend(list1)
# # list.clear()
#
# # if ('rohan' and 'anjali'and 'kaku' or 'kajal'or 'bharti') in list:
# # print (len(list ))
# # print ("yes it is there")
# # print(list)
#
# # else:
# #   print ("not in list")
#
# # p=['bmw' , 'audi' , 'rr' , 'xzy']
#
# # for x in p:
# # print (len(p))
# x=int(input())
# y=int(input())
# z=int(input())
# n=int(input())
# ar=[]
# p=0
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if(i+j+k) != n:
#                 ar.append([])
#                 ar[p] = [i, j, k]
#                 p += 1
#         print(ar)
# #ar=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k) != n )  ]
# #print (ar)
# #[0,1,2,3,4]
# #'''
# #'''
# """x = []
# for i in range(5):
#     x.append(input("enter number " + str(i + 1) + " "))
#     # x.append(input("enter number "+i+" "))
# x.sort()
# print(x)
# ''' '''
# for i in range(x):
#     temp = x[i]
# temp
# '''
# '''
# res="nil"
#
# for j in range((len(x)-2), 0,-1):
#
#     print("")
#     if x[len(x) - 1] > x[j]:
#         res = x[j]
#         break
#
# p
'''if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(len(arr)-1,-1,-1):
        if arr[len(arr)-1] != arr[i]:
            print(arr[i])
            break'''
#