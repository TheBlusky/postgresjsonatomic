import time
from django.db import transaction
from django.http import HttpResponse
import logging
from app.models import MyModel


logger = logging.getLogger(__name__)


def create_model(request):
    my_model = MyModel()
    my_model.id = 0
    my_model.save()
    return HttpResponse("Ok")


def append_data(request):
    with transaction.atomic():
        entry = MyModel.objects.select_for_update().get(id=0)
        entry.files += [request.GET["some_value"]]
        time.sleep(1)
        logger.warning(entry.files)
        entry.save()
    return HttpResponse(str(entry.files))
