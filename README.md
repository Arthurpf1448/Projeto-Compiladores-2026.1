# Projeto-Compiladores-2026.1
Nosso projeto trata-se de um gerador de HTML. Código HTML, presente em websites, frequentemente envolve repetição de várias estruturas, como Tags, e isto pode ser bastante repetitivo para quem estiver utilizando esta linguagem de marcação em seus projetos. Portanto nosso objetivo é tornar o trabalho envolvendo HTML menos repetitivo e tedioso.

## Como executar (GitHub Codespaces)

1. Clique no botão verde **"Code"**
2. Aba **"Codespaces"**
3. **"Create codespace on main"**.
4. No Terminal, instale a dependência:
   ```bash
   pip install lark
   ```
5. Edite o arquivo `exemplo.dsl` (ou crie o seu próprio arquivo `.dsl`).
6. Rode o compilador:
   - Usando o exemplo padrão (lê `exemplo.dsl` e gera `saida.html`):
     ```bash
     python compilador.py
     ```
   - Indicando arquivos de entrada e saída específicos:
     ```bash
     python compilador.py meu_site.dsl resultado.html
     ```
7. No explorador de arquivos (lado esquerdo), clique com o **botão direito** em
   `saida.html` → **"Download"**.
8. Abra o arquivo `saida.html` baixado no seu navegador.
9. Pronto! Este é o seu site gerado com a nossa DSL.

## Exemplos de programas

### Exemplo 1 — página simples

Entrada (`.dsl`):
```
header {
    h1 "Bem-vindo"
    nav {
        item { href "/" }
        item { href "/sobre" }
    }
}
```

Saída (`.html`):
```html
<header>
    <h1>Bem-vindo</h1>
    <nav>
        <a href="/"></a>
        <a href="/sobre"></a>
    </nav>
</header>
```

### Exemplo 2 — usando `repeat`

Entrada (`.dsl`):
```
main {
    section {
        h2 "Galeria"
        repeat 3 {
            image { src "foto.jpg" }
        }
    }
}
```

Saída (`.html`):
```html
<main>
    <section>
        <h2>Galeria</h2>
        <img src="foto.jpg">
        <img src="foto.jpg">
        <img src="foto.jpg">
    </section>
</main>
```

> O arquivo [`exemplo.dsl`](exemplo.dsl) contém um programa completo demonstrando
> todos os recursos da linguagem.
