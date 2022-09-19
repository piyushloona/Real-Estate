from django.urls import path
from . import views
urlpatterns = [
    path('', views.property, name='property'),
    path('gallery', views.gallery, name='gallery'),
    path('New', views.New, name='New'),
    path('login', views.login, name='login'),
    path('Welcome', views.Welcome, name='Welcome'),
    path('homes', views.homes, name='homes'),
    path('save', views.adddata, name='save'),
    path('loginchk', views.loginchk, name='loginchk'),
    path('error', views.error, name='error'),
    path('prop', views.prop, name='prop'),
    # path('addproperty', views.addproperty, name='addproperty'),
    path('addproperty1', views.addproperty1, name='addproperty1'),

    path('search', views.search, name='search'),
    path('searchr_view', views.searchr_view, name='searchr_view'),
    path('show', views.show, name='show'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('logout', views.logout, name='logout'),
    path('admin', views.admin, name='admin'),
    path('Welcome1', views.Welcome1, name='Welcome1'),
    path('viewuser', views.viewuser, name='viewuser'),
    path('view_properties', views.view_properties, name='view_properties'),
    path('show1', views.show1, name='show1'),
    path('delete1/<int:id>', views.delete1, name='delete1'),
    path('update1/<int:id>', views.update1, name='update1'),
    path('delete2/<int:id>', views.delete2, name='delete2'),
    path('update2/<int:id>', views.update2, name='update2'),
    path('update1/upadpro/<int:id>', views.upadpro, name='upadpro'),
    path('update/upadpr/<int:id>', views.upadpr, name='upadpr'),
    path('update2/upadp/<int:id>', views.upadp, name='upadp'),
    path('Add_st', views.Add_st, name='Add_st'),
    path('Add_state', views.Add_state, name='Add_state'),
    path('view_st', views.view_st, name='view_st'),
    path('view_s', views.view_s, name='view_s'),

    path('delete3/<int:id>', views.delete3, name='delete3'),
    path('update3/<int:id>', views.update3, name='update3'),
    path('update3/up_st/<int:id>', views.up_st, name='up_st'),

    path('manage_user', views.manage_user, name='manage_user'),
    path('delete4/<int:id>', views.delete4, name='delete4'),
    path('update4/<int:id>', views.update4, name='update4'),
    path('update4/upadate_users/<int:id>', views.upadate_users, name='upadate_users'),

    path('logout1', views.logout1, name='logout1'),
    path('Isthome', views.Isthome, name='Isthome'),


    path('showapi', views.showapi, name='showapi'),
    path('showapi1', views.showapi1, name='showapi1'),
    path('showapi2', views.showapi2, name='showapi2'),
    path('showapi3', views.showapi3, name='showapi3'),
    path('showapi4', views.showapi4, name='showapi4'),
    path('showapi5', views.showapi5, name='showapi5'),
    path('loginapi1', views.loginapi1, name='loginapi1'),
    path('addapi', views.addapi, name='addapi'),
    path('deleteapi',views.deleteapi, name="deleteapi"),
    path('updateapi', views.updateapi, name="updateapi"),

    path('search_property', views.search_property, name='search_property'),
    path('searchcus', views.searchcus, name='searchcus'),
    path('Contact/<int:id>', views.Contact, name='Contact'),
    path('Con_save', views.Con_save, name='Con_save'),
    path('Con_mess', views.Con_mess, name='Con_mess'),
    # path('already', views.already, name='already'),
    path('already1', views.already1, name='already1'),

]



