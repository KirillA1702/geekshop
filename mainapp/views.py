from django.shortcuts import render

def main(request):
    return render(request, 'mainapp/index.html')

def product(request):
    return render(request, 'mainapp/product.html')

def contacts(request):
    return render(request, 'contacts/index.html')
