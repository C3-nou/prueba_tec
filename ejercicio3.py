import math
prim_lugar_punt = 3 * 28
seg_lugar_punt = 6 * 16
ter_lugar_punt = 4 * 7
tt_punt = prim_lugar_punt + seg_lugar_punt + ter_lugar_punt
tt_operacion = ( tt_punt + (16*2) ) - math.sqrt(ter_lugar_punt)
print("Total de puntos obtenidos: ", tt_punt)
print("Total de puntos obtenidos primer lugar: ", prim_lugar_punt)
print("Puntaje total con operaciones: ", (tt_punt + (16*2)))