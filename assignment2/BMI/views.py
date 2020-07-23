from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'index.html')
def BMI(request):
     height = float(request.GET['Height'])
     weight = float(request.GET['Weight'])

     bmi1 = weight/(height**2)
     bmi = float("{:.2f}".format(bmi1))
     if bmi<18.5:
         temp = 'Underweight'
     elif bmi>18.5 and bmi<24.9:
         temp= 'Normal Weight'
     elif bmi>24.9 and bmi<29.9:
         temp = 'Over weight'
     elif bmi> 29.9:
         temp= "Obesity"

     return render(request, 'ans.html', {'bmi': bmi,'temp':temp})

"""def ans(request,bmi):
    bmi = bmi

    return render(request,'ans.html',{'bmi':bmi})"""