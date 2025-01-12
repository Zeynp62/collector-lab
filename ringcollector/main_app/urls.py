from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('rings/',views.ring_index,name='index'),
    path('rings/<int:ring_id>/',views.rings, name='detail'),
    path('rings/create/',views.RingCreate.as_view(),name='rings_create'),
    path('rings/<int:pk>/update/',views.RingUpdate.as_view(),name='rings_update'),
    path('rings/<int:pk>/delete/',views.RingDelete.as_view(),name='rings_delete'),
    path('rings/<int:ring_id>/add_polishing',views.add_polishing,name='add_polishing')
]