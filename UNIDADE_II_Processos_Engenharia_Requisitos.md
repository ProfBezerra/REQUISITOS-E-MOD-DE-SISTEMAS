# UNIDADE II – Processos da Engenharia de Requisitos (16 h/a)

## 1. Objetivos da Unidade
1. Selecionar técnicas e modelos para a gestão de requisitos em projetos de software.
2. Diagramar requisitos funcionais e não funcionais com o uso de técnicas formais de engenharia de software visando atender demandas sociais.
3. Aplicar coerentemente técnicas de levantamento e construção de ativos de desenho da solução.

## 2. Visão Geral
A unidade cobre o ciclo completo de requisitos: elicitação, análise, gerência e especificação/modelagem. Enfatiza rastreabilidade, qualidade e adequação a contextos sociais (governo, saúde, educação, inclusão, etc.).

## 3. Distribuição das 16 horas (proposta: 8 encontros de 2h)
| Encontro | Tema Principal | Foco | Saída/Entrega |
|----------|----------------|------|---------------|
| 1 | Introdução & Escopo dos Requisitos | Conceitos, stakeholders, visão e contexto social | Mapa de stakeholders + visão inicial |
| 2 | Técnicas de Elicitação (Parte 1) | Entrevistas, brainstorming, workshops, observação | Roteiro de entrevista + lista inicial de requisitos |
| 3 | Técnicas de Elicitação (Parte 2) | Personas, cenários, prototipação, user stories, story mapping | Personas + 5 user stories + esboço de story map |
| 4 | Análise de Requisitos | Classificação (F/NF), conflitos, priorização (MoSCoW, Kano, WSJF simplificado), consistência | Lista priorizada + matriz conflitos/resolução |
| 5 | Gerência de Requisitos | Versionamento, baseline, mudanças, rastreabilidade, ferramentas | Matriz de rastreabilidade inicial |
| 6 | Modelagem & Especificação | Diagrama de classes (UML), relacionamentos, multiplicidade, Modelo CRUD (matriz CR/CRUD) | Diagrama de classes rascunho + matriz CRUD |
| 7 | Qualidade & Validação | Critérios de qualidade (IEEE 29148), testes de requisitos, inspeções, refinamento | Checklist qualidade aplicado aos requisitos |
| 8 | Projeto Integrador | Consolidação: elicitar, analisar, gerir e modelar mini-projeto social | Artefatos consolidados + apresentação rápida |

## 4. Mapeamento Objetivos → Conteúdos
| Objetivo | Conteúdos Associados |
|----------|----------------------|
| 1 | Técnicas de elicitação; priorização; ferramentas de gerência; rastreabilidade |
| 2 | Classificação F/NF; modelagem UML (classes); matriz CRUD; formalização de requisitos |
| 3 | Workshops; entrevistas; personas; story mapping; validação; revisão de qualidade |

## 5. Conteúdo Detalhado por Encontro
### Encontro 1 – Fundamentos & Contexto
- Definição de requisito; diferença entre requisito e solução.
- Tipos: funcionais, não funcionais, de domínio, de negócio.
- Stakeholders: categorias, mapeamento de influência vs interesse.
- Escopo: limites, contexto social (ex.: sistema para agendamento de consultas públicas).
- Artefatos: visão do produto, objetivo social, indicadores de impacto.
- Atividade: identificar 6 stakeholders e 3 metas sociais.

### Encontro 2 – Elicitação (Parte 1)
- Princípios de elicitação: empatia, neutralidade, registro.
- Entrevistas: roteiro, perguntas abertas vs fechadas, riscos de viés.
- Brainstorming e técnicas de criatividade (SCAMPER, 6 chapéus brevemente).
- Workshops/JAD: estrutura, facilitador, time box.
- Observação e shadowing, etnografia leve (quando aplicar).
- Atividade: criar roteiro de 8 perguntas + simulação de entrevista dupla.

### Encontro 3 – Elicitação (Parte 2)
- Personas: formato (objetivos, dores, contexto), anti-persona.
- Cenários e narrativas.
- User Stories: formato "Como <tipo usuário> quero <ação> para <benefício>", INVEST.
- Story Mapping: eixos backbone vs tasks.
- Prototipação de baixa fidelidade (papel / ferramenta simples).
- Atividade: 2 personas + 5 user stories alinhadas + mini story map.

