from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def payment(request):
    if request.method == 'POST':
        amount=int(request.POST.get('amount'))
        print(amount)
        # print(type(amount))
        return render(request,'index.html')
    
    