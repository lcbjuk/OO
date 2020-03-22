class Aluno:
  def __init__(self,nome,nota):
    self.__nome=nome
    self.__nota=nota
  @property
  def nome(self):
    return self.__nome
  @nome.setter
  def nome(self,nome):
    self.__nome=nome

  @property
  def nota(self):
    return self.__nota
  @nota.setter
  def nota(self,nota):
    sefl.__nota=nota

class CadastroAlunos:
  def __init__(self):
    self.__alunos = []
  
  def addAluno(self, aluno):
    self.__alunos.append(aluno)

  def getAluno(self, posicao):
    return self.__alunos[posicao]

  def ordenaCalculaMedia(self):
    media = 0
    for i in range(0,len(self.__alunos),1):
      media += self.__alunos[i].nota
      for j in range(i+1,len(self.__alunos),1): 
        if (self.__alunos[i].nota > self.__alunos[j].nota):
          swap = self.__alunos[i]
          self.__alunos[i] = self.__alunos[j]
          self.__alunos[j] = swap;
      media /= len(self.__alunos)
      return media  
      
  def imprimeLista(self):
    for i in range(0,len(self.__alunos),1):
      print(self.__alunos[i].nome , ":" , self.__alunos[i].nota)


class CalculadoraFesta:
  def __init__(self,  numPessoas ,bebSaudavel,decDiferenciada):
    self.__numeroPessoas = numPessoas
    self.__bebidaSaudavel = bebSaudavel
    self.__decoracaoDiferenciada =decDiferenciada
  
  def __calcularValorComidas(self):
    return self.__numeroPessoas * 25
  
  def __calcularValorBebidas(self):
    if (self.__bebidaSaudavel):
      return self.__numeroPessoas * 5
    else:
      return self.__numeroPessoas * 20
  
  def __calcularValorDecoracao(self):
    if (self.__decoracaoDiferenciada):
      return 50 + self.__numeroPessoas * 15
    else:
      return 30 + self.__numeroPessoas * 7.5

  def __calcularDescontoPercentual(self):
    if (self.__bebidaSaudavel):
      return 5
    else:
      return 0

  def calcularTotalFesta(self):
    valorFesta=  self.__calcularValorComidas() + self.__calcularValorBebidas()+ self.__calcularValorDecoracao()
    valorFesta-= valorFesta * self.__calcularDescontoPercentual() / 100
    return valorFesta
