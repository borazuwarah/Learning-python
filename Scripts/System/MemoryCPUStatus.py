import psutil
import os
os.system('cls')
if __name__ == '__main__':
    perc_cpu = psutil.cpu_percent(interval=1, percpu=True)
    mem_virt = int(psutil.virtual_memory().used / (1024 ** 2))
    avail_mem = int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
    print(f'''Estado actual del PC:
La CPU está al {perc_cpu}%
Total memoria {int(psutil.virtual_memory().total / (1024 ** 2))} Mb de memoria
Usando {mem_virt} Mb de memoria
Quedando {avail_mem}% memoria libre
***************************
{round(psutil.virtual_memory().total / (1024 ** 3), 2)} Gb de memoria
Usando {round(mem_virt / (1024 ** 3), 2)} Gb de memoria
'''
)

