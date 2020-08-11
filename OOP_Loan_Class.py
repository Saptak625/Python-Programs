import math
class Loan:
	def __init__(self, principal, interest_rate, time, pmt=None):
		self.principal=principal
		self.interest_rate=interest_rate
		self.time=time
		if pmt==None:
			self.pmt(False)
		else:
			self.pmt=pmt
	def pmt(self, display=True):
		#Check here next. PMT seems not be executing properly
		p=self.principal
		r=float(self.interest_rate/12)
		n=self.time
		numerator=float(p*(r*((1+r)**n)))
		denominator= float(((1+r)**n)-1)
		pmt=float(math.ceil(float(numerator/denominator)*100)/100)
		self.pmt=pmt
		if display==True:
			print(pmt)
	def r_exec(self, time_disp=True, m_interest_disp=True, t_interest_disp=True, principal_disp=True):
		principal=int(self.principal)
		print("Loan Details")
		print(f"Principal: {principal}")
		print(f"Annual Interest Rate: {self.interest_rate}")
		print(f"Time: {self.time}")
		print(f"Monthly Payment: {self.pmt}")
		t_interest=0
		for t in range(self.time):
			print("")
			if time_disp==True:
				print(f"Month: {t+1}")
			interest=(self.interest_rate/12)*principal
			t_interest=round(t_interest+interest,2)
			if m_interest_disp==True:
				print(f"Interest this month: {round(interest,2)}")
			if t_interest_disp==True:
				print(f"Total Interest Accrued: {t_interest}")
			principal=principal-self.pmt+interest
			if principal_disp==True:
				if principal<=0:
					print(f"Loan finished after {t+1} months.")
					break
				else:
					print(f"Principal after payment: {round(principal,2)}")
loan_1=Loan(300000,0.039,360)
loan_1.r_exec()