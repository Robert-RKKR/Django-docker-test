from django.shortcuts import render
from .task import test_task

# Create your views here.
def test_page(request):
    data = {}
    data['output'] = test_task.delay()

    return render(request, 'basic.html', data)
