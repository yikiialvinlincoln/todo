from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import To_do

# Create your views here.
def homepage(request):
    if request.method == "POST":
        new_task = request.POST["task"]
        add_task = To_do(task=new_task)
        add_task.save()
    all_todo = To_do.objects.all()
    context = {
        "all_todo": all_todo,
    }
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context))
