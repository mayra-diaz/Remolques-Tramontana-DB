import csv
from random import randint

with open('files/bnames.txt', 'r') as f:
    data = f.read()
bnames = data.split()
bnamesl = len(bnames)-1
with open('files/gnames.txt', 'r') as f:
    data = f.read()
gnames = data.split()
gnamesl = len(gnames)-1
with open('files/random_words.txt', 'r') as f:
    data = f.read()
rwords = data.split()
rwordsl = len(rwords)-1
with open('files/surnames.txt', 'r') as f:
    data = f.read()
surnames = data.split()
surnamesl = len(surnames)-1
with open('files/tipos_herramientas.txt', 'r') as f:
    data = f.read()
therramientas = data.split()
therramientasl = len(therramientas)-1
with open('files/palabras.txt', 'r') as f:
    data = f.read()
palabras = data.split()
palabrasl = len(palabras)-1
with open('files/bd.txt', 'r') as f:
    data = f.read()
cumples = data.split()
cumplesl = len(cumples)-1
with open('files/dates.txt', 'r') as f:
    data = f.read()
fechas = data.split()
fechasl = len(fechas)-1
with open('files/times.txt', 'r') as f:
    data = f.read()
horas = data.split()
horasl = len(horas)-1

pref = ['Jr. ', 'Av. ', 'Calle ', 'Urbanización ', 'Coronel ']
prefl = len(pref)-1
areas = ['Gerencia', 'Comercio', 'Logı́stica', 'Seguridad y limpieza']
cargos = {'Gerencia': 'Admin empresa', 'Comercio': 'Admin ventas', 'Logı́stica': 'Supervisor obras', 'Seguridad y limpieza': 'Viligante'}
unidades = ['kg', 'g', 'mg', 'L', 'mL', 'unidades', 'metros']
colores = ['AMARILLO', 'MOSTAZA', 'AZUL', 'BLANCO', 'GRIS', 'ANARANJADO', 'NEGRO', 'MARRÓN']

cant = 1000000
# nCliente = 1000 # = contactos*cliente
nProveedor = cant # = contactos*proveedor
nEmpleado = int(cant*1.2)
nMaquina = int(cant*1.2)
nTrabajo = int(cant*1.5)
nDirige = int(nTrabajo*1.2)
nBien = cant
# nCompra = 900 || 3*bienes
nRequiere = int(nTrabajo*1.2)
# nCarroceria = 25
# nAsociado = nCarroceria*2

folder = '../1000000/'

""" Cliente """
"""
ruc = 1250610
with open(folder+'cliente.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for i in range(nCliente):
      direccion = pref[randint(0, prefl)] + ' ' + bnames[randint(0, bnamesl)] + ' ' + rwords[randint(0, rwordsl)] + ' ' + gnames[randint(0, gnamesl)]
      razonSocial = rwords[randint(0, rwordsl)] + gnames[randint(0, gnamesl)]
      tsv_writer.writerow([str(ruc), direccion, razonSocial])
      ruc += 27
"""
""" CCliente """
"""
ruc = 1250610
dni = 71457870
cel = 910222340
with open(folder+'ccliente.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for i in range(nCliente):
      nombre = bnames[randint(0, bnamesl)] + ' ' + gnames[randint(0, gnamesl)]
      correo = gnames[randint(0, gnamesl)] + '.' + bnames[randint(0, bnamesl)] + str(i) + '@gmail.com' 
      tsv_writer.writerow([str(dni), nombre, str(cel), correo, str(ruc)])
      ruc += 27
      dni += randint(1, 10)
      cel += randint(1, 10)
"""

