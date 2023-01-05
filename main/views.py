from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, Http404
from django.core.paginator import Paginator
from .models import Task
from .forms import TaskForm


# Create your views here.

def done(request):
    task_list = Task.objects.filter(status=True)
    paginator = Paginator(task_list, 7)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "main/index.html", context={
        "task_list": task_list,
        "page_obj": page_obj,
    })


def all_tasks(request):
    task_list = Task.objects.filter(status=False)  # .order_by("title")
    paginator = Paginator(task_list, 7)


    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "main/all_tasks.html", context={
        "task_list": task_list,
        "page_obj": page_obj,

    })


def add(request):
    form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "main/add.html", context=context)


def add_task(request):
    title = request.POST["title"]
    text = request.POST["text"]

    Task.objects.create(title=title, text=text)

    return HttpResponseRedirect(reverse("main:add", args=[]))


def change_status(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Exception:
        raise Http404("Err")

    if not task.status:
        task.status = True
        task.save()
        return HttpResponseRedirect(reverse("main:tasks", args=[]))
    else:
        task.status = False
        task.save()
        return HttpResponseRedirect(reverse("main:index", args=[]))