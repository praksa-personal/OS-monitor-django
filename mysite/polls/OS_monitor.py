import psutil, datetime

def cpu_cores():
    return psutil.cpu_count()

def cpu_util():
    return psutil.cpu_percent(interval=1)
    
def memory_used():
    return psutil.virtual_memory().percent

def memory_avail():
    return (100-psutil.virtual_memory().percent)

def disk_name():
    return psutil.disk_partitions()[0].device

def disk_total():
    d = psutil.disk_usage('/')
    total = d.total
    return total / (2**30)

def disk_used():
    d = psutil.disk_usage('/')
    return d.percent

def network():
    net = psutil.net_io_counters(pernic=True)
    print("Nerwork data:\n",net)

def users():
    info = psutil.users()
    print("User name: ",info[0].name)
    boot = psutil.boot_time()
    print("Boot time: ",boot)
    formated = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    print("Formated: ",formated)
