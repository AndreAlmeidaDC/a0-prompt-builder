# a0-prompt-builder

Skill de IA para construir apps mobile nativos (iOS e Android) no **a0.dev** sem o erro
clássico de tratar mobile como se fosse web. Ela traduz sua ideia para o vocabulário e
as restrições reais do mobile, e te leva do brief à submissão na loja.

---

## O problema que esta skill resolve

Quem chega no a0.dev vindo de builders web comete o mesmo erro: pede "páginas", "rotas"
e "SEO". O a0.dev faz o que dá, mas o resultado parece um site empacotado, não um app
nativo — navegação estranha, layout que ignora as áreas seguras do aparelho, nenhuma
noção de como o usuário realmente toca na tela.

Mobile tem complexidades que web não tem e que precisam ser decididas antes do primeiro
prompt: qual padrão de navegação (abas inferiores? pilha? gaveta lateral?), quais
permissões de aparelho (câmera, localização, notificação — cada uma exige justificativa
aprovada pela loja), áreas seguras (notch, Dynamic Island), e um pipeline de publicação
que envolve conta de desenvolvedor Apple (US$ 99/ano) e revisão que pode levar dias.

Pular essas decisões no começo significa retrabalho caro no meio.

## Como a skill foi pensada

A skill foi desenhada em torno de uma tradução: **pegar sua ideia de produto e
expressá-la no vocabulário do mobile nativo**, com as decisões estruturais tomadas antes
de gerar qualquer tela.

### Explorando as forças do a0.dev

- **O a0.dev gera React Native + Expo nativo e publica nas lojas.** A skill aproveita
  isso estruturando o brief para um app real de loja, não um protótipo, incluindo bundle
  identifier, permissões e estratégia de submissão desde o início.
- **O a0.dev tem preview instantâneo no celular.** A skill organiza o build em telas
  atômicas para você validar cada uma no preview antes de avançar.
- **O a0.dev integra Convex e Supabase como backend.** A skill modela os dados já na
  opção escolhida, em vez de deixar a IA decidir.
- **O a0.dev exporta o código real** (no plano Pro). A skill trata o projeto como código
  de verdade, com estrutura de navegação e dados pensada para durar.

### Mitigando as fraquezas do a0.dev

- **Vocabulário web aplicado a mobile.** Mitigado com uma tradução sistemática: telas em
  vez de páginas, navegação (stack/tab/drawer) em vez de rotas, ASO em vez de SEO,
  permissões de aparelho em vez de cookies.
- **Navegação confusa por falta de decisão.** Mitigada exigindo que o padrão de navegação
  seja definido explicitamente no brief, não deixado para a IA adivinhar.
- **Permissões mal declaradas (que travam aprovação na loja).** Mitigadas coletando as
  permissões necessárias no intake, cada uma com a justificativa que a loja exige.
- **Limite de mensagens por plano.** Mitigado com prompts bem especificados que reduzem
  idas e vindas — exploração livre esgota o limite rápido.
- **Plataforma nova, que muda rápido.** Mitigada com o protocolo de verificação de versão
  da skill e a recomendação de revalidar a referência periodicamente.

## O que a skill faz, passo a passo

**Intake mobile.** Além do escopo de produto: plataforma-alvo (iOS/Android/ambos),
padrão de navegação, permissões de aparelho necessárias, backend (Convex ou Supabase),
bundle identifier e estratégia de monetização (compras no app / assinatura).

**Modelagem de telas e navegação.** Mapeia o fluxo em telas e numa estrutura de
navegação explícita — quem leva a quem, e como.

**Brief estruturado.** Monta o prompt inicial no formato do a0.dev (organizado pelo
framework MAPS: Mission, Actions, Pages/Screens, Specs), com navegação, dados, permissões
e ordem de build.

**Loop de feedback.** Prompts atômicos por tela, tratamento de erro específico, e
reancoragem com os artefatos certos quando o a0.dev perde o contexto.

**Submissão.** Checklist de ASO (App Store Optimization) e dos requisitos de submissão
para App Store e Google Play.

## Como usar

1. Carregue esta skill no seu chat de IA (Claude, ChatGPT, etc.)
2. Responda o intake — com atenção a plataforma, navegação e permissões
3. Cole o brief gerado no a0.dev e siga o loop de feedback, tela por tela
4. Use o checklist de ASO e submissão ao final

A skill gera os prompts; você faz a ponte de copiar e colar para o a0.dev. Ela não
se conecta ao a0.dev nem executa nada por você — é uma ferramenta de raciocínio e
especificação, não de automação.

## FAQ

**Dá para fazer um app web com o a0.dev?**
Não — ele é mobile only (iOS e Android). Se você precisa também de um painel web, ele
teria que ser feito em outra ferramenta.

