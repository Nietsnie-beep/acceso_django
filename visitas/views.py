from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse, reverse_lazy
from .models import Visita, Persona, VisitasProgramadas
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, View

from django.db.models import Q
from django.http import HttpResponse

from django.views.generic.edit import FormMixin
from .forms import PersonaPost, PersonaForm, PersonaFormTwo, VisitaFormCarro, VisitaFormExit, VisitaFormPeaton, CommentForm, scheduled_visits, CreatePersonFoto

from .filters import SnippetFilter, SnippetFilterPersona


########### __________scheduled visits_________############
class CreateVisitScheduled(CreateView):
    model = VisitasProgramadas
    template_name = 'visita/createVisitScheduled.html'

    form_class = scheduled_visits
    success_url = reverse_lazy('visitas:index')


class VisitsPicture(ListView):
    model = Visita
    template_name = 'visita/listaImagens.html'
    context_object_name = 'lista'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Estatus='Entro')
        return queryset


def buscar(request):
    query = request.GET.get('q')
    resultados = []
    if query:
        # Buscamos productos que contengan el término de búsqueda en el nombre o la descripción
        resultados = Persona.objects.filter(Q(nombre__icontains=query))
    return render(request, 'visita/buscar.html', {'resultados': resultados, 'query': query})


def buscar_visit_scheduled(request):
    query = request.GET.get('q')
    resultados = []
    if query:
        # Buscamos productos que contengan el término de búsqueda en el nombre o la descripción
        resultados = VisitasProgramadas.objects.filter(
            Q(persona__nombre__icontains=query) | Q(empresa__icontains=query))
    return render(request, 'visita/visita_visit_scheduled.html', {'resultados': resultados, 'query': query})


def primera_vista(request, pk):
    personas = Persona.objects.get(pk=pk)
    print(personas)
    datos = {'id': personas.id}
    request.session['datos'] = datos
    return redirect('/segunda-vista')


def segunda_vista(request):
    datos = request.session.get('datos', {})
    id = datos.get('id', '')
    print(f"initial {id}")

    if request.method == 'POST':
        # procesar el formulario enviado por el usuario
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # guardar el registro del usuario
            form.save()
            # redirigir a una página de confirmación
            return redirect('/')
    else:
        # mostrar el formulario vacío con un valor predefinido para el campo "nombre"
        form = CommentForm(initial={'persona': id})
    return render(request, 'visita/registro.html', {'form': form})
    # hacer algo con los datos
    return HttpResponse("Hola {}".format(id))


def primera_vista_2(request, pk):
    personas = Visita.objects.get(pk=pk)
    print(personas)
    datos = {'id': personas.id}
    request.session['datos'] = datos
    return redirect('/segunda-vista')


def segunda_vista_2(request):
    datos = request.session.get('datos', {})
    id = datos.get('id', '')
    print(f"initial {id}")

    if request.method == 'POST':
        # procesar el formulario enviado por el usuario
        form = CommentForm(request.POST)
        if form.is_valid():
            # guardar el registro del usuario
            form.save()
            # redirigir a una página de confirmación
            return redirect('/')
    else:
        # mostrar el formulario vacío con un valor predefinido para el campo "nombre"
        form = CommentForm(initial={'persona': id})
    return render(request, 'visita/registro.html', {'form': form})
    # hacer algo con los datos
    return HttpResponse("Hola {}".format(id))


def PostDetailView(request, pk):
    post = Persona.objects.get(pk=pk)
    val_pr = 'val_pr'
    print(post.nombre)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('/')
    else:
        form = CommentForm()

    return render(request, 'visita/post_detail.html', {'form': form, "persona": post})

# En la vista donde se redirecciona con el valor


def vista_origen(request):
    valor = 'Hola'
    url_destino = reverse('vista_destino', args=[valor])
    return redirect(url_destino)


def vista_destino(request, valor):
    # hacer algo con el valor recibido
    return HttpResponse('Valor recibido: ' + valor)


