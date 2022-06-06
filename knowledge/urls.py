from django.urls import path

from knowledge.views import createSkill, deleteSkill, editeSkill, list_knowledge, get_knowledge, contact


urlpatterns = [
    path('liste', list_knowledge, name="skill-list" ),
    path('get<int:id>', get_knowledge, name="show"),
    path('contact', contact, name="contact" ),
    path('create', createSkill, name="create" ),
    path('<int:id>edite', editeSkill, name= "edite" ),
    path('<int:id>delete', deleteSkill, name= "delete" ),




  

]