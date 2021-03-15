from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class activeusers(models.Model):
    OrganizationName = models.CharField(max_length=45)
    FullName = models.CharField(max_length=200)
    EmailAddress =  models.CharField(max_length=100)
    Name = models.CharField(null=False,max_length=60)
    PostalAddress = models.CharField(max_length=150)
    UserCreationDate =  models.CharField(null=False,max_length=50)
    LastLoginDate = models.CharField(max_length=50)
    LoginStatus = models.CharField(max_length=50)
    PreferredFileServer = models.CharField(max_length=30)
    AuditGroup = models.CharField(max_length=30)
    GenericGroup =  models.CharField(max_length=15)
    UserLastModificationDate = models.CharField(max_length=30)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)


    class Meta:
        db_table = 'activeusers'
        # unique_together = (('Name', 'ReportWeek','ReportYear','UserCreationDate'),)


class loggedinusers(models.Model):
    EventLabel = models.CharField(max_length=100)
    EventKey = models.CharField(max_length=50)
    EventTime = models.CharField(null=False,max_length=50)
    UserName = models.CharField(max_length=100)
    UserID = models.CharField(null=False,max_length=60)
    IPAddress = models.CharField(max_length=50)
    UserOrganization = models.CharField(max_length=20)
    ObjectType = models.CharField(max_length=50)
    ObjectID = models.CharField(max_length=50)
    ObjectTypeBranchID = models.CharField(max_length=50)
    ObjectName = models.CharField(max_length=50)
    ObjectNumber = models.CharField(max_length=50)
    BranchID= models.CharField(max_length=50)
    WorkingBranchID = models.CharField(max_length=50)
    Version = models.CharField(max_length=50)
    MasterID = models.CharField(max_length=50)
    OrganizationID = models.CharField(max_length=50)
    OrganizationName=models.CharField(max_length=50)
    ContextID = models.CharField(max_length=50)
    ContextName = models.CharField(max_length=50)
    ContextTypeBranchID = models.CharField(max_length=50)
    FolderPath = models.CharField(max_length=50)
    DomainPath = models.CharField(max_length=50)
    Identity = models.CharField(max_length=50)
    LifecycleState =models.CharField(max_length=45)
    TransactionDescription = models.CharField(max_length=50)
    ObjectIdentity = models.CharField(max_length=50)
    SecurityLabels = models.CharField(max_length=50)
    EventSpecificData =models.CharField(max_length=50)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)

    class Meta:
        db_table = 'loggedinusers' # your view name
        # unique_together = (('EventTime','ReportWeek','ReportYear','UserID'),)


class organization(models.Model):
    org=models.CharField(max_length=45)

    def __str__(self):
        return self.org

    class Meta:
        db_table = 'organization'

class employeeTable(models.Model):
    employee=models.CharField(max_length=45)

    def __str__(self):
        return self.employee

    class Meta:
        db_table = 'employee'


class active_braking(models.Model):
    OrganizationName = models.CharField(max_length=45)
    FullName = models.CharField(max_length=200)
    EmailAddress =  models.CharField(max_length=100)
    Name = models.CharField(null=False,max_length=60)
    PostalAddress = models.CharField(max_length=150)
    UserCreationDate =  models.CharField(null=False,max_length=50)
    LastLoginDate = models.CharField(max_length=50)
    LoginStatus = models.CharField(max_length=50)
    PreferredFileServer = models.CharField(max_length=30)
    AuditGroup = models.CharField(max_length=30)
    GenericGroup =  models.CharField(max_length=15)
    UserLastModificationDate = models.CharField(max_length=30)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        # managed = False
        db_table = 'active_braking' # your view name
        unique_together = (('Name', 'ReportWeek','ReportYear','UserCreationDate'),)

