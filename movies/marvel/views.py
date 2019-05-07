from django.shortcuts import render


def get_marvel_movies(request):
    template_name = 'marvels/list.html'
    return render(request, template_name, {

    })
