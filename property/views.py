from django.shortcuts import render
from .models import Property, Category
from .forms import ReserveForm
from django.db.models import Q

# Create your views here.
def property_list(request):
    property_list = Property.objects.all()
    template = 'property/list.html'

    address_query = request.GET.get('q')
    property_type = request.GET.getlist('property_type', None)
    location = request.GET.getlist('location', None)
    beds_number = request.GET.getlist('beds_number', None)
    size = request.GET.getlist('size', None)
    category = request.GET.getlist('category', None)
    if address_query and property_type:
        property_list = property_list.filter(
            Q(name__icontains = address_query) &
            Q(property_type__icontains = property_type[0]) &
            Q(location__icontains = location[0]) &
            Q(beds_number__icontains = beds_number[0]) &
            Q(size__icontains = size[0]) &
            Q(category__icontains = category[0])
        ).distinct()

    context = {
        'property_list': property_list
        
    }

    return render(request, template, context)

def property_detail(request, id):
    property_detail = Property.objects.get(id=id)
    template = 'property/detail.html'

    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    
    else:
        reserve_form = ReserveForm()


    context = {
        'property_detail': property_detail,
        'reserve_form': reserve_form,
    }
    return render(request, template, context)