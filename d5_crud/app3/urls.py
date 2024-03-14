from django.urls import path,converters
from app3.views import home,details,subdetails,YearConverter
from app3.converters import FourDigitYearConverter
converters.register_converter(FourDigitYearConverter,'YYYY')
urlpatterns = [
    path('',home,{'check':'OK'},name='home'),
    path('details/<int:details_id>',details,name='details'),
    path('details/<int:details_id>/<int:subdetails_id>',subdetails,name='subdetails'),

    path('converter/<YYYY:year>',YearConverter,name='converter'), #only match if 4 digits given
]