print('=-='*3,'Amostragem de categoria do atleta','=-='*3)

idadeAtleta = (2023 - int(input('Digite o ano de nascimento do atleta: ')))

if idadeAtleta > 25:
    print('O atleta possui {} anos, sua categoria é: MASTER.'.format(idadeAtleta))
elif idadeAtleta >= 19:
    print('O atleta possui {} anos, sua categoria é: SÊNIOR.'.format(idadeAtleta))
elif idadeAtleta >= 14:
    print('O atleta possui {} anos, sua categoria é: JÚNIOR.'.format(idadeAtleta))
elif idadeAtleta >= 9:
    print('O atleta possui {} anos, sua categoria é: INFANTIL.'.format(idadeAtleta))
elif idadeAtleta < 9:
    print('O atleta possui {} anos, sua categoria é: MIRIM.'.format(idadeAtleta))
