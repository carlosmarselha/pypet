from django.shortcuts import render
from django.http import HttpResponse

# escreve 
def product_view(request):
    return render(request, 'product_list.html', {})
