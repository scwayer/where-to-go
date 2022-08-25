from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from places.models import Place
from places.models import Image


def index(request):
    places = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.62, 55.793676]
          },
          "properties": {
            "title": "«Легенды Москвы",
            "placeId": "moscow_legends",
            "detailsUrl": reverse("json_response", args=[1])
          }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.64, 55.753676]
          },
          "properties": {
            "title": "Крыши24.рф",
            "placeId": "roofs24",
            "detailsUrl": reverse("json_response", args=[2])
          }
        }
      ]
    }
    return render(request, 'index.html', context={"places": places})


def get_place(request, id):
    place = get_object_or_404(Place, pk=id)
    title = place.title
    description_short = place.description_short
    description_long = place.description_long
    coordinates = {"lat": place.coordinates_lat,
                   "lng": place.coordinates_lng}
    imgs = ["http://127.0.0.1:8000" + image.image.url for image in Image.objects.filter(place__title=place.title)]

    data = {"title": title,
            "imgs": imgs,
            "description_short": description_short,
            "description_long": description_long,
            "coordinates": coordinates}

    return JsonResponse(data, json_dumps_params={"indent": 4, "ensure_ascii": False})
