import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base= declarative_base()
class Hospital(Base):
	__tablename__ = 'hospital'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	@property
	def serialize(self):
		return{
		'name': self.name,
		'id': self.id
		}


class Patient(Base):
	__tablename__ = 'patient'

	name = Column(String(100), nullable=False)
	id = Column(Integer, primary_key=True)
	age = Column(Integer)
	disease = Column(String(250))
	health_cond = Column(String(250))
	bill = Column(String(250))
	type_of_drug = Column(String(250))
	drug_quant = Column(String(250))
	cost = Column(Integer)
	village = Column(String(100))
	phone = Column(Integer)
	address = Column(String(250))
	patient_id = Column(Integer, ForeignKey('hospital.id'))
	hospital = relationship(Hospital)
	@property
	def serialize(self):
		return{
			'name':self.name,
			'age':self.age,
			'id':self.id,
			'disease':self.disease,
			'health_cond':self.health_cond,
			'bill':self.bill,
			'type_of_drug':self.type_of_drug,
			'drug_quant':self.drug_quant,
			'cost':self.cost,
			'village':self.village,
			'phone':self.phone,
			'address':self.address,
			'patient_id':self.patient_id
			}
engine = create_engine('sqlite:///patientdata.db')
Base.metadata.create_all(engine)