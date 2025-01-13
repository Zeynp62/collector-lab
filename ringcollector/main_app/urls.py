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
    path('rings/<int:ring_id>/add_polishing',views.add_polishing,name='add_polishing'),
    #CRUD for toys using CBV's
    path('bands/',views.BandList.as_view(),name='bands_index'),
    path('bands/<int:pk>/',views.BandDetail.as_view(),name='bands_detail'),
    path('bands/create/',views.BandCreate.as_view(),name='bands_create'),
    path('bands/<int:pk>/update/',views.BandUpdate.as_view(),name='bands_update'),
    path('bands/<int:pk>/delete/',views.BandDelete.as_view(),name='bands_delete'),
    #----Many to Many
    path('rings/<int:ring_id>/assoc_band/<int:band_id>/',views.assoc_band,name='assoc_band'),
    path('rings/<int:ring_id>/unassoc_band/<int:band_id>/',views.unassoc_band,name='unassoc_band')
    
]