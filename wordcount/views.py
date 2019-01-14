from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')    

def result(request):
    text=request.GET['fulltext']
    words = text.split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1    
    return render(request, 'result.html', {'full':text, 'total':len(words), 'dict':word_dict.items()})
