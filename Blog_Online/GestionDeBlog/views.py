from django.shortcuts import render, redirect
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .models import Categoria, Usuario, Post
from .forms import CustomUserCreationForm, CustomUserCreationForm2

# Create your views here.

def home(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True)
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'index.html', {'post':post})

def generales(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Generales'))
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True, 
            categoria = Categoria.objects.get(nombre__iexact = 'Generales')
        ).distinct()
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'generales.html', {'post':post})

def programacion(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Programacion'))
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True, 
            categoria = Categoria.objects.get(nombre__iexact = 'Programacion')
        ).distinct()
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'programacion.html', {'post':post})

def videojuegos(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Videojuegos'))
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True, 
            categoria = Categoria.objects.get(nombre__iexact = 'Videojuegos')
        ).distinct()
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'videojuegos.html', {'post':post})

def tecnologia(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia'))
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True, 
            categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia')
        ).distinct()
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'tecnologia.html', {'post':post})

def tutoriales(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales'))
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True, 
            categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales')
        ).distinct()
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'tutoriales.html', {'post':post})

def detallepost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'detallepost':post})

def exit(request):
    logout(request)
    return redirect('inicio')

def categorias(request):
    categoriaslistadas = Categoria.objects.all()
    return render(request, 'categorias.html', {"categoriaslistadas" : categoriaslistadas})

def registrarcategoria(request):

    nombre=request.POST['txtNombre']
    estado=True

    categoria = Categoria.objects.create(nombre=nombre, estado=estado)

    messages.success(request, 'Se ha registrado una categoria')

    return redirect('categorias')

def edicioncategoria(request, id):

    categoria = Categoria.objects.get(id=id)

    return render(request, 'edicionCategorias.html', {"categoria":categoria})

def editarcategoria(request):

    id = request.POST['numberid']
    nombre=request.POST['txtNombre']
    estado=request.POST['estado']

    categoria = Categoria.objects.get(id=id)
    categoria.nombre = nombre
    categoria.estado = estado

    categoria.save()

    messages.success(request, 'Se ha editado con exito la categoria seleccionada')

    return redirect('categorias')

def eliminarcategoria(request, id):
    
    categoria = Categoria.objects.get(id=id)

    categoria.delete()

    messages.success(request, 'Se ha eliminado la categoria seleccionada')

    return redirect('categorias')

def usuarios(request):
    usuarioslistados = Usuario.objects.all()
    return render(request, 'usuarios.html', {"usuarioslistados" : usuarioslistados})

def registrarusuario(request):
    data = {
        'form' : CustomUserCreationForm2()
    }
    if request.method == 'POST':
        user_creation_form_2 = CustomUserCreationForm2(data=request.POST)
        if user_creation_form_2.is_valid():
            user_creation_form_2.save()
    return render(request, 'registrarUsuario.html', data)

def edicionusuario(request, username):

    usuario = Usuario.objects.get(username=username)

    return render(request, 'edicionUsuarios.html', {"usuario":usuario})

def editarusuario(request):

    username = request.POST['username']
    first_name = request.POST['txtNombres']
    last_name = request.POST['txtApellidos']
    email = request.POST['email']

    usuario = Usuario.objects.get(username=username)
    usuario.first_name = first_name
    usuario.last_name = last_name
    usuario.email = email

    usuario.save()

    messages.success(request, 'Se ha editado con exito el usuario seleccionado')

    return redirect('usuarios')

def eliminarusuario(request, username):
    
    usuario = Usuario.objects.get(username=username)

    usuario.delete()

    messages.success(request, 'Se ha eliminado el usuario seleccionado')

    return redirect('usuarios')

def posts(request):
    postslistados = Post.objects.all()
    categoriaslistadas = Categoria.objects.all()
    return render(request, 'posts.html', {"postslistados" : postslistados, "categoriaslistadas" : categoriaslistadas})

def registrarpost(request):

    nombre=request.POST['txtNombre']
    estado=True

    categoria = Categoria.objects.create(nombre=nombre, estado=estado)

    messages.success(request, 'Se ha registrado una categoria')

    return redirect('categorias')

def edicionpost(request, id):

    post = Post.objects.get(id=id)

    return render(request, 'edicionPost.html', {"post":post})

def editarpost(request):

    id = request.POST['numberid']
    titulo = request.POST['txtTitulo']
    slug = request.POST['txtSlug']
    descripcion = request.POST['txtDescripcion']
    contenido = request.POST['txtContenido']
    imagen = request.POST['txtImagen']

    post = Post.objects.get(id=id)
    post.titulo = titulo
    post.slug = slug
    post.descripcion = descripcion
    post.contenido = contenido
    post.imagen = imagen

    post.save()

    messages.success(request, 'Se ha editado con exito el post seleccionado')

    return redirect('posts')

def eliminarpost(request, id):
    
    post = Post.objects.get(id=id)

    post.delete()

    messages.success(request, 'Se ha eliminado el post seleccionado')

    return redirect('posts')

def register(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('inicio')
    return render(request, 'registration/register.html', data)