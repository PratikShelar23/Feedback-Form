from django.conf.urls import url
from apps.api.views import * 

urlpatterns = [
    url(r'^feedback/$', FeedbackCRUD.as_view(), name="Feedback CRUD"),
    url(r'^getfeedback/$', getFeedback.as_view(), name="get Feedback"),
    url(r'^agentlist/$', AgentMasterList.as_view(), name=" Agent Master List"),
    url(r'^getagentlist/$', GetAgentMasterList.as_view(), name="Get Agent Master List"),
    url(r'^productlist/$', ProductMasterList.as_view(), name=" Product Master List"),
    url(r'^getproductlist/$', GetProductMasterList.as_view(), name="Get Product Master List"),
]
