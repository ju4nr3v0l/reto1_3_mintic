def realizarPedido(sopa: str, plato_principal: str, bebida: str, postre: str) -> dict:
    total = 0
    if sopa != '':
        total += 3000
    if plato_principal != '':
        if plato_principal == 'Pollo apanado':
            total += 7000
        else:
            total += 8000
    if bebida != '':
        if bebida == 'Jugo de uva':
            total += 2000
        else:
            total += 1500
    if postre != '':
        if postre == 'Merengón':
            total += 5000
        else:
            total += 4000

    if (postre != '' and postre == 'Merengón' and plato_principal != '' and plato_principal == 'Pollo apanado') or (postre != '' and postre == 'Merengón' and sopa != '' and sopa == 'Sopa de pastas'):
        total = total * 0.7

    return {'sopa':sopa, 'plato principal':plato_principal, 'bebida':bebida,'postre':postre,'total':total}
