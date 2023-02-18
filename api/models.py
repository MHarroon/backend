from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# gloabal attribute 

title = ( 
    ("Mr" , "Mr" ),
    ("Ms" , "Ms"),
    ("Mrs" , "Mrs"))

maritalSatus = ( 
   ("Married" , "Married" ),
   ("Single" , "Single"),
   ("Divorced" , "Divorced"),
   ("Widowed", "Widowed"))

education = ( 
    ("Matric" , "Matric" ),
    ("Intermediate" , "Intermediate"),
    ("A/O level" , "A/O level"),
    ("Master", "MAster"),
    ("MPHill" , "MPHill"),
    ("PHD" , "PHD"))

geneder = ( 
    ("Male" , "Male" ),
    ("Female" , "Female"))

residentTypePermanat = ( 
    ("Owned" , "Owned" ),
    ("Rented" , "Rented"),
    ("Compnay" , "Compnay"),
    ("Parents", "Parents"),
    ("MPHill" , "MPHill"),
    ("Financed/Leased" , "Financed/Leased"))

c_EmployementType = ( 
    ("Permanent" , "Permanent" ),
    ("Contractual" , "Contractual"))

p_EmployementType = ( 
    ("Permanent" , "Permanent" ),
    ("Contractual" , "Contractual"))

s_TypeOFBusiness = ( 
    ("Sole Proprietorship" , "Sole Proprietorship" ),
    ("Patnership" , "Patnership"),
    ("Other" , "Other"))

s_ProfessionlaQulifications = ( 
    ("Chartered Accountant" , "Chartered Accountant" ),
    ("Doctor" , "Doctor"),
    ("Engineer" , "Engineer"),
    ("Architect" , "Architect"),
    ("Other" , "Other"))

accountType = ( 
    ("Current Account" , "Current Account" ),
    ("Saving Account" , "Saving Account"))

desiredRepTenure = ( 
    ("1 Year" , " 1 Year" ),
    ("2 Year " , "2 Year "),
    ("3 Year" , "3 Year "),
    ("5 Year" , "5 Year"))

loanReqFor = ( 
    ("Wedding" , "Wedding" ),
    ("Vacation" , "Vacation"),
    ("Studies" , "Studies"),
    ("Other" , "Other"))

AccomodationType = ( 
    ("House" , "House"),
    ("Appartment" , "Appartment"),
    ("Portion" , "Portion"),
    ("Room" , "Other"))

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255 , unique = True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    # username = None

    # USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = []

# Application Complete 

