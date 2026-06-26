head {
    title "Portal de Noticias"
    meta { charset "UTF-8" }
    meta { name "viewport" content "width=device-width, initial-scale=1.0" }
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
        image { src "capa.jpg" alt "Capa" }
        article {
            h3 "Economia"
            p "Texto da materia."
            button { onclick "ler()" }
        }
    }
    section {
        h2 "Galeria"
        repeat 4 {
            image { src "foto.jpg" }
        }
    }
}

footer {
    p "Rodape do portal"
}

script { src "main.js" defer "true" }
