from django.db import models

class ChurnMoel(models.Model):
    id = models.AutoField(primary_key=True)
    
    class Meta:
        db_table = 'churn'