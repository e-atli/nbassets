MFGSLUG = "generic"
SLUG = "patch-panel-12p-st"
MODEL = "Patch panel 12x ST Port"
U_HEIGHT = "1"
IS_FULL_DEPTH = False

RearPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="Port 1").save()
RearPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="Port [2-5]").save()

NEW_REAR_PORT_TEMPLATE = RearPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="Port 1")
NEW_REAR_PORT_TEMPLATE.type = "2000"
NEW_REAR_PORT_TEMPLATE.positions = "1"
NEW_REAR_PORT_TEMPLATE.save()

NEW_REAR_PORT_TEMPLATE = RearPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="Port [2-5]")
NEW_REAR_PORT_TEMPLATE.type = "2000"
NEW_REAR_PORT_TEMPLATE.positions = "4"
NEW_REAR_PORT_TEMPLATE.save()


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
