from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == "post":
        contact_form = contact_form(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            
            #Enviamos el correo y redireccionamos

            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email,content),
                "no-contestar@inbox.mailtrap.io",
                ["latiprogramacion@gmail.com"],
                reply_to=[email])
            
            try:
                email.send()
                #Suponemos que todo ha ido bien
                return redirect(reverse('contact')+"?ok")
            
            except:
                #Suponemos que algo ha salido mal
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html",{'form': contact_form})
