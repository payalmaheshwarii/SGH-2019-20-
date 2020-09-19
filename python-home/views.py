from django.shortcuts import render, redirect
from django.http import HttpResponse
import pyrebase
from django.contrib import auth


    
firebaseConfig = {
    'apiKey': "AIzaSyA8junLgjS4nse8lmtgfs3hiTnuRASCRMw",
    'authDomain': "sghfirebaseproject-c8a7f.firebaseapp.com",
    'databaseURL': "https://sghfirebaseproject-c8a7f.firebaseio.com",
    'projectId': "sghfirebaseproject-c8a7f",
    'storageBucket': "sghfirebaseproject-c8a7f.appspot.com",
    'messagingSenderId': "676289506437",
    'appId': "1:676289506437:web:b734e3f625487d7d1d0dec"
  }
firebase = pyrebase.initialize_app(firebaseConfig)

authe = firebase.auth()
db = firebase.database()
storage = firebase.storage()



def signIn(request):
    
    return render(request, 'SignIn.html')

def signUp(request):
    return render(request, 'SignUp.html')

def home(request):
    return render(request,'puff.html')

def doctorprofile(request):
    
    return render(request, 'doctordetails.html')


def singIn(request):
    return render(request, "signIn.html")
    


def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    repassw = request.POST.get('repass')
    contact = request.POST.get('contact')

    if passw!=repassw:
        message = "password didnot match"
        return render(request,"SignUp.html",{"msg" : message})

    else:
        try:
            user = authe.create_user_with_email_and_password(email,passw)
            uid = user['localId']
            data = {
                'name':name,
                'contact':contact,
                'email':email
            }

            db.child('Users').child(uid).child('profile').set(data)

            return render(request, "SignIn.html")
        except:
            message = "Email Exists"
            return render(request,"SignUp.html",{"msg" : message})



def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    role = request.POST.get("role")

    try:
        user = authe.sign_in_with_email_and_password(email,passw)
        # user = auth.refresh(user['refreshToken'])
    except:
        message = "invalid password or email"
        return render(request,"signIn.html",{"msg":message})
    
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    

    if role == "patient":
        return render(request, "welcome_patient.html",{"e":email})

        
    else:
        return render(request, "welcome_doctor.html",{"e":email})


def get_patient_name(request):
    emailid  = request.POST.get('emailid')
    password = request.POST.get('password')
    try:
        user = authe.sign_in_with_email_and_password(emailid,password)
    except:
        message = "invalid password or email"
        return render(request,"welcome_doctor.html",{"msg":message})


    return render(request, "welcome_pd.html")

def personaldet(request):
    return render(request, 'personaldetails.html')

def vitals(request):
    return render(request,'vitals.html')

def emergency(request):
    return render(request,'emergency_information.html')

def medicalhistory(request):
    return render(request,'medical_history.html')

def insurance(request):
    return render(request,'insuranceform.html')

def prescription(request):
    return render(request,'prescription_form.html')


def personaldetsub(request):
    gender =request.POST.get('gender')
    fname = request.POST.get("first_name")
    lname = request.POST.get("last_name")
    month = str(request.POST.get("month"))
    date = str(request.POST.get("date"))
    year = str(request.POST.get("year"))
    height = str(request.POST.get("height"))
    weight = str(request.POST.get("weight"))
    email = str(request.POST.get("email"))
    
    data = {
        "name": fname,
        "gender" : gender,
        "birthdate" : date + month + year,
        "height" : height,
        "weight" : weight,
        "email" : email

    }
    passdata = {
        "gender" : gender,
        "first_name" : fname,
        "last_name" : lname,
        "month" : month,
        "date" : date,
        "year" : year,
        "height" : height,
        "weight" : weight,
        "email" : email
    }


    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    db.child('Users').child(a).child('profile').set(data)
    return render(request,'welcome_patient.html',passdata)

def emegencydata(request):
    fname = request.POST.get("firstname")
    lname = request.POST.get("lastname")
    relation = str(request.POST.get("relation"))
    contact = str(request.POST.get("contact"))
    address = str(request.POST.get("address"))
    city = str(request.POST.get("city"))
    district = str(request.POST.get("district"))
    state = str(request.POST.get("state"))
    pin = str(request.POST.get("pin"))
    
    data = {
        "fname": fname,
        "lname" :  lname,
        "relation" : relation,
        "contact" : contact,
        "address" : address,
        "city"  : city,
        "district" : district,
        "state" : state,
        "pin" : pin

    }

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    db.child('Users').child(a).child('emergency_details').set(data)
    return render(request,'emergency_information.html',data)

def addprescription(request):
    hospital = request.POST.get("hospital")
    doctor = request.POST.get("doctor")
    prescribedon = request.POST.get("prescribedon")
    notes = request.POST.get("notes")
    file = request.POST.get("files")
    
    data = {
        "hospital": hospital,
        "doctor" :  doctor,
        "prescribedon" : prescribedon,
        "notes" : notes,
        "file" : file

    }
    
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    db.child('Users').child(a).child('prescriptions').set(data)
    return render(request,'prescription_form.html')