class active_elec(models.Model):
    OrganizationName = models.CharField(max_length=45)
    FullName = models.CharField(max_length=200)
    EmailAddress =  models.CharField(max_length=100)
    Name = models.CharField(null=False,max_length=60)
    PostalAddress = models.CharField(max_length=150)
    UserCreationDate =  models.CharField(null=False,max_length=50)
    LastLoginDate = models.CharField(max_length=50)
    LoginStatus = models.CharField(max_length=50)
    PreferredFileServer = models.CharField(max_length=30)
    AuditGroup = models.CharField(max_length=30)
    GenericGroup =  models.CharField(max_length=15)
    UserLastModificationDate = models.CharField(max_length=30)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        # managed = False
        db_table = 'active_elec' # your view name
        unique_together = (('Name', 'ReportWeek','ReportYear','UserCreationDate'),)

class active_css(models.Model):
    OrganizationName = models.CharField(max_length=45)
    FullName = models.CharField(max_length=200)
    EmailAddress =  models.CharField(max_length=100)
    Name = models.CharField(null=False,max_length=60)
    PostalAddress = models.CharField(max_length=150)
    UserCreationDate =  models.CharField(null=False,max_length=50)
    LastLoginDate = models.CharField(max_length=50)
    LoginStatus = models.CharField(max_length=50)
    PreferredFileServer = models.CharField(max_length=30)
    AuditGroup = models.CharField(max_length=30)
    GenericGroup =  models.CharField(max_length=15)
    UserLastModificationDate = models.CharField(max_length=30)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        # managed = False
        db_table = 'active_css' # your view name
        unique_together = (('Name', 'ReportWeek','ReportYear','UserCreationDate'),)

class active_oss(models.Model):

    OrganizationName = models.CharField(max_length=45)
    FullName = models.CharField(max_length=200)
    EmailAddress =  models.CharField(max_length=100)
    Name = models.CharField(null=False,max_length=60)
    PostalAddress = models.CharField(max_length=150)
    UserCreationDate =  models.CharField(null=False,max_length=50)
    LastLoginDate = models.CharField(max_length=50)
    LoginStatus = models.CharField(max_length=50)
    PreferredFileServer = models.CharField(max_length=30)
    AuditGroup = models.CharField(max_length=30)
    GenericGroup =  models.CharField(max_length=15)
    UserLastModificationDate = models.CharField(max_length=30)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        # managed = False
        db_table = 'active_oss' # your view name
        unique_together = (('Name', 'ReportWeek','ReportYear','UserCreationDate'),)

class active_lvs(models.Model):
    OrganizationName = models.CharField(max_length=45)
    FullName = models.CharField(max_length=200)
    EmailAddress =  models.CharField(max_length=100)
    Name = models.CharField(null=False,max_length=60)
    PostalAddress = models.CharField(max_length=150)
    UserCreationDate =  models.CharField(null=False,max_length=50)
    LastLoginDate = models.CharField(max_length=50)
    LoginStatus = models.CharField(max_length=50)
    PreferredFileServer = models.CharField(max_length=30)
    AuditGroup = models.CharField(max_length=30)
    GenericGroup =  models.CharField(max_length=15)
    UserLastModificationDate = models.CharField(max_length=30)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        # managed = False
        db_table = 'active_lvs' # your view name
        unique_together = (('Name', 'ReportWeek','ReportYear','UserCreationDate'),)

