
class JaMatriculadoException(Exception):
  def __ini__(nome):
    super().__ini__()
    self.__nome=nome
  
  @property
  def nome(self):
    return self.__nome

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
  
  def __getitem__(self, item):
    return self.__alunos[item]
  
  def __len__(self):
    return len(self.__alunos)
  
  def addAluno(self, aluno):
    if(not self.alunoJaMatriculado(aluno.nome) ):
      self.__alunos.append(aluno)
    else:
      raise JaMatriculadoException(aluno.nome) 

  def getAluno(self, posicao):
    return self.__alunos[posicao]
  
  def alunoJaMatriculado(self, nome):
    tem_o_aluno= False
    for aluno in self.__alunos:
      if (aluno.nome == nome):
        tem_o_aluno = True;
    return tem_o_aluno

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
