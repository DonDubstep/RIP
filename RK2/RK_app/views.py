from django.shortcuts import render
from .models import Computer, Disk

def PCDisks(request):
    disks = Disk.objects.all()
    computers = Computer.objects.all()
    context = {
        'disks': disks,
        'computers': computers
    }
    return render(request, 'base.html', context)
