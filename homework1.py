def geometric_area(shape,parameter1,parameter2):
    area=0
    if(shape==1):#矩形
            area=parameter1*parameter2
    else :#圓形
            area=(parameter1*parameter1)*3.14
    return area
def geometric_line(shape,parameter1,parameter2):
    line=0
    if(shape==1):#矩形
        line=(parameter1+parameter2)*2
    else :#圓形
        line=parameter1*2*3.14
    return line
print("ans is :",geometric_area(2,3,2),geometric_line(2,3,2))