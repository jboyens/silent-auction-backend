from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from .models import Auction
from rest_framework import viewsets, routers

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

class AuctionViewSet(viewsets.ModelViewSet):
    model = Auction

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'auctions', AuctionViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
