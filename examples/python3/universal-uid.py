import uuid
u = uuid.uuid1()
print(u)           # 882dad92-5385-11e9-90e9-0028f821ff7f
print(str(u))      # 882dad92-5385-11e9-90e9-0028f821ff7f
print(u.__str__()) # 882dad92-5385-11e9-90e9-0028f821ff7f
print(type(u))     # <class 'uuid.UUID'>
print(u.hex)       # 882dad92538511e990e90028f821ff7f
print(u.int)       # 181012181235403912317722105794514780031
print(u.urn)       # urn:uuid:882dad92-5385-11e9-90e9-0028f821ff7f
print(u.version)   # 1
print(u.variant)   # specified in RFC 4122
