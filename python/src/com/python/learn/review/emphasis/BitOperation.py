temp_num = 1
for i in range(1, 32):
    temp_num <<= 1
    print("2^%d = %d binary %d" % (i, temp_num, len(bin(temp_num))))

integer_size = 32
count_bits = integer_size - 3  # 32 高三位作为状态
capacity = (1 << count_bits) - 1

running = -1 << count_bits
shutdown = 0 << count_bits
stop = 1 << count_bits
tidying = 2 << count_bits
terminated = 3 << count_bits

print("capacity  = {},binary = {}".format(capacity, bin(capacity)))
print("running  = {},binary = {}".format(running, bin(running)))
print("shutdown  = {},binary = {}".format(shutdown, bin(shutdown)))
print("stop  = {},binary = {}".format(stop, bin(stop)))
print("tidying  = {},binary = {}".format(tidying, bin(tidying)))
print("terminated  = {},binary = {}".format(terminated, bin(terminated)))


def run_state_of(c):
    return c & ~capacity


def work_count_of(c):
    return c & capacity


def ctlOf(rs, wc):
    return rs | wc
