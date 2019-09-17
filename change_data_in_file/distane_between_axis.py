import math
import numpy as np

def calculate_angle(center_vector1,center_vector2):
    '''回傳值是角度'''
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
    answer = angle * 180 / math.pi #徑度換成角度
    return answer

def calculate_angle_new(center_vector1,center_vector2):
    '''回傳值是角度'''
    dot_product=0
    center_vector_long1 = 0
    center_vector_long2 = 0
    cos = 0
    angle = 0
    dot_product = np.dot(center_vector1,center_vector2)
    for i in range(0,3) :
        center_vector_long1 += math.pow(center_vector1[i],2)	
        center_vector_long2 += math.pow(center_vector2[i],2)	 
    center_vector_long1 = math.sqrt(center_vector_long1)
    center_vector_long2 = math.sqrt(center_vector_long2)
    cos = dot_product / (center_vector_long1 * center_vector_long2)
    angle = math.acos(cos)
    answer = angle * 180 / math.pi #徑度換成角度
    return answer

def calculateDistance(x1,y1,z1,x2,y2,z2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
     return dist

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def get_projection_axis_value_firstZone(projection_vector_d3_ct,standard_vector):
    value = []
    a = calculate_angle(projection_vector_d3_ct,standard_vector)
    value_origin = math.sqrt(projection_vector_d3_ct[0]**2 + projection_vector_d3_ct[1]**2 + projection_vector_d3_ct[2]**2)
    a = a * math.pi /180  #超級重要，如果要把三角函數套回，要把角度換回徑度
    x = -(value_origin * math.cos(a))
    y = value_origin * math.sin(a)
    value.append(x)
    value.append(y)
    return value

def get_projection_axis_value_secondZone(projection_vector_d3_ct,standard_vector):
    value = []
    a = calculate_angle(projection_vector_d3_ct,standard_vector)
    value_origin = math.sqrt(projection_vector_d3_ct[0]**2 + projection_vector_d3_ct[1]**2 + projection_vector_d3_ct[2]**2)
    a = a * math.pi /180  #超級重要，如果要把三角函數套回，要把角度換回徑度
    x = -(value_origin * math.cos(a))
    y = value_origin * math.sin(a)
    value.append(x)
    value.append(y)
    return value

def get_projection_axis_value_thirdZone(projection_vector_d3_ct,standard_vector):
    value = []
    a = calculate_angle(projection_vector_d3_ct,standard_vector)
    value_origin = math.sqrt(projection_vector_d3_ct[0]**2 + projection_vector_d3_ct[1]**2 + projection_vector_d3_ct[2]**2)
    a = a * math.pi /180  #超級重要，如果要把三角函數套回，要把角度換回徑度
    x = -(value_origin * math.cos(a))
    y = -(value_origin * math.sin(a))
    value.append(x)
    value.append(y)
    return value

def get_projection_axis_value_forthZone(projection_vector_d2_ct,standard_vector):
    value = []
    a = calculate_angle(projection_vector_d2_ct,standard_vector)
    value_origin = math.sqrt(projection_vector_d2_ct[0]**2 + projection_vector_d2_ct[1]**2 + projection_vector_d2_ct[2]**2)
    a = a * math.pi / 180 #超級重要，如果要把三角函數套回，要把角度換回徑度
    x = -(value_origin * math.cos(a))
    y = -(value_origin * math.sin(a))
    value.append(x)
    value.append(y)
    return value
