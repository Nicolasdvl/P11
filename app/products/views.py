"""
Django views for products app.

Python functions that takes a Web request and returns a Web response.
This response can be the HTML contents of a Web page, or a redirect,
or a 404 error, or an XML document, or an image . . .
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from authentification.models import User
from products.models import Product
from search.search import SearchForm
from products.forms.claims import ClaimForm

# Create your views here.


def substitutes(request, id):
    """Return a html page with a list of substitutes for a selected product."""
    product = Product.objects.get(id=id)
    search_form = SearchForm()
    context = {
        "product": product,
        "substitutes": product.get_subs_list(),
        "SearchForm": search_form,
    }
    if "submit_save" in request.POST:
        submit = request.POST.get("submit_save")
        submit = submit.split()
        product = Product.objects.get(id=submit[0])
        user = User.objects.get(id=submit[1])
        product.users_saves.add(user)
        product.save()
    return render(request, "products/substitutes.html", context)


def details(request, id):
    """Return a html page with details of a product selected."""
    product = Product.objects.get(id=id)
    search_form = SearchForm()
    context = {"product": product, "SearchForm": search_form}
    return render(request, "products/details.html", context)


def similar(request):
    """Return a 'product not found' page or products similar to user input."""
    search_input = request.POST.get("search_input")
    try:
        products = Product.objects.filter(name__icontains=search_input)
        if len(products) > 10:
            products = products[:10]
        context = {
            "similar_products": products,
            "product_search": search_input,
        }
    except ObjectDoesNotExist:
        context = {"product_search": search_input}
    return render(request, "products/similar.html", context)


@login_required
def my_substitutes(request):
    """Return a html page with a list of products saved by user."""
    user = request.user
    search_form = SearchForm()
    context = {"products": user.get_saves(), "SearchForm": search_form}
    return render(request, "products/saves.html", context)


@login_required
def claim(request):
    if request.method == "POST":
        claim_form = ClaimForm(request.POST)
        if claim_form.is_valid():
            user = request.user
            new_claim = claim_form.save()
            new_claim.user.add(user)
            return redirect("index")
    else:
        claim_form = ClaimForm()
    search_form = SearchForm()
    context = {"ClaimForm": claim_form, "SearchForm": search_form}
    return render(request, "products/claim.html", context)
