from sympy import *

def get_plane(center,point2,point3):
    '''透過三個點，得到立體空間平面方程式'''
    a = (point2[1] - center[1]) * (point3[2] - center[2]) - (point2[2] - center[2]) * (point3[1] - center[1])
    b = (point2[2] - center[2]) * (point3[0] - center[0]) - (point2[0] - center[0]) * (point3[2] - center[2])
    c = (point2[0] - center[0]) * (point3[1] - center[1]) - (point2[1] - center[1]) * (point3[0] - center[0])
    d = (0-(a*center[0]+b*center[1]+c*center[2]))
    answer = [a,b,c,d]
    return answer

def projection_point(center2,center,point2,point3,projection_vector1):
    '''用參數式的方式去計算立體空間上之點對平面產生的投影點
       要傳遞的參數，是要背投影的點
    '''
    t = Symbol('t')
    e = get_plane(center,point2,point3)
    x = center2[0]+ projection_vector1[0]*t
    y = center2[1]+projection_vector1[1]*t
    z = center2[2]+projection_vector1[2]*t
    total = e[0] * x + e[1] * y + e[2] * z + e[3] #參數是帶回原來的立體空間的平面方程式
    sol = solve(total,t)
    a = center2[0] + projection_vector1[0] * sol[0]
    b = center2[1] + projection_vector1[1] * sol[0]
    c = center2[2] + projection_vector1[2] * sol[0]
    answer = [a,b,c]
    return answer
