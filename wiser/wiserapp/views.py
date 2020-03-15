from django.shortcuts import render

# Create your views here.

# index
def index(request):
    datas = {

    }
    return render(request, 'index.html', datas)

# blog
def blog(request):
    datas = {

    }
    return render(request, 'blog.html', datas)

# admissions
def admissions(request):
    datas = {

    }
    return render(request, 'Admissions.html', datas)

# contact
def contact(request):
    datas = {

    }
    return render(request, 'contact.html', datas)

# courses
def courses(request):
    datas = {

    }
    return render(request, 'Courses.html', datas)

# elements
def elements(request):
    datas = {

    }
    return render(request, 'elements.html', datas)

# detail
def detail(request):
    datas = {

    }
    return render(request, 'event_details.html', datas)

# event
def event(request):
    datas = {

    }
    return render(request, 'Event.html', datas)

# main
def main(request):
    datas = {

    }
    return render(request, 'main.html', datas)

# single
def single(request):
    datas = {
        
    }
        
    
    return render(request, 'single-blog.html', datas)

# # index
# def panel(request):
#     datas = {

#     }
#     return render(request, 'https://18.223.41.243:3000/ui/panel', datas)