class loggedin_braking(models.Model):
    EventLabel = models.CharField(max_length=45)
    EventKey = models.CharField(max_length=50)
    EventTime = models.CharField(null=False,max_length=50)
    UserName = models.CharField(max_length=100)
    UserID = models.CharField(null=False,max_length=60)
    IPAddress = models.CharField(max_length=50)
    UserOrganization = models.CharField(max_length=20)
    ObjectType = models.CharField(max_length=50)
    ObjectID = models.CharField(max_length=50)
    ObjectTypeBranchID = models.CharField(max_length=50)
    ObjectName = models.CharField(max_length=50)
    ObjectNumber = models.CharField(max_length=50)
    BranchID= models.CharField(max_length=50)
    WorkingBranchID = models.CharField(max_length=50)
    Version = models.CharField(max_length=50)
    MasterID = models.CharField(max_length=50)
    OrganizationID = models.CharField(max_length=50)
    OrganizationName=models.CharField(max_length=50)
    ContextID = models.CharField(max_length=50)
    ContextName = models.CharField(max_length=50)
    ContextTypeBranchID = models.CharField(max_length=50)
    FolderPath = models.CharField(max_length=50)
    DomainPath = models.CharField(max_length=50)
    Identity = models.CharField(max_length=50)
    LifecycleState =models.CharField(max_length=45)
    TransactionDescription = models.CharField(max_length=50)
    ObjectIdentity = models.CharField(max_length=50)
    SecurityLabels = models.CharField(max_length=50)
    EventSpecificData =models.CharField(max_length=50)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        managed = False
        db_table = 'loggedin_braking' # your view name
        unique_together = (('EventTime', 'ReportWeek','ReportYear','UserID'),)

class loggedin_Elec(models.Model):
    EventLabel = models.CharField(max_length=45)
    EventKey = models.CharField(max_length=50)
    EventTime = models.CharField(null=False,max_length=50)
    UserName = models.CharField(max_length=100)
    UserID = models.CharField(null=False,max_length=60)
    IPAddress = models.CharField(max_length=50)
    UserOrganization = models.CharField(max_length=20)
    ObjectType = models.CharField(max_length=50)
    ObjectID = models.CharField(max_length=50)
    ObjectTypeBranchID = models.CharField(max_length=50)
    ObjectName = models.CharField(max_length=50)
    ObjectNumber = models.CharField(max_length=50)
    BranchID= models.CharField(max_length=50)
    WorkingBranchID = models.CharField(max_length=50)
    Version = models.CharField(max_length=50)
    MasterID = models.CharField(max_length=50)
    OrganizationID = models.CharField(max_length=50)
    OrganizationName=models.CharField(max_length=50)
    ContextID = models.CharField(max_length=50)
    ContextName = models.CharField(max_length=50)
    ContextTypeBranchID = models.CharField(max_length=50)
    FolderPath = models.CharField(max_length=50)
    DomainPath = models.CharField(max_length=50)
    Identity = models.CharField(max_length=50)
    LifecycleState =models.CharField(max_length=45)
    TransactionDescription = models.CharField(max_length=50)
    ObjectIdentity = models.CharField(max_length=50)
    SecurityLabels = models.CharField(max_length=50)
    EventSpecificData =models.CharField(max_length=50)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        managed = False
        db_table = 'loggedin_Elec' # your view name
        unique_together = (('EventTime', 'ReportWeek','ReportYear','UserID'),)

class loggedin_css(models.Model):
    EventLabel = models.CharField(max_length=45)
    EventKey = models.CharField(max_length=50)
    EventTime = models.CharField(null=False,max_length=50)
    UserName = models.CharField(max_length=100)
    UserID = models.CharField(null=False,max_length=60)
    IPAddress = models.CharField(max_length=50)
    UserOrganization = models.CharField(max_length=20)
    ObjectType = models.CharField(max_length=50)
    ObjectID = models.CharField(max_length=50)
    ObjectTypeBranchID = models.CharField(max_length=50)
    ObjectName = models.CharField(max_length=50)
    ObjectNumber = models.CharField(max_length=50)
    BranchID= models.CharField(max_length=50)
    WorkingBranchID = models.CharField(max_length=50)
    Version = models.CharField(max_length=50)
    MasterID = models.CharField(max_length=50)
    OrganizationID = models.CharField(max_length=50)
    OrganizationName=models.CharField(max_length=50)
    ContextID = models.CharField(max_length=50)
    ContextName = models.CharField(max_length=50)
    ContextTypeBranchID = models.CharField(max_length=50)
    FolderPath = models.CharField(max_length=50)
    DomainPath = models.CharField(max_length=50)
    Identity = models.CharField(max_length=50)
    LifecycleState =models.CharField(max_length=45)
    TransactionDescription = models.CharField(max_length=50)
    ObjectIdentity = models.CharField(max_length=50)
    SecurityLabels = models.CharField(max_length=50)
    EventSpecificData =models.CharField(max_length=50)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        managed = False
        db_table = 'loggedin_css' # your view name
        unique_together = (('EventTime', 'ReportWeek','ReportYear','UserID'),)

