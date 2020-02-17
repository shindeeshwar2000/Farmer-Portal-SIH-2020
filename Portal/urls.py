"""cpanel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home),
    path('postsign/' , views.postsign),
    path('logout/' , views.logout,name="log"),
    path('signup/' , views.signup,name="signup"),
    path('post_sign_up/' , views.post_sign_up,name="post_sign_up"),
    # path('create/' , views.create,name="create"),
    path('display/' , views.display,name="display"),
    path('post_create/' , views.post_create,name="post_create"),
    path('check/' , views.create,name="check"),
    path('upload_form/' , views.upload_form,name="upload_form"),
    # path('test/' , views.home,name="twilio_test"),
    path('category/' , views.category,name="category"),
    path('login/' , views.login,name="login"),
    path('checkout/' , views.checkout,name="checkout"),
    path('login-by-phone/' , views.login_by_phone,name="login-by-phone"),
    path('login-by-OTP/' , views.login_by_OTP,name="login-by-OTP"),
    path('link_myprod/' , views.link_myprod,name="link_myprod"),
    # path('product-list/<Name>' , views.product_list,name="product_list"),
    # url(r'^product-list/(?P<Name>)/$', views.product_list, name='product_list'),

    
    path('product-list/<Name>/' , views.product_list,name="product_list"),
    path('buyer-details/<str:buyer_number>/' , views.buyer_details,name="buyer_details"),
    path('accpet-order/<str:buyer_number>/' , views.accpet_order,name="accpet_order"),
    path('add_to_cart/<str:add_to_cart>/' , views.add_to_cart,name="add_to_cart"),
    
    # path('add_to_cart/<str:buyer_number>' , views.add_to_cart,name="add_to_cart"),
    url(r'^Post-OTP/(?P<OTP>\w)/$', views.post_otp,name="post_otp"),
    # url(r'^buyer-details/(?P<buyer_number>\w)/$', views.buyer_details,name="buyer_details"),

    path('Fruits/' , views.Fruits,name="Fruits"),
    path('Register/' , views.Register,name="Register"),
    path('Post-Register/' , views.Post_Register,name="Post_Register"),
    path('Post-form/' , views.post_form,name="post_form"),

    # url(r'^panel/person/(?P<person_id>/)$', 'apps.panel.views.person_form', name='panel_person_form'),

]
