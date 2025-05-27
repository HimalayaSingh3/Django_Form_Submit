from django.shortcuts import render, redirect
from .models import FormDetails

def base(request):
    return render(request, 'form.html')



def form_view(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        country = request.POST.get('country')
        experience = request.POST.get('experience')
        skills = request.POST.get('skills')
        education = request.POST.get('education')
        message = request.POST.get('message')

        FormDetails.objects.create(
            form_name=name,
            form_gender=gender.capitalize(),
            form_age=age,
            form_email=email,
            form_phone=phone,
            form_address=address,
            form_city=city,
            form_state=state,
            form_zip_code=pincode,
            form_country=country,
            form_experience=experience,
            form_skills=skills,
            form_education=education,
            form_message=message
        )

        return redirect('success')

    return render(request, 'form.html')

def success_view(request):
    return render(request, 'success.html')



