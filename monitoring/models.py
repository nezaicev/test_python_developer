from django.db import models

# Create your models here.


class Dumps(models.Model):
    side_number=models.CharField(primary_key=True, max_length=50,unique=True)
    dump_model=models.CharField(max_length=50)
    max_tonnage=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.side_number

class Parametrs(models.Model):
    dump=models.ForeignKey(Dumps,db_index=True, on_delete=models.CASCADE)
    tonnage=models.PositiveSmallIntegerField()

    def __str__(self):
        return  self.dump_id
