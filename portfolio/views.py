from django.shortcuts import render, redirect


def index(request):
    return render(request, "portfolio/index.html")

def projects(request, id):
    try:
        return render(request, "portfolio/projects.html", {
            "id":id,
        })
    except:
        return redirect('index')
    
def categories(request, cat):
    cats = ["DataScience", "DeepLearning", "WebDevelopment", "GenerativeAI"]
    try:
        if cat in cats: 
            return render(request, "portfolio/categories.html", {
                "cat":cat,
            })
        else:
            return redirect('index')
    except:
        return redirect('index')
