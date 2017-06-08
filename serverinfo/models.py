from django.db import models
import UnixTimestampField

# Create your models here.

class jids(models.Model):
    jid = models.CharField(max_length=255, unique=True)
    load = models.TextField()

    class Meta:
        db_table = 'jids'

class salt_events(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.CharField(max_length=255, db_index=True)
    data = models.TextField()
    alter_time = UnixTimestampField.UnixTimestampField()
    master_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'salt_events'

class salt_returns(models.Model):
    fun = models.CharField(max_length=50, db_index=True)
    jid = models.CharField(max_length=255, db_index=True)
    return_field = models.TextField(db_column='return')
    minion_id = models.CharField(max_length=255, db_index=True)
    success = models.CharField(max_length=10)
    full_ret = models.TextField()
    alter_time = UnixTimestampField.UnixTimestampField()

    class Meta:
        db_table = 'salt_returns'
