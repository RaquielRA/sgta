# 📝 Task Management System (API)

Este projeto é uma API para gerenciamento de livros emprestados a usuários..

## ✨ Funcionalidades

### 👤 Usuários
*   Listagem completa de usuários.
*   Busca detalhada por ID.

### 📋 Biblioteca
*   Listagem total de livros

## 🚦 Endpoints Principais


| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| GET | `/usuarios/` | Lista todos os usuários |
| GET | `/usuarios/<id>/` | Detalhes de um usuário específico |
| GET | `/biblioteca/` | Lista todos os livros |
| GET | `/biblioteca/no_catalogo` | Lista todos os livros no catalogo |