""" Proveedor """
ruc = 1250610
pRUCS = []
with open(folder+'proveedor.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for i in range(nProveedor):
      direccion = pref[randint(0, prefl)] + ' ' + bnames[randint(0, bnamesl)] + ' ' + rwords[randint(0, rwordsl)] + ' ' + gnames[randint(0, gnamesl)]
      razonSocial = rwords[randint(0, rwordsl)] + gnames[randint(0, gnamesl)]
      descripcion = rwords[randint(0, rwordsl)] + ' ' + rwords[randint(0, rwordsl)] + ' ' + rwords[randint(0, rwordsl)] + ' ' + rwords[randint(0, rwordsl)]
      tsv_writer.writerow([str(ruc), direccion, razonSocial, descripcion, randint(0, 1)])
      pRUCS.append(ruc)
      ruc += 14
""" CProveedor """
"""dni += randint(0, 10)
cel += randint(0, 10)
with open(folder+'cproveedor.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for i in range(nProveedor):
      nombre = bnames[randint(0, bnamesl)] + ' ' + gnames[randint(0, gnamesl)]
      correo = gnames[randint(0, gnamesl)] + '.' + bnames[randint(0, bnamesl)] + str(i) + '@gmail.com' 
      tsv_writer.writerow([str(dni), nombre, str(cel), correo, str(pRUCS[i])])
      dni += randint(1, 10)
      cel += randint(1, 10)
"""

###############################################
###############################################
###############################################

""" Empleado """
dni = 71457870
fabricantes = []
cel = 910222340
nCuenta = 19123781653924
with open(folder+'empleado.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    fabricadores = int(nEmpleado*0.7)
    for i in range(0, fabricadores):
      nombre = bnames[randint(0, bnamesl)] + ' ' + gnames[randint(0, gnamesl)]
      correo = gnames[randint(0, gnamesl)] + '.' + bnames[randint(0, bnamesl)] + str(i) + '@gmail.com'
      direccion = pref[randint(0, prefl)] + ' ' + bnames[randint(0, bnamesl)] + ' ' + rwords[randint(0, rwordsl)] + ' ' + gnames[randint(0, gnamesl)]
      nacimiento = cumples[randint(0, cumplesl)]
      area = areas[randint(0, 3)]
      cargo = cargos[area]
      sueldo = randint(930, 10000)
      tsv_writer.writerow([str(dni), nombre, str(cel), correo, direccion, nacimiento, nCuenta, area, cargo, str(sueldo)])
      fabricantes.append(dni)
      ruc += 27
      dni += 7
      cel += randint(1, 10)
      nCuenta += randint(1, 210)
    for i in range(fabricadores, nEmpleado):
      nombre = bnames[randint(0, bnamesl)] + ' ' + gnames[randint(0, gnamesl)]
      correo = gnames[randint(0, gnamesl)] + '.' + bnames[randint(0, bnamesl)] + str(i) + '@gmail.com'
      direccion = pref[randint(0, prefl)] + ' ' + bnames[randint(0, bnamesl)] + ' ' + rwords[randint(0, rwordsl)] + ' ' + gnames[randint(0, gnamesl)]
      nacimiento = cumples[randint(0, cumplesl)]
      area = areas[randint(0, 3)]
      cargo = cargos[area]
      sueldo = randint(930, 10000)
      tsv_writer.writerow([str(dni), nombre, str(cel), correo, direccion, nacimiento, nCuenta, area, cargo, str(sueldo)])
      ruc += 27
      dni += 7
      cel += randint(1, 10)
      nCuenta += randint(1, 210)



""" Maquina """
codigo = 1101
mCodigos = []
with open(folder+'maquina.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for i in range(nMaquina):
      descripcion =   therramientas[randint(0, therramientasl)] + ' ' + palabras[randint(0, palabrasl)]+ ' ' + palabras[randint(0, palabrasl)]+ ' ' + palabras[randint(0, palabrasl)]+ ' ' + palabras[randint(0, palabrasl)]
      tsv_writer.writerow([str(codigo), descripcion])
      mCodigos.append(codigo)
      codigo += randint(10, 1000)


""" Trabajo """
tt = {}
with open(folder+'trabajo.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for i in range(nTrabajo):
      descripcion =   therramientas[randint(0, therramientasl)] + ' ' + palabras[randint(0, palabrasl)]+ ' ' + palabras[randint(0, palabrasl)]+ ' ' + palabras[randint(0, palabrasl)]+ ' ' + palabras[randint(0, palabrasl)]
      tstamp = fechas[i] + ' ' + horas[i]
      if tstamp in tt.keys():
        tt[tstamp] = tt[tstamp]+1
      else:
        tt[tstamp] = 1
      tsv_writer.writerow([tstamp, str(tt[tstamp]), descripcion, str(randint(100, 600)/100), str(mCodigos[randint(0, nMaquina-1)])])
      
""" Dirige """
with open(folder+'dirige.tsv', 'wt') as out_file:
  tsv_writer = csv.writer(out_file, delimiter='\t')
  c = 0
  for i in range(nTrabajo):
    tstamp = fechas[i] + ' ' + horas[i]
    tsv_writer.writerow([str(fabricantes[c]), tstamp, randint(1, tt[tstamp])])
    c = c+1 if (c < fabricadores-1) else 0
  for i in range(nDirige-nTrabajo):
    tsv_writer.writerow([str(fabricantes[c]), tstamp, randint(1, tt[tstamp])])
    c = c+1 if (c < fabricadores-1) else 0

""" Bien """
bienes = []
with open(folder+'bien.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for i in range(nBien):
      descripcion =   therramientas[randint(0, therramientasl)] + ' ' + palabras[randint(0, palabrasl)] + ' ' + str(i)
      tsv_writer.writerow([descripcion, str(bool(randint(0, 1))), unidades[randint(0, len(unidades)-1)], str(randint(0, 200)), therramientas[randint(0, therramientasl)]])
      bienes.append(descripcion)

""" Compra """
factura = cant+4
with open(folder+'compra.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for j in range(3):
      for i in range(nBien):
        tsv_writer.writerow([str(factura), bienes[i], fechas[i], str(randint(10, 5000)), str(randint(1, 100)), str(pRUCS[randint(0, nProveedor-1)])])
        factura += 3


""" Requiere """
c = 0
with open(folder+'requiere.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for i in range(nTrabajo):
      tstamp = fechas[i] + ' ' + horas[i]
      tsv_writer.writerow([bienes[c], tstamp, randint(1, tt[tstamp]), randint(1, 10)])
      c = c+1 if (c < nBien-1) else 0
    for i in range(nRequiere-nTrabajo):
      tstamp = fechas[i] + ' ' + horas[i]
      tsv_writer.writerow([bienes[c], tstamp, randint(1, tt[tstamp]), randint(1, 10)])
      c = c+1 if (c < nBien-1) else 0


""" Carroceria """
"""
a = 65
b = 65
c = 65
ruc = 1250610
with open(folder+'carroceria.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for i in range(nCliente):
      placa = chr(a) + chr(b) + chr(c) + '-' + str((100+i)%1000)
      vin = (chr(randint(65, 90))+chr(randint(65, 90))+chr(randint(65, 90))+chr(randint(65, 90))+chr(randint(65, 90)))*3 + chr(randint(65, 90))+chr(randint(65, 90))+ str(i).rjust(8, '0')
      carroceria = 'SEMI REMOLQUE' if (randint(0, 1)) else 'PLATAFORMA'
      categoria = 'N'+str(randint(1, 3)) if (randint(0, 1)) else 'O'+str(randint(1, 3))
      medioPago = 'EFECTIVO' if (randint(0, 1)) else 'TRANSFERENCIA'
      tsv_writer.writerow([placa, vin, categoria, carroceria, str(float(randint(1000, 20000)/1000)), str(float(randint(1000, 3000)/1000)), str(float(randint(1000, 3000)/1000)), str(randint(14, 16)), str(randint(12, 32)), colores[randint(0, len(colores)-1)], str(float(randint(5000, 11000)/1000)), str(float(randint(20000, 50000)/1000)), str(ruc), str(i).rjust(4, '0'), str(float(randint(5000000, 11000000)/100)), medioPago, str(bool(randint(0, 1))), fechas[i]])
      a = a if (b<90) else a+1
      b = b if (c<90) else b+1 if (b<90) else 65
      c = c+1 if (c<90) else 65
      ruc += 27
    ruc = 1250610
    for i in range(nCarroceria-nCliente):
      placa = chr(a) + chr(b) + chr(c) + '-' + str((100+i)%1000)
      vin = (chr(randint(65, 90))+chr(randint(65, 90))+chr(randint(65, 90))+chr(randint(65, 90))+chr(randint(65, 90)))*3 + chr(randint(65, 90))+chr(randint(65, 90))+ str(i).rjust(8, '0')
      carroceria = 'SEMI REMOLQUE' if (randint(0, 1)) else 'PLATAFORMA'
      categoria = 'N'+str(randint(1, 3)) if (randint(0, 1)) else 'O'+str(randint(1, 3))
      medioPago = 'EFECTIVO' if (randint(0, 1)) else 'TRANSFERENCIA'
      tsv_writer.writerow([placa, vin, categoria, carroceria, str(float(randint(1000, 20000)/1000)), str(float(randint(1000, 3000)/1000)), str(float(randint(1000, 3000)/1000)), str(randint(14, 16)), str(randint(12, 32)), colores[randint(0, len(colores)-1)], str(float(randint(5000, 11000)/1000)), str(float(randint(20000, 50000)/1000)), str(ruc), str(i+1).rjust(4, '0'), str(float(randint(5000000, 11000000)/100)), medioPago, str(bool(randint(0, 1))), fechas[i]])
      a = a if (b<90) else a+1
      b = b if (c<90) else b+1 if (b<90) else 65
      c = c+1 if (c<90) else 65
      ruc += 27
"""
""" Asociado """
"""
with open(folder+'asociado.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    fact = 10004
    bieni = 0
    for i in range(nCarroceria):
      tsv_writer.writerow([str(i), str(fact), str(bienes[bieni])])
      tsv_writer.writerow([str(i), str(fact+3), str(bienes[bieni])])
      fact = fact+6 if (fact<factura) else 10004
      bieni = bieni+2 if (bieni < nBien) else 0
      """
