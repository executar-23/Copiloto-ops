#!/usr/bin/env python3
"""PF-24 / CV-DEPEND-001 — rede de dependências do EXECUTAR_HUB_Control_Plane_v2.xlsx.

Executa o especialista executar-dependency-architect (prompt mestre EXECUTAR-DEPENDENCY-ARCHITECT-001)
sobre a planilha real. As arestas abaixo SÃO a análise: cada uma cita os field_instance_id que a
demonstram (campo do destino ← campo da origem). O script só verifica e renderiza; não infere nada.

Uso: python3 analise_pf24.py <control_plane.json> <dir_saida>
  (control_plane.json = saída de skills/executar-dependency-architect/scripts/extrair_control_plane.py)
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

A = {  # abreviação → artifact_id canônico (14_REG_Artefatos; preservados)
    "DDE": "D01-DOC-DDE-001", "TAP": "D01-DOC-TAP-001", "MNE": "D01-DOC-MNE-001", "MRE": "D01-DOC-MRE-001",
    "DGRC": "D02-DOC-DGRC-001", "MRC": "D02-DOC-MRC-001", "PPT": "D02-DOC-PPT-001",
    "PFO": "D03-DOC-PFO-001", "MFO": "D03-DOC-MFO-001", "PPC": "D04-DOC-PPC-001",
    "EPGD": "D05-DOC-EPGD-001", "DCM": "D05-DOC-DCM-001", "EGC": "D06-DOC-EGC-001", "RMI": "D06-DOC-RMI-001",
    "PEX": "D07-DOC-PEX-001", "PIM": "D07-DOC-PIM-001", "MOP": "D08-DOC-MOP-001", "RUN": "D08-DOC-RUN-001",
    "PPE": "D09-DOC-PPE-001", "DEB": "D09-DOC-DEB-001", "DRP": "D10-DOC-DRP-001", "PRD": "D10-DOC-PRD-001",
    "EEP": "D11-DOC-EEP-001", "DSI": "D11-DOC-DSI-001", "ETE": "D12-DOC-ETE-001",
    "DRM": "D13-DOC-DRM-001", "GTM": "D13-DOC-GTM-001", "PCV": "D14-DOC-PCV-001", "PASC": "D15-DOC-PASC-001",
    "PEM": "D16-DOC-PEM-001", "PEP": "D17-DOC-PEP-001", "PCE": "D18-DOC-PCE-001", "PAC": "D19-DOC-PAC-001",
    "PPR": "D20-DOC-PPR-001", "PWB": "D21-DOC-PWB-001", "DRL": "D22-DOC-DRL-001", "PBL": "D23-DOC-PBL-001",
}

# Gate que certifica cada artefato — PROPOSED: 17_REG_Gates não declara required_artifact_types (GAP-DEP-B).
# Critério: semântica do nome do Gate × papel do artefato. G03 e G10 ficam sem artefato (ver A03).
GATE_DO_ARTEFATO = {
    "G00": ["DDE", "TAP"],
    "G01": ["MNE", "MRE", "MFO", "PFO", "DGRC", "MRC", "DRM", "DEB", "PPE", "PPC", "PEX"],
    "G02": ["DRP", "EEP", "DSI", "PRD"],
    "G04": ["PPR", "EPGD", "DCM", "ETE", "PCE", "PBL"],
    "G05": ["PIM", "PPT"],
    "G06": ["MOP", "RUN"],
    "G07": ["PASC"],
    "G08": ["PCV", "GTM", "PAC", "PEM"],
    "G09": ["PWB"],
    "G11": ["EGC", "RMI", "DRL"],
    "gate:tbd": ["PEP"],
}
GATE = {art: g for g, arts in GATE_DO_ARTEFATO.items() for art in arts}
HANDOFF_A03 = {("PRD", "ETE"), ("DSI", "ETE"), ("EEP", "ETE")}  # A02 → A04: avaliadas no G03 DEVELOPMENT_READY

# (origem, destino, bloqueante, tag, motivo, [(campo_destino, campo_origem), ...])
# Campos no formato SECAO.LABEL relativos ao artefato; expandidos e verificados contra 15_REG_Campos.
E = [
    ("DDE", "TAP", True, "DERIVED", "O termo de abertura operacionaliza a direção estratégica",
     [("OBJECTIVE.OBJETIVO_GERAL", "STRATEGIC_DIRECTION.OBJETIVOS_ESTRATEGICOS"), ("SCOPE.ESCOPO_EXCLUIDO", "STRATEGIC_DIRECTION.NAO_OBJETIVOS"), ("STAKEHOLDERS.PARTICIPANTES", "STAKEHOLDERS.STAKEHOLDERS")]),
    ("DDE", "MNE", True, "DERIVED", "O modelo de negócio parte do problema e do portfólio declarados na direção",
     [("CUSTOMER.PROBLEMAS", "PROBLEM_AND_OPPORTUNITY.PROBLEMA_CENTRAL"), ("OFFERINGS.PRODUTOS", "ECOSYSTEM.PRODUTOS"), ("OFFERINGS.SERVICOS", "ECOSYSTEM.SERVICOS")]),
    ("DDE", "MRE", True, "DERIVED", "Os nós do mapa de relações são os componentes do ecossistema",
     [("NODES.PRODUTOS", "ECOSYSTEM.PRODUTOS"), ("NODES.AGENTES", "ECOSYSTEM.AGENTES"), ("NODES.PLATAFORMAS", "ECOSYSTEM.PLATAFORMAS"), ("DEPENDENCIES.DEPENDENCIAS", "STRATEGIC_DEPENDENCIES.DEPENDENCIAS")]),
    ("MNE", "MRE", False, "DERIVED", "Fluxos de valor e comerciais vêm do modelo de negócio",
     [("FLOWS.FLUXO_COMERCIAL", "CHANNELS.DISTRIBUICAO"), ("FLOWS.FLUXO_DE_VALOR", "VALUE.PROPOSTAS_DE_VALOR")]),
    ("DDE", "DGRC", True, "DERIVED", "Papéis e autoridades jurídicas seguem o modelo de governança",
     [("GOVERNANCE.PAPEIS", "GOVERNANCE.PAPEIS_DECISORIOS"), ("GOVERNANCE.AUTORIDADES", "GOVERNANCE.DIREITOS_DE_DECISAO"), ("INTELLECTUAL_PROPERTY.MARCAS", "ECOSYSTEM.MARCAS")]),
    ("DGRC", "MRC", True, "DERIVED", "A matriz detalha riscos, controles e owners definidos na governança",
     [("SCHEMA.CATEGORIA", "RISK_MANAGEMENT.RISCOS"), ("SCHEMA.CONTROLES_EXISTENTES", "RISK_MANAGEMENT.CONTROLES"), ("SCHEMA.OWNER", "RISK_MANAGEMENT.OWNERS")]),
    ("DDE", "MRC", False, "DERIVED", "Riscos estratégicos entram como eventos de risco",
     [("SCHEMA.EVENTO_DE_RISCO", "RISKS.RISCOS_ESTRATEGICOS")]),
    ("TAP", "MRC", False, "DERIVED", "Riscos iniciais do projeto entram como eventos de risco",
     [("SCHEMA.EVENTO_DE_RISCO", "RISKS.RISCOS_INICIAIS")]),
    ("MNE", "MFO", True, "DERIVED", "O modelo financeiro precifica os produtos e custos do modelo de negócio",
     [("REVENUE_MODEL.PRODUTO", "OFFERINGS.PRODUTOS"), ("REVENUE_MODEL.PRECO", "REVENUE.PRECIFICACAO"), ("COST_MODEL.FIXOS", "COSTS.ESTRUTURA_DE_CUSTOS")]),
    ("MFO", "MNE", False, "PROPOSED", "Economia unitária do MNE resume o modelo financeiro (informativa: quebra o ciclo MNE↔MFO)",
     [("ECONOMICS.MARGEM", "UNIT_ECONOMICS.MARGEM"), ("ECONOMICS.CAC", "UNIT_ECONOMICS.CAC"), ("ECONOMICS.LTV", "UNIT_ECONOMICS.LTV"), ("ECONOMICS.BREAK_EVEN", "BREAK_EVEN.PONTO_DE_EQUILIBRIO")]),
    ("MNE", "PFO", True, "DERIVED", "Receitas, preços e custos do plano vêm do modelo de negócio",
     [("REVENUE.FONTES", "REVENUE.FONTES_DE_RECEITA"), ("PRICING.PRECOS", "REVENUE.PRECIFICACAO"), ("OPEX.CATEGORIA", "COSTS.OPEX")]),
    ("MFO", "PFO", True, "DERIVED", "Previsões, cenários e margem do plano são projeções do modelo",
     [("REVENUE.PREVISOES", "REVENUE_MODEL.VOLUME"), ("SCENARIOS.BASE", "SCENARIOS.CENARIO"), ("INDICATORS.MARGEM", "PNL.MARGEM")]),
    ("PFO", "MFO", False, "PROPOSED", "Premissas gerais (período, moeda) do plano calibram o modelo (informativa: quebra o ciclo MFO↔PFO)",
     [("MODEL_INPUTS.PREMISSAS", "ASSUMPTIONS.PREMISSAS_FINANCEIRAS")]),
    ("TAP", "PFO", False, "DERIVED", "Orçamento do termo de abertura baliza o limite do plano",
     [("BUDGET.LIMITE", "RESOURCES.ORCAMENTO")]),
    ("DDE", "PPC", True, "DERIVED", "Estrutura e autoridade de pessoas seguem o modelo de governança",
     [("ROLES.AUTORIDADE", "GOVERNANCE.DIREITOS_DE_DECISAO"), ("ORGANIZATION.ESTRUTURA", "GOVERNANCE.MODELO_DE_GOVERNANCA")]),
    ("PFO", "PPC", False, "DERIVED", "Contratações dependem do orçamento por área",
     [("HIRING.NECESSIDADES_FUTURAS", "BUDGET.ORCAMENTO_POR_AREA")]),
    ("TAP", "PEX", True, "DERIVED", "Objetivos, entregáveis e DoD da execução vêm do termo de abertura",
     [("OBJECTIVES.OBJETIVO", "OBJECTIVE.OBJETIVOS_ESPECIFICOS"), ("DELIVERABLES.ENTREGAVEL", "DELIVERABLES.ENTREGAVEIS_PRINCIPAIS"), ("DELIVERABLES.DOD", "DELIVERABLES.DEFINITION_OF_DONE")]),
    ("PPC", "PEX", True, "DERIVED", "Capacidade da execução é a capacidade de pessoas",
     [("CAPACITY.CAPACIDADE_BRUTA", "CAPACITY.HORAS_DISPONIVEIS"), ("CAPACITY.LIQUIDA", "CAPACITY.CAPACIDADE_LIQUIDA")]),
    ("PEX", "PPC", False, "PROPOSED", "Demanda de trabalho alimenta a carga de pessoas (informativa: quebra o ciclo PPC↔PEX)",
     [("WORKLOAD.DEMANDA", "BACKLOG.ITEM")]),
    ("DDE", "PEX", False, "DERIVED", "Gates da execução referenciam os gates da governança",
     [("GATES.GATE", "GOVERNANCE.GATES")]),
    ("MNE", "DRM", True, "DERIVED", "Segmentos, alternativas e diferenciação de mercado partem do modelo de negócio",
     [("SEGMENTS.SEGMENTO", "CUSTOMER.SEGMENTOS"), ("ALTERNATIVES.SUBSTITUTOS", "VALUE.ALTERNATIVAS_EXISTENTES"), ("POSITIONING.DIFERENCIACAO", "VALUE.DIFERENCIADORES")]),
    ("DEB", "DRM", False, "DERIVED", "Evidências de mercado citam o dossiê de evidências",
     [("EVIDENCE.ESTUDOS", "SCHEMA.CLAIM"), ("EVIDENCE.FONTES", "SCHEMA.CITATION")]),
    ("MNE", "PPE", True, "DERIVED", "Experimentos testam as hipóteses do modelo de negócio",
     [("HYPOTHESIS.HIPOTESE", "ASSUMPTIONS.HIPOTESES"), ("QUESTION.PERGUNTA_DE_PESQUISA", "ASSUMPTIONS.VALIDACOES_PENDENTES")]),
    ("DEB", "PPE", False, "DERIVED", "Revisão de evidências parte do dossiê existente",
     [("EVIDENCE_REVIEW.FONTES_EXISTENTES", "SCHEMA.SOURCE_ID"), ("EVIDENCE_REVIEW.LACUNAS", "SCHEMA.LIMITATION")]),
    ("DDE", "DRP", True, "DERIVED", "O problema do produto é o problema central declarado",
     [("PROBLEM.PROBLEMA", "PROBLEM_AND_OPPORTUNITY.PROBLEMA_CENTRAL"), ("PROBLEM.EVIDENCIA", "PROBLEM_AND_OPPORTUNITY.EVIDENCIAS_DO_PROBLEMA")]),
    ("MNE", "DRP", True, "DERIVED", "JTBD, proposta de valor e clientes do produto vêm do modelo de negócio",
     [("JTBD.TRABALHO", "CUSTOMER.JTBD"), ("VALUE.PROPOSTA_DE_VALOR", "VALUE.PROPOSTAS_DE_VALOR"), ("AUDIENCE.CLIENTES", "CUSTOMER.CLIENTES")]),
    ("DRM", "DRP", True, "DERIVED", "O ICP e os usuários do produto são os definidos no mercado",
     [("AUDIENCE.ICP", "ICP.PERFIL"), ("AUDIENCE.USUARIOS", "SEGMENTS.SEGMENTO")]),
    ("DEB", "DRP", False, "DERIVED", "A evidência do problema cita o dossiê",
     [("PROBLEM.EVIDENCIA", "SCHEMA.FINDING")]),
    ("PPE", "DRP", False, "DERIVED", "Decisões de experimentos ajustam o escopo",
     [("SCOPE.INCLUIDO", "DECISION.DECISAO_DERIVADA")]),
    ("DRP", "EEP", True, "DERIVED", "Jornadas e personas da experiência detalham as do produto",
     [("JOURNEYS.ETAPA", "JOURNEYS.JORNADAS"), ("FLOWS.ENTRADA", "JOURNEYS.FLUXOS"), ("PERSONAS.PERFIL", "AUDIENCE.USUARIOS")]),
    ("EEP", "DRP", False, "PROPOSED", "Pesquisa de usuários refina as jornadas do produto (informativa: quebra o ciclo DRP↔EEP)",
     [("JOURNEYS.JORNADAS", "USER_RESEARCH.NECESSIDADES")]),
    ("DSI", "EEP", False, "DERIVED", "Microcopy e feedback usam voz e padrões do design system",
     [("CONTENT.MICROCOPY", "CONTENT_DESIGN.VOZ"), ("INTERACTION.FEEDBACK", "PATTERNS.FEEDBACK")]),
    ("DDE", "DSI", False, "DERIVED", "Princípios do design system derivam dos princípios do ecossistema",
     [("FOUNDATIONS.PRINCIPIOS", "PURPOSE.PRINCIPIOS")]),
    ("DRP", "PRD", True, "DERIVED", "Os requisitos integrados por produto detalham o documento de requisitos",
     [("SCHEMA.PROBLEM", "PROBLEM.PROBLEMA"), ("SCHEMA.TARGET_USER", "AUDIENCE.USUARIOS"), ("SCHEMA.JTBD", "JTBD.TRABALHO"), ("SCHEMA.FUNCTIONAL_REQUIREMENTS", "REQUIREMENTS.FUNCIONAIS"), ("SCHEMA.NON_FUNCTIONAL_REQUIREMENTS", "REQUIREMENTS.NAO_FUNCIONAIS"), ("SCHEMA.ACCEPTANCE_CRITERIA", "ACCEPTANCE.CRITERIOS_DE_ACEITE")]),
    ("EEP", "PRD", True, "DERIVED", "Fluxos, estados e acessibilidade por produto vêm da especificação de experiência",
     [("SCHEMA.USER_FLOWS", "FLOWS.DECISAO"), ("SCHEMA.STATES", "STATES.LOADING"), ("SCHEMA.ACCESSIBILITY", "ACCESSIBILITY.SEMANTICA")]),
    ("DGRC", "PRD", False, "DERIVED", "Requisitos de privacidade e segurança citam bases legais e controles",
     [("SCHEMA.PRIVACY", "PRIVACY.BASES_LEGAIS"), ("SCHEMA.SECURITY", "COMPLIANCE.CONTROLES")]),
    ("DCM", "PRD", False, "DERIVED", "Analytics do produto usa as métricas catalogadas",
     [("SCHEMA.ANALYTICS", "SCHEMA.METRIC_OR_FIELD_ID")]),
    ("PRD", "ETE", True, "DERIVED", "Transição A03: arquitetura, integrações, dados e testes derivam dos requisitos integrados",
     [("ARCHITECTURE.VISAO_GERAL", "SCHEMA.FUNCTIONAL_REQUIREMENTS"), ("PERFORMANCE.BUDGETS", "SCHEMA.NON_FUNCTIONAL_REQUIREMENTS"), ("INTEGRATIONS.SERVICO", "SCHEMA.INTEGRATIONS"), ("DATA.SCHEMA", "SCHEMA.DATA_REQUIREMENTS"), ("TESTING.E2E", "SCHEMA.ACCEPTANCE_CRITERIA")]),
    ("DSI", "ETE", True, "DERIVED", "Transição A03: pacotes de UI da engenharia vêm do handoff do design system",
     [("PACKAGES.PACKAGE", "ENGINEERING_HANDOFF.PACKAGE"), ("PACKAGES.RESPONSABILIDADE", "ENGINEERING_HANDOFF.TOKENS")]),
    ("EEP", "ETE", False, "DERIVED", "Transição A03: responsabilidades das apps seguem a arquitetura de informação",
     [("APPLICATIONS.RESPONSABILIDADE", "INFORMATION_ARCHITECTURE.NAVEGACAO")]),
    ("PPR", "ETE", True, "DERIVED", "Repositórios, ambientes e hosting da engenharia são os inventariados nas plataformas",
     [("REPOSITORIES.REPOSITORIO", "REPOSITORIES.REPO"), ("ENVIRONMENTS.PRODUCTION", "ENVIRONMENTS.PRODUCTION"), ("INFRASTRUCTURE.HOSTING", "DEPLOYMENTS.PLATAFORMA")]),
    ("EPGD", "ETE", True, "DERIVED", "Banco e schemas da engenharia seguem a estratégia de dados",
     [("DATA.BANCO", "STORAGE.BANCO"), ("DATA.SCHEMA", "SCHEMAS.SCHEMA")]),
    ("DRL", "ETE", False, "DERIVED", "Links de ADR apontam para o log de decisões",
     [("ADR_LINKS.DECISOES_ARQUITETURAIS", "SCHEMA.DECISION_ID")]),
    ("DDE", "PPR", True, "DERIVED", "O inventário de plataformas parte das plataformas declaradas no ecossistema",
     [("SYSTEMS.PLATAFORMA", "ECOSYSTEM.PLATAFORMAS"), ("ACCOUNTS.ORGANIZACAO", "ECOSYSTEM.UNIDADES_DE_NEGOCIO")]),
    ("DGRC", "PPR", False, "DERIVED", "Permissões seguem os controles de conformidade",
     [("PERMISSIONS.ACESSO", "COMPLIANCE.CONTROLES")]),
    ("PPR", "EPGD", True, "DERIVED", "Fontes e armazenamento de dados são os sistemas e repositórios existentes",
     [("SOURCES.SISTEMA", "SYSTEMS.PLATAFORMA"), ("STORAGE.REPOSITORIO", "REPOSITORIES.REPO")]),
    ("DGRC", "EPGD", True, "DERIVED", "Finalidade, retenção e acesso a dados seguem o enquadramento jurídico",
     [("PRIVACY.FINALIDADE", "PRIVACY.FINALIDADES"), ("LIFECYCLE.RETENCAO", "PRIVACY.RETENCAO"), ("ACCESS.PERMISSAO", "GOVERNANCE.POLITICAS")]),
    ("EPGD", "DGRC", False, "PROPOSED", "O inventário de dados pessoais refina a seção de privacidade (informativa: quebra o ciclo DGRC↔EPGD)",
     [("PRIVACY.DADOS_PESSOAIS", "PRIVACY.DADOS_PESSOAIS")]),
    ("EPGD", "DCM", True, "DERIVED", "Fonte, dataset, classificação e retenção de cada métrica vêm da estratégia de dados",
     [("SCHEMA.FONTE", "SOURCES.FONTE"), ("SCHEMA.TABELA_DATASET", "ANALYTICS.DATASETS"), ("SCHEMA.CLASSIFICACAO", "SECURITY.CLASSIFICACAO"), ("SCHEMA.RETENCAO", "LIFECYCLE.RETENCAO")]),
    ("DDE", "DCM", False, "DERIVED", "Indicadores estratégicos entram no catálogo de métricas",
     [("SCHEMA.NOME", "MEASUREMENT.INDICADORES")]),
    ("DGRC", "PPT", True, "DERIVED", "Bases legais, retenção e direitos da política vêm da governança jurídica",
     [("PURPOSES.BASE_LEGAL", "PRIVACY.BASES_LEGAIS"), ("STORAGE.RETENCAO", "PRIVACY.RETENCAO"), ("RIGHTS.DIREITOS_DO_TITULAR", "PRIVACY.DIREITOS")]),
    ("EPGD", "PPT", True, "DERIVED", "A política declara os dados efetivamente coletados",
     [("COLLECTED_DATA.CATEGORIAS_DE_DADOS", "PRIVACY.DADOS_PESSOAIS"), ("COLLECTED_DATA.ORIGEM", "SOURCES.ORIGEM")]),
    ("PPR", "PPT", False, "DERIVED", "Operadores da política são as plataformas usadas",
     [("SHARING.OPERADORES", "SYSTEMS.PLATAFORMA")]),
    ("DCM", "PPT", False, "DERIVED", "Cookies de analytics correspondem aos eventos catalogados",
     [("COOKIES.ANALYTICS", "SCHEMA.CAMPO_EVENTO")]),
    ("ETE", "PCE", True, "DERIVED", "Contratos de API e eventos registram as interfaces da engenharia",
     [("API_CONTRACTS.ENDPOINT", "INTERFACES.API"), ("EVENT_CONTRACTS.EVENTO", "INTERFACES.EVENTOS")]),
    ("EPGD", "PCE", True, "DERIVED", "Contratos de dados registram schemas e linhagem",
     [("DATA_CONTRACTS.PAYLOAD", "SCHEMAS.SCHEMA"), ("DATA_CONTRACTS.PRODUCER", "LINEAGE.ORIGEM"), ("DATA_CONTRACTS.CONSUMER", "LINEAGE.DESTINO")]),
    ("DGRC", "PCE", False, "DERIVED", "Inventário de contratos inclui os contratos jurídicos",
     [("CONTRACT_INVENTORY.CONTRATO", "CONTRACTS.CONTRATOS_EXISTENTES")]),
    ("EGC", "PCE", False, "DERIVED", "Registro e versionamento de contratos seguem o padrão de IDs e versões",
     [("REGISTRY.ID", "IDENTITY.PADRAO_DE_IDS"), ("VERSIONING.VERSAO", "VERSIONING.VERSAO")]),
    ("DCM", "PCE", False, "DERIVED", "Propriedades de eventos seguem as dimensões catalogadas",
     [("EVENT_CONTRACTS.PROPRIEDADES", "SCHEMA.DIMENSOES")]),
    ("MRE", "PCE", False, "DERIVED", "Contratos de handoff formalizam os handoffs do mapa de relações",
     [("HANDOFF_CONTRACTS.ORIGEM", "INTERFACES.HANDOFFS")]),
    ("PRD", "PBL", True, "DERIVED", "Problema, escopo e aceite do blueprint vêm dos requisitos integrados",
     [("PROBLEM.PROBLEMA", "SCHEMA.PROBLEM"), ("ACCEPTANCE.CRITERIOS", "SCHEMA.ACCEPTANCE_CRITERIA"), ("SCOPE.INCLUIDO", "SCHEMA.USE_CASES")]),
    ("ETE", "PBL", True, "DERIVED", "Arquitetura, interfaces e implementação do blueprint vêm da especificação técnica",
     [("ARCHITECTURE.COMPONENTES", "ARCHITECTURE.VISAO_GERAL"), ("IMPLEMENTATION.REPOSITORIO", "REPOSITORIES.REPOSITORIO"), ("IMPLEMENTATION.PACOTE", "PACKAGES.PACKAGE"), ("INTERFACES.API", "INTERFACES.API")]),
    ("PCE", "PBL", False, "DERIVED", "Contratos do blueprint referenciam o registro de contratos",
     [("CONTRACTS.SCHEMAS", "DOCUMENT_SCHEMAS.SCHEMA"), ("CONTRACTS.INTERFACES", "API_CONTRACTS.ENDPOINT")]),
    ("EEP", "PBL", False, "DERIVED", "Fluxo de usuário do blueprint segue as jornadas",
     [("USER_FLOW.ACAO", "JOURNEYS.ACAO")]),
    ("PEX", "PIM", True, "DERIVED", "Pacotes, gates e recursos da implementação vêm do plano de execução",
     [("WORK_PACKAGES.ENTREGAVEL", "DELIVERABLES.ENTREGAVEL"), ("GATES.GATE", "GATES.GATE"), ("RESOURCES.PESSOA", "CAPACITY.LIQUIDA")]),
    ("ETE", "PIM", True, "DERIVED", "Pacotes, rollback e verificação da implementação vêm da especificação técnica",
     [("WORK_PACKAGES.PACOTE", "PACKAGES.PACKAGE"), ("ROLLBACK.PROCEDIMENTO", "ROLLBACK.PROCEDIMENTO"), ("VERIFICATION.TESTE", "TESTING.INTEGRACAO")]),
    ("TAP", "PIM", False, "DERIVED", "Marcos da implementação partem dos marcos do termo (campo em CONFLICT: D22-DEC-CFL-02)",
     [("MILESTONES.MARCO", "MILESTONES.MARCOS")]),
    ("PCE", "PIM", False, "DERIVED", "Handoffs da implementação usam os contratos de handoff",
     [("HANDOFF.CONTRATO", "HANDOFF_CONTRACTS.REQUISITOS")]),
    ("MNE", "MOP", True, "DERIVED", "Serviços e processos operados são os do modelo de negócio",
     [("OPERATING_MODEL.SERVICOS", "OFFERINGS.SERVICOS"), ("PROCESS_INVENTORY.PROCESSO", "ACTIVITIES.ATIVIDADES_CHAVE")]),
    ("PPC", "MOP", False, "DERIVED", "Executores dos processos são papéis definidos em pessoas",
     [("ROLES.EXECUTOR", "ROLES.PAPEL")]),
    ("DGRC", "MOP", False, "DERIVED", "Controles operacionais implementam controles de conformidade",
     [("CONTROLS.CONTROLE", "COMPLIANCE.CONTROLES")]),
    ("MOP", "RUN", True, "DERIVED", "Cada runbook operacionaliza um processo/incidente do manual",
     [("SCHEMA.OBJETIVO", "PROCESS_INVENTORY.OBJETIVO"), ("SCHEMA.TRIGGER", "INCIDENTS.TIPO"), ("SCHEMA.PASSOS", "PROCEDURES.ETAPAS"), ("SCHEMA.ESCALACAO", "INCIDENTS.RESPOSTA")]),
    ("PPR", "RUN", True, "DERIVED", "Sistemas e credenciais do runbook são os inventariados",
     [("SCHEMA.SISTEMAS", "SYSTEMS.PLATAFORMA"), ("SCHEMA.CREDENCIAIS_NECESSARIAS", "SECRETS.SECRET_NAME")]),
    ("ETE", "RUN", False, "DERIVED", "Rollback operacional segue o procedimento técnico",
     [("SCHEMA.ROLLBACK", "ROLLBACK.PROCEDIMENTO")]),
    ("DRM", "PCV", True, "DERIVED", "ICP, qualificação e objeções de vendas vêm do mercado",
     [("CUSTOMER.ICP", "ICP.PERFIL"), ("QUALIFICATION.CRITERIOS", "ICP.CRITERIOS"), ("OBJECTIONS.OBJECAO", "ALTERNATIVES.CONCORRENTES")]),
    ("PFO", "PCV", True, "DERIVED", "Preço, desconto e quota vêm do plano financeiro (valor em CONFLICT: D22-DEC-CFL-03)",
     [("PRICING.PRECO", "PRICING.PRECOS"), ("PRICING.DESCONTO", "PRICING.DESCONTOS"), ("TARGETS.QUOTA", "REVENUE.PREVISOES")]),
    ("MNE", "PCV", False, "DERIVED", "Pacotes de venda seguem os planos do modelo de negócio",
     [("OFFERS.PACOTE", "OFFERINGS.PLANOS")]),
    ("PCV", "PFO", False, "PROPOSED", "Forecast comercial refina previsões de receita (informativa: quebra o ciclo PFO↔PCV)",
     [("REVENUE.PREVISOES", "FORECAST.RECEITA")]),
    ("PPR", "PCV", False, "DERIVED", "O CRM é uma das plataformas inventariadas",
     [("CRM.SISTEMA", "SYSTEMS.PLATAFORMA")]),
    ("PCV", "PASC", False, "PROPOSED", "Onboarding recebe o handoff comercial (informativa: o CS desenha o onboarding antes do G08)",
     [("ONBOARDING.ETAPAS", "HANDOFF.ONBOARDING"), ("SERVICE_MODEL.SEGMENTOS", "CUSTOMER.SEGMENTOS")]),
    ("MNE", "PASC", True, "DERIVED", "O modelo de atendimento segue relacionamento e suporte do modelo de negócio",
     [("SERVICE_MODEL.MODELO", "RELATIONSHIPS.RELACIONAMENTO_COM_CLIENTE"), ("CHANNELS.OUTROS", "RELATIONSHIPS.SUPORTE")]),
    ("MOP", "PASC", False, "DERIVED", "Prazos de atendimento respeitam os SLAs operacionais",
     [("SLA.PRAZO", "SLA.META")]),
    ("PRD", "PASC", False, "DERIVED", "Base de conhecimento cobre os casos de uso do produto",
     [("KNOWLEDGE_BASE.ARTIGOS", "SCHEMA.USE_CASES")]),
    ("PASC", "MFO", False, "DERIVED", "Churn da economia unitária vem da métrica de sucesso do cliente",
     [("UNIT_ECONOMICS.CHURN", "METRICS.CHURN")]),
    ("DRM", "GTM", True, "DERIVED", "ICP, posicionamento e mensagem de lançamento vêm do mercado",
     [("AUDIENCE.ICP", "ICP.PERFIL"), ("POSITIONING.POSICIONAMENTO", "POSITIONING.CATEGORIA"), ("POSITIONING.MENSAGEM", "MESSAGING.PROMESSA")]),
    ("PFO", "GTM", True, "DERIVED", "Preço da oferta e investimento do lançamento vêm do plano financeiro",
     [("OFFER.PRECO", "PRICING.PRECOS"), ("BUDGET.INVESTIMENTO", "BUDGET.ORCAMENTO_POR_AREA")]),
    ("PRD", "GTM", True, "DERIVED", "Produto ofertado e objetivo do lançamento vêm dos requisitos integrados",
     [("OFFER.PRODUTO", "SCHEMA.PRODUCT_NAME"), ("OBJECTIVES.OBJETIVO_DE_LANCAMENTO", "SCHEMA.RELEASE_CRITERIA")]),
    ("PIM", "GTM", True, "DERIVED", "Data de lançamento depende dos marcos de implementação (valor em CONFLICT: D22-DEC-CFL-02)",
     [("LAUNCH.LAUNCH", "MILESTONES.MARCO"), ("LAUNCH.PRE_LAUNCH", "ROLLOUT.PILOTO")]),
    ("PASC", "GTM", True, "DERIVED", "Prontidão de suporte é critério do lançamento",
     [("SUPPORT_READINESS.ATENDIMENTO", "SERVICE_MODEL.MODELO"), ("SUPPORT_READINESS.FAQ", "KNOWLEDGE_BASE.FAQ")]),
    ("GTM", "PCV", False, "DERIVED", "Etapas de vendas recebem o handoff de marketing",
     [("PROCESS.ETAPAS", "SALES_HANDOFF.MARKETING_PARA_VENDAS")]),
    ("DCM", "GTM", False, "DERIVED", "Métricas e eventos do lançamento usam o catálogo",
     [("ANALYTICS.METRICAS", "SCHEMA.METRIC_OR_FIELD_ID"), ("ANALYTICS.EVENTOS", "SCHEMA.CAMPO_EVENTO")]),
    ("GTM", "PAC", True, "DERIVED", "Campanha, produto e headline dos assets vêm do plano de lançamento",
     [("PURPOSE.CAMPANHA", "CAMPAIGN.FASE"), ("PURPOSE.PRODUTO", "OFFER.PRODUTO"), ("CONTENT.HEADLINE", "POSITIONING.MENSAGEM")]),
    ("PPR", "PAC", False, "DERIVED", "Destinos dos CTAs são domínios publicados",
     [("DESTINATION.URL", "DOMAINS.DOMINIO")]),
    ("DSI", "PAC", False, "DERIVED", "Visual e legibilidade dos assets seguem o design system",
     [("CONTENT.VISUAL", "TOKENS.COR"), ("ACCESSIBILITY.LEGIBILIDADE", "ACCESSIBILITY.CONTRASTE")]),
    ("DCM", "PAC", False, "DERIVED", "Tracking dos assets usa os eventos catalogados",
     [("TRACKING.EVENTO", "SCHEMA.CAMPO_EVENTO")]),
    ("DRM", "PEM", True, "DERIVED", "Públicos e teses editoriais vêm do mercado",
     [("AUDIENCE.PUBLICOS", "SEGMENTS.SEGMENTO"), ("CONTENT_PILLARS.TESE", "MESSAGING.PROBLEMA")]),
    ("DEB", "PEM", True, "DERIVED", "Claims publicados exigem evidência no dossiê",
     [("BRAND_COMPLIANCE.CLAIMS", "SCHEMA.CLAIM"), ("PRODUCTION.PESQUISA", "SCHEMA.FINDING")]),
    ("PAC", "PEM", True, "DERIVED", "CTAs e destinos das peças vêm do catálogo de CTAs",
     [("CTA.CTA", "CTA_CATALOG.CTA_ID"), ("CTA.DESTINO", "DESTINATION.URL")]),
    ("GTM", "PEM", False, "DERIVED", "Calendário editorial acompanha as atividades de campanha",
     [("EDITORIAL_CALENDAR.TEMA", "CAMPAIGN.ATIVIDADE")]),
    ("DSI", "PEM", False, "DERIVED", "Voz e visual de marca seguem o design system",
     [("BRAND_COMPLIANCE.VISUAL", "TOKENS.COR"), ("BRAND_COMPLIANCE.VOZ", "CONTENT_DESIGN.VOZ")]),
    ("DCM", "PEM", False, "DERIVED", "Conversão é medida pela fórmula catalogada",
     [("MEASUREMENT.CONVERSAO", "SCHEMA.FORMULA")]),
    ("DDE", "PEP", False, "DERIVED", "Inventário de portfólio profissional cita os produtos do ecossistema",
     [("PORTFOLIO_INVENTORY.PROJETO", "ECOSYSTEM.PRODUTOS")]),
    ("DEB", "PEP", False, "DERIVED", "Evidências de cases citam o dossiê",
     [("CASE_STUDIES.EVIDENCIA", "SCHEMA.CITATION")]),
    ("PAC", "PEP", False, "DERIVED", "Portfólio publicado reutiliza assets",
     [("ASSETS.PORTFOLIO", "ASSET_INVENTORY.ASSET_ID")]),
    ("EGC", "RMI", True, "DERIVED", "IDs, tipos, domínios e supersedes do registro seguem a gestão do conhecimento",
     [("SCHEMA.CANONICAL_ID", "IDENTITY.PADRAO_DE_IDS"), ("SCHEMA.OBJECT_TYPE", "ONTOLOGY.OBJETOS"), ("SCHEMA.DOMAIN_ID", "TAXONOMY.DOMINIOS"), ("SCHEMA.SUPERSEDES", "VERSIONING.SUPERSEDE")]),
    ("PPR", "RMI", False, "DERIVED", "Repositório e localização do registro são os inventariados",
     [("SCHEMA.REPOSITORY", "REPOSITORIES.REPO"), ("SCHEMA.LOCATION", "DIRECTORIES.PATH")]),
    ("PPR", "EGC", False, "DERIVED", "Repositórios de conhecimento são os inventariados",
     [("REPOSITORIES.REPOSITORIO", "REPOSITORIES.REPO")]),
    ("DDE", "DRL", True, "DERIVED", "O log de decisões nasce das decisões vigentes e pendentes",
     [("SCHEMA.DECISION_ID", "DECISIONS.DECISOES_VIGENTES"), ("SCHEMA.DECISION_REQUIRED", "DECISIONS.DECISOES_PENDENTES")]),
    ("EGC", "DRL", False, "DERIVED", "Supersedes de decisões seguem a regra de versionamento",
     [("SCHEMA.SUPERSEDES", "VERSIONING.SUPERSEDE")]),
    ("DCM", "PWB", True, "DERIVED", "Campos, fórmulas e indicadores dos workbooks vêm do catálogo de métricas",
     [("FIELDS.DEFINICAO", "SCHEMA.DEFINICAO"), ("FORMULAS.FORMULA", "SCHEMA.FORMULA"), ("OUTPUTS.INDICADOR", "SCHEMA.NOME")]),
    ("EPGD", "PWB", False, "DERIVED", "Fontes dos workbooks são as fontes de dados",
     [("SOURCE_DATA.FONTE", "SOURCES.FONTE")]),
    ("EGC", "PWB", False, "DERIVED", "Versionamento dos workbooks segue a regra de versões",
     [("VERSIONING.VERSAO", "VERSIONING.VERSAO")]),
]

# Arquitetura de Preenchimento: (fase, contexto único, [artefatos em ordem], gate(s), fronteira)
F = [
    ("F1", "Direção e abertura do ecossistema", ["DDE", "TAP"], "G00 INITIATIVE_READY",
     "Raiz da rede: nenhum artefato bloqueia DDE; TAP depende só de DDE."),
    ("F2", "Modelo de negócio e economia", ["MNE", "MFO", "PFO", "MRE"], "G01 BUSINESS_READY (parcial)",
     "Mudança de contexto (estratégia → economia); MNE bloqueia 8 artefatos, inclusive toda a F3."),
    ("F3", "Mercado, pesquisa e evidências", ["DEB", "DRM", "PPE"], "G01 BUSINESS_READY (parcial)",
     "Mesmo contexto comercial de F2, mas bloqueado por MNE; DRM e DEB bloqueiam produto e conteúdo."),
    ("F4", "Governança jurídica e riscos", ["DGRC", "MRC"], "G01 BUSINESS_READY (parcial)",
     "Contexto jurídico; depende só de DDE; bloqueia privacidade/dados (F8)."),
    ("F5", "Pessoas e capacidade de execução", ["PPC", "PEX"], "G01 BUSINESS_READY (fecha)",
     "Contexto de capacidade; PEX exige TAP e PPC; fecha o G01."),
    ("F6", "Produto e experiência (A02)", ["DSI", "DRP", "EEP", "PRD"], "G02 PRODUCT_READY",
     "Bloqueada por DDE, MNE e DRM; ordem interna DRP → EEP → PRD; DSI sem bloqueante (entra primeiro)."),
    ("F7", "Transição Produto → Engenharia (A03)", [], "G03 DEVELOPMENT_READY",
     "Checkpoint sem artefato: 14_REG não tem nenhum artefato em A03 (GAP-DEP-C). Avalia PRD/DSI/EEP para a engenharia."),
    ("F8", "Plataformas, dados e privacidade", ["PPR", "EPGD", "DCM", "PPT"], "G04 (parcial) · G05 (PPT)",
     "Contexto técnico-dados; PPR→EPGD→DCM/PPT; exige DGRC (F4). Precede a engenharia para evitar retrabalho em ETE."),
    ("F9", "Engenharia, contratos e blueprints (A04)", ["ETE", "PCE", "PBL"], "G04 ENGINEERING_READY",
     "Bloqueada por PRD, DSI (via G03), PPR e EPGD; ETE → PCE → PBL."),
    ("F10", "Implementação e operação", ["PIM", "MOP", "RUN"], "G05 RELEASE_READY · G06 GO_LIVE",
     "PIM exige PEX e ETE; RUN exige MOP e PPR; contexto de entrega e operação."),
    ("F11", "Comercial e sucesso do cliente", ["PCV", "PASC"], "G07 OPERATIONAL_READY · G08 (parcial)",
     "PCV exige DRM e PFO; PASC exige MNE; PASC bloqueia o lançamento."),
    ("F12", "Lançamento e conteúdo", ["GTM", "PAC", "PEM"], "G08 GTM_READY",
     "GTM exige DRM, PFO, PRD, PIM e PASC; GTM → PAC → PEM; PEM exige DEB (claims)."),
    ("F13", "Conhecimento, registros e workbooks", ["EGC", "RMI", "DRL", "PWB"], "G09 MEASURED · G11 DOCUMENTED",
     "Contexto de governança do conhecimento; RMI recebe o próprio 16_REG (depends_on/blocks); PWB exige DCM."),
    ("F14", "Emprego e portfólio (A12)", ["PEP"], "gate:tbd",
     "Ramo independente: só dependências informativas; pode correr em paralelo desde F1."),
]


def main() -> int:
    cp_path, out = Path(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    cp = json.loads(cp_path.read_text(encoding="utf-8"))
    campos = {c["field_instance_id"]: c for c in cp["abas"]["15_REG_Campos"]["registros"]}
    arts14 = {a["artifact_id"] for a in cp["abas"]["14_REG_Artefatos"]["registros"]}
    assert set(A.values()) == arts14, "abreviações ≠ 14_REG_Artefatos"
    assert set(GATE) == set(A), "todo artefato precisa de gate (ou gate:tbd)"
    erros, linhas, anexo, mapa = [], [], [], []
    pares = set()
    for i, (s, t, bloq, tag, motivo, refs) in enumerate(E, start=1):
        if (s, t) in pares:
            erros.append(f"aresta duplicada {s}->{t}")
        pares.add((s, t))
        prova = []
        for ct, cs in refs:
            ft, fs = f"{A[t]}.{ct}", f"{A[s]}.{cs}"
            for f in (ft, fs):
                if f not in campos:
                    erros.append(f"campo inexistente: {f}")
            prova.append(f"{ft} ← {fs}")
        did = f"DEP-{i:03d}"
        handoff = (s, t) in HANDOFF_A03
        gate = "G03" if handoff else GATE[s]
        linhas.append([did, A[s], A[t], "depends_on", "TRUE" if bloq else "FALSE", gate, "APPROVED", "PROPOSED"])
        anexo.append([did, tag, f"{motivo}. Campos: " + "; ".join(prova),
                      "PROPOSED — 17_REG_Gates sem required_artifact_types" + ("; transição A03 (G03)" if handoff else "")])
        mapa.append((did, s, t, bloq, tag, motivo, gate, handoff, [p for p in prova]))
    if erros:
        print("\n".join(erros))
        return 1
    sch = ["dependency_id", "source_artifact_id", "target_artifact_id", "relation", "mandatory", "gate_id", "required_status", "status"]
    for nome in ("registro.csv", "registro_para_colar.csv"):  # 16_REG está vazio: todas as linhas são novas
        with (out / nome).open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(sch)
            w.writerows(linhas)
    with (out / "anexo.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dependency_id", "status_epistemico", "justificativa", "gate_status_epistemico"])
        w.writerows(anexo)
    (out / "fases.json").write_text(json.dumps([{"fase": f, "contexto": c, "artefatos": [A[x] for x in arts], "gate": g}
                                                for f, c, arts, g, _ in F], ensure_ascii=False, indent=2), encoding="utf-8")
    (out / "_mapa.json").write_text(json.dumps({"mapa": mapa, "fases": F, "A": A, "gate": GATE}, ensure_ascii=False), encoding="utf-8")
    b = sum(1 for m in mapa if m[3])
    print(f"arestas: {len(E)} (bloqueantes {b}, informativas {len(E) - b}); campos citados verificados: "
          f"{sum(len(m[8]) for m in mapa) * 2}; fases: {len(F)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