class ApplicationModel(models.Model):
    # Personal Information
    applicationID = models.AutoField(primary_key = True , editable=False )
    # Titles = models.CharField(max_length=50 , choices=title ,default="Mr")
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    FatherName = models.CharField(max_length=50)
    CNIC = models.IntegerField()
    Old_Nic = models.IntegerField()
    CNIC_Is_Date = models.DateField(default=timezone.now)
    CNIC_Ex_Date = models.DateField(default=timezone.now)
    PassportNumber = models.CharField( max_length=50)
    DateOfBirth = models.DateField(default=timezone.now )
    MaritalStatus = models.CharField(max_length=50, choices=maritalSatus)
    # Dependants = models.IntegerField()
    Children = models.IntegerField()
    OtherDependants = models.CharField( max_length=50)
    Education = models.CharField( max_length=50 ,choices=education)
    Gender = models.CharField(max_length=50 , choices=geneder)
      # Contact Info
    address = models.CharField( max_length=50)
    postalcode = models.CharField(max_length=50)
    city = models.CharField( max_length=50)
    mobileNumber = models.IntegerField()
    email = models.EmailField(max_length=50)
    residentType = models.CharField( max_length=50 , choices = residentTypePermanat)
    accomodationType = models.CharField(max_length = 50 , choices = AccomodationType)
    monthlyRent = models.IntegerField()
    installementAmount = models.IntegerField()
    permanentAddress = models.CharField( max_length=50)
    prepostalcode = models.CharField( max_length=50)
    cityPer = models.CharField( max_length=50)
    preresidentType = models.CharField(max_length=50 , choices=residentTypePermanat)
    numberOfCar = models.IntegerField()
    Model = models.CharField(max_length=50)
    # Employement Details (For Salaried Indivisual Only)
    C_CompnayName = models.CharField(max_length=50)
    C_CompanyAddres = models.CharField(max_length=50)
    C_JobTitle = models.CharField(max_length=50)
    C_Department = models.CharField(max_length=50)
    C_EmployementSince = models.DateField(default=timezone.now)
    C_EmploymentNumber = models.CharField(max_length=50)
    C_Extension = models.CharField(max_length=50)
    C_OfficeEmail = models.EmailField(max_length=50)
    C_EmployementType = models.CharField(max_length=50, choices=c_EmployementType)
         # Previous Employement Details
    P_CompnayName = models.CharField(max_length=50)
    P_CompanyAddres = models.CharField(max_length=50)
    P_JobTitle = models.CharField(max_length=50)
    P_Department = models.CharField(max_length=50)
    P_EmployementSince = models.DateField(default=timezone.now )
    P_EmployementSinceT = models.DateField(default=timezone.now )
    P_EmploymentNumber = models.CharField(max_length=50)
    P_Extension = models.CharField(max_length=50)
    P_OfficeEmail = models.EmailField(max_length=50)
    P_EmployementType = models.CharField(max_length=50, choices=p_EmployementType)
     # Income Details
    MonthlyGrossIncome = models.IntegerField()
    MonthlyNetIncome =models.IntegerField()
    SalarayDisbursementDay =models.DateField( default=timezone.now)
    OtherVerIncome = models.IntegerField()
    SourceOfOtherIncome = models.CharField(max_length=50)
    AverageMonthlyIncome = models.IntegerField()
    BankName = models.CharField(max_length=50)
    AccountNumber = models.CharField(max_length=50)
    AccountType = models.CharField(max_length=50, choices=accountType)
    Branch = models.CharField(max_length=50 )
    DesiredRepTenure = models.CharField(max_length=50 , choices=desiredRepTenure)
    LoanReqFor = models.CharField(max_length=50, choices = loanReqFor)
    s_LoanReqFor = models.CharField(max_length=50)
    AmmountSoughtPKR = models.IntegerField()
    IncomeAmountPreMonth = models.IntegerField()
     # Business Details (If Your Income Is From Business)
    numberOfBusiness = models.IntegerField()
    businessTitle = models.CharField(max_length=50)
    businessAddress = models.CharField(max_length=50)
    businessType = models.CharField(max_length=50)
    industryType = models.CharField(max_length=50) 
    ntnNumber = models.CharField(max_length=50)
    establishedSince = models.DateField(default=timezone.now )
    registerWith = models.CharField(max_length=50)
    businessTelephoneNumber = models.IntegerField()
    businessEmail = models.EmailField(max_length=50)
    companyName = models.CharField(max_length=50)
    typeOfBusiness = models.CharField(max_length=50,choices=s_TypeOFBusiness)
    s_specify_TypeOFBusiness = models.CharField( max_length=50)
    professionalQualifications = models.CharField(max_length=50,choices=s_ProfessionlaQulifications)
    # s_specify_professionalQualifications = models.CharField(max_length=50)
    
    #    Details Of References
    R_FullName = models.CharField(max_length=50)
    R_CINC = models.IntegerField()
    R_PossportNumber = models.CharField(max_length=50)
    R_Address = models.CharField(max_length=50)
    R_TelephoneNumOffice = models.IntegerField()
    R_TelephoneNumResidence = models.IntegerField()
    R_Email = models.EmailField(max_length=50)
    R_CellNumber = models.IntegerField()
    R_Relationship = models.CharField(max_length=50)
     #    Details Of References 02
    R2_FullName = models.CharField(max_length=50)
    R2_CINC = models.IntegerField()
    R2_PossportNumber = models.CharField(max_length=50)
    R2_Address = models.CharField(max_length=50)
    R2_TelephoneNumOffice = models.IntegerField()
    R2_TelephoneNumResidence = models.IntegerField()
    R2_Email = models.EmailField(max_length=50)
    R2_CellNumber = models.IntegerField()
    R2_Relationship = models.CharField(max_length=50)
     # Document Submission
    bankStatementFile = models.FileField(upload_to="employee/")
    nicPicFile = models.FileField(upload_to="employee/")
    keBillFile = models.FileField(upload_to="employee/")
    gasBillFile = models.FileField(upload_to="employee/")
    profilePicFile = models.FileField(upload_to="employee/")

    def __str__(self):
         return self.FirstName 
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    # def nic_upload_to(instance, filename):
    #     return f'media/employee/{instance.id}/nice/{filename}'

    # def bankstatment_upload_to(instance, filename):
    #     return f'media/employee/{instance.id}/bankstate/{filename}'
       
    # def kebill_upload_to(instance, filename):
        
    #     return f'media/employee/{instance.id}/electricitybill/{filename}'
    # def gassbill_upload_to(instance, filename):
    #     return f'media/employee/{instance.id}/gasbill/{filename}'
   
    # nicpdf = models.FileField(upload_to=nic_upload_to)
    # bankstatmentptdf = models.FileField(upload_to=bankstatment_upload_to)
    # kebilllpdf = models.FileField(upload_to=kebill_upload_to)
    # gassbillpdf = models.FileField(upload_to=gassbill_upload_to)


