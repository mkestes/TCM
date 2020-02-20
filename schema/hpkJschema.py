
from mongothon import Schema

#car_schema = Schema({
#    "make":         {"type": basestring, "required": True},
#    "model":        {"type": basestring, "required": True},
#    "num_wheels":   {"type": int,        "default": 4, "validates": gte(0)}
#    "color":        {"type": basestring, "validates": one_of("red", "green", "blue")}
#})
#
##generate reusable model class from the schema and pymongo collection
#
#Car = create_model(car_schema, db['car'])
#
#
##find, modify, and save a document
#
#car = Car.find_by_id(some_id)
#car['color'] = "green"
#car.save
#
#
##create a new document
#
# car = Car({
#    "make":     "Ford",
#    "model":    "F-150",
#    "color":    "red"
#})
#car.save()



## datafiles are Hydrapak Invoice / Open Orders Reports, intended to be used for shipping information

invoice = Schema({
	"Invoice":		{"type": basestring, "required": False},
	"Date":			{"type": basestring, "required": False},
	"Customer No.":	{"type": basestring, "required": False},
	"Item Code":	{"type": basestring, "required": False},
	"Description": 	{"type": basestring, "required": False},
	"Shipped":		{"type": int,		 "required": True},
	"Revenue":		{"type": int,		 "required": True}
	})

