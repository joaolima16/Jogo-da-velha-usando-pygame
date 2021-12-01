import pygame,sys
from pygame.locals import *

class JogoVelha(object):

	ULTIMO_INICIAR_PC = True # primeiro jogo sempre player joga primeiro

	JOGO = [0,
			[' '],[' '],[' '],
			[' '],[' '],[' '],
			[' '],[' '],[' '],]

	PADROES_VENCE = [[7,8,9],[4,5,6],[1,2,3],
					 [7,4,1],[8,5,2],[9,6,3],
					 [7,5,3],[9,5,1]]

	ESQUERDO = 1

	BRANCO 		  = (255, 255, 255)
	PRETO 		  = (  0,   0,   0)
	CINZA 		  = (128, 128, 128)
	PRATA 		  = (192, 192, 192)
	VERMELHO 	  = (255,   0,   0)
	VERDE 		  = (  0, 128,   0)
	LIMA 		  = (  0, 255,   0)
	AZUL 		  = (  0,   0, 255)
	AZUL_ESCURO   = (  0,   0, 128)
	AMARELO 	  = (255, 255,   0)
	AQUA 		  = (  0, 255, 255)
	MAGENTA 	  = (255,   0, 255)
	MARROM 		  = (128,   0,   0)
	AZUl_PETROLEO = (  0, 128, 128)
	ROXO 		  = (128,   0, 128)
	OLIVA 		  = (128, 128,   0)

	ESPESSURA = 5

	ESPACO_O = [0,( 10, 290, 110, 110),
				  (145, 290, 110, 110),
				  (290, 290, 110, 110),
				  ( 10, 145, 110, 110),
				  (145, 145, 110, 110),
				  (290, 145, 110, 110),
				  ( 10,  10, 110, 110),
				  (145,  10, 110, 110),
				  (290,  10, 110, 110)]

	ESPACO_X = [0,
				[[( 10, 290),(110, 390)],[( 10, 390),(110, 290)]],
				[[(145, 290),(245, 390)],[(145, 390),(245, 290)]],
				[[(290, 290),(390, 390)],[(290, 390),(390, 290)]],
				[[( 10, 145),(110, 245)],[( 10, 245),(110, 145)]],
				[[(145, 145),(245, 245)],[(145, 245),(245, 145)]],
				[[(290, 145),(390, 245)],[(290, 245),(390, 145)]],
				[[( 10,  10),(110, 110)],[(110,  10),( 10, 110)]],
				[[(145,  10),(245, 110)],[(145, 110),(245,  10)]],
				[[(290,  10),(390, 110)],[(290, 110),(390,  10)]],
				]

	POSICOES = {
				7:{'x':[  0, 125],'y':[  0, 125]},
				8:{'x':[125, 275],'y':[  0, 125]},
				9:{'x':[275, 420],'y':[  0, 125]},
				4:{'x':[  0, 125],'y':[125, 275]},
				5:{'x':[125, 275],'y':[125, 275]},
				6:{'x':[275, 420],'y':[125, 275]},
				1:{'x':[  0, 125],'y':[275, 420]},
				2:{'x':[125, 275],'y':[275, 420]},
				3:{'x':[275, 420],'y':[275, 420]}
				}

	pygame.init()
	pygame.display.set_caption('Jogo da Velha com AI')

	TELA = pygame.display.set_mode((420,420))
	BACKGROUND = pygame.Surface(TELA.get_size())

	BACKGROUND = BACKGROUND.convert()

	def verifica_vence(self,atual,desenha=False):
		campeao = ''
		padrao_vencedor = []
		campeao = False
		for pos in self.PADROES_VENCE:
			if(atual[pos[0]]==atual[pos[1]]==atual[pos[2]]=='O'): 
				campeao = 'O'
				padrao_vencedor = pos
			if(atual[pos[0]]==atual[pos[1]]==atual[pos[2]]=='X'): 
				campeao = 'X'
				padrao_vencedor = pos
		if len(self.checa_livres(atual)) == 0: campeao = ' '
		if desenha and campeao in ['O','X']:
			self.desenha_linha_vencedor(padrao_vencedor)
		return campeao

	def reseta_jogo(self):
		for i in range(1,len(self.JOGO)):
			self.JOGO[i] = ' '

	def checa_livres(self,atual):
		livres = []
		for i in range(1,len(atual)):
			if atual[i] == ' ': livres.append(i)
		return livres

	def move_ai(self,atual,player):
		oponente = 'O' if player == 'X' else 'X'
		ganho = 0
		perda = 0
		if len(self.checa_livres(atual)) == 9: return 5
		for pos in self.checa_livres(atual):
			atual[pos] = player
			if self.verifica_vence(atual) == player:
				ganho = pos
			atual[pos] = ' '
		for pos in self.checa_livres(atual):
			atual[pos] = oponente
			if self.verifica_vence(atual) == oponente:
				perda = pos
			atual[pos] = ' '
		if ganho > 0: return ganho
		if perda > 0: return perda
		move = self.negamax(atual,player,9)
		return move

	def negamax(self,atual,player,terminal):
		oponente = 'O' if player=='X' else 'X'
		melhor_valor = -float('inf') # infinito negativo para que qualquer valor seja maior que ele
		melhor_posicao = 0
		if terminal > 0:
			if self.verifica_vence(atual) == player: return 1
			elif self.verifica_vence(atual) == oponente: return -1
			elif self.verifica_vence(atual) == ' ': return 0
		else: return 0
		for pos in self.checa_livres(atual):
			atual[pos] = player
			valor = -self.negamax(atual,oponente,terminal-1)
			if valor > melhor_valor:
				melhor_valor = valor
				melhor_posicao = pos
			atual[pos] = ' '
		return melhor_posicao

	def cria_linhas(self):
		pygame.draw.line(self.BACKGROUND, self.PRETO, (  0, 125), (420, 125), self.ESPESSURA)
		pygame.draw.line(self.BACKGROUND, self.PRETO, (  0, 275), (420, 275), self.ESPESSURA)
		pygame.draw.line(self.BACKGROUND, self.PRETO, (125,   0), (125, 420), self.ESPESSURA)
		pygame.draw.line(self.BACKGROUND, self.PRETO, (275,   0), (275, 420), self.ESPESSURA)

	def posicao_clique(self,mouse_pos):
		x,y = mouse_pos
		clique = 0

		for i in range(1,len(self.POSICOES)+1):
			if self.POSICOES[i]['x'][0] <= x <= self.POSICOES[i]['x'][1] and self.POSICOES[i]['y'][0] <= y <= self.POSICOES[i]['y'][1]:
				clique = i
		return clique

	def marca_o_em(self,pos):
		pygame.draw.ellipse(self.BACKGROUND, self.AZUL, self.ESPACO_O[pos], self.ESPESSURA)
		self.JOGO[pos] = 'O'

	def marca_x_em(self,pos):
		pygame.draw.line(self.BACKGROUND, self.VERDE, self.ESPACO_X[pos][0][0], self.ESPACO_X[pos][0][1], self.ESPESSURA)
		pygame.draw.line(self.BACKGROUND, self.VERDE, self.ESPACO_X[pos][1][0], self.ESPACO_X[pos][1][1], self.ESPESSURA)
		self.JOGO[pos] = 'X'

	def desenha_linha_vencedor(self,padrao):
		x_ini = (self.POSICOES[padrao[0]]['x'][0]+self.POSICOES[padrao[0]]['x'][1])/2
		y_ini = (self.POSICOES[padrao[0]]['y'][0]+self.POSICOES[padrao[0]]['y'][1])/2
		x_fin = (self.POSICOES[padrao[2]]['x'][0]+self.POSICOES[padrao[2]]['x'][1])/2
		y_fin = (self.POSICOES[padrao[2]]['y'][0]+self.POSICOES[padrao[2]]['y'][1])/2
		desenho = (x_ini,y_ini),(x_fin,y_fin)
		pygame.draw.line(self.BACKGROUND, self.VERMELHO, desenho[0], desenho[1], self.ESPESSURA)

	def main(self):
		while True:
			self.BACKGROUND.fill(self.BRANCO)
			self.cria_linhas()
			player_joga = False
			if self.ULTIMO_INICIAR_PC:
				player_joga = True
			self.ULTIMO_INICIAR_PC = not self.ULTIMO_INICIAR_PC
			while not self.verifica_vence(self.JOGO):
				if player_joga:
					while True:
						escolheu = False
						for event in pygame.event.get():
							if event.type == QUIT:
								pygame.quit()
								sys.exit()
							elif event.type == pygame.MOUSEBUTTONUP and event.button == self.ESQUERDO:
								self.marca_o_em(self.posicao_clique(event.pos))
								escolheu = True
								break
						if escolheu: break
					player_joga = False
				else:
					self.marca_x_em(self.move_ai(self.JOGO,'X'))
					player_joga = True
				self.TELA.blit(self.BACKGROUND,(0,0))
				pygame.display.update()
			vencedor = self.verifica_vence(self.JOGO,True)
			self.TELA.blit(self.BACKGROUND,(0,0))
			pygame.display.update()
			print ("vencedor")
			self.reseta_jogo()
jogoVelha = JogoVelha()
jogoVelha.main()