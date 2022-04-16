

entregas = []

dias = ('viernes','sabado','domingo')
print()

for i in dias:
    entregas.append(int(input(f'ingresa el nº de entregas del dìa {i} ==> ')))
    
print()
tarifa = (300,300,200)


def cobr_viernes():
    subtotal_viernes = entregas[0] * tarifa[0]
    return subtotal_viernes
def cobr_sabado():
    subtotal_sabado = entregas[1] * tarifa[1]
    return subtotal_sabado
def cobr_domingo():
    subtotal_domingo = entregas[2] * tarifa[2]
    return subtotal_domingo

tot_entr = 0

for i in entregas:
    tot_entr =tot_entr + i


if tot_entr >= 20:
    tot_cobr =cobr_viernes() +cobr_sabado() +cobr_domingo()+ 1000
else:
    tot_cobr =cobr_viernes() +cobr_sabado() +cobr_domingo()

print()
print(f'VIERNES  -- {entregas[0]} entregas -- ${cobr_viernes()} cobrados ')
print(f'SABADO   -- {entregas[1]}  entregas -- ${cobr_sabado()}  cobrados')
print(f'DOMINGO  -- {entregas[2]} entregas -- ${cobr_domingo()} cobrados')

print()

print(f'ENTREGA SEMANAL ==> {tot_entr} ---INGRESO TOTAL ==> $ {tot_cobr}')
print()
if __name__ == '__main__':
     cobr_viernes()
   













