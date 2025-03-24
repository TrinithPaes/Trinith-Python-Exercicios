n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
média = (n1 + n2) / 2
if média < 5:
    print("Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}".format(n1, n2,média))
    print("O aluno esta\033[0;31m REPROVADO.")
elif média >= 5 and média < 6.9:
    print("Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}".format(n1, n2, média))
    print("O aluno está em\033[0;33m RECUPERAÇÂO.")
elif média >= 7:
    print("Tirando {:.1f} e {}, a media do aluno é {:.1f}".format(n1, n2, média))
    print("O aluno está\033[0;34m APROVADO.")
