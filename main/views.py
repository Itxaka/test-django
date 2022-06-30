from django.shortcuts import render
from django.views import generic
from main.models import DockerAddresses, Containers
from main.forms import SelectDocker


class MyView(generic.ListView):
    title = ""
    context_object_name = "object_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['dockerForm'] = SelectDocker
        print(context)
        print(kwargs)
        return context


class IndexView(MyView):
    template_name = 'main/index.html'
    context_object_name = "dockerAddresses"
    title = "Addresses"

    def get_queryset(self):
        """Return the last five published questions."""
        print("get queryset")
        return DockerAddresses.objects.get_queryset()


class MainDockerView(MyView):
    template_name = 'main/containers.html'

    def get_queryset(self):
        docker_id = self.request.session.get("docker_id")
        return Containers.objects.filter(docker_id=docker_id)

    def post(self, *args, **kwargs):
        docker_id = self.request.POST["name"]
        self.request.session.setdefault("docker_id", docker_id)
        return self.get(self.request, args, kwargs)
