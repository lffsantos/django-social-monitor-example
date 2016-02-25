# -*- coding: utf-8 -*-
from accounts.views import register_confirm_email, register, login, \
    forgot_password, forgot_password_confirm, social_account_list, \
    social_account_delete, connect_twitter, connect_twitter_callback
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from staticpages.views import index, about
from dashboard.views import index as dashboard_index, search_list, search_new, \
    search_edit, search_delete, item_list, item_delete


admin.autodiscover()


urlpatterns = [
    # admin app
    url(r'^admin/', include(admin.site.urls)),

    # staticpages app
    url(r'^$', index, name='staticpages_index'),
    url(r'^about/$', about, name='staticpages_about'),

    # accounts app
    url(r'^signup/$', register_confirm_email,
        name='accounts_register_confirm_email'),
    url(r'^signup/(?P<token>[\w:-]+)/$', register,
        name='accounts_register'),
    url(r'^login/$', login, name='accounts_login'),
    url(r'^logout/$', logout,
        {'next_page': '/',}, name='accounts_logout'),
    url(r'^forgot-password/$', forgot_password,
        name='accounts_forgot_password'),
    url(r'^forgot-password/(?P<token>[\w:-]+)/$', forgot_password_confirm,
        name='accounts_forgot_password_confirm'),
    url(r'^account/social/$', social_account_list,
        name='accounts_social_account_list'),
    url(r'^account/social/(?P<pk>[0-9]+)/delete/$', social_account_delete,
        name='accounts_social_account_delete'),
    url(r'^account/connect/twitter/$', connect_twitter,
        name='accounts_connect_twitter'),
    url(r'^account/connect/twitter/callback/$', connect_twitter_callback,
        name='accounts_connect_twitter_callback'),

    # dashboard app
    url(r'^dashboard/$', dashboard_index, name='dashboard_index'),
    url(r'^dashboard/searchs/$', search_list,
        name='dashboard_search_list'),
    url(r'^dashboard/searchs/new/$', search_new,
        name='dashboard_search_new'),
    url(r'^dashboard/searchs/(?P<pk>[0-9]+)/edit/$', search_edit,
        name='dashboard_search_edit'),
    url(r'^dashboard/searchs/(?P<pk>[0-9]+)/delete/$', search_delete,
        name='dashboard_search_delete'),
    url(r'^dashboard/items/$', item_list,
        name='dashboard_item_list'),
    url(r'^dashboard/items/(?P<pk>[0-9]+)/delete/$', item_delete,
        name='dashboard_item_delete'),
]


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )


urlpatterns += staticfiles_urlpatterns()
