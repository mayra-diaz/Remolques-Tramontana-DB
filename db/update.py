cant = 1000000
nEmpleado = int(cant*1.2)
fabricadores = int(nEmpleado*0.7)

dni = 71457870
file1 = open("update.txt","w")
for i in range(0, fabricadores):
    file1.write("UPDATE RT1000000.Empleado SET area = 'Fabricacion' WHERE dni =" + str(dni) + "; \n")
    area = 'Fabricación'
    dni += 7