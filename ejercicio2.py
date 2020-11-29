sueldo_base = 950000
sueldo_tr = int(input("Ingresar Sueldo Trabajador: "))

ded_base = (8 * sueldo_tr) / 100
sal_ded = sueldo_tr - ded_base
ded_extra = 0
if sueldo_tr < int(2000000):
    ded_extra = (1.5 * sueldo_tr) / 100
elif sueldo_tr > int(2000000):
    ded_extra = (1.5 * sueldo_tr) / 100

sal_ded -= ded_extra 
tot_ded = ded_extra + ded_base

print("Salario base trabajador: ", sueldo_tr)
print("Salario con deducciones: ", sal_ded)
print("Total Deducido: ", tot_ded)
