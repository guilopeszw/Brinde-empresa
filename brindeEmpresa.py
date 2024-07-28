qtdIngressos = 0
genero = str(input("Digite o gênero com qual você se identifica: ")
             ).lower().strip()
# homem:
if genero == "homem" or genero == "h":
    qtdIngressos = 1
    time = str(input("Para qual time você torce? ")).lower().strip()
    estadoCivil = str(input("Informe seu estado civil: ")).lower().strip()
    if estadoCivil == "casado":
        qtdIngressos == qtdIngressos + 1
    elif estadoCivil == "namoro" or estadoCivil == "namorando" or estadoCivil == "solteiro" or estadoCivil == "noivo":
        qtdIngressos = 1
    temFilhos = str(input("Você tem filhos(as)? ")).lower().strip()
    if temFilhos == "sim" or temFilhos == "s":
        qtdFilhos = int(input("Informe quantos filhos você têm: "))
        if qtdFilhos > 0:
            qtdIngressos = qtdIngressos + qtdFilhos
    if qtdFilhos > 0 and estadoCivil == "casado":
        print(f"Parabéns! Você recebeu {qtdIngressos} ingressos para o próximo jogo do {time.capitalize()}. Os ingressos são\
 direcionados para você, sua(seu) parceira(o) e seus {qtdFilhos} filhos. Divirtam-se! =)")
    elif qtdFilhos > 0 and estadoCivil == "solteiro" or "namorando" or "namoro" or "noivo":
        print(f"Parabéns! Você recebeu {qtdIngressos} ingressos para o próximo jogo do {time.capitalize()}.\
Os ingressos são direcionados para você e seus {qtdFilhos} filhos(as). Divirtam-se! =)")
    elif qtdFilhos == 0 and estadoCivil == "casado":
        print(f"Parabéns! Você ganhou {qtdIngressos} para o próximo jogo do {time.capitalize()}.\
Os ingressos são direcionados para você e sua(seu) parceira(o). Divirtam-se! =)")
    elif qtdFilhos == 0 and estadoCivil == "solteiro" or "namorando" or "namoro" or "noivo":
        print(f"Parabéns! Você ganhou {qtdIngressos} para o próximo jogo do {
              time.capitalize()}. Divirta-se! =)")
if genero == "mulher" or "m":
    qtdIngressos = 1
    filme = str(input("Informe qual filme você deseja assistir: ")).lower().strip()
    estadoCivil = str(input("Informe seu estado civil: ")).lower().strip()
    if estadoCivil == "casada":
        qtdIngressos == qtdIngressos + 1
    elif estadoCivil == "namoro" or estadoCivil == "namorando" or estadoCivil == "solteira" or estadoCivil == "noiva":
        qtdIngressos = 1
    temFilhos = str(input("Você tem filhos(as)? ")).lower().strip()
    if temFilhos == "sim" or temFilhos == "s":
        qtdFilhos = int(input("Informe quantos filhos você têm: "))
        if qtdFilhos > 0:
            qtdIngressos = qtdIngressos + qtdFilhos
    if qtdFilhos > 0 and estadoCivil == "casado":
        print(f"Parabéns! Você recebeu {qtdIngressos} ingressos para o filme {filme.upper()}. Os ingressos são\
 direcionados para você, seu(sua) parceiro(a) e seus {qtdFilhos} filhos. Divirtam-se! =)")
    elif qtdFilhos > 0 and estadoCivil == "solteiro" or "namorando" or "namoro" or "noivo":
        print(f"Parabéns! Você recebeu {qtdIngressos} ingressos para o filme {filme.upper()}.\
 Os ingressos são direcionados para você e seus {qtdFilhos} filhos(as). Divirtam-se! =)")
    elif qtdFilhos == 0 and estadoCivil == "casado":
        print(f"Parabéns! Você ganhou {qtdIngressos} para o filme {filme.upper()}.\
 Os ingressos são direcionados para você e seu(sua) parceiro(a). Divirtam-se! =)")
    elif qtdFilhos == 0 and estadoCivil == "solteiro" or "namorando" or "namoro" or "noivo":
        print(f"Parabéns! Você ganhou {qtdIngressos} para o filme {filme.upper()}. Divirta-se! =)")
