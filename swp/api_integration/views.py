from django.shortcuts import render, redirect
import json
import requests
from django.contrib.auth import login, logout, authenticate
from django.template import loader, Context
from django.contrib.auth.models import User
from .models import Student
import datetime

def authenticate_api(token):
    url = "https://serene-wildwood-35121.herokuapp.com/oauth/getDetails"
    Payload = {'token' : token,'secret' : "8190d9225074e3a366ad244769c1aed43a72746f61ed0912c89d8311d15f0f4e495635b7f3dc1a6c0e48747297d76e1c82b930b79704e0b3d365577aaf033208"}
    k = requests.post(url,Payload)
    details = json.loads(k.content)
    return details

def callback(request,token):
    info = authenticate_api(token)
    student_data = info['student']

    s_id = student_data[0]['Id']
    student_id = student_data[0]['Student_ID']
    student_first_name = student_data[0]['Student_First_Name']
    student_middle_name = student_data[0]['Student_Middle_Name']
    student_last_name = student_data[0]['Student_Last_name']
    student_dob = student_data[0]['Student_DOB']
    student_gender = student_data[0]['Student_Gender']
    student_email = student_data[0]['Student_Email']
    student_mobile = student_data[0]['Student_Mobile']
    student_blood_group = student_data[0]['Student_Blood_Group']
    student_mother_tongue = student_data[0]['Student_Mother_Tongue']
    # student_registered_year = student_data[0]['Student_Registered_Year']
    student_registered_degree = student_data[0]['Student_Registered_Degree']
    student_registered_degree_duration = student_data[0]['Student_Registered_Degree_Duration']
    student_cur_yearofstudy = student_data[0]['Student_Cur_YearofStudy']
    student_cur_sem = student_data[0]['Student_Cur_Sem']
    student_academic_status = student_data[0]['Student_Academic_Status']
    rand_password = "Toor@123"

    try:
        user = User.objects.get(username = student_first_name)
    except User.DoesNotExist:
        user = None
    if user is None:
        user = User.objects.create(username = student_first_name, password = rand_password)
        user.set_password(rand_password)
        user.save()
        Student.objects.create(user = user, s_id = s_id, roll = student_id,
        student_first_name = student_first_name, student_middle_name = student_middle_name,
        student_last_name = student_last_name, student_dob = student_dob, student_gender = student_gender,
        student_mobile = student_mobile, student_email = student_email, student_blood_group = student_blood_group,
        student_mother_tongue = student_mother_tongue,
        student_registered_degree = student_registered_degree,
        student_registered_degree_duration = student_registered_degree_duration,
        student_cur_yearofstudy = student_cur_yearofstudy, student_cur_sem = student_cur_sem,
        student_academic_status = student_academic_status, created_at=datetime.datetime.now().date(),
        created_by = student_first_name, modified_at = datetime.datetime.now().date(),
        modified_by = student_first_name)
    else:
        user = authenticate(request, username = student_first_name, password = rand_password)
        if user is not None:
            login(request, user)
            student = Student.objects.get(user = request.user)
            if student.is_hostel_admin:
                return redirect('hostel_admin:hostel_admin_index')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('/dashboard/')
        else:
            return render(request, 'api_integration/invalid.html')

    # else:
    #     return redirect('/home/')
    # is_blacklisted = student_data[0]['is_blacklisted']
    # student_image = student_data[0]['Student_Image']
    # is_alumini = student_data[0]['is_Alumini']
    # print('end')
    # print(student_image)
    # return render(request, 'api_integration/api_student_details.html', {
    # 'student_data': student_data
    # })
