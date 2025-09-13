from django.shortcuts import render

# escreve 
def product_view(request):
    return render(request, 'pages/product_list.html', {})
