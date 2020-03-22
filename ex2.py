
class Figura:
  def area(self):
    return 0

class Triangulo(Figura):
  def __init__(self, base, altura):
    self.__base=base
    self.__altura=altura

  def area(self):
    return ((self.__base * self.__altura)/2)

class Quadrado(Figura):
  def __init__(self, lado):
    self.__lado=lado

  def area(self):
    return self.__lado * self.__lado

class Circulo(Figura):
  def __init__(self, raio):
    self.__raio = raio
  
  def area(self):
    return 3.14 * self.__raio * self.__raio



class CalculadoraFesta:
  def __init__(self , numeroPessoas, decoracaoDiferenciada):
     self.__numeroPessoas=numeroPessoas
     self.__decoracaoDiferenciada=decoracaoDiferenciada
  
  @property
  def numeroPessoas(self):
    return self.__numeroPessoas

  def calcularValorComidas(self):
    return self.__numeroPessoas * 25

  def calcularValorDecoracao(self):
    if (self.__decoracaoDiferenciada):
      return 50 + self.__numeroPessoas * 15
    else:
      return 30 + self.__numeroPessoas * 7.5

  def calcularTotalFesta(self):
    return 0

class EscritaEmBolo:
  def __init__(self,tamanhoBolo,  textoBolo):
    self.__tamanhoBolo=tamanhoBolo
    self.__textoBolo=textoBolo

  @property
  def tamanhoBolo(self):
    return self.__tamanhoBolo

  def setTamanhoBolo(self, tamanhoBolo):
    if (tamanhoBolo != 8 and tamanhoBolo != 16):
      print("Desculpe, mas nao trabalhamos como bolos de " , tamanhoBolo , " cm (apenas 8 ou 16 cm) " )
    else:
      self.__tamanhoBolo = tamanhoBolo
  
  def setTextoBolo(self, textoBolo):
    if(tamanhoBolo == 8 and len(textoBolo) > 0 and len(textoBolo) <= 16):
      self.__textoBolo = textoBolo
    elif (tamanhoBolo == 16 and len(textoBolo) > 0 and len(textoBolo) <= 40):
      self.__textoBolo = textoBolo
    else:
      print("Desculpe, mas nao é possivel escrever '" , textoBolo , "' ( " + textoBolo.Length , " letras) em um bolo de " , tamanhoBolo + " cm")
  
  def calcularPrecoEscrita(self):
    return 0.25 * len(self.__textoBolo)
    
#bolo =  EscritaEmBolo(8, "alo mamae!")
#print("> " + bolo.textoBolo)

class CalculadoraFestaAniversario(CalculadoraFesta):
  def __init__(self,numPessoas,  decDiferenciada,  textoBolo):
    super().__init__(numPessoas,  decDiferenciada)
    if (numPessoas <= 4):
      self.__tamanhoBolo = 8
    else:
      self.__tamanhoBolo = 16
    self.__escritaEmBolo =  EscritaEmBolo(self.__tamanhoBolo, textoBolo)
  
  def calcularPrecoBolo(self):
    precoBolo = 0
    if (self.__escritaEmBolo.tamanhoBolo == 8):
      precoBolo= 40
    elif (self.__escritaEmBolo.tamanhoBolo == 16):
      precoBolo= 75
    return precoBolo
    
  def calcularTotalFesta(self):
     valorFesta = self.calcularValorComidas() + self.calcularValorDecoracao()
     valorFesta += self.calcularPrecoBolo()+ self.__escritaEmBolo.calcularPrecoEscrita()
     return valorFesta

class CalculadoraFestaCoquetel(CalculadoraFesta):
  def __init__(self, numPessoas,decDiferenciada,bebidaSaudavel):
    super().__init__(numPessoas,  decDiferenciada)
    self.__bebidaSaudavel=bebidaSaudavel
  
  def calcularValorBebidas(self):
    if (self.__bebidaSaudavel):
      return super().numeroPessoas * 5
    else:
      return super().numeroPessoas * 20
      
  def calcularDescontoPercentual(self):
    if (self.__bebidaSaudavel):
      return 5
    else:
      return 0
  
  def calcularTotalFesta(self):
    valorFesta = self.calcularValorComidas() + self.calcularValorBebidas() + self.calcularValorDecoracao()
    valorFesta -= valorFesta * self.calcularDescontoPercentual() / 100
    return valorFesta


