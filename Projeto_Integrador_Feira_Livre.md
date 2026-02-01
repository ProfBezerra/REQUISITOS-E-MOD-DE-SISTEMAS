# Projeto Integrador — Site da Feira Livre

## 1. Visão do Produto
Um site informativo e de apoio à **Feira Livre** local, voltado a feirantes, organizadores e visitantes. O objetivo é disponibilizar dados confiáveis sobre datas, localização, bancas, produtos e agenda, com foco em **acessibilidade, usabilidade e transparência**.

## 2. Objetivos
- Centralizar informações oficiais da feira.
- Facilitar a descoberta de **feirantes** e **produtos/categorias**.
- Exibir **mapa das bancas** e informações de localização/acesso.
- Publicar **agenda de eventos** e destaques.
- Promover comunicação básica (contato/sugestões).

## 3. Stakeholders
- **Feirantes**: cadastro/visibilidade dos produtos.
- **Organizadores**: gestão de calendário, regras e comunicação.
- **Visitantes/Clientes**: busca e navegação por produtos/categorias.
- **Prefeitura/Órgãos Públicos**: alinhamento com normas e segurança.
- **Admin do Site/Equipe TI**: manutenção, qualidade e evolução.
- **Comunicação/Marketing**: divulgação de eventos.

## 4. Escopo Inicial
- Público-alvo: comunidade local e visitantes.
- Plataforma: web (desktop e mobile).
- Sem transações financeiras; foco informativo.
- Conteúdo básico: feirantes, produtos, categorias, agenda, localização, contato.

## 5. Personas (Template)
| Campo | Valor |
|---|---|
| Nome | Ana, Visitante |
| Objetivos | Encontrar produtos/artesãos específicos |
| Dores | Informação espalhada e desatualizada |
| Motivadores | Economia local, artesanato, alimentação |
| Restrições | Acesso via celular, tempo curto |

| Campo | Valor |
|---|---|
| Nome | João, Feirante |
| Objetivos | Divulgar produtos e bancas |
| Dores | Baixa visibilidade |
| Motivadores | Aumentar fluxo de clientes |
| Restrições | Pouca familiaridade com tecnologia |

## 6. User Stories (Exemplos)
- Como visitante quero **buscar produtos por categoria** para encontrar itens rapidamente.
- Como visitante quero **ver o mapa das bancas** para localizar feirantes na feira.
- Como feirante quero **editar meus dados e produtos** para manter informações atualizadas.
- Como organizador quero **publicar o calendário da feira** para informar o público.
- Como administrador quero **aprovar novos cadastros** para garantir a confiabilidade.

## 7. Priorização (MoSCoW) — Rascunho
- **Must**: Página de feira (datas/local), catálogo de feirantes e produtos, busca, agenda.
- **Should**: Mapa das bancas, categorias e filtros, contato.
- **Could**: Destaques e eventos temáticos, avaliações públicas simples.
- **Won't** (por ora): E-commerce, pagamentos, logística.

## 8. Requisitos Funcionais (RF) — Esboço
- RF-01: Exibir página principal com **informações da feira** (datas, horário, local, regras).
- RF-02: **Listar feirantes** com campos essenciais (nome, categoria, banca, contatos).
- RF-03: **Listar produtos** com descrição e categoria.
- RF-04: **Buscar** por produto/categoria com filtros.
- RF-05: Exibir **agenda** com as próximas datas/eventos.
- RF-06: Exibir **mapa das bancas** com identificação dos feirantes.
- RF-07: Página de **contato/sugestões**.
- RF-08: Área **admin** (mínima) para aprovar/editar cadastros.
- RF-09: Exibir **destaques** (feirantes/produtos/eventos) na home.
- RF-10: **Exportar** calendário (iCal) opcional.

