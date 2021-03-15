

#models
from sqlalchemy.engine.result import rowproxy_reconstructor
from .models import *

# from .forms import FirstForm
from .forms import ChartSelectionForm
from .forms import fileform
from .forms import ChartDeletionForm 

#python package
import csv
import datetime
from datetime import date
import subprocess
import json
import pandas as pd
from sqlalchemy import create_engine

from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.sessions.models import Session






#Home view - Project Description
def home(request):

    return render(request, 'home.html')

#Login View - Login page
@csrf_protect
def login(request):
    
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        print(username)
        if User.objects.filter(username=username).exists():
            user=auth.authenticate(username=username,password=password)
            print(user)
            if user is not None:
                auth.login(request,user)
                # messages.info(request, f"You are now logged in as {username}")
                return redirect('home')
            else:
                messages.info(request,'incorrect password')
                return redirect('login')
        else:
            messages.error(request,"user doesn't exists")
            return redirect('login')

    else:
        
        return render(request,template_name = "login.html")

#Register View - User Registration
@csrf_protect
def register(request):

    if request.method == 'POST':

        username= request.POST['username']
        email= request.POST['email']
        password1= request.POST['password']
        password2= request.POST['confirm_password']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken. Try different one.")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)    
                user.save()
                print("User Created")
                messages.info(request,"User created Successfully!")
                return redirect('login')

        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('login')
    else:

        return render(request, 'register.html')

#Logout View - User Logout
def logout(request):

    auth.logout(request)
    request.session.flush()
    print("logged out")
    messages.success(request,"Successfully logged out")
    for sesskey in request.session.keys():
        del request.session[sesskey]

    return redirect('login')     


#Charts Form View  - From to input the values for Chart report
@login_required(login_url='login')
def chartsform(request):

    form = ChartSelectionForm()

    return render(request, 'chartform.html', {'form':form,"charts_form": "btn-disabled"})

#Ajax view -  To load the list of weeks for choosen Year of Report
def load_week_charts(request):
    print(request.GET)
    ReportYear = request.GET.get('ReportWeek')
    print(ReportYear)
    weeks = activeusers.objects.values_list('ReportWeek',flat=True).filter(ReportYear=ReportYear).distinct().order_by('ReportWeek')
    print(weeks)


    return render(request,'weeklist_charts.html',{'weeks':weeks})

# Delete View - To delete the selected week data of chart
@login_required(login_url='login')
def delete(request):

    form = ChartDeletionForm()
    
    return render(request, 'delete.html', {'form':form,"delete_form": "btn-disabled"})

def ajax_delete(request):

    ChartDeletionForm(request.POST)

    ReportWeek=request.POST['ReportWeek']

    ReportYear=request.POST['ReportYear']


    activeusers_delete = activeusers.objects.filter(ReportWeek = ReportWeek ,ReportYear = ReportYear).delete()

    loggedinusers_delete = activeusers.objects.filter(ReportWeek = ReportWeek ,ReportYear = ReportYear).delete()
  
    # active_delete_result = subprocess.call('C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysql -uroot -padmin123 logindata -e "DELETE FROM logindata.activeusers where  ReportWeek = {0} and ReportYear = {1};'.format(ReportWeek,ReportYear))
    # delete_result = subprocess.call('C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysql -uroot -padmin123 logindata -e "DELETE FROM logindata.loggedinusers where  ReportWeek = {0} and ReportYear = {1};'.format(ReportWeek,ReportYear))

    return render(request, 'deletesuccess.html')

