def diagSintoma(paciente:dict)->dict:
    enfermedad = 0
    if paciente['diag_ta'] == 'Si':
        if paciente['diag_pa'] == 'Si':
            if paciente['diag_do'] == 'Si':
                if paciente['diag_dg'] == 'Si':
                    if paciente['diag_dc'] == 'Si':
                        enfermedad = 'Malaria'
                    else:
                        enfermedad = 1
                else:
                    enfermedad = 1
            else:
                enfermedad = 1
        else:
            if paciente['diag_do'] == 'Si':
                enfermedad = 1
            else:
                if paciente['diag_dg'] == 'Si':
                    if paciente['diag_dc'] == 'Si':
                        enfermedad = 'Gripa'
                    else:
                        enfermedad = 1
                else:
                    enfermedad = 1
    else:
        if paciente['diag_pa'] == 'Si':
            if paciente['diag_do'] == 'Si':
                if paciente['diag_dg'] == 'Si':
                    if paciente['diag_dc'] == 'Si':
                        enfermedad = 1
                    else:
                        enfermedad = 'Otitis'
                else:
                    enfermedad = 1
            else:
                enfermedad = 1

        else:
            if paciente['diag_do'] == 'Si' or paciente['diag_dg'] == 'Si' or paciente['diag_dc'] == 'Si':
                enfermedad = 1
            else:
                enfermedad = 0

    if isinstance(enfermedad,int):
        estado = False
        if enfermedad == 0:
            enfermedad = 'No tiene síntomas'
        else:
             enfermedad = 'Presencia de síntomas'
    else:
        estado = True

    return {'id_diagnostico':paciente['id_diagnostico'],'resultado':enfermedad,'estado': estado}
