from django.shortcuts import render, HttpResponse
from django.views import View
from .form import LinkForm
# from scraper.management.commands.crawl import Command

global link
link = 'https://github.com/scrapy/'
class GitParse(View):
    def get(self, request):
        form = LinkForm()

        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = LinkForm(request.POST)
        if form.is_valid():
            links = form.cleaned_data['link']

            return HttpResponse('Its OK')
