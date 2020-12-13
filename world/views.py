from django.contrib.auth.decorators import login_required
from django.shortcuts import render

locations = [
    {
        'author': 'John Doe',
        'title': 'location 1',
        'content': 'First post content',
        'date_posted': 'January, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'location 2',
        'content': 'Second post content',
        'date_posted': 'January, 2021'
    }
]

@login_required
def home(request):
    context = {
        'locations': locations
    }
    return render(request, 'world/home.html', context)


def about(request):
    return render(request, 'world/about.html', {'title': 'About'})