class loggedin_oss(models.Model):
    EventLabel = models.CharField(max_length=45)
    EventKey = models.CharField(max_length=50)
    EventTime = models.CharField(null=False,max_length=50)
    UserName = models.CharField(max_length=100)
    UserID = models.CharField(null=False,max_length=60)
    IPAddress = models.CharField(max_length=50)
    UserOrganization = models.CharField(max_length=20)
    ObjectType = models.CharField(max_length=50)
    ObjectID = models.CharField(max_length=50)
    ObjectTypeBranchID = models.CharField(max_length=50)
    ObjectName = models.CharField(max_length=50)
    ObjectNumber = models.CharField(max_length=50)
    BranchID= models.CharField(max_length=50)
    WorkingBranchID = models.CharField(max_length=50)
    Version = models.CharField(max_length=50)
    MasterID = models.CharField(max_length=50)
    OrganizationID = models.CharField(max_length=50)
    OrganizationName=models.CharField(max_length=50)
    ContextID = models.CharField(max_length=50)
    ContextName = models.CharField(max_length=50)
    ContextTypeBranchID = models.CharField(max_length=50)
    FolderPath = models.CharField(max_length=50)
    DomainPath = models.CharField(max_length=50)
    Identity = models.CharField(max_length=50)
    LifecycleState =models.CharField(max_length=45)
    TransactionDescription = models.CharField(max_length=50)
    ObjectIdentity = models.CharField(max_length=50)
    SecurityLabels = models.CharField(max_length=50)
    EventSpecificData =models.CharField(max_length=50)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        managed = False
        db_table = 'loggedin_oss' # your view name
        unique_together = (('EventTime', 'ReportWeek','ReportYear','UserID'),)

class loggedin_lvs(models.Model):
    EventLabel = models.CharField(max_length=45)
    EventKey = models.CharField(max_length=50)
    EventTime = models.CharField(null=False,max_length=50)
    UserName = models.CharField(max_length=100)
    UserID = models.CharField(null=False,max_length=60)
    IPAddress = models.CharField(max_length=50)
    UserOrganization = models.CharField(max_length=20)
    ObjectType = models.CharField(max_length=50)
    ObjectID = models.CharField(max_length=50)
    ObjectTypeBranchID = models.CharField(max_length=50)
    ObjectName = models.CharField(max_length=50)
    ObjectNumber = models.CharField(max_length=50)
    BranchID= models.CharField(max_length=50)
    WorkingBranchID = models.CharField(max_length=50)
    Version = models.CharField(max_length=50)
    MasterID = models.CharField(max_length=50)
    OrganizationID = models.CharField(max_length=50)
    OrganizationName=models.CharField(max_length=50)
    ContextID = models.CharField(max_length=50)
    ContextName = models.CharField(max_length=50)
    ContextTypeBranchID = models.CharField(max_length=50)
    FolderPath = models.CharField(max_length=50)
    DomainPath = models.CharField(max_length=50)
    Identity = models.CharField(max_length=50)
    LifecycleState =models.CharField(max_length=45)
    TransactionDescription = models.CharField(max_length=50)
    ObjectIdentity = models.CharField(max_length=50)
    SecurityLabels = models.CharField(max_length=50)
    EventSpecificData =models.CharField(max_length=50)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        managed = False
        db_table = 'loggedin_lvs' # your view name
        unique_together = (('EventTime', 'ReportWeek','ReportYear','UserID'),)

class uploadmodel(models.Model):
    Before = models.FileField(upload_to=None)
    From = models.FileField(upload_to=None)
    AuditReport = models.FileField(upload_to=None)
