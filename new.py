# def new():
#     print('1123')
#
# def login():
#     print('2123')
#
# def go():
#     pass
#
# list = [1,2,3,4]

import random

def v_code():

    code = ''
    for i in range(5):
        num=random.randint(0,9)
        alf=chr(random.randint(65,90))
        add=random.choice([num,alf])
        code="".join([code,str(add)])
        print(alf)
    return code

print(v_code())