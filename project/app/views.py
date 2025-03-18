from django.shortcuts import render
import razorpay

def index(request):
    return render(request,'index.html')


def payment(request):
    if request.method == 'POST':
        amount=int(request.POST.get('amount'))
        # print(amount)
        # print(type(amount))
        client = razorpay.Client(auth=("YOUR_ID", "YOUR_SECRET"))

        data = { "amount": amount*100, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data) #Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
        print(payment)
    
    