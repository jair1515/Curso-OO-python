class Restaurante:
    nome = ''
    cidade = ''
    Ativo = False
    Categoria = ''

restaurantes_praça = Restaurante()
restaurantes_praça.nome = 'IntalHouse'
restaurantes_praça.cidade = 'Intaliana'
restaurantes_praça.Ativo = True

categoria = Restaurante.categoria

print(f'O restaurante {restaurantes_praça.nome} se encontra {restaurantes_praça.Ativo}')
