# Guia de Documentação — Padrão Markdown

Toda a documentação da disciplina e do projeto integrador deve ser elaborada exclusivamente em **Markdown (.md)**. Este guia define estrutura, formatação e organização dos arquivos.

## Princípios
- Simplicidade e legibilidade primeiro.
- Padronização de títulos e listas para consistência.
- Rastreabilidade via links relativos entre arquivos.

## Organização de Arquivos
- Extensão obrigatória: `.md`.
- Nomes descritivos, curtos e em `kebab-case` ou com `_` (ex.: `plano_semestral.md`, `projeto_integrador_feira_livre.md`).
- Imagens em `imagens/` com nomes claros (ex.: `mapa_bancas.png`).
- Slides em Markdown via **Marp** (ex.: `Feira_Livre_Kickoff.md`).

## Estrutura Recomendada
- Título (`#`), seções com `##`, subseções com `###`.
- Listas com `-` para itens; usar tabelas quando necessário.
- Adicionar "Última atualização: DD/MM/AAAA" ao final.

## Links e Referências
- Usar links relativos: `[Plano_Semestral.md](Plano_Semestral.md)`.
- Referenciar linhas/trechos apenas quando útil, mantendo clareza.

## Imagens e Diagramas
- Inserir imagens com `![Descrição](imagens/arquivo.png)`.
- Diagramas preferenciais: **Mermaid**/PlantUML (como bloco de código) ou exportar de draw.io para PNG/JPG.
- Manter fontes dos diagramas (ex.: `.drawio`) quando possível.

## Slides (Marp)
- Frontmatter mínimo:
  ```
  ---
  marp: true
  theme: requisitos
  class: requisitos, lead
  paginate: true
  footer: 'Nome da Disciplina • Tópico'
  ---
  ```
- Exportação: HTML/PDF gerado a partir do `.md`.

## Checklists
- Consistência de títulos e bullets.
- Ortografia e gramática revisadas.
- Links funcionais e relativos.
- Metadado de atualização preenchido.

## Exemplos
- Ver `Plano_Semestral.md`, `Programa_Oficial.md` e `feira-livre/artefatos/*.md` como referência.

---
Última atualização: 17/01/2026
