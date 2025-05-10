from django.db import models

# <<-------------------proxy model (farzi-model)--------------->>

from django.db import models
from datetime import date

class mainproxy(models.Model):
    name = models.CharField(max_length=50)
    email=models.EmailField()
    contact = models.IntegerField()

    def _str_(self):
        return self.name

class farziproxy(mainproxy):
    class Meta:
        proxy=True


    def _str_(self):
        return self.name

# -------------------------meta class-------------------


# from django.db import models
# from datetime import date

# class student(models.Model):
#     name = models.CharField(max_length=50)
#     email=models.EmailField()
#     contact = models.IntegerField()
#     city=models.CharField(max_length=50)

#     # class meta ki help se work------------
#     # claa meta ka use kisi bhi class ke internal kaam ko change karne ke liye use hota hai,uske behaviour ko define karta hai
#     class Meta:
#         db_table='Student'   #db.sqlite me table ka naam change 
#         verbose_name='new student'  #admin panel me jo dikhega wo name change 
#         verbose_name_plural='new student'  #admin panel me jo dikhega wo name change 's' hatane ke liye
#         ordering=['id'] #id ki help se order hoga like 1,2,3,4
#         ordering=['-id'] #id ki help se order hoga like 4,3,2,1
#         ordering=['name'] #name ki help se order hoga like a,b,c,d
#         ordering=['-name']  #name ki help se order hoga like d,c,b,a
        


#     def _str_(self):
#         return self.name
