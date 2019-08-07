from django.shortcuts import render
from django.db.models import F
from django.http import HttpResponse
from monitoring.models import Dumps, Parametrs


# Create your views here.


def get(request):

    if 'q' not in request.GET or request.GET['q'] == 'all':
        dumps = Parametrs.objects.all().values('dump__side_number', 'dump__dump_model', 'dump__max_tonnage',
                                               'tonnage').annotate(
            overload=(100 * (F('tonnage') - F('dump__max_tonnage'))) / F('tonnage'))
    else:
        dumps = Parametrs.objects.filter(dump__dump_model=request.GET['q']).values('dump__side_number',
                                                                                   'dump__dump_model',
                                                                                   'dump__max_tonnage',
                                                                                   'tonnage').annotate(
            overload=(100 * (F('tonnage') - F('dump__max_tonnage'))) / F('tonnage'))
    list_models = Dumps.objects.values_list('dump_model', flat=True).distinct()

    return render(request, 'index.html', {'dumps': dumps, 'list_models': list_models})
