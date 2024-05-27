from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    meus_produtos: List[Product]
    minhas_vendas: List[Pedido]
    meus_pedidos: List[Pedido]

class Product(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: User
    produto: Product
    qtd: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'
