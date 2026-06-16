# Platform Reference — a0.dev

a0.dev (a0.dev) é um AI app builder mobile nativo, apoiado pelo Y Combinator (W25).
Gera React Native + Expo para iOS e Android. Pipeline completo de ideia à App Store.

> **Pré-requisito:** complete as Fases 1 a 4 do CORE antes de usar esta referência.
> Atenção: o vocabulário do mobile é completamente diferente do web. Leia a seção
> de vocabulário antes de começar o intake.

---

## Regra Fundamental: Mobile é Diferente

Ao trabalhar com a0.dev, abandone os termos web. O vocabulário muda inteiramente:

| Termo web | Termo mobile (a0.dev) |
|---|---|
| Página / rota | Tela (Screen) |
| URL / path | Navegação (Stack / Tab / Drawer) |
| Viewport responsivo | Safe area + thumb zone |
| SEO / GEO | ASO (App Store Optimization) |
| Deploy web | Publicar na App Store / Google Play |
| LGPD web | Permissões de device + políticas de store |
| Cookie consent | Solicitação de permissão de notificação/localização |
| Banco de dados SQL direto | Convex ou Supabase via prompt |

---

## a0.dev — O que é e o que não é

**É:**
- Gerador de apps nativas iOS e Android via React Native + Expo
- Preview instantâneo (sem Mac/Xcode necessário) via app mobile próprio
- Pipeline 1-click para App Store e Google Play
- Exporta código-fonte real (.tsx) no plano Pro — sem lock-in

**Não é:**
- Gerador de web apps (mobile only)
- Adequado para lógica server-side complexa, APIs customizadas ou microserviços
- Adequado para empresas reguladas (sem SOC 2, HIPAA, audit logs)
- Uma plataforma madura: YC W25, lançou fev/2025. Documentação ainda crescendo.

---

## Perguntas adicionais de intake (Fase 1 do CORE — vocabulário mobile)

Após as perguntas genéricas do CORE, adicione:

**Plataforma:**
12. iOS only / Android only / ambos?

**Navegação:**
13. Qual padrão de navegação principal?
    - Bottom Tab (3-5 seções principais — padrão para apps consumer)
    - Stack Navigation (fluxos lineares, como onboarding ou checkout)
    - Drawer (menu lateral, para muitas seções)
    - Combinação (Bottom Tab com Stack dentro de cada tab — mais comum)

**Permissões de device:** (declare no intake — cada permissão requer aprovação da store)
14. O app precisa de: câmera / localização / notificações push / microfone / contatos / galeria?
    Para cada uma: qual é o caso de uso específico?

**Backend:**
15. Prefere Convex ou Supabase como backend? (Convex é o default do a0.dev)

**Distribuição:**
16. App gratuito / freemium / pago? Vai usar in-app purchases (IAP)?
17. Vai publicar na App Store (iOS)? Tem conta Apple Developer ($99/ano)?
18. Vai publicar no Google Play (Android)? Tem conta Google Play Developer ($25 único)?

**Bundle identifier** (necessário para publicação):
19. Qual o bundle identifier? Ex: com.empresa.nomeapp (reverse domain notation)

---

## Modelo de Dados no a0.dev (Fase 2 do CORE)

No a0.dev, o modelo de dados vai no prompt inicial e usa Convex ou Supabase.

Para Convex (default):
```
Data model (Convex):
- users: { id, email, name, createdAt, role }
- [entidade2]: { id, userId, [campos], createdAt }
Relationships: [entidade2].userId → users.id
```

Para Supabase:
```
Database schema (Supabase):
CREATE TABLE users (id uuid, email text, name text, created_at timestamp);
CREATE TABLE [tabela2] (id uuid, user_id uuid REFERENCES users(id), [campos]);
-- Enable RLS on all tables
```

---

## Estrutura de Navegação (Fase 2 do CORE — específico mobile)

Declare a estrutura de navegação EXPLICITAMENTE no brief. Não deixe a IA escolher.

