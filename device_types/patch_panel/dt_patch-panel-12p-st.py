MFGSLUG = "generic"
SLUG = "patch-panel-12p-st"
MODEL = "Patch Panel 12 Ports ST"
U_HEIGHT = "1"
IS_FULL_DEPTH = False

NEW_REAR_PORT_TENPLATE = RearPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="Port 1/2")
#NEW_REAR_PORT_TEMPLATE = RearPortTemplate.objects.get(device_type_id=NEW_DEVICE_TYPE.id, name="Port 1/2")
NEW_REAR_PORT_TEMPLATE.type = "2000"
NEW_REAR_PORT_TEMPLATE.positions = "1"
NEW_REAR_PORT_TEMPLATE.save()

NEW_FRONT_PORT_TEMPLATE = FrontPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, rear_port_id=NEW_REAR_PORT_TEMPLATE.id, name="Port 1/2")
NEW_FRONT_PORT_TEMPLATE.type = "2000"
NEW_FRONT_PORT_TEMPLATE.rear_port_position = "1"
NEW_FRONT_PORT_TEMPLATE.save()




#RearPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="Port 3/4").save()
#NEW_REAR_PORT_TEMPLATE = RearPortTemplate.objects.get(device_type_id=NEW_DEVICE_TYPE.id, name="Port 3/4")
#NEW_REAR_PORT_TEMPLATE.type = "2000"
#NEW_REAR_PORT_TEMPLATE.positions = "1"
#NEW_REAR_PORT_TEMPLATE.save()###
#
#FrontPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, rear_port_id=NEW_REAR_PORT_TEMPLATE.id, name="Port 3/4", rear_port_position="1").save()

#RearPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="Port 5/6").save()#
#NEW_REAR_PORT_TEMPLATE = RearPortTemplate.objects.get(device_type_id=NEW_DEVICE_TYPE.id, name="Port 5/6")
#NEW_REAR_PORT_TEMPLATE.type = "2000"
#NEW_REAR_PORT_TEMPLATE.positions = "1"
#NEW_REAR_PORT_TEMPLATE.save()

#RearPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="Port 7/8").save()
#NEW_REAR_PORT_TEMPLATE = RearPortTemplate.objects.get(device_type_id=NEW_DEVICE_TYPE.id, name="Port 7/8")
#NEW_REAR_PORT_TEMPLATE.type = "2000"
#NEW_REAR_PORT_TEMPLATE.positions = "1"
#NEW_REAR_PORT_TEMPLATE.save()

#RearPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="Port 9/10").save()
#NEW_REAR_PORT_TEMPLATE = RearPortTemplate.objects.get(device_type_id=NEW_DEVICE_TYPE.id, name="Port 9/10")
#NEW_REAR_PORT_TEMPLATE.type = "2000"
#NEW_REAR_PORT_TEMPLATE.positions = "1"
#NEW_REAR_PORT_TEMPLATE.save()

#RearPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="Port 11/12").save()
#NEW_REAR_PORT_TEMPLATE = RearPortTemplate.objects.get(device_type_id=NEW_DEVICE_TYPE.id, name="Port 11/12")
#NEW_REAR_PORT_TEMPLATE.type = "2000"
#NEW_REAR_PORT_TEMPLATE.positions = "1"
#NEW_REAR_PORT_TEMPLATE.save()

#PORT_TYPE_8P8C = 1000
#PORT_TYPE_110_PUNCH = 1100
#PORT_TYPE_ST = 2000
#PORT_TYPE_SC = 2100
#PORT_TYPE_SC_APC = 2110
#PORT_TYPE_FC = 2200
#PORT_TYPE_LC = 2300
#PORT_TYPE_LC_APC = 2310
#PORT_TYPE_MTRJ = 2400
#PORT_TYPE_MPO = 2500
#PORT_TYPE_LSH = 2600
#PORT_TYPE_LSH_APC = 2610
#PORT_TYPE_CHOICES = [
 
#  |  device_type_id = <django.db.models.query_utils.DeferredAttribute object>
# |  get_type_display = _method(self, *, field=<django.db.models.fields.PositiveSmallIntegerField: type>)
# |
# |  id = <django.db.models.query_utils.DeferredAttribute object>
# |  name = <django.db.models.query_utils.DeferredAttribute object>
# |  positions = <django.db.models.query_utils.DeferredAttribute object>
# |  type = <django.db.models.query_utils.DeferredAttribute object>



 #|  device_type_id = <django.db.models.query_utils.DeferredAttribute object>
 #|  get_type_display = _method(self, *, field=<django.db.models.fields.PositiveSmallIntegerField: type>)
 #|
 #|  id = <django.db.models.query_utils.DeferredAttribute object>
 #|  name = <django.db.models.query_utils.DeferredAttribute object>
 #|  rear_port_id = <django.db.models.query_utils.DeferredAttribute object>
 #|  rear_port_position = <django.db.models.query_utils.DeferredAttribute object>
 #|  type = <django.db.models.query_utils.DeferredAttribute object>
 