""" Read different temperatures from OrangePi """

def CPU(bPrecise=0):
    """ Return CPU temp in degC """
    temp_file0='/sys/devices/virtual/thermal/thermal_zone0/temp'
    temp_file1='/sys/devices/virtual/thermal/thermal_zone1/temp'
    temp0=0
    temp1=0
    cat = lambda file: open(file, 'r').read().strip()
    # check if both files exist, otherwise use one of them only
    try:
        temp0 = int(cat(temp_file0)) 
        temp1 = int(cat(temp_file1))
    except IOError:
        if temp1==0:
            temp1=temp0
        if temp0==0:
            temp0=temp1
    temp = (temp0+temp1)/2
    # default kernel return temp*1000, legacy returns normal
    if temp>1000:
        if bPrecise>0:
            temp=temp/1000.0
        else:
            temp=temp/1000
    return temp
