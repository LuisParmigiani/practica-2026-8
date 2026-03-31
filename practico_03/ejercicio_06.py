"""Magic Methods"""

from __future__ import annotations
from typing import List


# NO MODIFICAR - INICIO
class Article:
    """Agregar los métodos que sean necesarios para que los test funcionen.
    Hint: los métodos necesarios son todos magic methods
    Referencia: https://docs.python.org/3/reference/datamodel.html#basic-customization
    """

    def __init__(self, name: str) -> None:
        self.name = name

    # NO MODIFICAR - FIN

    # Completar
    def __repr__(self) -> str:
        return f"Article('{self.name}')"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Article):
            return False
        return self.name == other.name



# NO MODIFICAR - INICIO
class ShoppingCart:
    """Agregar los métodos que sean necesarios para que los test funcionen.
    Hint: los métodos necesarios son todos magic methods
    Referencia: https://docs.python.org/3/reference/datamodel.html#basic-customization
    """

    def __init__(self, articles: List[Article] = None) -> None:
        if articles is None:
            self.articles = []
        else:
            self.articles = articles

    def add(self, article: Article) -> ShoppingCart:
        self.articles.append(article)
        return self

    def remove(self, remove_article: Article) -> ShoppingCart:
        new_articles = []

        for article in self.articles:
            if article != remove_article:
                new_articles.append(article)

        self.articles = new_articles

        return self

    # NO MODIFICAR - FIN

    # Completar
    def __str__(self) -> str:
        return str([articulo.name for articulo in self.articles])
    
    def __repr__(self) -> str:
        return f"ShoppingCart([{','.join(repr(a) for a in self.articles)}])" #esto es como compresion de listas pero más eficiente
    #debería devolver ShoppingCart([Article('Manzana'), Article('Pera')]) para poder cumplir

    def __eq__(self, other) -> bool:
        if not isinstance(other, ShoppingCart):
            return False
    # Copias para no modificar los originales
        self_articles = self.articles[:]
        other_articles = other.articles[:]
        if len(self_articles) != len(other_articles):
            return False
    # Para cada artículo en self, buscá uno igual en other y sacalo
        for articulo in self_articles:
            for i, otro in enumerate(other_articles):
                if articulo == otro:
                    del other_articles[i]
                    break
            else:
                return False  # No se encontró un match. si, se pueden hacer else para for en python para que se ejecute si el for terminó normalmente sin break
        return not other_articles  # Debe quedar vacío si son iguales. not verifica falsedad (en listas, verifica [])

    def __add__(self, other) -> ShoppingCart:
        if not isinstance(other, ShoppingCart):
            return NotImplemented
        new_articles = self.articles + other.articles
        return ShoppingCart(new_articles)
    
# NO MODIFICAR - INICIO

manzana = Article("Manzana")
pera = Article("Pera")
tv = Article("Television")

# Test de conversión a String
assert str(ShoppingCart().add(manzana).add(pera)) == "['Manzana', 'Pera']"

# Test de reproducibilidad
carrito = ShoppingCart().add(manzana).add(pera)
assert carrito == eval(repr(carrito))

# Test de igualdad
assert ShoppingCart().add(manzana) == ShoppingCart().add(manzana)

# Test de remover objeto
assert ShoppingCart().add(tv).add(pera).remove(tv) == ShoppingCart().add(pera)

# Test de igualdad con distinto orden
assert ShoppingCart().add(tv).add(pera) == ShoppingCart().add(pera).add(tv)

# Test de suma
combinado = ShoppingCart().add(manzana) + ShoppingCart().add(pera)
assert combinado == ShoppingCart().add(manzana).add(pera)

# NO MODIFICAR - FIN
