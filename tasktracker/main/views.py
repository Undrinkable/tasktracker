from django.shortcuts import render
from .models import Task, TaskForm
from django.forms import modelformset_factory
# Create your views here
def index(request):
    TaskFormSet = modelformset_factory(Task, exclude=('Id',))
    if request.method == 'POST':
        formset = TaskFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    elif request.method == 'DELETE':
        Task.objects.filter(id=request.DELETE['id']).delete()
        formset = TaskFormSet()
    else:
        formset = TaskFormSet()
        DisplayFormSet = modelformset_factory(Task, form=TaskForm, fields=("name", "duedate","priority","status"))    
        displayset = DisplayFormSet()
   
    tasks = Task.objects.all() 
    return render(request, 'index.html', {'tasks' : tasks, 'formset' : formset, 'displayset' : displayset})
