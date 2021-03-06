from datetime import datetime
import time
import os

log_file=open('main_log.txt','w+')
sleep_time_addon=15
current_sleep_time=5
threshold_for_sleep_increase=100
wait_upper_threshold=100
last_terminate_time=datetime.now()
while True:
    os.system('python3 basic_info.py')
    print('Program Exits. Taking a break...')
    log_file.write(str(datetime.now())+'#Program Terminated. Time elapsed: ' + \
                   str((last_terminate_time-datetime.now()).seconds)+'\n')
    if (last_terminate_time-datetime.now()).seconds < threshold_for_sleep_increase:
        current_sleep_time+=sleep_time_addon
        if current_sleep_time>wait_upper_threshold:
            #API may be blocked. Directly quit
            log_file.write(str(datetime.now())+'#Waittime Exceed Upper Threshold. Exit.\n')
    time.sleep(current_sleep_time)
    last_terminate_time=datetime.now()
