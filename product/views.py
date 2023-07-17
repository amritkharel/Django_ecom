# products/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ReviewForm

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            review = form.cleaned_data['review']
            # You can save the review or perform any other actions here
            # For this example, we're not saving the review.

            # Return a response or redirect after the review submission
            return render(request, 'product/review_success.html')
    else:
        form = ReviewForm()

    return render(request, 'product/product_detail.html', {'product': product, 'form': form})