def load_charts(request):
    ChartSelectionForm(request.POST)

    org = request.POST['org']
    ReportWeek = request.POST['ReportWeek']
    ReportYear = request.POST['ReportYear']
    size = request.POST.get('size')
    
    
    Organization_withquotes = "'"+org+"'"
    # Organization_withquotes = 'Braking'

    # Initilize View names
    act_Organization_withquotes="active_"+org
    # act_Organization_withquotes = active_braking

    log_Organization_withquotes="loggedin_"+org
    # log_Organization_withquotes= loggedin_braking


    # active_db = subprocess.call('C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysql -uroot -padmin123 logindata -e "CREATE OR REPLACE VIEW {0} AS SELECT id, OrganizationName, FullName, EmailAddress, Name, PostalAddress, UserCreationDate, LastLoginDate, LoginStatus, PreferredFileServer, AuditGroup, GenericGroup, UserLastModificationDate, ReportWeek, ReportYear FROM logindata.activeusers where OrganizationName={1} and ReportWeek <= {2};'.format(act_Organization_withquotes,Organization_withquotes,ReportWeek))
    # loggedin_db = subprocess.call('C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysql -uroot -padmin123 logindata -e "CREATE OR REPLACE VIEW {0} AS SELECT id,EventLabel, EventKey, EventTime, UserName, UserID, IPAddress, UserOrganization, ObjectType, ObjectID, ObjectTypeBranchID, ObjectName, ObjectNumber, BranchID, WorkingBranchID, Version, MasterID, OrganizationID, OrganizationName, ContextID, ContextName, ContextTypeBranchID, FolderPath, DomainPath, Identity, LifecycleState, TransactionDescription, ObjectIdentity, SecurityLabels, EventSpecificData, ReportWeek, ReportYear FROM logindata.loggedinusers where UserOrganization={1} and ReportWeek <= {2};'.format(log_Organization_withquotes,Organization_withquotes,ReportWeek))

    if int(ReportWeek) > int(size):
        i = int(ReportWeek) - (int(size)-1)
    else:
        i = 1

    print(i)
    # i=1
    array =[]
    array_Braking = []
    array_Elec=[]
    array_LVS=[]
    array_CSS=[]
    array_OSS=[]
    org_list = []

    if 'Braking' in org: 
        while i <= int(ReportWeek):
            dict={}

            Loggedin = loggedinusers.objects.filter(ReportYear=ReportYear,ReportWeek=i,UserOrganization=org).distinct().values('UserName')

            Active = activeusers.objects.filter(GenericGroup="Regular",AuditGroup= 'Active',OrganizationName=org,ReportWeek = i,ReportYear=ReportYear)

            print(ReportWeek)
            print(len(Loggedin))
            print(len(Active))
        
            try:
                Percentage = int((len(Loggedin)/len(Active))*100)
            except ZeroDivisionError:
                Percentage=0

            dict["Week"] = i
            dict["Active"] = len(Active)
            dict["Logged In"] = len(Loggedin)
            dict["% Usage"] = Percentage
            dict["org"] = org
            
            array.append(dict)
            i+=1


    if 'Elec' in org:
        while i <= int(ReportWeek):
            dict={}
            Loggedin = loggedinusers.objects.filter(ReportYear=ReportYear,ReportWeek=i,UserOrganization=org).distinct().values('UserName')

            Active = activeusers.objects.filter(ReportYear=ReportYear,GenericGroup="Regular",AuditGroup= 'Active',OrganizationName=org,ReportWeek = i)


            try:
                Percentage = int((len(Loggedin)/len(Active))*100)
            except ZeroDivisionError:
                Percentage=0

            dict["Week"] = i
            dict["Active"] = len(Active)
            dict["Logged In"] = len(Loggedin)
            dict["% Usage"] = Percentage
            dict["org"] = org
            
            array.append(dict)
            i+=1

    if 'OSS' in org:
        while i <= int(ReportWeek):
            dict={}
            Loggedin = loggedinusers.objects.filter(ReportYear=ReportYear,ReportWeek=i,UserOrganization=org).distinct().values('UserName')

            Active = activeusers.objects.filter(ReportYear=ReportYear,GenericGroup="Regular",AuditGroup= 'Active',OrganizationName=org,ReportWeek = i)


            try:
                Percentage = int((len(Loggedin)/len(Active))*100)
            except ZeroDivisionError:
                Percentage=0

            dict["Week"] = i
            dict["Active"] = len(Active)
            dict["Logged In"] = len(Loggedin)
            dict["% Usage"] = Percentage
            dict["org"] = org
            
            array.append(dict)
            i+=1

    if 'LVS' in org:
        while i <= int(ReportWeek):
            dict={}
            Loggedin = loggedinusers.objects.filter(ReportYear=ReportYear,ReportWeek=i,UserOrganization=org).distinct().values('UserName')

            Active = activeusers.objects.filter(ReportYear=ReportYear,GenericGroup="Regular",AuditGroup= 'Active',OrganizationName=org,ReportWeek = i)


            try:
                Percentage = int((len(Loggedin)/len(Active))*100)
            except ZeroDivisionError:
                Percentage=0

            dict["Week"] = i
            dict["Active"] = len(Active)
            dict["Logged In"] = len(Loggedin)
            dict["% Usage"] = Percentage
            dict["org"] = org
            
            array.append(dict)
            i+=1

    if 'CSS' in org:
        while i <= int(ReportWeek):
            dict={}
            Loggedin = loggedinusers.objects.filter(ReportYear=ReportYear,ReportWeek=i,UserOrganization=org).distinct().values('UserName')

            Active = activeusers.objects.filter(ReportYear=ReportYear,GenericGroup="Regular",AuditGroup= 'Active',OrganizationName=org,ReportWeek = i)
  

            try:
                Percentage = int((len(Loggedin)/len(Active))*100)
            except ZeroDivisionError:
                Percentage=0

            dict["Week"] = i
            dict["Active"] = len(Active)
            dict["Logged In"] = len(Loggedin)
            dict["% Usage"] = Percentage
            dict["org"] = org
            
            array.append(dict)
            i+=1
    
    if 'All' in org:

        org_list = ['Braking','Elec','LVS','CSS','OSS']
        list1 = organization.objects.values_list('org',flat=True).distinct()
        print(list1)
        for item in org_list:
            
            if int(ReportWeek) > int(size):
                i = int(ReportWeek) - (int(size)-1)
            else:
                i = 1

            while i <= int(ReportWeek):

                dict={}
                Loggedin = loggedinusers.objects.filter(ReportYear=ReportYear,ReportWeek=i,UserOrganization=item).distinct().values('UserName')

                Active = activeusers.objects.filter(ReportYear=ReportYear,GenericGroup="Regular",AuditGroup= 'Active',ReportWeek = i,OrganizationName=item)
    

                try:
                    Percentage = int((len(Loggedin)/len(Active))*100)
                except ZeroDivisionError:
                    Percentage=0

                dict["Week"] = i
                dict["Active"] = len(Active)
                dict["Logged In"] = len(Loggedin)
                dict["% Usage"] = Percentage
                dict["org"] = item
            


                if 'Braking' in item:
                    array_Braking.append(dict)
                elif 'Elec' in item:
                    array_Elec.append(dict)
                elif 'LVS' in item:
                    array_LVS.append(dict)
                elif 'CSS' in item:
                    array_CSS.append(dict)
                elif 'OSS' in item:
                    array_OSS.append(dict)
                
                i+=1


    # to convery the dictionary data type to String
    org_list = len(org_list)
    array = json.dumps(array)
    array_Braking = json.dumps(array_Braking)
    array_Elec = json.dumps(array_Elec)
    array_LVS = json.dumps(array_LVS)
    array_CSS = json.dumps(array_CSS)
    array_OSS = json.dumps(array_OSS)

    print(array_Braking)
    print(array_Elec)

    

    if len(array) == 0 or array_Braking==0 or array_Elec ==0 or array_LVS==0 or array_CSS==0 or  array_OSS==0:
        print("Empty")
        return render(request, 'nodata.html', {})
    else:
        return render(request, 'chartview.html', {'array_Braking':array_Braking,'array_Elec':array_Elec,'array_LVS':array_LVS,'array_CSS':array_CSS,'array_OSS':array_OSS,'org_list':org_list,'size':size,'array':array,'org':org})



