from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from hospital_database import Patient, Base, Hospital
engine = create_engine('sqlite:///patientdata.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

hospital1=Hospital(name = "Delta Hospital")
session.add(hospital1)
session.commit()

patient1 = Patient(
	name = "prakash",
	age = "36",
	disease = "Bypass surgery",
	health_cond = "Good",
	bill = "Arogya sri",
	type_of_drug ="",
	drug_quant= "",
	cost = "1,40,000",
	village = "Vijayawada",
	phone = "9898989898",
	address = "Bhimavaram near ASR nagar",
	patient_id=1,
	)
session.add(patient1)
session.commit()


patient1 = Patient(
	name = "ravi",
	age = "30",
	disease = "",
	health_cond = "Good",
	bill = "Arogya sri",
	type_of_drug ="",
	drug_quant= "",
	cost = "1,40,000",
	village = "Vijayawada",
	phone = "9898989898",
	address = "Bhimavaram near ASR nagar",
	patient_id=1,
	)
session.add(patient1)
session.commit()
print("List of patients are added")