class Cara():
  def __init__(self, nome, grana):
    self.nome = nome
    self.grana = grana
  
  def emprestar(self, valor):
    if(self.grana > valor):
      self.grana = self.grana - valor
      return True
    else:
      return False

  def tomar_emprestado(self, valor):
    self.grana = self.grana + valor
    
    
class Calculadora:
  def somar (self, v1,  v2):
		return v1 + v2
  
  def subtrair(self, v1,  v2):
		return v1 - v2
    
  def multiplicar (self,  v1,   v2):
		return v1 * v2
    
  def dividir (self, v1,  v2):
		if (v2 != 0):
			return v1 / v2
		else:
			return -1