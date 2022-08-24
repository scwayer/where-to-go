from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse

from places.models import Place, Image


def get_place(request, id):
    place = get_object_or_404(Place, pk=id)

    title = place.title
    description_short = place.description_short
    description_long = place.description_long
    coordinates = {"lat": place.coordinates_lat,
                  "lng": place.coordinates_lng}
    imgs = [image.image.url for image in Image.objects.filter(place__title=place.title)]

    data = {"title": title,
            "imgs": imgs,
            "description_short": description_short,
            "description_long": description_long,
            "coordinates": coordinates}

    return JsonResponse(data, safe=False, json_dumps_params={"ensure_ascii": False})
