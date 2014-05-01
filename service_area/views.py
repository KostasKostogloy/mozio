from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from service_area.models import ServiceArea, Vertice, Supplier
import json
import decimal

# Create your views here.

def create(request):
    
    if request.method == 'POST':
        i = 0
        x1= -999
        y1= -999
        x2 = 999
        y2 = 999
        vertices = json.loads(request.POST['vertices'])
        
        # First I will get the biggest and lower latitudes and longitudes, we need them for the ServiceArea model
        while i < len(vertices):
            x1 = max (vertices[i]['A'] , x1)
            y1 = max (vertices[i]['k'] , y1)
            x2 = min (vertices[i]['A'] , x2)
            y2 = min (vertices[i]['k'] , y2)
            i += 1
        service_area = ServiceArea()
        service_area.supplier = Supplier(id=1)
        service_area.x1 = x1
        service_area.y1 = y1
        service_area.x2 = x2
        service_area.y2 = y2
        service_area.save()
        # Now lets save the Vertices
        i = 0
        while i < len(vertices):
            vertice = Vertice()
            vertice.service_area = service_area
            vertice.longitude = vertices[i]['A']
            vertice.latitude = vertices[i]['k']
            vertice.save()
            i += 1
            
        return HttpResponseRedirect('service_area/search')
    return render(request, 'service_area/create.html')

def search(request):
    supplier_list = "List of suppliers <br />"
    if request.method == 'POST':
        x = json.loads(request.POST['x'])
        y = json.loads(request.POST['y'])
        service_areas = ServiceArea.objects.all().filter( x1__gte = x , x2__lte = x, y1__gte = y, y2__lte = y)
        for i in range(len(service_areas)):
            vertices = Vertice.objects.all().filter(service_area = ServiceArea(service_areas[i].id))
            # Call a function to check if point is within the polygon
            found = inside_polygon(x, y, vertices)
            if found:
                supplier_list += "Supplier " + service_areas[i].supplier.first_name + ' ' + service_areas[i].supplier.last_name + ' provides a shuttle for this service_area with id:' + str(service_areas[i].id) + '<br />'
    return HttpResponse(supplier_list)
            
def interactive_map(request):        
    return render(request, 'service_area/search.html')

def inside_polygon(x, y, vertices):
    points = []
    for i in range(len(vertices)):
        points.append([ vertices[i].longitude , vertices[i].latitude])
    n = len(points)
    inside = False
    p1x, p1y = points[0]
    for i in range(1, n + 1):
        p2x, p2y = points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (decimal.Decimal(y) - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside