# Gerenciador de Acólitos ⛪

Aplicativo desktop para auxiliar na escala de acólitos de uma igreja.

## Funcionalidades

### Aba Escala
- Criação de horários de escala com data, hora e descrição opcional
- Lista de acólitos ordenada por número de escalas (crescente)
- Adicionar/remover acólitos de cada horário
- Botão **Finalizar Escala**: gera texto formatado para publicação (copiável) e registra no histórico

**Exemplo de texto gerado:**
```
ESCALA DA SEMANA

Quarta-feira, 04/03 - 18:30:
Andrew e Jonas

Sábado, 07/03 - 19:30:
Missa solene
Edmilson
```

### Aba Eventos
- Cadastro de eventos gerais (ex: reunião) com data obrigatória e hora opcional
- Gerenciar quais acólitos não participaram de um evento
- Registrar participação para contabilizar no histórico de cada acólito

### Aba Acólitos
- Cadastro, edição e exclusão de acólitos
- Registrar faltas (data + descrição)
- Suspender (razão + duração) e levantar suspensão
- Dar/Usar bônus com descrição registrada como movimentação
- Editar bônus diretamente sem registrar movimentação
- **Fechar Semestre**: reseta faltas de todos (com opção de resetar bônus)
- **Gerar Relatório PDF**: PDF completo com estado de cada acólito (escalas, eventos, faltas, suspensões, bônus)

## Instalação

```bash
pip install -r requirements.txt
```

> Requer Python 3.8+ e `tkinter` (normalmente já incluso no Python).  
> Para Ubuntu/Debian: `sudo apt-get install python3-tk`

## Uso

```bash
python3 main.py
```

Os dados são salvos automaticamente em `acolitos_data.json` na pasta do projeto.
