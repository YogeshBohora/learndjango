from django.http.response import HttpResponse
from django.shortcuts import render

projectsList = [
    {
        'id':'1',
        'title':'Ecommerce Website',
        'description':'Fully functional ecommerce website.'
    },
    {
        'id':'2',
        'title':'Portfolio Website',
        'description':'This was a project where I built out my portfolio.'
    },
    {
        'id':'3',
        'title':'Social Network',
        'description':'Awesome open source project I am still working.'
    },
]
# Create your views here.
def projects(request):
    msg = "This is my project message"
    num = 9
    context = {'message':msg, 'number':num, 'projects':projectsList}
    return render(request, 'projects\projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i 
    return render(request, 'projects\single_project.html', {'project':projectObj})   