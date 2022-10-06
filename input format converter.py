from obspy import UTCDateTime, Trace, Stream
import pandas as pd
from PyQt5.QtWidgets import QFileDialog
import numpy as np
import os
#%%___________USER INPUT______________________________
Date=input("Enter event date in YYYY-MM-DD format (eg.:2015-04-25 ) : ")
Time=input("Enter event time in hh:mm:ss format (eg.06:11:00) : ")
event_time=Date+'T'+Time
dt=input("Enter sampling time step (eg. 0.01) : ")
dt=float(dt)
net=input('Network ID: ') 
Loc=input("Location ID: ")
stn=input('Station ID: ')
print("\nSupported formats: MSEED, SAC, GSE2, SACXY, Q, SH_ASC, SLIST, TSPAIR, PICKLE, SEGY, SU, WAV, AH\n")
Out=input('Enter output format (write in lowercase, e.g mseed) : ')
f_name=input("Enter file name: ")

#%%___________________________________________________
cwd=os.getcwd()
DATA=pd.read_csv(cwd+'\\input.csv')
EW=np.array(DATA.E)
EW=EW.flatten()
EW= EW.astype('float32')

NS=np.array(DATA.N)
NS=NS.flatten()
NS= NS.astype('float32')

UD=np.array(DATA.Z)
UD=UD.flatten()
UD= UD.astype('float32')

# Fill header attributes

stats_EW = {'network': net, 
         'station': stn, 
         'location': Loc,
         'channel': "E", 
         'npts': len(EW), 
         'delta': dt,
         'mseed': {'dataquality': 'D'}}
stats_NS = {'network': net, 
         'station': stn, 
         'location': Loc,
         'channel': "N", 
         'npts': len(NS), 
         'delta': dt,
         'mseed': {'dataquality': 'D'}}
stats_UD = {'network': net, 
         'station': stn, 
         'location': Loc,
         'channel': "V", 
         'npts': len(UD), 
         'delta': dt,
         'mseed': {'dataquality': 'D'}}

# set current time
stats_EW['starttime'] = UTCDateTime(event_time)
stats_NS['starttime'] = UTCDateTime(event_time)
stats_UD['starttime'] = UTCDateTime(event_time)
st_EW = Stream([Trace(data=EW, header=stats_EW)])
st_NS = Stream([Trace(data=NS, header=stats_NS)])
st_UD = Stream([Trace(data=UD, header=stats_UD)])
#Compiling traces
st=st_EW+st_NS+st_UD
st.write(f_name+'.'+Out.lower(), format=Out.upper()) 



