# Visão da Demanda (VD): Gestão de Ativos CCT (GAC)

## Histórico de Versões

- **21/03/2026 - Versão 1.0:** versão inicial da demanda para apoiar atividades de requisitos. Autor: Notebook LM / Prof Bezerra.

## 1. Objetivo

O propósito deste documento é apresentar uma visão inicial para a digitalização do controle de empréstimo de projetores, chaves e itens associados do CCT/Unifor.

## 2. Proposta de Valor

A solução GAC busca substituir controles manuais e dispersos por um processo digital com maior rastreabilidade do inventário e das movimentações de empréstimo e devolução.

Como benefícios esperados, destacam-se:

- visibilidade da situação de cada ativo em tempo real;
- redução de erros de registro e perda de informação;
- apoio à responsabilização pelo uso e guarda dos equipamentos;
- apoio à equipe administrativa no controle de disponibilidade, devolução e conferência;
- criação de histórico para auditoria e melhoria do processo.

Do ponto de vista de negócio, a proposta considera que o empréstimo de bens institucionais deve ser formalizado por meio de um termo eletrônico de responsabilidade. O enquadramento jurídico exato do processo deverá ser validado com a instituição durante o detalhamento dos requisitos.

## 3. Descrição da Demanda

Atualmente, o controle de empréstimo de projetores e chaves pode envolver registros manuais, comunicação informal e conferência operacional pouco padronizada. Como consequência, podem ocorrer dificuldades para identificar quem está com determinado item, quando o item foi retirado, quando deveria ser devolvido e em que estado foi entregue.

A proposta é criar uma plataforma digital integrada a identificadores físicos, preferencialmente NFC e/ou QR Code, para apoiar o ciclo de vida dos ativos. Em uma visão inicial, o processo contempla:

1. cadastro dos ativos e seus identificadores;
2. consulta da disponibilidade do item;
3. retirada do item pelo professor com identificação e aceite de responsabilidade;
4. registro dos acessórios vinculados ao empréstimo;
5. devolução com conferência e checklist técnico;
6. atualização do status do ativo no inventário.

Espera-se que a solução tenha pelo menos dois pontos de uso:

