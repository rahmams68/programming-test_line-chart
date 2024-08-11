import re
from datetime import datetime, timedelta

def getData():
    ### Read data from .txt file
    source = 'data.txt'
    
    f = open(source, 'r')
    lines = f.read()
    f.close()

    lines_per_test = lines.split('iperf Done.')
    lines_per_test.pop()

    ### Define dictionary, regex pattern, and datetime format
    data = {
        'date_time': [],
        'sender_avg_speed': []
    }

    re_speed = re.compile(r'[.\d]+ [MK]*bi')
    re_time = re.compile('(Timestamp: )([-: 0-9]+)')
    dt_format = '%Y-%m-%d %H:%M:%S'

    ### Get data per test
    for i in lines_per_test:
        ### Get datetime
        dt = re.search(re_time, i).group(2)
        dt = datetime.strptime(dt, dt_format)
        

        ### Get sender average speed
        s = re.findall(re_speed, i)
        s_sender = s[-2]
        s_value = float(re.search('[.0-9]+', s_sender).group(0))

        if re.search('Kbi', s_sender):
            s_value /= 8000

        ### Append data to dictionary        
        data['date_time'].append(dt)
        data['sender_avg_speed'].append(s_value)

    return data