from config.config1 import *



with open('report_{}.html'.format(today) ,'wr') as f:
    f.write(now)
    f.write('pass')
    print (now)