def IndexView(request):
    visitas = Visita.objects.all()
    personas = Persona.objects.all()
    # visitas_sch = VisitasProgramadas.objects.all()

    carros = Visita.objects.filter(carro=True)
    carros_true = len(carros)
    visitas_sch = VisitasProgramadas.objects.filter(Estatus='Entro')

    visitas_scheduled_len = len(visitas_sch)
    total_personas = len(personas)
    total = len(visitas)
    return render(request, 'visita/index.html', {'visitas': visitas, "total": total, "total_personas": total_personas, "carro": carros, "carro_true": carros_true, "scheduled": visitas_sch, "visitas_scheduled_len": visitas_scheduled_len})


# Create your views here.
# class IndexView(TemplateView):
#     model = Visita
#     template_name = 'visita/index.html'

class Register(CreateView):
    model = Visita
    template_name = 'visita/create.html'
    fields = ['persona', 'empresa', 'motivo', 'placa', 'fecha', 'empresa']
    # fields = ('__all__')
    success_url = reverse_lazy('visitas:success')


class SuccessView(TemplateView):
    template_name = 'visita/success.html'


class VisitaExit(UpdateView):
    template_name = 'visita/exit.html'
    fields = ['Estatus']
    model = Visita
    success_url = reverse_lazy('visitas:success')


class VisitasList(ListView):
    template_name = 'visita/lista_visitas.html'
    model = Visita
    context_object_name = 'lista'


class VisitasListByKword(ListView):
    template_name = 'visita/search.html'
    context_object_name = "visitas"

    def get_queryset(self):
        print("---------------------")
        palabra_clave = self.request.GET.get("kword", "")
        lista = Visita.objects.filter(
            empresa=palabra_clave
        )
        print("============", palabra_clave)
        return lista


class VisitasListByKwordPerson(ListView):
    template_name = 'visita/searchPerson.html'
    context_object_name = "Personas"

    def get_queryset(self):
        print("---------------------")
        palabra_clave = self.request.GET.get("kword", "")
        lista = Persona.objects.filter(
            nombre=palabra_clave
        )
        print("============", palabra_clave)
        return lista


class VisitasListByKwordVisit(ListView):
    template_name = 'visita/searchVisit.html'
    context_object_name = "Personas"

    def get_queryset(self):
        print("---------------------")
        palabra_clave = self.request.GET.get("kword", "")
        lista = Persona.objects.filter(
            nombre=palabra_clave
        )
        print("============", palabra_clave)
        return lista


class VisitasListByKwordVisitExit(ListView):
    template_name = 'visita/searchVisitExit.html'
    context_object_name = "Visitas"

    def get_queryset(self):
        name = self.kwargs.get('empresa', '')
        object_list = self.model.objects.all()
        if name:
            object_list = object_list.filter(name__icontains=name)
        return object_list


activo = []


class addVisita(UpdateView):

    template_name = 'visita/visitaAdd.html'

    fields = ('__all__')
    model = Visita
    success_url = reverse_lazy('visitas:success')
    # print(activo[0])


class addVisita_peaton(CreateView):

    template_name = 'visita/visitaAddPeaton.html'

    fields = ['persona', 'empresa', 'motivo', 'fecha', 'empresa']
    model = Visita
    success_url = reverse_lazy('visitas:success')
    # print(activo[0])


class RegisterPerson(CreateView):
    model = Persona
    template_name = 'visita/createPerson.html'
    # fields = ['nombre', 'apellido', 'empresa', 'foto_1']
    form_class = CreatePersonFoto
    success_url = reverse_lazy('visitas:index')


