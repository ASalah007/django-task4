from django.urls import path, include
from .views import *


urlpatterns= [ 
    path('parent/', include([ 
        path('', ParentListView.as_view()),
        path('<int:pk>/', ParentDetailView.as_view())
    ])),
    path('Subject/', include([ 
        path('', SubjectListView.as_view()),
        path('<int:pk>/', SubjectDetailView.as_view())
    ])),
    path('student/', include([ 
        path('', StudentListView.as_view()),
        path('<int:pk>/', StudentDetailView.as_view())
    ])),
]