from django.conf import settings
from django.urls import path, include
from .views import IndexView, Register, SuccessView, VisitaExit, VisitasList, VisitasListByKword, VisitasListByKwordPerson, addVisita, RegisterPerson, VisitasListByKwordVisit, addVisita_peaton, detail_view, create_post, ParticularPost, VisitasListByKwordVisitExit, crearPersona, listarPersonas, editarPersona, editarPersonaTwo, crearVisita, listarVisitas, editarVisitaExit, SnippetListView, crearVisitaPeaton, SnippetListViewPersonas, PostDetailView, primera_vista, segunda_vista, buscar, CreateVisitScheduled, buscar_visit_scheduled, VisitsPicture
from django.conf.urls.static import static


app_name = 'visitas'

urlpatterns = [
    path('', IndexView, name='index'),
    path('buscar/', buscar, name='buscar'),
    path('buscar_sche/', buscar_visit_scheduled, name='buscar_sche'),
    path('lista_fotos/', VisitsPicture.as_view(), name='lista_fotos'),


    path('primera-vista/<pk>', primera_vista, name='primera-vista'),
    path('segunda-vista/', segunda_vista, name='segunda_vista'),

    path('add-visita/', Register.as_view(), name='registro'),

    path('success/', SuccessView.as_view(), name='success'),

    path('salida/<pk>/', VisitaExit.as_view(), name='visita_salida'),

    path('historial-visitas/', VisitasList.as_view(), name='visita_historial'),

    path('buscar-visitas/', VisitasListByKword.as_view(), name='visita_buscar'),

    path('buscar-personas/', VisitasListByKwordPerson.as_view(),
         name='Persona_buscar'),

    path('buscar-personas_salida/',
         VisitasListByKwordVisitExit.as_view(), name='personas_salida'),

    path('buscar-visitas_kword/',
         VisitasListByKwordVisit.as_view(), name='Persona_buscar'),

    path('add-person/', RegisterPerson.as_view(), name='registro_persona'),

    path('person_details/<pk>', RegisterPerson.as_view(), name='registro_persona'),

    path('add-visita_person/', addVisita_peaton.as_view(), name='registro_persona'),


    path('personas_detail/<pk>', ParticularPost.as_view(), name='personas_detail'),

    path('model1/<pk>', PostDetailView, name='personas_detail'),


    path('personas_create/<pk>', create_post, name='personas_create'),
    ##########################################################
    path('crear_persona/', crearPersona, name='crear_persona_admin'),


    path('personas_list/', listarPersonas, name='personas_list'),
    path('persona_edit/<int:id>', editarPersona, name='persona_edit'),

    # pagina para betar
    path('persona_edit_ /<int:id>', editarPersonaTwo, name='persona_edit'),

    # crear visita
    path('crear_visita/', crearVisita, name='persona_edit'),
    path('VisitaFormPeaton-peaton/', crearVisitaPeaton, name='persona_edit'),

    # visitantas activas_salida
    path('visitas_list/', listarVisitas, name='vistas_list'),
    path('visita_exit/<int:id>', editarVisitaExit, name='visita_exit'),

    # Historial de visitas
    path('visitas_filtro/', SnippetListView.as_view(), name='visitas_filtro'),

    # historial de personas
    path('visitas_filtro_person/',
         SnippetListViewPersonas.as_view(), name='visitas_filtro'),


    ########### __________scheduled visits_________############
    path('create_visit_scheduled/',
         CreateVisitScheduled.as_view(), name='visitas_filtro'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