class ParticularPost(FormMixin, DetailView):
    template_name = 'visita/createPerson.html'
    model = Persona
    form_class = PersonaPost

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(ParticularPost, self).get_context_data(**kwargs)
        context['form'] = PersonaPost(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(ParticularPost, self).form_valid(form)

# pass id attribute from urls


def detail_view(request, pk):
    personas = Persona.objects.get(pk=pk)
    return render(request, 'visita/detail_view.html', {'personas', personas})

# pass id attribute from urls


def detail_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = Persona.objects.get(pk=pk)

    if request.method == 'POST':
        form = PersonaPost(request.POST)
        if form.is_valid():
            form.save()
    form = PersonaPost()
    return render(request, "visita/detail_view.html",  {'form': form}, )


def create_post(request, pk):
    context = {}

    # add the dictionary during initialization
    context["data"] = Persona.objects.get(pk=pk)

    if request.method == 'POST':
        form = PersonaPost(request.POST)
        if form.is_valid():
            form.save()

    form = PersonaPost()

    return render(request, 'visita/post.html', {'form': form})


#################
def crearPersona(request):
    if request.method == 'POST':
        autor_form = PersonaForm(request.POST)

        if autor_form.is_valid():
            autor_form.save()
            return redirect('/')

    else:
        autor_form = PersonaForm()

    return render(request, 'visita/crear_persona.html', {'autor_form': autor_form})


def listarPersonas(request):
    personas = Persona.objects.all()
    return render(request, 'visita/listaPersonas.html', {'personas': personas})


def editarPersona(request, id):
    error = None
    persona_form = None
    try:
        persona = Persona.objects.get(id=id)
        if request.method == 'GET':
            persona_form = PersonaForm(instance=persona)

        else:
            persona_form = PersonaForm(request.POST, instance=persona)
            persona_form.save()
            if persona_form.is_valid():
                persona_form.save()

            return redirect('/')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'visita/editar_persona.html', {'persona_form': persona_form, 'persona': persona, 'error': error})


def editarPersonaTwo(request, id):
    error = None
    persona_form = None
    try:
        persona = Persona.objects.get(id=id)
        if request.method == 'GET':
            persona_form = PersonaFormTwo(instance=persona)

        else:
            persona_form = PersonaFormTwo(request.POST, instance=persona)
            persona_form.save()
            if persona_form.is_valid():
                persona_form.save()

            return redirect('/')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'visita/editar_persona.html', {'persona_form': persona_form, 'persona': persona, 'error': error})


def crearVisita(request):
    if request.method == 'POST':
        autor_form = VisitaFormCarro(request.POST)

        if autor_form.is_valid():
            autor_form.save()
            return redirect('/')

    else:
        autor_form = VisitaFormCarro()

    return render(request, 'visita/crear_visita.html', {'autor_form': autor_form})


def listarVisitas(request):
    personas = Visita.objects.filter(Estatus='Entro')
    return render(request, 'visita/listaVisitas.html', {'personas': personas})


def editarVisitaExit(request, id):
    initial_data = {
        'Estatus': "Salio"
    }
    error = None
    persona_form = None
    try:
        persona = Visita.objects.get(id=id)
        if request.method == 'GET':
            persona_form = VisitaFormExit(
                initial=initial_data, instance=persona)

        else:
            persona_form = VisitaFormExit(request.POST, instance=persona)
            persona_form.save()
            if persona_form.is_valid():
                persona_form.save()

            return redirect('/')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'visita/editar_visita_exit.html', {'persona_form': persona_form, 'error': error, 'persona': persona})


class SnippetListView(ListView):
    model = Visita
    template_name = 'visita/filtroVisita.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SnippetFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class SnippetDetailView(DetailView):
    model = Visita
    template_name = 'visita/DetalleVisita.html'


class SnippetListViewPersonas(ListView):
    model = Persona
    template_name = 'visita/filtroPersona.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SnippetFilterPersona(
            self.request.GET, queryset=self.get_queryset())
        return context


def crearVisitaPeaton(request):
    if request.method == 'POST':
        autor_form = VisitaFormPeaton(request.POST)

        if autor_form.is_valid():
            autor_form.save()
            return redirect('/')

    else:
        autor_form = VisitaFormPeaton()

    return render(request, 'visita/crear_visita_peaton.html', {'autor_form': autor_form})
