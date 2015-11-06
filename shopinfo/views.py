from django.shortcuts import render

# Create your views here.

from django.db.models import Q
from models import Shopinformation
from django.shortcuts import render_to_response
#from django.http import HttpResponse
#from django.template import Context, Template
#from django.template.loader import get_template

def search(request):
  query = request.GET.get('q', '')
  if query:
    qset = (
      Q(name__contains = query)|
      Q(addr__contains = query))
    results = Shopinformation.objects.filter(qset).distinct()
  else:
    results = []
#  t = get_template('search.html')
#  html = t.render(Context({'results': results, 'query': query}))
#  return HttpResponse(html)
  return render_to_response('search.html',
                            {'results': results, 'query': query})
