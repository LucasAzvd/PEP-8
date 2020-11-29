from typing import Dict, Union, List

from fila_base import FilaBase
from constantes import CODIGO_NORMAL
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada


Classes = Union[EstatisticaResumida, EstatisticaDetalhada] 

class FilaNormal(FilaBase):
    def gera_senha_atual(self) -> None:  # TypeHint: Retorno
        self.senhaatual = f'{CODIGO_NORMAL}{self.codigo}'

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senhaatual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop()
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')

    def estatistica(self, retorna_estatistica: Classes) -> dict:
        return retorna_estatistica.roda_estatistica(self.clientes_atendidos)