### Encontro 4 – Análise de Requisitos
- Classificação e categorização (funcional, não funcional: desempenho, segurança, usabilidade, conformidade etc.).
- Priorização: MoSCoW, Kano (básico), WSJF simplificado (valor / esforço).
- Detectar conflitos e ambiguidade; critérios para comparação.
- Rastreabilidade inicial: origem → requisito → justificativa.
- Normalização de linguagem: evitar termos vagos (rápido, fácil, seguro...).
- Atividade: aplicar MoSCoW em 10 requisitos; refinar 3 vagos.

### Encontro 5 – Gerência de Requisitos
- Ciclo de vida do requisito: proposta → aceito → baseline → mudança.
- Controle de mudanças (change request): fluxo mínimo.
- Versionamento: referência única (ID), histórico.
- Matriz de rastreabilidade (Requisito ↔ Fonte ↔ Caso de Uso ↔ Classe ↔ Teste).
- Ferramentas (exemplo): Jira, Azure DevOps, Trello (limitações), DOORS NG.
- Atividade: montar 1 matriz simples com 6 requisitos.

### Encontro 6 – Modelagem & Especificação
- Motivação da modelagem: comunicação, alinhamento, base para implementação/teste.
- UML Diagrama de Classes: elementos, associações, multiplicidade, herança, agregação vs composição.
- Modelo CRUD / Matriz CR: relacionar entidades a operações (Create, Read, Update, Delete) para verificar cobertura funcional.
- Especificação estruturada: caso de uso breve vs detalhado.
- Requisitos não funcionais: tabela categorizada com métricas (ex.: tempo de resposta < 2s p/ 95% das requisições).
- Atividade: diagrama de classes inicial + matriz CRUD (tabela entidades x operações).

### Encontro 7 – Qualidade & Validação
- Qualidade de requisitos: clareza, atomicidade, testabilidade, consistência, rastreabilidade.
- Padrões IEEE 830 / 29148 (visão geral): estrutura de SRS.
- Anti-padrões: requisitos compostos, ambíguos, solução disfarçada.
- Técnicas de validação: inspeções, protótipo, testes de aceitacão antecipados.
- Checklist de revisão.
- Atividade: revisar 5 requisitos e marcar problemas + corrigir.

### Encontro 8 – Projeto Integrador
- Consolidação de todos os artefatos.
- Mini-projeto (ex.: Sistema de apoio à triagem social). Entregas: visão, stakeholders, user stories, priorização, diagrama classes, matriz CRUD, rastreabilidade, requisitos NFs.
- Pitch rápido (5 min) com justificativa de decisões.
- Feedback cruzado (pares).
- Atividade: refinamento final e checklist completo.

## 6. Templates e Modelos
### 6.1 Roteiro de Entrevista (Exemplo)
1. Contexto atual do processo?
2. Principais dificuldades?
3. Informações necessárias diariamente?
4. Que decisões dependem de rapidez?
5. Restrições legais ou regulatórias?
6. Volumes (transações/dia)?
7. Erros mais comuns?
8. Expectativa de melhoria? (métrica)

### 6.2 Persona (Formato)
| Campo | Valor |
|-------|-------|
| Nome | Maria (Agente Social) |
| Objetivos | Agilizar triagem de famílias |
| Dores | Perda de dados em planilhas soltas |
| Motivadores | Impacto social rápido |
| Restrições | Pouco tempo de treinamento |

### 6.3 User Story
Como [tipo de usuário] quero [ação] para [benefício].
Ex.: Como agente social quero registrar visita domiciliar para manter histórico confiável.

### 6.4 Critérios INVEST
- I: Independente
- N: Negociável
- V: Valiosa
- E: Estimável
- S: Pequena
- T: Testável

### 6.5 Matriz CRUD (Exemplo)
| Entidade \ Operação | Create | Read | Update | Delete |
|---------------------|--------|------|--------|--------|
| Família | X | X | X | (restrito) |
| Visita | X | X | X | X |
| Benefício | X | X | X | (restrito) |

