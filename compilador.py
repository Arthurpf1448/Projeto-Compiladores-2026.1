from lark import Lark, Transformer

analisador = Lark(r"""
start: bloco*

?bloco: head
      | header
      | main
      | footer
      | script

head: "head" "{" head_element* "}"
header: "header" "{" header_element* "}"
main: "main" "{" main_element* "}"
footer: "footer" "{" footer_element* "}"
script: "script" "{" atributo* "}"

?head_element: title
             | meta
             | link

?header_element: h1
               | nav

?main_element: section

?footer_element: paragraph

title: "title" STRING

meta: "meta" "{" atributo* "}"
link: "link" "{" atributo* "}"

h1: "h1" STRING
h2: "h2" STRING
h3: "h3" STRING

nav: "nav" "{" item* "}"

item: "item" "{" atributo* "}"

section: "section" "{" section_content* "}"

?section_content: h2
                | paragraph
                | image
                | article

article: "article" "{" article_content* "}"

?article_content: h3
                | paragraph
                | button

button: "button" "{" atributo* "}"

image: "image" "{" atributo* "}"

paragraph: ("paragraph" | "p") STRING

atributo: IDENT STRING

IDENT: /[a-zA-Z_][a-zA-Z0-9_]*/

%import common.ESCAPED_STRING -> STRING
%import common.WS
%ignore WS
""")

class GeradorHTML(Transformer):
    def _envolver(self, tag, itens):
        """Função auxiliar para criar a tag e indentar o conteúdo interno"""
        conteudo = "\n".join([str(i) for i in itens if i])

        if conteudo:
            conteudo_identado = "\n".join(["    " + linha for linha in conteudo.split("\n")])
            return f"<{tag}>\n{conteudo_identado}\n</{tag}>"
        else:
            return f"<{tag}></{tag}>"

    def start(self, blocos):
        return "\n".join(blocos)

    def head(self, itens): return self._envolver("head", itens)
    def header(self, itens): return self._envolver("header", itens)
    def main(self, itens): return self._envolver("main", itens)
    def footer(self, itens): return self._envolver("footer", itens)
    def nav(self, itens): return self._envolver("nav", itens)
    def section(self, itens): return self._envolver("section", itens)
    def article(self, itens): return self._envolver("article", itens)

    def title(self, s):
        return f"<title>{self._string(s[0])}</title>"

    def h1(self, s): return f"<h1>{self._string(s[0])}</h1>"
    def h2(self, s): return f"<h2>{self._string(s[0])}</h2>"
    def h3(self, s): return f"<h3>{self._string(s[0])}</h3>"
    def paragraph(self, s): return f"<p>{self._string(s[0])}</p>"

    def script(self, attrs):
        attr_str = " ".join(attrs)
        return f"<script {attr_str}></script>".replace("<script ></script>", "<script></script>")

    def meta(self, attrs):
        attr_str = " ".join(attrs)
        return f"<meta {attr_str}>".replace("<meta >", "<meta>")

    def link(self, attrs):
        attr_str = " ".join(attrs)
        return f"<link {attr_str}>".replace("<link >", "<link>")

    def item(self, attrs):
        attr_str = " ".join(attrs)
        return f"<a {attr_str}></a>".replace("<a ></a>", "<a></a>")

    def button(self, attrs):
        attr_str = " ".join(attrs)
        return f"<button {attr_str}></button>".replace("<button ></button>", "<button></button>")

    def image(self, attrs):
        attr_str = " ".join(attrs)
        return f"<img {attr_str}>".replace("<img >", "<img>")

    def atributo(self, children):
        ident = str(children[0])
        valor = self._string(children[1])
        return f'{ident}="{valor}"'

    def _string(self, token):
        return token[1:-1]


codigo = """
head {
    title "Portal de Noticias"
    meta { }
    meta { charset "UTF-8" }
    meta { name "viewport" content "width=device-width, initial-scale=1.0" }
    link { }
    link { rel "stylesheet" href "estilo.css" }
}

header {
    h1 "Jornal Diario"
    nav {
        item { href "/" }
        item { href "/esportes" }
        item { href "/cultura" }
    }
}

main {
    section {
        h2 "Manchete"
        image { }
        image { src "capa.jpg" alt "Capa" }
        article {
            h3 "Economia"
            p "Texto da materia."
            button { }
            button { onclick "ler()" }
        }
    }
    section {
        h2 "Galeria"
        image { src "1.jpg" }
        image { }
        image { src "2.jpg" width "300" }
    }
}

footer {
    p "Rodape do portal"
}

script { }
script { src "main.js" defer "true" }
"""

arvore = analisador.parse(codigo)

html = GeradorHTML().transform(arvore)
print(html)