from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.auth.decorators import login_required

from .app_settings import INVITE_ONLY
from .views import InvitationView, RegistrationView


login_required_direct_to_template = login_required(TemplateView.as_view())


urlpatterns = patterns('',
    url(r'^invitation/$', login_required_direct_to_template,
        {'template': 'invitation/invitation_home.html'},
        name='invitation_home'),
    url(r'^invitation/invite/$', InvitationView.as_view(),
        name='invitation_invite'),
    url(r'^invitation/invite/complete/$', login_required_direct_to_template,
        {'template': 'invitation/invitation_complete.html'},
        name='invitation_complete'),
    url(r'^invitation/invite/unavailable/$', login_required_direct_to_template,
        {'template': 'invitation/invitation_unavailable.html'},
        name='invitation_unavailable'),
    url(r'^invitation/accept/complete/$', TemplateView.as_view(),
        {'template': 'invitation/invitation_registered.html'},
        name='invitation_registered'),
    url(r'^invitation/accept/(?P<invitation_key>\w+)/$',
        RegistrationView.as_view(), name='invitation_register'),
)


if INVITE_ONLY:
    urlpatterns += patterns('',
        url(r'^register/$', RedirectView.as_view(),
            {'url': '../invitation/invite_only/', 'permanent': False},
            name='registration_register'),
        url(r'^invitation/invite_only/$', TemplateView.as_view(),
            {'template': 'invitation/invite_only.html'},
            name='invitation_invite_only'),
    )
