import time

test = []
start_time = time.time()
for i in range(50000):
    test.append(i*2)
elapsed_time = time.time() - start_time
print(elapsed_time)
