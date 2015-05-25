from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from main.views.views import ContentList, ContentDetail, CategoryTypeList, CategoryTypeDetail, CategoryList, CategoryDetail, SubcategoryList, SubcategoryDetail, ContentCategoryList, ContentCategoryDetail, ContentSubcategoryList, ContentSubcategoryDetail
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = patterns('',
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^tabletable/', 'main.views.views.table'),
                        url(r'^$', 'main.views.views.home', name='home'),
                        url(r'^contentform/', 'main.views.views.content_manager'),
                        url(r'^categoryform/', 'main.views.views.category_manager'),
                        url(r'^categorytypeform/', 'main.views.views.category_type_manager'),
                        url(r'^contentcategoryform/', 'main.views.views.content_category_manager'),
                        url(r'^contentsubcategoryform/', 'main.views.views.content_subcategory_manager'),
                        url(r'^subcategoryform/', 'main.views.views.subcategory_manager'),
                        url(r'^data/contents/$', ContentList.as_view()),
                        url(r'^data/contents/(?P<pk>[0-9]+)/$', ContentDetail.as_view()),
                        url(r'^data/categorytypes/$', CategoryTypeList.as_view()),
                        url(r'^data/categorytypes/(?P<pk>[0-9]+)/$', CategoryTypeDetail.as_view()),
                        url(r'^data/categories/$', CategoryList.as_view()),
                        url(r'^data/categories/(?P<pk>[0-9]+)/$', CategoryDetail.as_view()),
                        url(r'^data/subcategories/$', SubcategoryList.as_view()),
                        url(r'^data/subcategories/(?P<pk>[0-9]+)/$', SubcategoryDetail.as_view()),
                        url(r'^data/contentcategories/$', ContentCategoryList.as_view()),
                        url(r'^data/contentcategories/(?P<pk>[0-9]+)/$', ContentCategoryDetail.as_view()),
                        url(r'^data/contentsubcategories/$', ContentSubcategoryList.as_view()),
                        url(r'^data/contentsubcategories/(?P<pk>[0-9]+)/$', ContentSubcategoryDetail.as_view()),
                        url(r'^content/(?P<id>\d+)/$',
                            'main.views.views.content_details'),
                        url(r'^(?P<category_slug>[\w-]+)/$',
                            'main.views.views.category_details'),
                        url(r'^(?P<category_slug>[\w-]+)/(?P<subcategory_slug>[\w-]+)/$',
                            'main.views.views.subcategory_details'),
                        )