from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

types = [('Xray','Xray')]
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    doctorId = models.IntegerField()
    clinicname = models.CharField(max_length = 30)
    specialization = models.CharField(max_length = 30,choices = departments)


    #profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)

    #status=models.BooleanField(default=False)

    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)




class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    patientId= models.IntegerField()
    patientStatus = models.BooleanField(default=True)
    patientOverduePay = models.IntegerField()


    #profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)

    #assignedDoctorId = models.PositiveIntegerField(null=True)


    @property
    def get_id(self):
        return self.user.id

class Receptionist(models.Model):
    receptionistid = models.IntegerField()
    clinicname = models.CharField(max_length = 20)
    jobstatus = models.CharField(max_length = 1)


class Appointment(models.Model):
    appointmentId = models.IntegerField()
    patientId=models.ForeignKey(Patient, on_delete=models.CASCADE )
    doctorId=models.ForeignKey(Doctor, on_delete=models.CASCADE )
    receptionistid = models.ForeignKey(Receptionist, on_delete=models.CASCADE )
    date = models.DateTimeField()
    timing=models.DateTimeField()
    isCancelled=models.BooleanField(default=False)
    #appointmentDate=models.DateField(auto_now=True)
    #description=models.TextField(max_length=500)
    #status=models.BooleanField(default=False)






#Developed By : sumit kumar
#facebook : fb.com/sumit.luv
#Youtube :youtube.com/lazycoders

# Receptionist - Done
# user - Done
# phone number - Done
# doctor
# patient
# records - Done
# description - Done
# attends to - Done
# symptoms - Done
# medical tests - Done
# prescription  - done
# medicines prescribed - done
# Appointment
# prescribed_in- Done



class Prescription(models.Model):
    prescriptionid = models.AutoField(primary_key=True)

class MedicinesPrescribed(models.Model):
    prescriptionid = models.ForeignKey(Prescription, on_delete=models.CASCADE )
    mdosage = models.IntegerField()
    mduration = models.CharField(max_length =20)
    mname = models.CharField(max_length= 20)

class MedicalTest(models.Model):
    prescriptionid = models.ForeignKey(Prescription, on_delete=models.CASCADE )
    medicaltest = models.CharField(max_length = 20)

class Symptoms(models.Model):
    prescriptionid = models.ForeignKey(Prescription, on_delete=models.CASCADE )
    symptoms = models.CharField(max_length = 20)

class Records(models.Model):
    # pid = models.ForeignKey(Patient, on_delete = models.CASCADE )
    rid = models.AutoField(primary_key=True)

class Description(models.Model):
    type = models.CharField(max_length=50,choices=types,default='Xray')
    title = models.CharField(max_length = 30)
    recimage= models.ImageField(upload_to='recordimages/',null=True,blank=True)
    # pid = models.ForeignKey(Patient, on_delete = models.CASCADE )
    rid = models.ForeignKey(Records,on_delete = models.CASCADE)

# class AttendsTO(models.Model):
    # pid = models.ForeignKey(Patient, on_delete = models.CASCADE )
    # did = models.ForeignKey(Doctor, on_delete = models.CASCADE )

# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     Fname = models.CharField(max_length=30, blank=True)
#     Lname = models.CharField(max_length=30, blank=True)
#     Mname = models.CharField(max_length=30, blank=True)
#     sex = models.CharField(max_length=1, blank=True)
#     age = models.IntegerField()
#     Bname = models.CharField(max_length=30, blank=True)
#     Sname = models.CharField(max_length=30, blank=True)
#     city = models.CharField(max_length=30, blank=True)
#     pincode= models.IntegerField()

class Profile(models.Model):
    sex = models.CharField(max_length=1, blank=True)
    age = models.IntegerField()
    Bname = models.CharField(max_length=30, blank=True)
    Sname = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    pincode= models.IntegerField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class PhoneNumber(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.IntegerField()

class PrescribedIn(models.Model):
    prescriptionid = models.ForeignKey(Prescription, on_delete=models.CASCADE )
    fees = models.IntegerField()
    aid = models.ForeignKey(Appointment,on_delete=models.CASCADE)
