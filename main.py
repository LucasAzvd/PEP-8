# from fila_normal import FilaNormal
# from fila_prioritaria import FilaPrioritaria
# from pprint import pprint
from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida 

# fila_teste = FilaNormal()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# print(fila_teste.chamacliente(1))
# print(fila_teste.chamacliente(10))

# fila_teste = FilaPrioritaria()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# print(fila_teste.chama_cliente(1))
# print(fila_teste.chama_cliente(10))
# pprint(fila_teste.estatistica('10/01/2020', 198, 'detail'))
# print(fila_teste.estatistica('10/01/2020', 198, 'no_detal'))

teste_fabrica = FabricaFila().pega_fila('prioritaria')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.estatistica(EstatisticaDetalhada('20-10-2020', 10)))