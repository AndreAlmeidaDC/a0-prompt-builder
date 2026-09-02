# Vibecode Core — fluxo proporcional para mobile AI builders

Este CORE preserva disciplina sem importar vocabulário web para apps nativos.

## Regras

1. Inspecione projeto, runtime, builds, navegação, backend e store state antes de perguntar.
2. Separe contexto persistente, plano, mudança atômica, verificação e release.
3. Não force auth, backend, push, pagamentos ou permissões antes do caso de uso.
4. Trate runtime/build e JavaScript/assets como camadas diferentes.
5. Preview rápido não substitui build nativo e aparelho real.
6. Cada mudança tem escopo, critérios, sensores, rollback e ações proibidas.
7. OTA, builds, TestFlight, Play, credenciais e publicação exigem aprovação explícita.

## Fases

### 0. Estado

Registre:

- app novo ou existente;
- runtime version e estado de upgrade;
- iOS, Android ou ambos;
- navegação e telas;
- backend e dados;
- permissões e módulos nativos;
- builds, OTA e stores;
- branch/repositório quando houver;
- ambiente e dados reais.

### 1. Intenção

Defina problema, usuário, principal ação, menor versão valiosa, fora de escopo, critérios de sucesso e riscos.

### 2. Especificação proporcional

Produza somente o necessário:

- screen flow e navegação;
- contrato de tela/componente;
- data model e autorização se houver persistência;
- permission map;
- build/runtime spec;
- release plan para mudança que alcança usuários.

### 3. Plano

Liste arquivos/telas, dependências, risco nativo, sequência, sensor por etapa, compatibilidade de runtime e rollback.

### 4. Implementação

Uma mudança por rodada. Preserve navegação, storage, deep links, acessibilidade e comportamento de background quando relevantes. Não altere build settings escondido numa tarefa de UI.

### 5. Verificação

Use a camada correta:

- web preview para feedback rápido compatível;
- a0 app/Expo Go para UI e fluxo suportado;
- native IPA/APK/TestFlight para pagamentos, push e módulos nativos;
- iOS e Android separados;
- network loss, background/foreground, permissions denied, deep link, font scaling e reduced motion.

### 6. Release

Escolha OTA apenas quando o código é compatível com o runtime instalado. Mudança de runtime, ícone, permissões ou configuração nativa pede novo build. Registre versão, rollout, rollback e smoke.

## Encerramento

Informe mudança, camada testada, dispositivos/builds, resultados, pontos cegos, risco de runtime e próximo estado. Não declare “testado no mobile” quando só houve web preview.
