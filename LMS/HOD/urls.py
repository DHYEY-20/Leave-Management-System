from django.contrib import admin
from django.urls import path
from HOD.views import *

urlpatterns = [
    path('hod/',das_HOD,name="das_hod"),
    path('pending_leaves/',pend_leav,name="pend_leav"),
    path('approved_leaves/',appr_leav,name="appr_leav"),
    path('rejected_leaves/',rej_leav,name="rej_leav"),
]