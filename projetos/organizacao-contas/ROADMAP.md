# Organização de Contas — Roadmap

## Stack

- Twilio WhatsApp Sandbox (recebimento de mensagens)
- n8n rodando local via Docker (depois migração pra AWS via Terraform)
- Google Sheets via API (armazenamento e relatório)
- Terraform (provisionamento da infraestrutura na AWS)
- Jenkins (pipeline de CI/CD: build, teste e deploy automático)

## Arquitetura

```mermaid
flowchart LR
    A[WhatsApp do usuário] -->|mensagem de gasto| B[Twilio WhatsApp Sandbox]
    B -->|webhook| C[n8n]
    C -->|parse do texto| D{Validação}
    D -->|válido| E[Google Sheets API]
    D -->|inválido| F[Resposta de erro via WhatsApp]
    E --> G[Planilha de gastos]
    G --> H[Relatório]

    I[git push] --> J[Jenkins]
    J -->|terraform apply / deploy| K[AWS EC2 - n8n hospedado]
```

## Etapas

| # | Etapa | Status |
|---|-------|--------|
| 1 | Docker + n8n rodando localmente | Concluído |
| 2 | Twilio WhatsApp Sandbox configurado | Concluído |
| 3 | Webhook Twilio → n8n recebendo mensagens | Concluído |
| 4 | Parsing do texto da mensagem (valor + categoria) | Concluído |
| 5 | Integração com Google Sheets API | Pendente |
| 6 | Geração de relatório | Pendente |
| 7 | Provisionar infraestrutura na AWS via Terraform (hospedagem) | Pendente |
| 8 | Pipeline CI/CD com Jenkins (build, teste e deploy automático) | Pendente |