def medicaldetails(request):
    anyallergy = request.POST.get("anyallergy")
    allergy = request.POST.get("allergy")
    anymedicine = request.POST.get("anymedicine")
    medicine = request.POST.get("medicine")
    typeofd = request.POST.get("typeofd")
    disease = request.POST.get("disease")
    severityofd = request.POST.get("severityofd")
    nameofreport = request.POST.get("nameofreport")
    typeofreport = request.POST.get("typeofreport")
    report = request.POST.get("report")
    doctor = request.POST.get("doctor")
    clinic = request.POST.get("clinic")


    data = {
        "anyallergy": anyallergy,
        "allergy" :  allergy,
        "anymedicine" : anymedicine,
        "medicine" : medicine,
        "typeofd" : typeofd,
        "severityofd" : severityofd,
        "disease" : disease,
        "nameofreport"  : nameofreport,
        "typeofreport" : typeofreport,
        "doctor" : doctor,
        "clinic" : clinic

    }
    
    
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    db.child('Users').child(a).child('medical_details').set(data)
    storage.child('Users').child(a).child('report').child(report)
    return render(request,'medical_history.html',data)

def addvitals(request):
    bloodgroup = request.POST.get("bloodgroup")
    bp = request.POST.get("bp")
    temp = request.POST.get("temp")
    heartrate = request.POST.get("heartrate")
    respirationrate = request.POST.get("respirationrate")
    
    data = {
        "bloodgroup": bloodgroup,
        "bp" :  bp,
        "temp" : temp,
        "heartrate" : heartrate,
        "respirationrate" : respirationrate      

    }
     
    print("bp")
    print(bp)
    
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    db.child('Users').child(a).child('vitals').set(data)
    return render(request,'welcome_patient.html')

def addinsurance(request):
    insurance = request.POST.get("insurance")
    number = request.POST.get("number")
    policy = request.POST.get("policy")
    valid = request.POST.get("valid")

    
    data = {
        "insurance": insurance,
        "number" :  number,
        "policy" : policy,
        "valid" : valid    

    }
     
    
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    db.child('Users').child(a).child('insurance').set(data)
    return render(request,'welcome_patient.html')

def adddoctordetails(request):
    name = request.POST.get("name")
    spec = request.POST.get("spec")
    clinicname = request.POST.get("clinicname")
    address = request.POST.get("address")

    
    data = {
        "name": name,
        "spec" :  spec,
        "clinicname" : clinicname,
        "address" : address    

    }
     
    
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    db.child('Users').child(a).child('drprofile').set(data)
    return render(request,'welcome_patient.html')



def viewvitals(request):

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    bloodgroup = db.child('Users').child(a).child('vitals').child('bloodgroup').get().val()
    bp = db.child('Users').child(a).child('vitals').child('bp').get().val()
    heartrate = db.child('Users').child(a).child('vitals').child('heartrate').get().val()
    respirationrate = db.child('Users').child(a).child('vitals').child('respirationrate').get().val()
    temp = db.child('Users').child(a).child('vitals').child('temp').get().val()
    
    passdata = {
        "bloodgroup" : bloodgroup,
        "bp" : bp,
        "heartrate" : heartrate,
        "respirationrate" : respirationrate,
        "temp" : temp
        }  
    

    return render(request,'viewvitals.html',passdata)


def viewprofiledetails(request):

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    name = db.child('Users').child(a).child('profile').child('name').get().val()
    email = db.child('Users').child(a).child('profile').child('email').get().val()
    gender = db.child('Users').child(a).child('profile').child('gender').get().val()
    relname = db.child('Users').child(a).child('emergency_details').child('fname').get().val()
    relation = db.child('Users').child(a).child('emergency_details').child('relation').get().val()
    contact = db.child('Users').child(a).child('emergency_details').child('contact').get().val()
    

    passdata = {
        "name" : name,
        "email" : email,
        "gender" : gender,
        "relname" : relname,
        "contact" : contact,
        "relation" : relation
        }  
    

    return render(request,'viewprofile.html',passdata)

def viewmedical(request):

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    allergy = db.child('Users').child(a).child('medical_details').child('allergy').get().val()
    anyallergy = db.child('Users').child(a).child('medical_details').child('anyallergy').get().val()
    clinic = db.child('Users').child(a).child('medical_details').child('clinic').get().val()
    medicine = db.child('Users').child(a).child('medical_details').child('medicine').get().val()
    disease = db.child('Users').child(a).child('medical_details').child('disease').get().val()
    doctor = db.child('Users').child(a).child('medical_details').child('doctor').get().val()
    typeofreport = db.child('Users').child(a).child('medical_details').child('typeofreport').get().val()
    nameofreport = db.child('Users').child(a).child('medical_details').child('nameofreport').get().val()
    severityofd = db.child('Users').child(a).child('medical_details').child('severityofd').get().val()
    typeofd = db.child('Users').child(a).child('medical_details').child('typeofd').get().val()
    

    passdata = {
        "allergy" : allergy,
        "anyallergy" : anyallergy,
        "medicine" : medicine,
        "disease" : disease,
        "clinic" : clinic,
        "doctor" : doctor,
        "typeofreport" : typeofreport,
        "nameofreport" : nameofreport,
        "severityofd" :severityofd,
        "typeofd" : typeofd

        }  
    

    return render(request,'viewmedical.html',passdata)


def logout(request):
    auth.logout(request)
    return render(request,'SignIn.html')
