"""Books views."""

# Django
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.core.mail import send_mail

# Models
from .models import Book

# Forms
from .forms import ContactForm


def hello_world(request):
    """Returns a greeting."""

    return HttpResponse('Hello, world!')


def current_view_url(request):
    """Returns the url."""

    return HttpResponse('Welcome to my page in {} (url).'.format(request.path))


def current_view_host(request):
    """Returns the host."""

    return HttpResponse('Welcome to my page in {} (host).'.format(request.get_host()))


def current_view_is_secure(request):
    """Returns if the request was made via HTTPS."""

    return HttpResponse('Is this website safe? {}'.format(request.is_secure()))


def show_browser(request):
    """Show web browser."""

    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknown'

    return HttpResponse('Your web browser is {}'.format(ua))


def show_ip(request):
    """Show ip address."""

    ra = request.META['REMOTE_ADDR']
    return HttpResponse('Your IP address is {}'.format(ra))


def search_form(request):
    """Search form."""

    return render(request, 'books/search-form.html')


def search(request):
    """Search form."""

    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Please, enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter a search term less than 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/results.html', {
                'books': books,
                'query': q,
            })
    return render(request, 'books/search-form.html', {'errors': errors})


def contact(request):
    """Contact form."""

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['subject'],
                      cd['message'],
                      cd.get('email', 'noreply@email.com'),
                      ['siteowner@email.com'], )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact/contact-form.html', {'form': form})
