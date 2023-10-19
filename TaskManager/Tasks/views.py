from django.views import View
from .models import Task
from django.http import JsonResponse


class TaskListView(View):
     def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return JsonResponse(list(tasks.values()), safe=False)

class CreateTaskView(View):
    def post(self, request, *args, **kwargs):
        task = request.POST.get('task')
        Task.objects.create(task=task)
        return JsonResponse({'message': 'Task has been created successfully!'})
    
class CompleteTaskView(View):
    def post(self, request, task_id, *args, **kwargs):
        task = Task.objects.get(pk=task_id)
        task.completed = True
        task.save()
        return JsonResponse({'message': 'Task has been completed successfully!'})

class DeleteTaskView(View):
    def post(self, request, task_id, *args, **kwargs):
        task = request.POST.get(pk = task_id)
        task.delete()
        return JsonResponse({'mensage': 'Task has been deleted sucessfully!'})
        
        