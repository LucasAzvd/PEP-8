# Curso sobre PEP 8 e Boa Programação

Arquivos gerados do curso da Alura sobre boa programação em python. 

--- 

### TypeHint: 
É uma notação que auxilia ao desenvolvedor qual o tipó da variável. Notação:
1. VARIAVEL: TIPO  
2. FUNCAO()->TIPO RETORNO:    

Ex:  
```python
variavel_numero: int
def funcao_retorna_string(argumento1)->str:
    return str("Frase")
```

Quando se tem mai de um retorno na função, para criar o typehint utilizamos o **Union** da biblioteca typing, podendo retornar tipos e até mesmo classes.
Ex:  
```python
from typing import Union


def funcao_retorna_string(argumento1) -> Union[RETORNO_1, RETORNO_2]:
    return str("Frase")
```

Quando se trabalha com Listas e Dicionários, temos que import da biblioteca **typing** o tipo _List_ e _Dict_.  
Ex:  
```python
from typing import Dict, Union, List


def funcao_retorna_string(argumento1) -> Union[RETORNO_1, RETORNO_2]:  
    estatistica: Dict[str, Union[List[str], str, int]] = {}
```

---

### Mypy
Mypy é uma biblioteca do python que verifica se o código está seguindo as boas normas e principalmente o **TypeHint** que foi definido. 

Para usar o mypy executa:  
`mypy ARQUIVO.py`

---

### Flake8
É uma biblioteca do python para verificar se o código segue o padrão da PEP-8.

Para executar:  
`flake8 ARQUIVO.py`  
E ele aponta na saída onde não se segue a norma e como corrigir.  

Se quiser filtrar por tipo de erro (para olhar os códigos de erro, verificar documentação):  
`flake8 --select CODIGO_ERRO ARQUIVO.py`  

Ou ignorar erros:  
`flake8 --ignore CODIGO_ERRO ARQUIVO.py`  

Para configurar os erros a serem acusados ou ignorados, se cria o arquivo **tox.ini** e passa para ele as informações. Existe como configurar para que commits sejam barrados caso o falke8 identifique algo fora do padrão.    

---

### Classe abstratas
São classes que são como um contrato, a classe mãe cria métodos abstratos e obriga que a classe filha tenha os mesmos métodos. Além de obrigar a usar as mesmas classes obriga também a usar as mesmas variáveis e os mesmos tipos.

### Método Template
São métodos presentes na classe mãe que não sibescritos pela classe filha, mas são utilizados por ela.