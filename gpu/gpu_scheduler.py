
def gpu_score(util, mem_free):
    return mem_free*0.7 - util*0.3

print(gpu_score(65, 14000))
