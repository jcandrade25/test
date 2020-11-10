global MAN_Route
global NY_Route

from scipy import integrate

try:
	if(pd in dir()):
		pass
except NameError:
	import pandas as pd

class busRoute:
	def __init__(self, city):
		self.city = city
		self._routeVelocity = None;	self._routeEnergy = None
		self._avgVelocity = None;	self._stdVelocity = None
		self._avgPower = None;		self._stdPower 	  = None
		self.readData()

	def readData(self):
		data_path = 'routes_data/'
		filename = f'Test_{self.city}(Ibat_Vbat_Tm_Wm_Vel_Dis_Time).csv'
		self.df = pd.read_csv(
					f'{data_path}{filename}',
					names=[
						'Ibat[A]','Vbat[V]','Tm[Nm]','Wm[rad/s]','Vel[m/s]','Dis[m]','t[s]'
					],
					index_col='t[s]', 
					dtype='float64'
				)
		return

	@property
	def routeVelocity(self):
		if self._routeVelocity is None:
			self._routeVelocity = self.df[['Vel[m/s]']]
		return self._routeVelocity


	@property
	def routeEnergy(self):
		if self._routeEnergy is None:
			self.df['P[W]'] = self.df['Vbat[V]']*self.df['Ibat[A]']
			self.df['E[J]'] = self.df['P[W]']*self.df.index
			# self.df['E[J]'] = self.df['P[W]'].apply(lambda p: integrate.trapz(p,self.df.index))
			self._routeEnergy = self.df[['E[J]']]
		return self._routeEnergy

	@property
	def avgVelocity(self):
		if self._avgVelocity is None:
			self._avgVelocity = float(self.routeVelocity.mean(axis=0))
		return self._avgVelocity
	@property
	def stdVelocity(self):
		if self._stdVelocity is None:
			self._stdVelocity = float(self.routeVelocity.std(axis=0))
		return self._stdVelocity

	@property
	def avgPower(self):
		if self._avgPower is None:
			try:
				self._avgPower = float(self.df['P[W]'].mean(axis=0))
			except KeyError:
				self.df['P[W]'] = self.df['Vbat[V]']*self.df['Ibat[A]']
				self._avgPower = float(self.df['P[W]'].mean(axis=0))

		return self._avgPower
	@property
	def stdPower(self):
		if self._stdPower is None:
			try:
				self._avgPower = float(self.df['P[W]'].mean(axis=0))
			except KeyError:
				self.df['P[W]'] = self.df['Vbat[V]']*self.df['Ibat[A]']
				self._stdPower = float(self.df['P[W]'].std(axis=0))
				
		return self._stdPower

	def printRouteInfo(self):
		print(f"""
			Bus Route City: {self.city}
			Bus' Velocity over time:\n {self.routeVelocity}\n
			Bus' Energy usage over time:\n {self.routeEnergy}\n
			Velocity Moments->	average: {self.avgVelocity}m/s	standard deviation: {self.stdVelocity}
			Power Moments ->	average: {self.avgPower}m/s		standard deviation: {self.stdPower}\n 
			"""
		)


MAN_Route = busRoute('Manhatan')
NY_Route  = busRoute('NY')