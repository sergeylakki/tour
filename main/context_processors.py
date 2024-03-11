from main import models


def categories(request):
    categories = models.CategoryEvent.objects.all()
    #categories = [{'name': item.name, 'id': item.id} for item in categories]
    return {"categories": categories}