**Exemplo de estrutura Bottom Tab + Stack:**
```
Navigation Structure:
- Bottom Tab Navigator (4 tabs):
  - Home (Stack):
    - HomeScreen (lista de itens)
    - ItemDetailScreen (detalhe do item)
    - CreateItemScreen (formulário de criação)
  - Search (Stack):
    - SearchScreen (busca + resultados)
  - Notifications (Stack):
    - NotificationsScreen (lista de notificações)
  - Profile (Stack):
    - ProfileScreen
    - EditProfileScreen
    - SettingsScreen
- Auth Stack (fora do Bottom Tab):
  - OnboardingScreen
  - LoginScreen
  - SignupScreen
  - ForgotPasswordScreen
```

---

## Brief Inicial (formato a0.dev)

```
# [Nome do App] — a0.dev Brief

## App Overview
[O que é, problema que resolve, usuário principal]
Platform: iOS and Android (React Native + Expo)
Backend: [Convex / Supabase]

## Competitive Edge
[2-3 diferenciais baseados na pesquisa]

## Navigation Structure
[Estrutura completa de navegação da Fase 2]

## Core Screens (MVP, em ordem de prioridade)
1. [Screen 1]: [o que o usuário faz nesta tela]
2. [Screen 2]: [o que o usuário faz nesta tela]
...

## Data Model
[Schema do Fase 2 — Convex ou Supabase]

## Device Permissions Required
- [Permissão 1]: [justificativa para o usuário e para a store]
- [Permissão 2]: [justificativa]
(Apenas as permissões necessárias — cada uma é aprovada pela store)

## App Identity
Bundle identifier: [com.empresa.nomeapp]
App name: [Nome exato como vai aparecer na store]

## Monetization
[Gratuito / IAP / Subscription — especificar produto e preço se aplicável]

## Visual Style
[Estilo visual: clean/bold/etc, cores primária e secundária, dark mode]
[Referências visuais de outros apps se houver]

## Build Order
1. Auth flow (login, signup, forgot password)
2. Main navigation structure
3. [Screen 1 principal]
4. [Screen 2 principal]
...
N. Push notifications setup
N+1. App Store submission prep

## Safe-Guard Instructions
- NÃO construa múltiplas telas de uma vez
- NÃO avance sem testar a tela anterior no preview
- NÃO use permissões de device sem justificativa clara para a store
- SEMPRE use safe area insets (SafeAreaView / useSafeAreaInsets)
- SEMPRE respeite thumb zones: ações primárias na metade inferior da tela
```

---

## Artefatos de Reancoragem (Fase 5.5 do CORE — mobile)

Quando o a0.dev perder o contexto, recole:
- A estrutura de navegação completa
- O data model (Convex/Supabase schema)
- O bundle identifier e nome do app
- As permissões de device declaradas
- O estado atual: quais telas estão prontas e quais estão em andamento

---

## ASO — App Store Optimization (em vez de SEO/GEO)

Perto do lançamento, inclua na fila:

**Checklist de submissão:**
- [ ] Nome do app (máximo 30 chars no iOS)
- [ ] Subtitle (iOS, 30 chars) / Short description (Android, 80 chars)
- [ ] Descrição completa (4000 chars — include keywords naturalmente)
- [ ] Keywords (iOS: 100 chars de keywords separadas por vírgula)
- [ ] Screenshots para todos os tamanhos obrigatórios
- [ ] App preview video (opcional mas aumenta conversão)
- [ ] Ícone do app: 1024x1024px PNG sem alpha
- [ ] Privacy Policy URL (obrigatória para ambas as stores)
- [ ] Categoria principal e secundária
- [ ] Rating (conteúdo e faixa etária)

---

## Limitações e Gotchas do a0.dev

- **Mobile only**: se precisar de web também, use Lovable/Bolt em paralelo.
- **Message caps**: plataforma baseada em mensagens. Prompts bem especificados
  economizam mensagens. Exploração livre esgota rápido.
- **Sem compliance enterprise**: sem SOC 2, HIPAA, audit logs. Para apps em
  setores regulados, avaliar alternativas.
- **Plataforma muito nova** (fev/2025): edge cases, documentação e suporte ainda
  maturando. Evolui rápido — revalidar esta referência a cada 3-6 meses.
- **Preview web ≠ device**: React Native Web no preview não é idêntico ao app real.
  Testar no device físico antes de submeter à store.
- **Perda de contexto em projetos grandes**: igual outros geradores. Use a
  reancoragem antes que a divergência acumule.
- **Apple Developer Account**: $99/ano. Obrigatório para publicar no iOS.
  Processo de aprovação pode levar dias. Planejar antecipadamente.
