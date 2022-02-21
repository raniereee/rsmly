from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from urlshortener.models import Shortener

ITEMS_PER_PAGE = 10

@login_required
def index(request):
    if request.method == 'GET':
        context = {}

        urls_list = Shortener.objects.all().order_by('-created')

        '''
        from: https://docs.djangoproject.com/en/4.0/topics/pagination/
        Give Paginator a list of objects,
        plus the number of items you'd like to have on each page,
        and it gives you methods for accessing the items for each page
        '''
        paginator = Paginator(urls_list, ITEMS_PER_PAGE)

        page = request.GET.get('page')
        posts = paginator.get_page(page)

        return render(request, 'dashboard/index.html', {'posts':posts})

