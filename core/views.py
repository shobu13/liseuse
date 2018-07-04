from django.shortcuts import render

from core.models import Doujinshi

from liseuse import settings


def home(request):
    doujin_liste = Doujinshi.objects.all()
    return render(request, 'core/core_home.html', locals())


def lire(request, doujin_id, page=1):
    images = []
    doujin = Doujinshi.objects.get(id=doujin_id)
    images_raw = doujin.doujinshiimage_set.all()
    for image in images_raw:
        images.append(image)
    return render(request, 'core/core_lire.html', locals())
