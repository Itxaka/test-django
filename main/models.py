from django.db import models


# Create your models here.


class DockerAddresses(models.Model):
    name = models.CharField(max_length=200)
    uri = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Docker Addresses"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name} ({self.uri})'


class Images(models.Model):
    repository = models.CharField(max_length=200)
    imageid = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField()
    size = models.IntegerField()
    tag = models.CharField(max_length=200)
    docker = models.ForeignKey(DockerAddresses, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Images"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.repository}:{self.tag}'


ContainerStatusChoices = [
    ("created", "created"),
    ("running", "running"),
    ("restarting", "restarting"),
    ("exited", "exited"),
    ("paused", "paused"),
    ("dead", "dead"),
]


class Containers(models.Model):
    containerid = models.CharField(max_length=200, unique=True)
    command = models.CharField(max_length=200)
    created = models.DateTimeField()
    status = models.CharField(max_length=100, choices=ContainerStatusChoices)
    ports = models.JSONField(null=True, blank=True)
    names = models.CharField(max_length=200)
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    docker = models.ForeignKey(DockerAddresses, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Containers"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.names}({self.containerid})'

