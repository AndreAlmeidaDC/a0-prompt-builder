# Platform Reference — a0.dev

**Última verificação:** 2026-09-02, documentação oficial do a0.dev.

a0 gera apps Expo/React Native para iOS e Android e oferece preview, builds nativos, OTA e publicação. O fluxo seguro depende de distinguir runtime, código JavaScript/assets, configuração nativa e store state.

Fontes oficiais principais:

- https://docs.a0.dev/development/testing/overview
- https://docs.a0.dev/development/testing/web-preview
- https://docs.a0.dev/development/testing/native-build-testing
- https://docs.a0.dev/advanced/upgrading-your-project
- https://docs.a0.dev/development/deep-links
- https://docs.a0.dev/development/push-notifications
- https://docs.a0.dev/publishing/ota-updates/deploy-updates
- https://docs.a0.dev/publishing/ios/deploying-on-a0

## Inspeção inicial

Antes do plano, obtenha do projeto:

- `.a0/build.yaml` e `runtimeVersion`;
- package/dependencies;
- telas e navegação;
- iOS bundle ID e Android package;
- versões de app/build;
- permissões e módulos nativos;
- deep-link schemes;
- backend, auth e dados;
- deployed OTA update;
- últimos IPA/APK/TestFlight/Play builds;
- credenciais configuradas;
- dispositivos e OS cobertos.

Não pergunte o que os arquivos ou dashboard já respondem.

## Build and Runtime Spec

Mantenha um registro:

```yaml
runtime_version: [observado]
expo_sdk: [observado]
app_version:
  ios: [valor]
  android: [valor]
build_number:
  ios: [valor]
  android: [valor]
permissions: []
schemes: []
native_modules: []
last_ota: [id/data]
last_native_build: [id/data]
compatibility_notes: []
```

Runtime upgrade pode alterar Expo, React Native e módulos. Faça branch/checkpoint, leia breaking changes, rode teste completo e prepare novo build.

## OTA decision

Use OTA apenas quando:

- runtime instalado é compatível;
- mudança é JavaScript/asset suportado;
- não altera ícone, permissões, scheme ou configuração nativa;
- beta/smoke foi executado;
- rollback está definido.

Novo build é necessário quando há runtime upgrade ou mudança nativa/configuração de build. Usuários em runtime antigo não recebem update incompatível.

## Evidence ladder

### Web preview

React Native Web: rápido para layout e lógica compatível. Não prova câmera, biometria, push, pagamentos, módulos nativos ou diferenças de plataforma.

### a0 app / Expo Go

Útil para UI/UX e recursos suportados. Pode não suportar pagamentos, ads e módulos customizados.

### Native IPA/APK/TestFlight

Obrigatório para comportamento nativo, push, pagamento, entitlement, credenciais e release. Teste em iOS e Android reais quando ambos são suportados.

## Deep links

Schemes são declarados em `.a0/build.yaml` e precisam alinhar:

- bundle/package;
- NavigationContainer;
- rotas e parâmetros;
- auth/email callbacks;
- ambiente dev/prod;
- validação de origem e parâmetros;
- testes simulador e aparelho.

Não aceite um link abrir o app como prova de que a rota e autorização estão corretas.

## Push notifications

Push usa token nativo do dispositivo e backend. Verifique:

- pedido de permissão contextual;
- token armazenado e rotacionado;
- usuário/dispositivo/ambiente;
- FCM/APNs credentials;
- envio somente server-side;
- payload mínimo e sem dado sensível desnecessário;
- tap routing e autorização;
- foreground/background/terminated;
- opt-out e limpeza de token;
- TestFlight/custom APK, não apenas Expo Go.

## Backend e dados

Não force Convex ou Supabase sem observar projeto/caso de uso. Para persistência:

- ownership e autorização server-side;
- validação;
- offline/sync e conflitos;
- exclusão e retenção;
- migração e backup;
- ambientes e secrets.

## Prompt de planejamento

```text
Inspecione o projeto a0 sem editar nem implantar.

Objetivo: [resultado]
Plataformas: [iOS/Android]
Runtime/build observados: [valores]
Preservar: [itens]
Escopo: [telas/arquivos]

Entregue fatos, risco nativo, arquivos, etapas pequenas, camada de teste por etapa,
decisão OTA versus novo build e rollback. Não gere build nem update.
```

## Prompt atômico

```text
Implemente somente [mudança] no runtime atual.

Preserve: [navegação/dados]
Áreas permitidas: [lista]
Contrato: [comportamento]
Permissões: não adicionar sem aprovação
Deep links/push/background: [impacto]
Verificação: [web/mobile/native conforme necessário]

Não altere build settings, não faça OTA, build ou submissão.
Mostre diff, testes e pontos cegos.
```

## Native test matrix

Registre pelo menos:

| Plataforma | Dispositivo/OS | Build/runtime | Estado de permissão | Cenário | Resultado |
|---|---|---|---|---|---|

Inclua rede ruim/offline, background/foreground, cold start, deep link, denial de permissão, font scaling, reduced motion, login expirado e upgrade quando aplicável.

## Release gates

Antes de OTA ou store:

- runtime/build spec atualizado;
- versão e release notes;
- credenciais e bundle/package corretos;
- privacy labels/data safety baseadas no app real;
- política e suporte próprios;
- beta test;
- crash/log/analytics proporcionais;
- staged/manual release quando possível;
- rollback;
- aprovação explícita.

Não copie recomendações genéricas de classificação etária ou privacidade sem avaliar o app e as regras atuais das lojas.

## Claims voláteis

Versões de Expo/a0, previews, planos, contas, store rules e documentação de device registration mudam. Revalide no dia do build ou submissão.
