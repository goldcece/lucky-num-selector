
## Lotto number selector

import random

def random_select():

    num_list = []
    for i in range(6):
	n = random.randint(1,46)
	num_list.append(n)

print(num_list)
	
