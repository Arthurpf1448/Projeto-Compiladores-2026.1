# Projeto-Compiladores-2026.1
Nosso projeto trata-se de um gerador de HTML. Código HTML, presente em websites, frequentemente envolve repetição de várias estruturas, como Tags, e isto pode ser bastante repetitivo para quem estiver utilizando esta linguagem de marcação em seus projetos. Portanto nosso objetivo é tornar o trabalho envolvendo HTML menos repetitivo e tedioso.

# Equipe:
Arthur Pontes  
Júlia Rodrigues  
Maria Luiza  
Luca Fiorenzano  

## Como executar (GitHub Codespaces)

1. Clique no botão verde **"Code"**
2. Clique na aba **"Codespaces"**
3. Clique em **"Create codespace on main"**
4. No terminal, instale a dependência:
   ```bash
   pip install lark
   ```
5. Edite a parte "codigo" do projeto ou utilize o exemplo existente
6. No terminal, digite:
   ```bash
   python projeto.py
   ```
7. Copie e cole o código gerado num arquivo .txt e mude seu formato para .html e abra-o. Ou, se preferir, utilize algum testador online de HTML. Ex: https://www.lncc.br/~borges/php/testar.html
8. Pronto! Este é o seu site gerado com a nossa DSL.

## Exemplos de programas  

# 1. Site simples com um texto de Boas vindas  
```bash
codigo = """
   header {
       h1 "Bem-vindo"
       nav {
           item { href "/" }
           item { href "/sobre" }
       }
   }
"""
```
Código gerado:  
```bash
<header>
    <h1>Bem-vindo</h1>
    <nav>
        <a href="/"></a>
        <a href="/sobre"></a>
    </nav>
</header>
```
Resultado:  

![Site de Boas vindas](img_site01.png)  

# 2. Página de uma receita de bolo  
```bash
codigo = """
head {
    title "Receita de Bolo de Cenoura"
    meta { charset "UTF-8" }
}

header {
    h1 "Bolo de Cenoura com Cobertura de Chocolate"
}

main {
    section {
        h2 "Ingredientes da Massa"
        p "3 cenouras medias raladas"
        p "4 ovos"
        p "Meia xicara de oleo"
        p "2 xicaras e meia de farinha de trigo"
        p "2 xicaras de acucar"
        p "1 colher de sopa de fermento em po"
    }
    
    section {
        h2 "Modo de Preparo"
        article {
            h3 "Passo 1: Mistura liquida"
            p "Bata no liquidificador as cenouras, os ovos e o oleo ate obter uma mistura homogenea."
        }
        article {
            h3 "Passo 2: Mistura seca"
            p "Em uma tigela, junte a farinha e o acucar. Despeje o liquido do liquidificador e mexa bem."
        }
        article {
            h3 "Passo 3: Forno"
            p "Adicione o fermento delicadamente. Asse em forno pre-aquecido a 180°C por 40 minutos."
        }
    }

    section {
        image { src "https://upload.wikimedia.org/wikipedia/commons/c/ca/Peda%C3%A7o_de_Bolo_de_Cenoura%2C_08-12-2020.jpg" alt "Fatia de bolo de cenoura" width "400" }
    }
}
"""
```
Código gerado:  
```bash
<head>
    <title>Receita de Bolo de Cenoura</title>
    <meta charset="UTF-8">
</head>
<header>
    <h1>Bolo de Cenoura com Cobertura de Chocolate</h1>
</header>
<main>
    <section>
        <h2>Ingredientes da Massa</h2>
        <p>3 cenouras medias raladas</p>
        <p>4 ovos</p>
        <p>Meia xicara de oleo</p>
        <p>2 xicaras e meia de farinha de trigo</p>
        <p>2 xicaras de acucar</p>
        <p>1 colher de sopa de fermento em po</p>
    </section>
    <section>
        <h2>Modo de Preparo</h2>
        <article>
            <h3>Passo 1: Mistura liquida</h3>
            <p>Bata no liquidificador as cenouras, os ovos e o oleo ate obter uma mistura homogenea.</p>
        </article>
        <article>
            <h3>Passo 2: Mistura seca</h3>
            <p>Em uma tigela, junte a farinha e o acucar. Despeje o liquido do liquidificador e mexa bem.</p>
        </article>
        <article>
            <h3>Passo 3: Forno</h3>
            <p>Adicione o fermento delicadamente. Asse em forno pre-aquecido a 180°C por 40 minutos.</p>
        </article>
    </section>
    <section>
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/Peda%C3%A7o_de_Bolo_de_Cenoura%2C_08-12-2020.jpg" alt="Fatia de bolo de cenoura" width="400">
    </section>
</main>
```
Resultado:  

![Site de Receita de bolo](img_site02.png)  
