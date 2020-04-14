from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'HOME'),
    path('file_upload/', views.file_upload, name = "FILE_UPLOAD"),
    path('columns/', views.dataset_columns, name = "COLUMNS"),
    path('barchart/', views.barplot_script, name = "BARCHART"),
    path('piechart/', views.pieplot_script, name = "PIECHART"),
    path('polararea/', views.polararea_script, name = "POLARAREA"),
    path('linechart/', views.lineplot_script, name = "LINECHART"),
    path('scatterplot/', views.scatterplot_script, name = "SCATTERPLOT"),
    path('histogram/', views.histogram_script, name = "HISTOGRAM"),
    path('linear/', views.linear_regression, name = "LINEAR"),
    path('data_categorical/', views.data_send_categorical, name = "DATA-SEND-CATEGORICAL"),
    path('data_send_numerical/', views.data_send_numerical, name = "DATA-SEND-NUMERICAL"), 
]

#bar, hist, pie, linear,  scatter, line