from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import ContactMessage
from .models import Proyecto
from django.core.paginator import Paginator
from django.contrib import messages

def home(request):
    
    lista_proyecto = Proyecto.objects.all().order_by('prioridad')
    
    paginator = Paginator(lista_proyecto, 3)
    pagina = request.GET.get('page') or 1
    lista_proyecto = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, lista_proyecto.paginator.num_pages + 1)
    context = {
        'lista_proyecto': lista_proyecto,
        'paginas': paginas, 
        'pagina_actual': pagina_actual
        }
    
    return render(request, 'home.html', context)

def contact_form(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        contact_name = request.POST['contactName']
        contact_email = request.POST['contactEmail']
        contact_subject = request.POST['contactSubject']
        contact_message = request.POST['contactMessage']

        # Validar que los campos requeridos no estén vacíos
        if not contact_name or not contact_email or not contact_message:
            messages.error(request, "Por favor, completa todos los campos requeridos.")
            return redirect('home')  # Redirigir a la página principal o donde desees

        # Guardar el mensaje en la base de datos
        ContactMessage.objects.create(
            contact_name=contact_name,
            contact_email=contact_email,
            contact_subject=contact_subject,
            contact_message=contact_message
        )

        # Enviar correo electrónico
        subject = f'Nuevo mensaje de {contact_name}: {contact_subject}'
        message = f'Nombre: {contact_name}\nEmail: {contact_email}\n\nMensaje:\n{contact_message}'
        sender_email = 'sistemamatricula007@gmail.com'  # Dirección de correo desde la que enviar el mensaje
        recipient_email = 'ksucapuca007@gmail.com'  # Dirección de correo que recibirá el mensaje

        send_mail(subject, message, sender_email, [recipient_email])

        messages.success(request, "Mensaje Enviado Correctamente")
        return redirect('home')  # Redirigir a la página principal o donde desees

    return render(request, 'home.html')