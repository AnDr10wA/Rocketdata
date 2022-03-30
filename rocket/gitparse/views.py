from django.shortcuts import render, HttpResponse
from django.views import View
from .form import LinkForm
from .models import ReposInfo
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *



class GitParse(View):
    def get(self, request):
        # form = LinkForm()
        data  = ReposInfo.objects.all().values("default_link").distinct()

        return render(request, 'index.html', {'data': data})

    def post(self, request):
        form = LinkForm(request.POST)
        if form.is_valid():
            links = form.cleaned_data['link']

            return HttpResponse('Its OK')
class ProjectListView(APIView):



    def get(self, request):

        project = ReposInfo.objects.all().values("default_link").distinct()
        serializer = ProjectListSerializers(project, many=True)
        return Response(serializer.data)


class ReposListView(APIView):

    def get(self, request, project):
        repos = ReposInfo.objects.filter(default_link__contains=project)
        serializer = ReposListSerializers(repos, many=True)
        return Response(serializer.data)

class StatsView(APIView):

    def get(self, request):
        serializer = StatsSerializers(stats_all_data())
        return Response(serializer.data)

class StatsOneView(APIView):

    def get(self, request, project):

        serializer = StatsOneSerializers(stats_one_user(project))
        return Response(serializer.data)


class StatsAll:

    def __init__(self, users, repos,average_repos):
        self.users = users
        self.repos = repos
        self.average_repos = average_repos

def stats_all_data():

    users = ReposInfo.objects.all().values("default_link").distinct()
    amount_users = len(users)
    repos = len(ReposInfo.objects.all())
    list_repos = []
    for user in users:
        repos_user = ReposInfo.objects.filter(default_link=user.get('default_link'))
        amount_repos = len(repos_user)
        list_repos.append(amount_repos)

    average_repos = sum(list_repos)/len(list_repos)
    stats = StatsAll(amount_users, repos, average_repos)
    return stats

class StatsOneUser:

    def __init__(self, commit,repo_name,  av_stars):
        self.repo_max_commit = commit
        self.repo_name = repo_name
        self.av_stars = av_stars


def stats_one_user(project):
    repos = ReposInfo.objects.filter(default_link__contains=project)
    commits_list = []
    av_stars_list = []
    for repo in repos:
        commit_str = repo.commits
        commit = int(commit_str.replace(',', ''))
        commits_list.append(commit)
        stars_str = repo.stars
        if 'k' in stars_str:
            stars_str = stars_str.replace('k', '00')

        stars = int(stars_str.replace('.', ''))
        av_stars_list.append(stars)
    for repo in repos:
        commit_str = repo.commits

        if max(commits_list) == int(commit_str.replace(',', '')):
            repo_name = repo.name_repo
    av_star = sum(av_stars_list)/len(av_stars_list)
    return StatsOneUser(max(commits_list), repo_name, av_star)