# if the above line not work use the below code 
# profilepdf = models.FileField(upload_to='employee/profile/pdfs/')
# electricitybillpdf = models.FileField(upload_to='employee/electricitybill/pdfs/')

   
   
   
   
   
   
   
   
   
# class CustomerAccountModel(models.Model):
#     CustomerAccountID = models.AutoField(primary_key = True , editable=False)
#     # primaray key of CustomerAccount
#     # foreign key of ApplicationForum
#     applicationModelID = models.ForeignKey(ApplicationModel,   on_delete=models.CASCADE)
#     # Income Details
#     MonthlyGrossIncome = models.IntegerField()
#     MonthlyNetIncome = models.IntegerField()
#     SalarayDisbursementDay =models.DateField( )
#     # Other Verifiable Income (if any) For SEP's Only
#     OtherVerIncome =models.IntegerField()
#     SourceOfOtherIncome = models.CharField(max_length=50)
#     AverageMonthlyIncome = models.IntegerField()
# #  Banking Details
#     BankName = models.CharField(max_length=50)
#     AccountNumber = models.CharField(max_length=50)
#     AccountType = ( 
#         ("Cuurent Account" , "Cuurent Account" ),
#         ("Saving Account" , "Saving Account"))
#     accountType = models.CharField(max_length=50, choices=AccountType)
#     Branch = models.CharField(max_length=50)
#     # BankBranch = models.CharField(max_length=50)
#     # Desired Financing
#     DesiredRepTenure = ( 
#         ("12 Month" , "12 Montht" ),
#         ("24 Month" , "24 Month"),
#         ("36 Month" , "36 Month"),
#         ("48 Month" , "48 Month"))
#     desiredRepTenure = models.CharField(max_length=50 , choices=DesiredRepTenure)
#     LoanReqFor = ( 
#         ("Wedding" , "Wedding" ),
#         ("Vacation" , "Vacation"),
#         ("Studies" , "Studies"),
#         ("Other" , "Other"))
#     loanReqFor = models.CharField(max_length=50 , choices=LoanReqFor)
#     AmmountSoughtPKR = models.IntegerField()
#     IncomeAmountPreMonth = models.IntegerField()
    
    
    