import math
from sympy import *

def get_plane(center,point2,point3):
    
    a = (point2[1] - center[1]) * (point3[2] - center[2]) - (point2[2] - center[2]) * (point3[1] - center[1])
    b = (point2[2] - center[2]) * (point3[0] - center[0]) - (point2[0] - center[0]) * (point3[2] - center[2])
    c = (point2[0] - center[0]) * (point3[1] - center[1]) - (point2[1] - center[1]) * (point3[0] - center[0])
    d = (0-(a*center[0]+b*center[1]+c*center[2]))
    e = [a,b,c,d]
    return e

def projection_point(center2):
    t = Symbol('t')
    e = get_plane(center,point2,point3)
    x = center2[0]+ projection_vector1[0]*t
    y = center2[1]+projection_vector1[1]*t
    z = center2[2]+projection_vector1[2]*t
    total = e[0]*x+e[1]*y+e[2]*z+e[3]
    sol = solve(total,t)
    a = ('%.6f' % (float(center2[0] + projection_vector1[0]*sol[0])))
    b = ('%.6f' % (float(center2[1]+ projection_vector1[1]*sol[0])))
    c = ('%.6f' % (float(center2[2]+projection_vector1[2] * sol[0])))
    answer = [a,b,c]
    return answer

def calculate_angle(center_vector1,center_vector2):
    dot_product=0
    center_vector_long1 = 0
    center_vector_long2 = 0
    cos = 0
    angle = 0
    for i in range(0,3) :
        dot_product += (center_vector1[i] * center_vector2[i])
        center_vector_long1 += math.pow(center_vector1[i],2)	
        center_vector_long2 += math.pow(center_vector2[i],2)	 
    center_vector_long1 = math.sqrt(center_vector_long1)
    center_vector_long2 = math.sqrt(center_vector_long2)
    cos = dot_product / (center_vector_long1 * center_vector_long2)
    angle = math.acos(cos)
    answer = angle * 180 / math.pi # return 角度
    return answer


'''

def projection_angle(center_vector1,projection_vector1,projection_vector2):
    a = 90 - calculate_angle(center_vector1,projection_vector1) #這是domin中心與point2,point3平面的夾角
    a = a / 180 * math.pi  #角度轉換成徑度
    #把立體的向量，壓到平面上，所以center加上向量就可以是平面上的點
    projection_plane_vector1 = center_vector1.copy() #淺複製
    projection_plane_vector1[2] =  projection_plane_vector1[2] - math.sqrt(projection_plane_vector1[0]**2 +\
       projection_plane_vector1[1]**2 + projection_plane_vector1[2]**2) * math.sin(a)
    answer = ('%0.6f' % float(calculate_angle(projection_plane_vector1,projection_vector2))) #domin2在平面上的投影角度
    return answer

def projection_point_wrong(center,projection_vector1,center_vector1): #改變的參數是center_vector1，因為 projection_vector1是center與point1的向量 ，算與投影平面的角度
    a = 90 - calculate_angle(center_vector1,projection_vector1) #這是domin中心與point2,point3平面的夾角 或是空間中的點與point2&point3平面的夾角
    a = a / 180 * math.pi                                       #角度轉換成徑度                        
    #把立體的向量，壓到平面上，所以center加上向量就可以是平面上的點
    projection_plane_vector1 = center_vector1.copy() #淺複製
    projection_plane_vector1[2] = projection_plane_vector1[2] - math.sqrt(projection_plane_vector1[0]**2 +\
       projection_plane_vector1[1]**2 + projection_plane_vector1[2]**2) * math.sin(a)
    projection_point = center + projection_plane_vector1
    #b = 90 - calculate_angle(projection_vector3,projection_vector1)#這是domin2的趨勢向量頂點與point2,point3平面的夾角
    #b = b / 180 * math.pi
    #projection_plane_vector2 = projection_vector3.copy()
    #projection_plane_vector2[2] = projection_plane_vector2[2] - math.sqrt(projection_plane_vector2[0]**2 +\
       # projection_plane_vector2[1]**2 + projection_plane_vector2[2]**2) * math.sin(b) 
   # projection_point2 = center + projection_plane_vector2
    return projection_point

def projection_plane_vector_wrong(center,projection_vector1,center_vector1,projection_vector3): 
    #能更改的只有後面兩個參數，而且兩個參數是連動的，用哪個domin就要用哪個向量，第一個參數是center，第二個參數，是為了算出與point1的夾角，藉此投影
    #寫投影在平面上的點，形成的向量，參數的前兩個不動，後兩個會換
    a = projection_point(center,center_vector1,projection_vector1)
    b = projection_point(center,projection_vector3,projection_vector1)
    c = list(b-a)
    return c
'''
