from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
def alert1(req):
    stat = req['stat'].split(",")
    SERVER_ID = stat[0]
    CPU_UTILIZATION = int(stat[1])
    MEMORY_UTILIZATION = int(stat[2])
    DISK_UTILIZATION = int(stat[3])
    message = ""
    if CPU_UTILIZATION > 85 or MEMORY_UTILIZATION > 75 or DISK_UTILIZATION > 65 :
        message  = message + "Alert," + SERVER_ID
        if CPU_UTILIZATION > 85:
            message = message + ", CPU_UTILIZATION VIOLATED"
        if MEMORY_UTILIZATION > 75:
            message = message + ", MEMORY_UTILIZATION VIOLATED"
        if DISK_UTILIZATION > 65:
            message = message + ", DISK_UTILIZATION VIOLATED"
    else:
        message = "No Alert,"+SERVER_ID
    return message
@api_view(['POST'])
def alert(request):
    if request.method == 'POST':
        stat = request.data
        message = alert1(stat)
        return Response({'response':message})
        