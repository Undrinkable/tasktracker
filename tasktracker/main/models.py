from django.forms import ModelForm, DateInput
from django.db import models
from datetime import date

# Create your models here.
class Task(models.Model):
    PRIORITY_HIGH = 'h'
    PRIORITY_MEDIUM = 'm'
    PRIORITY_LOW = 'l'
    PRIORITY_CHOICES = (
        (PRIORITY_HIGH, 'high'),
        (PRIORITY_MEDIUM, 'medium'),
        (PRIORITY_LOW, 'low'),
    )
    
    STATUS_GREEN = 'g'
    STATUS_YELLOW = 'y'
    STATUS_RED = 'r'
    STATUS_CHOICES = (
        (STATUS_GREEN, 'green'),
        (STATUS_YELLOW, 'yellow'),
        (STATUS_RED, 'red'),
    )
    
    name = models.CharField(max_length=100)
    duedate = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default=PRIORITY_LOW)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_GREEN)
    comment = models.TextField(blank=True)
    subtasks = models.ManyToManyField("self", symmetrical=False, blank=True)
#    recurringTasks = models.ManyToManyField("self", blank=True)
    
#    @classmethod
#    def createRecurringTask(cls, name, duedate, priority, status, comment, subtasks, recurringEvery, recurrenceCount):
#        task = cls(name=name, duedate=duedate, priority=priority, status=status, comment=comment, subtasks=subtasks)
#        task.save()
#        for i in xrange(recurrenceCount):
#            recurringTask = Task(name=name+str(i), duedate=duedate+recurringEvery, priority=priority, status=status, comment=comment, subtasks= subtasks)
#            recurringTask.save()
#            task.recurringTasks.append(recurringTask)
#        return task
    
    def __str__(self):
        return self.name
 
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'duedate', 'priority', 'status', 'comment']
        widgets = {
            'duedate': DateInput(attrs={'class':'datepicker'}),
        } 
