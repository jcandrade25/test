####Inputs
	###Route
	###Bus type (depending of charging method)
	###Passangers 

####Outputs
###Route data
	##Cards
		##Length
		##Bus daily distance
		##Number of cycles per day
	##Graphs
		#Vel vs t (line)
		#Avg vel vs time of the day (bar)
###Bus info (depending of charging method)
	##Graphs
		#E vs Distance (line)
		#E vs time of day (bar)
		#Efficiency (line)
		#Range of operation (?) [km]

######################################################

import pandas as pd
RouteName = "C850"

Bus = {
	'overnight':'L12',
	'opportunity':'K9'
}

Passangers = [80,48,24]

EnergyDistance=[,,]

for i in range(length(EnergyDistance)):
	EnergyDistance[i]=pd.read_excel(
		f'Energy-Distance {RouteName}.xls',
		sheet_name=i,
		index_col=1,
		names=['Distance','Energy'])

EnergyDistance