### 6.6 Matriz de Rastreabilidade (Simplificada)
| Requisito | Origem | User Story | Classe | Caso de Teste |
|-----------|--------|------------|--------|---------------|
| RF-01 Registrar visita | Entrevista Stakeholder A | US-03 | Visita, Família | TC-01 |
| RNF-02 Tempo resposta <2s | Workshop desempenho | - | Infra (API) | TC-Perf-02 |

### 6.7 Checklist Qualidade
| Critério | OK? | Observações |
|----------|-----|-------------|
| Claro | | |
| Não ambíguo | | |
| Testável | | |
| Rastreável | | |
| Consistente | | |
| Sem solução embutida | | |

### 6.8 Estrutura SRS (Resumo)
1. Introdução (Escopo, Propósito, Público)
2. Referências
3. Visão Geral do Produto
4. Funcionalidades (Requisitos Funcionais)
5. Requisitos Não Funcionais
6. Modelos (Diagramas, CRUD, etc.)
7. Restrições
8. Apêndices

## 7. Requisitos Funcionais vs Não Funcionais
- Funcionais: descrevem comportamentos/serviços (ex.: Registrar visita, Gerar relatório).
- Não Funcionais: qualidade/atributos (desempenho, segurança, disponibilidade, conformidade, usabilidade, acessibilidade, escalabilidade).

## 8. Métricas e Exemplos de RNF
| Categoria | Exemplo |
|-----------|---------|
| Desempenho | 95% das requisições de listagem em < 2s |
| Segurança | Autenticação MFA para perfis administrativos |
| Usabilidade | Treinamento máximo de 30 min para novo usuário |
| Disponibilidade | SLA de 99,5% mensal |
| Acessibilidade | Conformidade WCAG 2.1 nível AA |

## 9. Avaliação Sugerida
| Tipo | Peso | Descrição |
|------|------|-----------|
| Exercícios práticos parciais | 30% | Artefatos de encontros 2–7 |
| Projeto integrador | 40% | Conjunto completo de requisitos e modelos |
| Participação/colaboração | 10% | Interações, feedback em pares |
| Revisão crítica (Encontro 7) | 20% | Análise de qualidade de requisitos |

## 10. Estratégias Didáticas
- Alternância teoria ↔ prática.
- Micro-exemplos antes de atividades maiores.
- Feedback imediato (rubrica simples: Completo / Parcial / Revisar).
- Contextualização social para relevância e motivação.

## 11. Ferramentas Recomendas (Opcional)
- Modelagem: Draw.io, PlantUML, Mermaid.
- Gestão: Jira, Trello (limitações para rastreabilidade), Azure DevOps.
- Documentação: Markdown + repositório Git.

## 12. Glossário Rápido
| Termo | Definição |
|-------|-----------|
| Baseline | Conjunto aprovado e congelado de requisitos em uma versão |
| Rastreabilidade | Capacidade de seguir um requisito da origem à implementação/teste |
| Persona | Arquétipo de usuário representativo |
| Story Mapping | Organização de user stories por fluxo e profundidade |
| CRUD | Operações fundamentais sobre dados |

## 13. Perguntas Norteadoras para Discussão
1. Como equilibrar detalhes de requisitos sem engessar inovação?
2. Quais riscos ao não priorizar corretamente requisitos não funcionais?
3. Em que momento formalizar baseline? Quais critérios?
4. Quando usar prototipação vs entrevistas profundas?

## 14. Ajuste: "Modelo CR"
Interpretação adotada: Modelo CRUD (Create, Read, Update, Delete) / Matriz CR para cobertura funcional. Caso "CR" tenha significado distinto (ex.: Classe-Responsabilidade ou Cliente-Requisito), favor esclarecer para adaptação.

## 15. Próximos Passos
1. Validar se a interpretação de "modelo CR" está correta.
2. Refinar exemplos para o domínio social específico escolhido (indicar qual). 
3. Gerar slides a partir desta estrutura (um arquivo por encontro ou consolidado). 
4. Incluir exercícios extras de validação de RNF (testes de carga simulados). 

---
Última atualização: {{DATA}} (substituir pela data corrente ao publicar).
