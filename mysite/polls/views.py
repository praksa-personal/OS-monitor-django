from django.http.response import JsonResponse

from .OS_monitor import cpu_cores, cpu_util, disk_name, disk_total, disk_used, memory_avail, memory_used, user_boot_time, user_name

def index(request):
    response = JsonResponse(
        {'cpu cores': cpu_cores(),
        'cpu util': cpu_util(),
        'memory used': memory_used(),
        'memory available': memory_avail(),
        'disk name': disk_name(),
        'disk space': disk_total(),
        'disk used': disk_used(),
        'user name': user_name(),
        'user boot time': user_boot_time(),
        }
        )
    return response
