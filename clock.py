# import time

# while True:
#     current_time = time.localtime()
#     formatted_time = time.strftime("%H:%M:%S", current_time)
#     print(formatted_time)
#     time.sleep(10)

import time


def get_current_time():
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec
    return hour, minute, second


def update_clock():
    hour, minute, second = get_current_time()
    time_str = f"{hour:02d}:{minute:02d}:{second:02d}"
    print(time_str)
    # time.sleep(1)
    # update_clock()


# Start updating the clock
update_clock()
