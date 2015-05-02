from ECCO_functions_v2 import *
import os

lo_polo = 140.0
la_polo = 22.0
nc_path = os.path.join('NORA10', 'nc', 'NORA10_DM_11km_tas_2012.nc')
FILE = os.path.join('NORA10', 'h5', 'weights.h5')
metacsv = os.path.join('NORA10', 'csv', 'meta.csv')
dirname = os.path.join('NORA10', 'shp')

Catchment_Weights_Meta(nc_path, lo_polo, la_polo, FILE, metacsv, dirname, 
                       sbar=False, cordex=False)


