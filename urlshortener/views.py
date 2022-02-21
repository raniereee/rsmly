from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound

from .models import Shortener

from .forms import ShortenerForm

from django.utils import timezone # Usefull for naive or aware datetime struct in now method

def home_view(request):

    template = 'urlshortener/home.html'

    context = {}

    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':

        used_form = ShortenerForm(request.POST)

        if used_form.is_valid():

            shortened_object = used_form.save()
            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            long_url = shortened_object.long_url

            context['new_url']  = new_url
            context['long_url'] = long_url

            return render(request, template, context)

        print("used_form.errors: ", used_form.errors )
        context['errors'] = used_form.errors

        return render(request, template, context)


def redirect_url_view(request, shortened_part):

    try:
        shortener = Shortener.objects.get(short_url=shortened_part)

        now = timezone.now()
        if now > shortener.expire_in:
            ret = shortener.delete()
            return HttpResponseNotFound('<h1>Page not found</h1>')

        return HttpResponseRedirect(shortener.long_url)

    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')

