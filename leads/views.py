from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import LeadForm

def home(request):
    return render(request, 'leads/home.html')

def cotizar(request):
    if request.method == 'POST':
        form = LeadForm(request.POST, request.FILES)
        if form.is_valid():
            lead = form.save()
            
            # Enviar correo al dueño
            subject = f'Nueva cotización de {lead.nombre}'
            message = f"""
            Nuevo lead de Roof Repair:
            
            Nombre: {lead.nombre}
            Teléfono: {lead.telefono}
            Email: {lead.email}
            Dirección: {lead.direccion}
            Mensaje: {lead.mensaje}
            """
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['urameshikosaku@gmail.com'],  
                fail_silently=False,
            )
            
            messages.success(request, '¡Cotización enviada con éxito! Te contactaremos pronto.')
            return redirect('cotizar')
    else:
        form = LeadForm()
    
    return render(request, 'leads/cotizar.html', {'form': form})