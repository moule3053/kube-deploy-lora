# -*- coding: utf-8 -*-

def wind(data_hex):
    
    # 02 20 e7 00 03 80 0a 81 da 80 0a 80 c1 7c 7c 83 84 80 07 80 07 0b 71
    payload_dict = {}
    
    value = int(data_hex[10:14], 16)
    # print(data_hex[10:14], value)
    payload_dict['Windspeed'] =  str(round((value-32768)/100.0, 2)) + ' m/s'
    
    value = int(data_hex[14:18], 16)
    payload_dict['Winddirection'] =  str(round((value-32768)/10.0, 2)) + ' º'    
    
    value = int(data_hex[18:22], 16)
    payload_dict['Maximumwindspeed'] =  str(round((value-32768)/100.0, 2)) + ' m/s'  

    value = int(data_hex[22:26], 16)
    payload_dict['Airtemperature'] =  str(round((value-32768)/10.0, 2)) + ' ºC'   

    value = int(data_hex[26:30], 16)
    payload_dict['TiltangleXorientation'] =  str(round((value-32768)/10.0, 2)) + ' º'         

    value = int(data_hex[30:34], 16)
    payload_dict['TiltangleYorientationn'] =  str(round((value-32768)/10.0, 2)) + ' º'     
    
   
    value = int(data_hex[34:38], 16)
    payload_dict['Northwindspeed'] =  str(round((value-32768)/100.0, 2)) + ' m/s'   

    value = int(data_hex[38:42], 16)
    payload_dict['Eastwindspeed'] =  str(round((value-32768)/100.0, 2)) + ' m/s'

    value = int(data_hex[42:46], 16)
    payload_dict['Batteryvoltage'] =  str(round(value/1000.0, 2)) + ' V'
    
    return payload_dict