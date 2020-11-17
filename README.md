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

Para configurar os erros a serem acusados ou ignorados, se cria o arquivo **tox.ini** e passa para ele as informações.