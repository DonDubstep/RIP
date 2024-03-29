import json
from cm_timer import cm_timer_1, cm_timer_2
from field import field
from Unique import Unique
from print_result import print_result
from get_random import get_random


@print_result
def f1(data):
    return sorted(Unique(field(data,'job-name'), ignore_case=True))

@print_result
def f2(data):
    return list(filter(lambda d: 'программист' in d[:11], data))

@print_result
def f3(data):
    return list(map(lambda x: x + " с опытом Python", data))

@print_result
def f4(data):
    return list(zip(data, list(map(lambda x: "Зарплата " + x + " руб",map(str,(get_random(len(data), 100000, 200000)))))))


if __name__ == "__main__":
    with open('D:\\ProgRAMS\\Python\\lab_python_fp\\data_light.json', 'r', encoding='utf8') as jft:
        data = json.load(jft)
    with cm_timer_1():
        f4(f3(f2(f1(data))))



        
