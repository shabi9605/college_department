from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    path('add_ebook/',views.add_ebook,name='add_ebook'),
    path('ebook_details/',views.ebook_details,name='ebook_details'),
    path('update_ebook/<int:id>/',views.update_ebook,name='update_ebook'),
    path('delete_ebook_details/<int:id>/',views.delete_ebook_details,name='delete_ebook_details'),
    
    path('search_student/',views.search_student,name='search_student'),
    path('studentbook/',views.studentbook,name='studentbook'),
    path('search_studentbook/',views.search_studentbook,name='search_studentbook'),
     path('search_ebook/',views.search_ebook,name='search_ebook'),

    path('addstudentbook/<int:id>',views.addstudentbook,name='addstudentbook'),
    path('book_details/', views.book_details, name='book_details'),
    path('update_book/<int:id>/', views.update_book, name='update_book'),
    path('delete_book_details/<int:id>/',views.delete_book_details,name="delete_book_details"),

    path('view_library_detail',views.view_library_detail,name='view_library_detail'),

    path('staff_profile',views.staff_profile,name='staff_profile'),

    # # path('update_profile/',views.update_profile,name='update_profile'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)