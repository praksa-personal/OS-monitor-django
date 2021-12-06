from django.http import JsonResponse, response
from .OS_monitor import cpu_cores, cpu_util, disk_name, disk_total, disk_used, memory_avail, memory_used, user_boot_time, user_name
from django.shortcuts import render
from django.urls import reverse

def allData(request):
    response = JsonResponse(
        {
        'cpu cores': cpu_cores(),
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

def cpu(request):
    response = JsonResponse(
        {'cpu cores': cpu_cores(),
        'cpu util': cpu_util(),
        }
        )
    return response

def memory(request):
    response = JsonResponse(
        {
        'memory used': memory_used(),
        'memory available': memory_avail(),
        }
        )
    return response

def table(request):
    context = {
        'cpu_cores': cpu_cores(),
        'cpu_util': cpu_util(),
        'memory_used': memory_used(),
        'memory_available': memory_avail(),
        'disk_name': disk_name(),
        'disk_space': disk_total(),
        'disk_used': disk_used(),
        'user_name': user_name(),
        'user_boot_time': user_boot_time(),
    }

    return render(request, "simple/table.html",context=context)


