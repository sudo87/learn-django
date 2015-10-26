from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from .views import home, home_files

urlpatterns = [
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$', 
        home_files, name='home-files'),
    url(r'i18n/', include('django.conf.urls.i18n')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
]

urlpatterns += i18n_patterns(
    # Examples:
    # url(r'^$', 'taskbuster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    
)
