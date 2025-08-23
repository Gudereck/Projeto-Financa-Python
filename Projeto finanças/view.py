import sqlite3 as lite 

con = lite.connect('dados.db')


#funçoes de inserção
# inserir dados na tabela categoria
def inserir_categoria(i):
 with con:
    cur = con.cursor()
    query = "INSERT INTO Categoria(nome) VALUES (?)"
    cur.execute(query,i )

def inserir_Receita(i):
 with con:
    cur = con.cursor()
    query = "INSERT INTO Receitas(categoria, adiconado_em,valor) VALUES (?,?,?)"
    cur.execute(query,i )

def inserir_Gastos(i):
 with con:
    cur = con.cursor()
    query = "INSERT INTO Receitas(categoria, retirado_em,valor) VALUES (?,?,?)"
    cur.execute(query,i )
# ----------------------------------------

#funçoes de delete
def deletar_receita(i):
  with con:
    cur = con.cursor()
    query = "DELETE FROM Receitas WHERE id = ?"
    cur.execute(query,i )

def deletar_gasto(i):
  with con:
    cur = con.cursor()
    query = "DELETE FROM Gastos WHERE id = ?"
    cur.execute(query,i )

def deletar_categoria(i):
  with con:
    cur = con.cursor()
    query = "DELETE FROM Categoria WHERE id = ?"
    cur.execute(query,i )

#funçoes de consulta
def consulta_categoria():
 list_item = []
 with con:
     cur = con.cursor()
     query = "SELECT * FROM Categoria"
     cur.execute(query)
     linha = cur.fetchall()
     for i in linha:
         list_item.append(i)
     return list_item

#ver receitas
def consulta_receita():
    list_item = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM Receitas"
        cur.execute(query)
        linha = cur.fetchall()
        for i in linha:
            list_item.append(i)
        return list_item
    
#ver gastos
def consulta_gasto():   
    list_item = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM Gastos"
        cur.execute(query)
        linha = cur.fetchall()
        for i in linha:
            list_item.append(i)
        return list_item 