- interface de uso rápido, preferencialmente compatível com dispositivos móveis, para apoiar a retirada do item;
- interface administrativa, preferencialmente web/desktop, para cadastro, acompanhamento e devolução.
- **Hardware sugerido para prototipação:** [Tags NFC/Adesivas - AliExpress](https://pt.aliexpress.com/item/1005005715485875.html)

![1774144782640](image/Visao-Gemanda-GAC/1774144782640.png "Tags NFC")

## 4. Partes Interessadas

### 4.1. Diretor do CCT

- **Descrição:** autoridade gestora interessada na preservação do patrimônio institucional.
- **Papel:** acompanhar resultados e apoiar decisões relacionadas à adoção do processo.
- **Interesse principal:** controle, segurança patrimonial e prestação de contas.

### 4.2. Coordenação de Apoio / Administração local

- **Descrição:** responsável pelo acompanhamento operacional do inventário.
- **Papel:** validar regras do processo, supervisionar cadastros e acompanhar indicadores de uso.
- **Interesse principal:** organização do inventário, visibilidade de pendências e padronização do fluxo.

### 4.3. Atendentes do CCT

- **Descrição:** equipe que realiza atividades operacionais de entrega e devolução.
- **Papel:** executar conferência, registrar inconsistências e apoiar usuários no processo.
- **Interesse principal:** rapidez no atendimento e redução de retrabalho.

### 4.4. Professores

- **Descrição:** usuários que solicitam e utilizam os ativos para atividades acadêmicas.
- **Papel:** identificar-se no sistema, retirar o item e devolvê-lo nas condições esperadas.
- **Interesse principal:** agilidade, clareza das regras e facilidade de uso.

### 4.5. Equipe de TI ou suporte ao sistema

- **Descrição:** equipe potencialmente responsável pela sustentação técnica da solução.
- **Papel:** apoiar implantação, integrações, permissões e manutenção técnica.
- **Interesse principal:** viabilidade técnica, segurança de acesso e facilidade de administração.

## 5. Personas

### 5.1. Professor solicitante

- **Descrição:** docente que precisa retirar projetores, chaves ou acessórios para uso em aula ou atividade institucional.
- **Objetivo principal:** localizar rapidamente um item disponível e concluir a retirada com o mínimo de etapas.
- **Necessidades percebidas:** processo simples, confirmação do que foi retirado e comprovação de responsabilidade.

### 5.2. Atendente validador

- **Descrição:** colaborador que realiza a conferência física de retirada e devolução.
- **Objetivo principal:** registrar a movimentação do item sem depender de anotações paralelas.
- **Necessidades percebidas:** checklist claro, visão do status do item e registro de ocorrências.

### 5.3. Administrador do inventário

- **Descrição:** responsável por cadastrar ativos, controlar disponibilidade e acompanhar pendências.
- **Objetivo principal:** manter o inventário confiável e atualizado.
- **Necessidades percebidas:** consulta por ativo, relatórios gerenciais e histórico de movimentações.

## 6. Necessidades e Funcionalidades

### Necessidade 1: Manter um inventário digital confiável dos ativos

#### F1.1 Cadastro de ativos

- **Descrição:** permitir o cadastro de ativos como projetores, chaves e outros itens controlados pelo CCT.
- **Detalhamento inicial:** o sistema deve permitir atributos comuns, como identificação patrimonial, descrição, categoria, status e observações. Campos específicos por tipo de ativo deverão ser definidos no refinamento.
- **Atores:** administrador do inventário.
- **Frequência:** eventual, com consultas frequentes.
- **Valor:** alto.

#### F1.2 Associação de identificadores físicos

- **Descrição:** permitir vincular um identificador NFC, QR Code ou outro código ao ativo cadastrado.
- **Atores:** administrador do inventário.
- **Frequência:** eventual.
- **Valor:** alto.

#### F1.3 Consulta de disponibilidade

- **Descrição:** permitir verificar se um ativo está disponível, emprestado, reservado, em manutenção ou indisponível.
- **Atores:** professores, atendentes, administrador.
- **Frequência:** alta.
- **Valor:** alto.

### Necessidade 2: Registrar a retirada do ativo com responsabilidade do usuário

#### F2.1 Identificação do solicitante

- **Descrição:** permitir identificar quem está realizando a retirada do item antes da confirmação do empréstimo.
- **Detalhamento inicial:** a forma de identificação poderá envolver matrícula, login institucional, leitura de código, integração com sistema acadêmico ou outra alternativa a ser validada.
- **Atores:** professores, atendentes.
- **Frequência:** alta.
- **Valor:** alto.

#### F2.2 Aceite de termo de responsabilidade

- **Descrição:** apresentar um termo eletrônico com regras de uso, guarda e devolução do item, registrando o aceite do usuário.
- **Detalhamento inicial:** o formato do termo, o valor jurídico do aceite e os dados mínimos de auditoria ainda precisam ser definidos com a instituição.
- **Atores:** professores.
- **Frequência:** alta.
- **Valor:** alto.

#### F2.3 Registro de acessórios e itens vinculados

- **Descrição:** permitir informar acessórios entregues juntamente com o ativo principal, como cabos, fonte, controle remoto ou adaptadores.
- **Atores:** professores, atendentes.
- **Frequência:** média.
- **Valor:** médio.

#### F2.4 Confirmação do empréstimo

- **Descrição:** gerar um registro com data, hora, usuário, item retirado, acessórios e situação inicial do ativo.
- **Atores:** professores, atendentes, administrador.
- **Frequência:** alta.
- **Valor:** alto.

### Necessidade 3: Garantir devolução com conferência do estado do item

#### F3.1 Checklist de devolução

- **Descrição:** permitir realizar a conferência física e funcional do item no momento da devolução.
- **Detalhamento inicial:** o checklist poderá variar por tipo de ativo. Para projetores, pode incluir integridade física, liga/desliga, cabos e acessórios. Para chaves, pode incluir identificação e estado de conservação.
- **Atores:** atendentes.
- **Frequência:** alta.
- **Valor:** alto.

#### F3.2 Registro de ocorrência

- **Descrição:** permitir informar problemas encontrados na devolução, como avaria, ausência de acessório, atraso ou divergência de identificação.
- **Atores:** atendentes, administrador.
- **Frequência:** média.
- **Valor:** alto.

#### F3.3 Atualização do status do ativo

- **Descrição:** atualizar automaticamente a situação do ativo após a devolução ou abertura de ocorrência.
- **Atores:** atendentes, administrador.
- **Frequência:** alta.
- **Valor:** alto.

### Necessidade 4: Apoiar gestão e acompanhamento do processo

#### F4.1 Histórico de movimentações

- **Descrição:** disponibilizar o histórico de retiradas, devoluções, ocorrências e responsáveis por cada ativo.
- **Atores:** administrador, coordenação.
- **Frequência:** média.
- **Valor:** alto.

#### F4.2 Painel de acompanhamento

- **Descrição:** apresentar visão consolidada dos itens disponíveis, emprestados, atrasados, com ocorrência ou indisponíveis.
- **Atores:** administrador, coordenação.
- **Frequência:** média.
- **Valor:** médio.

## 7. Arquitetura Inicial da Demanda

Como hipótese inicial, a solução poderá ser estruturada com os seguintes elementos:

- aplicação web responsiva ou interface mobile para apoio à retirada;
- aplicação administrativa web/desktop para gestão do inventário e devolução;
- base de dados central para armazenar ativos, usuários, empréstimos e ocorrências;
- integração com identificadores físicos, como NFC e QR Code;
- mecanismo de autenticação para perfis administrativos e, se necessário, para usuários solicitantes.

Essa arquitetura deve ser entendida como ponto de partida e não como decisão definitiva.

## 8. Premissas e Restrições Iniciais

- o processo envolve bens institucionais cujo uso precisa ser rastreado;
- a solução deve ser simples o suficiente para uso frequente pela equipe operacional;
- o ambiente pode ter diferentes tipos de ativos, com regras específicas por categoria;
- a instituição pode exigir autenticação com vínculo ao usuário real;
- regras jurídicas e administrativas do termo de responsabilidade ainda precisam ser validadas;
- a disponibilidade de dispositivos com leitura NFC pode variar entre usuários.

## 9. Pontos para Aprofundamento nas Atividades de Requisitos

Os itens abaixo devem ser tratados pelos alunos nas próximas atividades:

1. definir o fluxo atual do processo e suas principais dores;
2. identificar regras de negócio para atraso, dano, perda e bloqueio de novos empréstimos;
3. detalhar atributos obrigatórios por tipo de ativo;
4. definir perfis de usuário e permissões de acesso;
5. especificar o que caracteriza um aceite válido do termo de responsabilidade;
6. identificar requisitos não funcionais, como segurança, disponibilidade, usabilidade e auditoria;
7. decidir se haverá reserva antecipada do item ou apenas empréstimo imediato;
8. modelar cenários alternativos e exceções, como item sem tag, tag danificada, devolução parcial ou divergência no checklist.
