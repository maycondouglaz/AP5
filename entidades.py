class Aluno :
  def __init__(self, n, r) :
    self.nome = n
    self.registro = r
    self.atividades = []

  def getTotal(self) :
    tot = 0
    for carga in self.atividades :
      tot = tot + carga.getCarga()
    return tot
		
class Atividade :
	def __init__(self, titulo, duracao) :
		self.titulo = titulo
		self.duracao = duracao
		self.estado = 1

	def getCarga(self) :
		if self.estado == 4 :
			return self.duracao
		else :
			return 0

	def aprova(self) :
		self.estado = 4

  