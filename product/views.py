from django.shortcuts import render

from product.forms import ProductForm


def product_creation(request):
    if request != 'POST':
        form = ProductForm()
    else:
        # post has been filled, ready for processing
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    context = {
        "form": form
    }
    return render(request, 'product/product_creation.html', context)


