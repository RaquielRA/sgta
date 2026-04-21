# 📝 Task Management System (API)

Este projeto é uma API para gerenciamento de tarefas e usuários, permitindo o controle de prioridades, status e prazos de entrega através do Django.

## 🚀 Sobre o Projeto
A aplicação gerencia o ciclo de vida de tarefas vinculadas a usuários, fornecendo diversos filtros dinâmicos via JSON para facilitar a visualização de pendências, urgências e atrasos.

## ✨ Funcionalidades

### 👤 Usuários
*   Listagem completa de usuários.
*   Busca detalhada por ID.

### 📋 Tarefas
*   Listagem total de tarefas.
*   Filtros por status (Abertas, Em andamento, Concluídas, Canceladas).
*   Filtros por prioridade (Urgente, Não Urgente).
*   Listagem de tarefas **atrasadas** (data de entrega menor que hoje e não concluídas).
*   Busca textual por título.

## 🛠 Tecnologias
*   Python 3
*   Django Framework
*   SQLite

## 🚦 Endpoints Principais


| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| GET | `/usuarios/` | Lista todos os usuários |
| GET | `/usuarios/<id>/` | Detalhes de um usuário específico |
| GET | `/tarefas/` | Lista todas as tarefas |
| GET | `/tarefas/abertas/` | Apenas tarefas com status 'ABERTA' |
| GET | `/tarefas/prioridade/<prioridade>/` | Filtra por prioridade (ex: urgente) |
| GET | `/tarefas/atrasadas/` | Tarefas fora do prazo |
| GET | `/tarefas/busca/<termo>/` | Filtra tarefas pelo título |
