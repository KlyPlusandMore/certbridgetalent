from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib import messages
from .forms import RegistrationForm
from .models import Course

class HomeView(TemplateView):
    template_name = 'pages/home.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class ContactView(TemplateView):
    template_name = 'pages/contact.html'

class TrainingsView(TemplateView):
    template_name = 'pages/trainings.html'

class RegisterView(View):
    template_name = 'pages/register.html'

    def get(self, request, course_id=None):
        initial = {}
        if course_id:
            try:
                initial['course'] = Course.objects.get(id=course_id, is_active=True)
            except Course.DoesNotExist:
                pass
        
        form = RegistrationForm(initial=initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save()
            messages.success(request, f"Thank you, {registration.full_name}! Your registration for {registration.course.title} has been received.")
            return redirect('pages:register_success')
        
        return render(request, self.template_name, {'form': form})

class RegisterSuccessView(TemplateView):
    template_name = 'pages/register_success.html'