## 9. Requisitos Não Funcionais (RNF)
- Desempenho: 95% das páginas informativas em < 2s.
- Disponibilidade: 99,5% mensal (meta de projeto).
- Acessibilidade: **WCAG 2.1 nível AA** (contraste, navegação por teclado, alt text, etc.).
- Segurança/Privacidade: **LGPD** para dados pessoais (feirantes/admins).
- Usabilidade: linguagem simples; protótipo validado com 3 usuários.
- Portabilidade: compatível com navegadores modernos; responsivo mobile.

## 10. Modelo de Dados (Esboço)
- **Feirante**(id, nome, categoria, bancaId, contato, descrição)
- **Produto**(id, nome, categoriaId, feiranteId, descrição)
- **Categoria**(id, nome, tipo)
- **Feira**(id, nome, datas, localId, regras)
- **Banca**(id, número, feiraId, localização)
- **Local**(id, nome, endereço, mapa)
- **Agenda**(id, data, evento, descrição, feiraId)
- **Avaliação**(id, feiranteId, nota, comentário) — opcional

## 11. Matriz CRUD (Exemplo)
| Entidade \ Operação | Create | Read | Update | Delete |
|---|---|---|---|---|
| Feirante | X | X | X | (restrito) |
| Produto | X | X | X | X |
| Categoria | X | X | X | X |
| Feira | X | X | X | (restrito) |
| Banca | X | X | X | X |
| Agenda | X | X | X | X |

## 12. Casos de Uso (Rascunho)
- UC-01: Manter Feirante (admin)
- UC-02: Manter Produto (feirante/admin)
- UC-03: Consultar Catálogo e Buscar
- UC-04: Visualizar Mapa de Bancas
- UC-05: Publicar Agenda da Feira (organizador)
- UC-06: Enviar Contato/Sugestão

## 13. Rastreabilidade (Inicial)
| Requisito | Origem | User Story | Caso de Uso | Classe | Teste |
|---|---|---|---|---|---|
| RF-02 Listar Feirantes | Entrevista/organizador | US-Feirantes-01 | UC-03 | Feirante | TC-List-Feirante |
| RF-04 Busca | Persona/visitante | US-Busca-01 | UC-03 | Produto, Categoria | TC-Busca-01 |
| RF-06 Mapa Bancas | Workshop | US-Mapa-01 | UC-04 | Banca, Feira | TC-Mapa-01 |

## 14. Critérios de Aceitação (Exemplos)
- Busca por produto retorna resultado relevante em < 2s (95%).
- Mapa exibe bancas com identificação e link para feirante.
- Agenda mostra pelo menos as próximas 4 datas futuras.
- Páginas atendem WCAG 2.1 AA (verificação de contraste e navegação por teclado).

## 15. BPMN (Sugestão)
- Processo "Preparar Feira": Planejar datas → Alocar bancas → Publicar calendário → Atualizar mapa.

## 16. Protótipo
- Baixa/média fidelidade com navegação: Home → Catálogo → Feirante → Produto → Mapa → Agenda → Contato.

## 17. SRS (Estrutura IEEE 29148)
1. Introdução (Escopo, Propósito, Público)
2. Referências
3. Visão Geral do Produto
4. RF (funcionais)
5. RNF (não funcionais com métricas)
6. Modelos (Classes, Sequência/Estado, BPMN, CRUD)
7. Restrições (legais, técnicas)
8. Apêndices (protótipo, checklist, rubricas)

## 18. Entregas por Semana (alinhadas ao Plano)
- 1–3: Visão + Stakeholders + Personas + Stories + Story Map
- 4–5: Priorização + Conflitos + Rastreabilidade
- 6: Classes + CRUD
- 7: Qualidade (Checklist)
- 8: Checkpoint Integrador
- 9–11: Casos de Uso + Dinâmicos + BPMN
- 12: RNF com métricas
- 13: Protótipo + Testes de Aceitação
- 14–16: SRS + Apresentação + Ajustes

---
Última atualização: 17/01/2026
