from django.db import models
from django.contrib.auth.models import User
import datetime
# s_id = student_data[0]['Id']
# student_id = student_data[0]['Student_ID']
# student_first_name = student_data[0]['Student_First_Name']
# student_middle_name = student_data[0]['Student_Middle_Name']
# student_last_name = student_data[0]['Student_Last_name']
# student_dob = student_data[0]['Student_DOB']
# student_gender = student_data[0]['Student_Gender']
# student_email = student_data[0]['Student_Email']
# student_mobile = student_data[0]['Student_Mobile']
# student_blood_group = student_data[0]['Student_Blood_Group']
# student_mother_tongue = student_data[0]['Student_Mother_Tongue']
# student_registered_year = student_data[0]['Student_Registered_Year']
# student_registered_degree = student_data[0]['Student_Registered_Degree']
# student_registered_degree_duration = student_data[0]['Student_Registered_Degree_Duration']
# student_cur_yearofstudy = student_data[0]['Student_Cur_YearofStudy']
# student_cur_sem = student_data[0]['Student_Cur_Sem']
# student_academic_status = student_data[0]['Student_Academic_Status']

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    s_id = models.CharField(max_length = 1000)
    roll = models.CharField(max_length = 11)
    student_first_name = models.CharField(max_length = 50)
    student_middle_name = models.CharField(max_length = 50)
    student_last_name = models.CharField(max_length = 50)
    student_dob = models.DateTimeField()
    student_gender = models.CharField(max_length = 5)
    student_email = models.EmailField()
    student_mobile = models.CharField(max_length = 14)
    student_blood_group = models.CharField(max_length = 3)
    student_mother_tongue = models.CharField(max_length = 50)
    student_registered_year = models.DateField(default = datetime.date.today)
    student_registered_degree = models.CharField(max_length = 50)
    student_registered_degree_duration = models.CharField(max_length = 1)
    student_cur_yearofstudy = models.CharField(max_length = 1)
    student_cur_sem = models.CharField(max_length = 1)
    student_academic_status = models.CharField(max_length = 20)
    bio = models.CharField(max_length=100, blank=True, null=True)
    is_hostel_admin = models.BooleanField(default=False)
    is_mess_admin = models.BooleanField(default=False)
    is_medical_admin = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="images/", default="images/default.png")
    timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return(str(self.student_first_name))
