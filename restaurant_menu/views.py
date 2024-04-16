from django.shortcuts import render
from django.views import generic
from .models import Item


class MenuList(generic.ListView):
    # connects model to the view
    queryset = Item.object.order_by("-date_created")

    # template name connects view to html page
    template_name = "index.html"


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"