from math import sin, cos, acos, sqrt
from haversine import haversine

# Forumal (x2 - x1)**2 + (y2 - y1)**2
def distancia(coord1, coord2):
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]
    
    return sqrt((lat1-lat2)**2+(lon1-lon2)**2)


# Formula Haversine
def geodist(lat1, lon1, lat2, lon2):
    grad_rad = 0.01745329
    rad_grad = 57.29577951
    longitud = lon2 - lon1
    value = (sin(lat1*grad_rad)*sin(lat2*grad_rad)) + (cos(lat1*grad_rad)*cos(lat2*grad_rad)*cos(longitud*grad_rad))
    return value


conexiones = {
    'Ayuntamiento': (40.63366109817389, 0.28537153806529464),
    'La caixa': (40.63582076123997, 0.28272878414060487),
    'Campo futbol': (40.63849977588732, 0.2862456853088551),
    'Sabadell': (40.63639088440736, 0.28350997568020037),
    'Cap': (40.63692611361758, 0.2846182170454564),
    'Spar': (40.63251940927485, 0.28541992251808396),
    'La sala': (40.63492594135365, 0.2815432554030222),
    'Estanco': (40.63522903300719, 0.2799023065768252),
    'Correos': (40.6353043435043, 0.2837816976722523),
}

print(geodist(conexiones['Ayuntamiento'][0],
              conexiones['Ayuntamiento'][1], 
              conexiones['Sabadell'][0],
              conexiones['Sabadell'][1]))

print(haversine(conexiones['Ayuntamiento'], conexiones['Sabadell']))