#Upload View - form to get the inputs for import the data into database
@login_required(login_url='login')
@csrf_protect
def upload(request):

    form = fileform()

    return render(request, 'csvupload.html', {'form':form,"upload": "btn-disabled"})

#Ajax View - To load the list of weeks for choosen Year of Report
def load_week_upload(request):
    print(request.GET)
    ReportYear = request.GET.get('ReportWeek')
    print(ReportYear)
    weeks = activeusers.objects.values_list('ReportWeek',flat=True).filter(ReportYear=ReportYear).distinct().order_by('ReportWeek')
    print(weeks)

    x1=1
    x2=52
    week_list=range(x1,x2+1)

    return render(request,'weeklist_upload.html',{'weeks':weeks,'week_list':week_list})

#Upload View - import the data into database
def UploadSuccess(request):

    template = "UploadSuccess.html"
    

    weekNumber = request.POST['ReportWeek']
    year = request.POST['ReportYear']


    my_connect = create_engine("mysql+mysqldb://root:admin@localhost/sampledata?charset=utf8mb4") #fill details
    print("Connection Established")
    

    before_csv = pd.read_csv(request.FILES["Before"].file,encoding='cp1252')
    before_csv = before_csv.rename(columns={'Organization Name': 'OrganizationName','Full Name':'FullName','Email Address':'EmailAddress','Postal Address':'PostalAddress','User Creation Date':'UserCreationDate','Last Login Date':'LastLoginDate','Login Status':'LoginStatus','Preferred File Server':'PreferredFileServer','Audit Group':'AuditGroup','Generic Group':'GenericGroup','User Last Modification Date':'UserLastModificationDate'})
    before_csv['ReportWeek'] = weekNumber
    before_csv['ReportYear'] = year

    print(before_csv)
    print(type(before_csv))

    for index, row in before_csv.iterrows(): 
        print (row["OrganizationName"], row["FullName"])


    ActiveusersModel = []
    
    for index,row in before_csv.iterrows():
        ActiveusersModel.append(
        activeusers(
        OrganizationName = row["OrganizationName"],
        FullName = row["FullName"],
        EmailAddress =  row["EmailAddress"],
        Name = row["Name"],
        PostalAddress = row["PostalAddress"],
        UserCreationDate =  row["UserCreationDate"],
        LastLoginDate = row["LastLoginDate"],
        LoginStatus = row["LoginStatus"],
        PreferredFileServer = row["PreferredFileServer"],
        AuditGroup = row["AuditGroup"],
        GenericGroup =  row["GenericGroup"],
        UserLastModificationDate = row["UserLastModificationDate"],
        ReportWeek = row["ReportWeek"],
        ReportYear = row["ReportYear"],
    )
    )



    print("Week Number: ",weekNumber)
    print("Year Number: ",year)

    Active = activeusers.objects.filter(ReportWeek =weekNumber,ReportYear=year)
    loggedin = loggedinusers.objects.filter(ReportWeek =weekNumber,ReportYear=year)

    # Active = my_connect.execute("SELECT * FROM sampledata.activeusers where ReportWeek={0} and ReportYear = {1}".format(weekNumber,year)).fetchall()
    # loggedin = my_connect.execute("SELECT * FROM sampledata.loggedinusers where ReportWeek={0} and ReportYear = {1}".format(weekNumber,year)).fetchall()

    print("Active user count : ",len(Active))
    print("Loggedin user count : ",len(loggedin))


    if len(Active) >0:
        return render(request, "UploadError.html",{})
    elif len(loggedin) >0:
        return render(request, "UploadError.html",{})

       

    # before_csv.to_sql(con=my_connect,name='activeusers',if_exists='append',index=False)

    
    # from_csv = pd.read_csv(request.FILES["From"],encoding='utf-8')
    # from_csv = from_csv.rename(columns={'Organization Name': 'OrganizationName','Full Name':'FullName','Email Address':'EmailAddress','Postal Address':'PostalAddress','User Creation Date':'UserCreationDate','Last Login Date':'LastLoginDate','Login Status':'LoginStatus','Preferred File Server':'PreferredFileServer','Audit Group':'AuditGroup','Generic Group':'GenericGroup','User Last Modification Date':'UserLastModificationDate'})
    # from_csv['ReportWeek'] = weekNumber
    # from_csv['ReportYear'] = year
    # print(from_csv)
    # from_csv.to_sql(con=my_connect,name='activeusers',if_exists='append',index=False)

    
    audit_csv = pd.read_csv(request.FILES["AuditReport"],encoding='unicode_escape')
    audit_csv = audit_csv.rename(columns={'Event Label':'EventLabel','Event Key':'EventKey','Event Time':'EventTime','User Name':'UserName','User ID':'UserID','IP Address':'IPAddress','User Organization':'UserOrganization','Object Type':'ObjectType','Object ID':'ObjectID','Object Type Branch ID':'ObjectTypeBranchID','Object Name':'ObjectName','Object Number':'ObjectNumber','Branch ID':'BranchID','Working Branch ID':'WorkingBranchID','Master ID':'MasterID','Organization ID':'OrganizationID','Organization Name':'OrganizationName','Context ID':'ContextID','Context Name':'ContextName','Context Type Branch ID':'ContextTypeBranchID','Folder Path':'FolderPath','Domain Path':'DomainPath','Lifecycle State':'LifecycleState','Transaction Description':'TransactionDescription','Object Identity':'ObjectIdentity','Security Labels':'SecurityLabels','Event Specific Data':'EventSpecificData'})
    audit_csv['ReportWeek'] = weekNumber
    audit_csv['ReportYear'] = year

    LoggedinusersModel = []
    
    for index,row in audit_csv.iterrows():
        LoggedinusersModel.append(
        loggedinusers(
        EventLabel = row["EventLabel"],
        EventKey = row["EventKey"],
        EventTime =row["EventTime"],
        UserName = row["UserName"],
        UserID = row["UserID"],
        IPAddress = row["IPAddress"],
        UserOrganization = row["UserOrganization"],
        ObjectType = row["ObjectType"],
        ObjectID = row["ObjectID"],
        ObjectTypeBranchID = row["ObjectTypeBranchID"],
        ObjectName = row["ObjectName"],
        ObjectNumber = row["ObjectNumber"],
        BranchID= row["BranchID"],
        WorkingBranchID = row["WorkingBranchID"],
        Version = row["Version"],
        MasterID = row["MasterID"],
        OrganizationID = row["OrganizationID"],
        OrganizationName= row["OrganizationName"],
        ContextID = row["ContextID"],
        ContextName = row["ContextName"],
        ContextTypeBranchID = row["ContextTypeBranchID"],
        FolderPath = row["FolderPath"],
        DomainPath = row["DomainPath"],
        Identity = row["Identity"],
        LifecycleState =row["LifecycleState"],
        TransactionDescription = row["TransactionDescription"],
        ObjectIdentity = row["ObjectIdentity"],
        SecurityLabels = row["SecurityLabels"],
        EventSpecificData =row["EventSpecificData"],
        ReportWeek = row["ReportWeek"],
        ReportYear = row["ReportYear"],

    )
    )

    activeusers.objects.bulk_create(ActiveusersModel)
    loggedinusers.objects.bulk_create(LoggedinusersModel)

    # audit_csv.to_sql(con=my_connect,name='loggedinusers',if_exists='append',index=False)
    
    return render(request, template,{})

