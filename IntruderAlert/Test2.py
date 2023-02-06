# t=0
#
# def findMin(a,b):
#     global t
#     minimum=a[0]+b[0]
#     m=0
#     for i in range(len(a)):
#         if a[i]+b[i]<minimum:
#             minimum=a[i]+b[i]
#             m=i
#     return m
#
# def kill(a,b,i):
#     global t
#     if len(a)>1:
#         if i == 0:
#             a[1] += b[0]
#         elif i == len(a) - 1:
#             a[-2] += b[-1]
#         else:
#             a[i - 1], a[i + 1] = a[i - 1] + b[i], a[i + 1] + b[i]
#         a.pop(i)
#         b.pop(i)
#     return a,b
#
# def time_calc(a,b):
#     global t
#     x=findMin(a,b)
#     t1=a[x]
#     if len(a)>1:
#         t+=t1
#         a, b = kill(a, b, x)
#         return time_calc(a,b)
#     else:
#         t+=a[0]
#         return None
#
# a=[2,6,7,3]
# b=[3,6,0,5]
# a=[10]
# b=[0]
# time_calc(a,b)
# print(a,b,t)
#
# import cv2
# import urllib.request
# import numpy as np
#
#
# def nothing(x):
#     pass
#
#
# # change the IP address below according to the
# # IP shown in the Serial monitor of Arduino code
# url = 'http://192.168.171.74:81/stream'
#
# while True:
#     img_resp = urllib.request.urlopen(url)
#     imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
#     frame = cv2.imdecode(imgnp, -1)
#     cv2.imshow("live transmission", frame)
#     key = cv2.waitKey(5)
#     if key == ord('q'):
#         break
#
# cv2.destroyAllWindows()

# import cv2
# from urllib.request import urlopen
# import numpy as np
#
# url = r'http://192.168.171.74'
# while True:
#     img_resp = urlopen(url)
#     imgnp = np.asarray(bytearray(img_resp.read()), dtype="uint8")
#     img = cv2.imdecode(imgnp, -1)
#     cv2.imshow("Camera", img)
#     if cv2.waitKey(1) == 113:
#         break

num = 100
for i in range(10):
    num-=2
print(num)