**Preciso de Mac para usar?**
Para desenvolver e ver o preview, não — o a0.dev tem preview no próprio celular. Para
publicar na App Store, você precisa de uma conta de desenvolvedor Apple (US$ 99/ano); o
processo de build em si o a0.dev resolve.

**Por que a skill insiste em definir a navegação antes?**
Porque a estrutura de navegação é a espinha de um app mobile. Definir antes evita que a
IA escolha um padrão que não combina com o seu produto e que seja caro mudar depois.

**O preview no celular é igual ao app final?**
Quase. Algumas dependências sem suporte no preview web funcionam no aparelho físico.
A skill recomenda testar no device antes de submeter à loja.

**A skill se conecta ao a0.dev automaticamente?**
Não. Ela gera os prompts e você cola no a0.dev. Funciona em qualquer chat de IA.

**O a0.dev serve para app corporativo regulado?**
Tenha cautela: a plataforma é voltada a indie hackers e não traz, por padrão,
certificações como SOC 2 ou HIPAA nem logs de auditoria. A skill sinaliza isso.

**E acessibilidade?**
A skill traz uma referência de acessibilidade, mas ela cobre só interface web (DOM). O
a0.dev gera app mobile nativo, onde acessibilidade é outra coisa (touch target, screen
reader nativo, contraste próprio), e isso não está coberto aqui por enquanto. No fluxo,
a pergunta de acessibilidade web não se aplica: responda que não e siga.

## Estrutura do repositório

```
SKILL.md                          # Ponto de entrada: papel e como usar
references/
  vibecode-core.md                # Processo de engenharia (compartilhado na família)
  platform-a0dev.md               # Navegação mobile, permissões, ASO, pipeline de loja
  archetypes.md                   # Guia de escolha de plataforma
  version-check.md                # Protocolo de auto-atualização
  accessibility-web.md            # Acessibilidade web (opcional, ver gate na Fase 1)
templates/
  PRD.md                          # Template de requisitos de produto
  DATA_MODEL.md                   # Template de modelo de dados
  USER_FLOW.md                    # Template de fluxo de usuário
scripts/
  validate_skill.py               # Validação local da skill
```

## Por que existem 6 skills e não uma só

Essa pergunta é legítima — o processo de fundo (especificar antes de gerar, modelar
dados, iterar de forma atômica, reancorar quando a IA perde o contexto) é o mesmo em
todas as plataformas. Seria tentador fazer uma skill única que cobre tudo.

Não fizemos, por três razões:

**1. Contexto desperdiçado.** Uma skill única carregaria as particularidades de seis
plataformas em toda sessão, sendo que você só usa uma. A maior parte do que entrasse no
contexto seria ruído para a sua tarefa. Skills separadas carregam só o que importa para
a plataforma que você escolheu.

**2. As plataformas divergem mais do que parecem.** O v0 gera componentes, não apps.
O a0.dev fala de telas e navegação, não de páginas e rotas. O Base44 não te dá o código.
O emergent usa MongoDB e um time de agentes; os outros não. Espremer tudo num fluxo único
exigiria tantos "se for plataforma X, faça Y" que o resultado seria confuso e frágil.

**3. Evolução independente.** Cada plataforma muda no seu ritmo. Quando uma lança um
recurso novo, a skill dela é atualizada sem tocar nas outras cinco.

O que é genuinamente compartilhado (o processo de engenharia) vive em um único arquivo,
`references/vibecode-core.md`, idêntico em todas as skills. Assim evitamos duplicação no
que importa e mantemos independência onde importa.

## Família vibecode

| Skill | Plataforma | Melhor para |
|---|---|---|
| [lovable-prompt-builder](https://github.com/AndreAlmeidaDC/lovable-prompt-builder) | Lovable | App web full-stack com fluxo guiado passo a passo |
| [bolt-prompt-builder](https://github.com/AndreAlmeidaDC/bolt-prompt-builder) | bolt.new | App web full-stack com brief único e controle total |
| [v0-prompt-builder](https://github.com/AndreAlmeidaDC/v0-prompt-builder) | v0 (Vercel) | Componentes React/shadcn de alta qualidade |
| **a0-prompt-builder** (esta skill) | a0.dev | App mobile nativo iOS/Android |
| [base44-prompt-builder](https://github.com/AndreAlmeidaDC/base44-prompt-builder) | Base44 | Ferramenta interna / protótipo com backend incluído |
| [emergent-prompt-builder](https://github.com/AndreAlmeidaDC/emergent-prompt-builder) | emergent.sh | Full-stack multi-agente (web + mobile), código seu |

## Licença

MIT — André Almeida
