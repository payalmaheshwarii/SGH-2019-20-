from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='self'),
    path('SignUp.html', views.signUp, name='SignUp'),
    path('SignIn.html', views.signIn, name='info'),
    path(r'postsign/',views.postsign),
    path(r'postsignup/',views.postsignup),
    path(r'logout/',views.logout, name="log"),
    path(r'get_patient_name/',views.get_patient_name, name="patientinfo"),
    path(r'doctordetails.html/',views.doctorprofile, name="doctorprofile"),
    path(r'postsign/personaldetails.html/', views.personaldet, name='info'),
    path(r'postsign/emergency_information.html/', views.emergency, name='info'),
    path(r'postsign/insuranceform.html/', views.insurance, name='info'),
    path(r'postsign/medical_history.html/', views.medicalhistory, name='info'),
    path(r'postsign/prescription_form.html/', views.prescription, name='info'),
    path(r'vitals.html/', views.vitals, name='info'),
    path(r'submitemergencyinfo/', views.emegencydata, name='info'),
    path(r'submitinsurance/', views.addinsurance, name='info'),
    path(r'submitvitals/', views.addvitals, name='info'),
    path(r'submitmedicaldetails/', views.medicaldetails, name='info'),
    path(r'submitdoctordetails/', views.adddoctordetails, name='info'),
    path(r'submitpersonaldata/', views.personaldetsub, name='info'),
    path(r'submitprescription/', views.addprescription, name='info'),
    path(r'viewvitals.html/', views.viewvitals, name='info'),
    path(r'postsign/viewprofile.html/', views.viewprofiledetails, name='info'),
    path(r'postsign/viewmedical.html/', views.viewmedical, name='info'),
    path(r'get_patient_name/viewprofile.html',views.viewprofiledetails, name="info"),
    path(r'get_patient_name/viewmedical.html',views.viewmedical, name="info"),
    path(r'get_patient_name/viewvitals',views.viewvitals, name="info"),
    path(r'get_patient_name/prescription_form.html',views.addprescription, name="info"),



    ]