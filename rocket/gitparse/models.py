from django.db import models



class ReposInfo(models.Model):
    default_link = models.CharField(max_length=100, default='Some link')
    name_repo = models.CharField(max_length=100, null=True)
    about = models.CharField(max_length=100, null=True)
    link_site = models.CharField(max_length=100, null=True)
    stars = models.CharField(max_length=100, null=True)
    forks = models.CharField(max_length=100, null=True)

    watching = models.CharField(max_length=100, null=True)
    commits = models.CharField(max_length=100, null=True)
    commit_autor = models.CharField(max_length=100, null=True)
    commit_name = models.CharField(max_length=100, null=True)
    commit_date = models.CharField(max_length=100, null=True)
    releases = models.CharField(max_length=100, null=True)
    releases_version = models.CharField(max_length=100, null=True)
    releases_date = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name_repo