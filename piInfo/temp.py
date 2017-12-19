""" Read different temperatures from OrangePi """

def CPU():
    """ Return CPU temp in degC """
    temp_file0='/sys/devices/virtual/thermal/thermal_zone0/temp'
    temp_file1='/sys/devices/virtual/thermal/thermal_zone1/temp'
    cat = lambda file: open(file, 'r').read().strip()
    temp0 = int(cat(temp_file0))
    temp1 = int(cat(temp_file1))
    temp = (temp0+temp1)/2
    return temp

