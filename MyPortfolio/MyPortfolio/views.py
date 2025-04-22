from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html', {'active_section': 'home'})

def aboutpage(request):
    return render(request, 'about.html', {'active_section': 'about'})

def educationpage(request):
    return render(request, 'education.html', {'active_section': 'education'})

def skillspage(request):
    return render(request, 'skills.html', {'active_section': 'skills'})

def contactpage(request):
    return render(request, 'contact.html', {'active_section': 'contact'})
