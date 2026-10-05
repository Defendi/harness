# Guia do Visual Companion

Companheiro visual de brainstorming baseado em navegador para exibir mockups, diagramas e opções.

## Quando Usar

Decida por pergunta, não por sessão. O teste: **o usuário entenderia isso melhor vendo do que lendo?**

**Use o navegador** quando o próprio conteúdo for visual:

- **Mockups de UI** — wireframes, layouts, estruturas de navegação, designs de componentes
- **Diagramas de arquitetura** — componentes do sistema, fluxo de dados, mapas de relacionamento
- **Comparações visuais lado a lado** — comparação entre dois layouts, dois esquemas de cores, duas direções de design
- **Polimento de design** — quando a pergunta for sobre look and feel, espaçamento, hierarquia visual
- **Relações espaciais** — máquinas de estado, fluxogramas, relacionamentos de entidades renderizados como diagramas

**Use o terminal** quando o conteúdo for textual ou tabular:

- **Perguntas de requisitos e escopo** — "o que X significa?", "quais funcionalidades estão no escopo?"
- **Escolhas conceituais A/B/C** — escolher entre abordagens descritas em palavras
- **Listas de tradeoffs** — prós/contras, tabelas de comparação
- **Decisões técnicas** — design de API, modelagem de dados, seleção de abordagem arquitetural
- **Perguntas de esclarecimento** — qualquer caso em que a resposta seja em palavras, não uma preferência visual

Uma pergunta *sobre* um tópico de UI não é automaticamente uma pergunta visual. "Que tipo de wizard você quer?" é conceitual — use o terminal. "Qual destes layouts de wizard parece melhor?" é visual — use o navegador.

## Como Funciona

O servidor monitora um diretório em busca de arquivos HTML e serve o mais recente para o navegador. Você grava o conteúdo HTML em `screen_dir`, o usuário o visualiza no navegador e pode clicar para selecionar opções. As seleções são registradas em `state_dir/events`, que você lê no seu próximo turno.

**Fragmentos de conteúdo vs documentos completos:** Se o seu arquivo HTML começar com `<!DOCTYPE` ou `<html`, o servidor o servirá no estado em que se encontra (apenas injeta o script auxiliar). Caso contrário, o servidor envolve automaticamente o seu conteúdo no template de frame — adicionando o cabeçalho, tema CSS, status de conexão e toda a infraestrutura interativa. **Escreva fragmentos de conteúdo por padrão.** Escreva documentos completos apenas quando precisar de controle total sobre a página.

## Iniciando uma Sessão

```bash
# Inicie DEPOIS que o usuário aprovar o companion. --open abre o navegador automaticamente na
# primeira tela; --project-dir persiste mockups e permite reiniciar na mesma porta.
bash scripts/start-server.sh --project-dir /path/to/project --open

# Retorna: {"type":"server-started","port":52341,
#           "url":"http://localhost:52341/?key=ab12…",
#           "screen_dir":"/path/to/project/.superpowers/brainstorm/12345-1706000000/content",
#           "state_dir":"/path/to/project/.superpowers/brainstorm/12345-1706000000/state"}
```

Salve o `screen_dir` e o `state_dir` da resposta. Com `--open`, o navegador se abre sozinho quando você envia a primeira tela — não é necessário pedir ao usuário para abri-lo, mas ainda assim compartilhe a URL como fallback (configurações headless/remotas não abrirão automaticamente).

**A URL contém uma chave de sessão (`?key=…`).** O servidor rejeita qualquer requisição sem ela, portanto, sempre forneça ao usuário a URL **completa** do campo `url` — nunca remova a query string e nunca entregue um `http://host:port` simples. A chave controla o acesso HTTP e WebSocket para que uma aba perdida do navegador ou outra máquina na rede não possa ler as telas ou injetar eventos. Após o primeiro carregamento, o navegador lembra da chave via cookie, portanto, recarregamentos e assets em `/files/*` funcionam sem precisar repeti-la.

**Localizando informações de conexão:** O servidor grava seu JSON de inicialização em `$STATE_DIR/server-info`. Se você iniciou o servidor em segundo plano e não capturou o stdout, leia esse arquivo para obter a URL e a porta. Ao usar `--project-dir`, verifique `<project>/.superpowers/brainstorm/` para encontrar o diretório da sessão.

**Nota:** Passe a raiz do projeto como `--project-dir` para que os mockups persistam em `.superpowers/brainstorm/` e sobrevivam a reinicializações do servidor. Sem isso, os arquivos vão para `/tmp` e são descartados. Lembre o usuário de adicionar `.superpowers/` ao `.gitignore` se ainda não estiver lá.

**Iniciando o servidor por plataforma:**

**Claude Code:**
```bash
# O modo padrão funciona — o próprio script coloca o servidor em segundo plano.
bash scripts/start-server.sh --project-dir /path/to/project --open
```

No Windows, o script detecta automaticamente e alterna para o modo foreground (que bloqueia a chamada de ferramenta). Use `run_in_background: true` na chamada da ferramenta Bash para que o servidor sobreviva entre os turnos de conversa e, em seguida, leia `$STATE_DIR/server-info` no próximo turno para obter a URL e a porta.

**Codex:**
```bash
# O Codex encerra processos em segundo plano. O script detecta automaticamente CODEX_CI e
# alterna para o modo foreground. Execute normalmente — nenhuma flag extra é necessária.
bash scripts/start-server.sh --project-dir /path/to/project --open
```

**Gemini CLI:**
```bash
# Use --foreground e defina is_background: true na sua chamada de ferramenta de shell
# para que o processo sobreviva entre os turnos
bash scripts/start-server.sh --project-dir /path/to/project --open --foreground
```

**Copilot CLI:**
```bash
# Inicie com o mecanismo de shell não bloqueante/em segundo plano do Copilot CLI para que o
# servidor sobreviva entre os turnos. Mantenha --foreground para que o harness, e não o
# script, gerencie a execução em segundo plano. O inicializador é um .sh, portanto, invoque-o via bash
# (no Windows, chame o bash.exe do Git Bash a partir da ferramenta PowerShell).
bash scripts/start-server.sh --project-dir /path/to/project --open --foreground
```

**Outros ambientes:** O servidor deve continuar rodando em segundo plano entre os turnos de conversa. Se o seu ambiente encerra processos desanexados, use `--foreground` e execute o comando com o mecanismo de execução em segundo plano da sua plataforma.

Se a URL estiver inacessível pelo seu navegador (comum em ambientes remotos/conteinerizados), vincule a um host que não seja de loopback:

```bash
bash scripts/start-server.sh \
  --project-dir /path/to/project \
  --host 0.0.0.0 \
  --url-host localhost
```

Use `--url-host` para controlar qual hostname será exibido no JSON da URL retornada.

## O Loop

1. **Verifique se o servidor está ativo**, depois **escreva o HTML** em um novo arquivo em `screen_dir`:
   - **Obrigatório: confirme que o servidor está ativo antes de referenciar a URL ou enviar uma tela.** Verifique se `$STATE_DIR/server-info` existe e `$STATE_DIR/server-stopped` não existe. Se ele tiver sido encerrado, reinicie-o com `start-server.sh` usando o **mesmo `--project-dir`** — ele reutiliza a mesma porta, permitindo que a aba aberta do usuário se reconecte sozinha (ela exibe uma sobreposição de "paused" enquanto o servidor estiver fora do ar) e você não precise enviar uma nova URL. O servidor é encerrado automaticamente após 4 horas de inatividade (configurável com `--idle-timeout-minutes`).
   - Use nomes de arquivo semânticos: `platform.html`, `visual-style.html`, `layout.html`
   - **Nunca reutilize nomes de arquivo** — cada tela recebe um arquivo novo
   - Use sua ferramenta de criação de arquivos — **nunca use cat/heredoc** (gera ruído desnecessário no terminal)
   - O servidor serve automaticamente o arquivo mais recente

2. **Informe ao usuário o que esperar e finalize seu turno:**
   - Lembre-o da URL (a cada etapa, não apenas na primeira)
   - Forneça um breve resumo em texto do que está na tela (ex.: "Exibindo 3 opções de layout para a página inicial")
   - Peça para responderem no terminal: "Dê uma olhada e me diga o que acha. Clique para selecionar uma opção, se desejar."

3. **No seu próximo turno** — após o usuário responder no terminal:
   - Leia `$STATE_DIR/events` se ele existir — este arquivo contém as interações do usuário no navegador (cliques, seleções) como linhas de JSON
   - Junte com o texto do terminal do usuário para obter o panorama completo
   - A mensagem no terminal é o feedback principal; `state_dir/events` fornece dados estruturados da interação

4. **Itere ou avance** — se o feedback alterar a tela atual, escreva um novo arquivo (ex.: `layout-v2.html`). Avance para a próxima pergunta apenas quando a etapa atual for validada.

5. **Descarregue ao retornar ao terminal** — quando a próxima etapa não precisar do navegador (ex.: uma pergunta de esclarecimento, uma discussão de tradeoffs), envie uma tela de espera para limpar o conteúdo obsoleto:

   ```html
   <!-- nome do arquivo: waiting.html (ou waiting-2.html, etc.) -->
   <div style="display:flex;align-items:center;justify-content:center;min-height:60vh">
     <p class="subtitle">Continuando no terminal...</p>
   </div>
   ```

   Isso evita que o usuário fique olhando para uma escolha já resolvida enquanto a conversa avança. Quando a próxima pergunta visual surgir, envie um novo arquivo de conteúdo normalmente.

6. Repita até concluir.

## Escrevendo Fragmentos de Conteúdo

Escreva apenas o conteúdo que vai dentro da página. O servidor o envolve automaticamente no template de frame (cabeçalho, CSS do tema, status de conexão e toda a infraestrutura interativa).

**Exemplo mínimo:**

```html
<h2>Qual layout funciona melhor?</h2>
<p class="subtitle">Considere a legibilidade e a hierarquia visual</p>

<div class="options">
  <div class="option" data-choice="a" onclick="toggleSelect(this)">
    <div class="letter">A</div>
    <div class="content">
      <h3>Coluna Única</h3>
      <p>Experiência de leitura limpa e focada</p>
    </div>
  </div>
  <div class="option" data-choice="b" onclick="toggleSelect(this)">
    <div class="letter">B</div>
    <div class="content">
      <h3>Duas Colunas</h3>
      <p>Navegação na barra lateral com conteúdo principal</p>
    </div>
  </div>
</div>
```

É isso. Nenhuma tag `<html>`, CSS ou `<script>` é necessária. O servidor fornece tudo isso.

## Classes CSS Disponíveis

O template de frame fornece estas classes CSS para o seu conteúdo:

### Opções (escolhas A/B/C)

```html
<div class="options">
  <div class="option" data-choice="a" onclick="toggleSelect(this)">
    <div class="letter">A</div>
    <div class="content">
      <h3>Título</h3>
      <p>Descrição</p>
    </div>
  </div>
</div>
```

**Seleção múltipla:** Adicione `data-multiselect` ao container para permitir que os usuários selecionem múltiplas opções. Cada clique alterna a estilização de seleção do item.

```html
<div class="options" data-multiselect>
  <!-- mesma marcação de opções — os usuários podem selecionar/desmarcar múltiplos itens -->
</div>
```

### Cards (designs visuais)

```html
<div class="cards">
  <div class="card" data-choice="design1" onclick="toggleSelect(this)">
    <div class="card-image"><!-- conteúdo do mockup --></div>
    <div class="card-body">
      <h3>Nome</h3>
      <p>Descrição</p>
    </div>
  </div>
</div>
```

### Container de mockup

```html
<div class="mockup">
  <div class="mockup-header">Preview: Layout do Dashboard</div>
  <div class="mockup-body"><!-- seu HTML de mockup --></div>
</div>
```

### Visualização dividida (lado a lado)

```html
<div class="split">
  <div class="mockup"><!-- esquerda --></div>
  <div class="mockup"><!-- direita --></div>
</div>
```

### Prós/Contras

```html
<div class="pros-cons">
  <div class="pros"><h4>Prós</h4><ul><li>Vantagem</li></ul></div>
  <div class="cons"><h4>Contras</h4><ul><li>Desvantagem</li></ul></div>
</div>
```

### Elementos mock (blocos de construção de wireframe)

```html
<div class="mock-nav">Logo | Início | Sobre | Contato</div>
<div style="display: flex;">
  <div class="mock-sidebar">Navegação</div>
  <div class="mock-content">Área de conteúdo principal</div>
</div>
<button class="mock-button">Botão de Ação</button>
<input class="mock-input" placeholder="Campo de entrada">
<div class="placeholder">Área de placeholder</div>
```

### Tipografia e seções

- `h2` — título da página
- `h3` — cabeçalho de seção
- `.subtitle` — texto secundário abaixo do título
- `.section` — bloco de conteúdo com margem inferior
- `.label` — texto de rótulo pequeno em maiúsculas

## Formato dos Eventos do Navegador

Quando o usuário clica em opções no navegador, suas interações são registradas em `$STATE_DIR/events` (um objeto JSON por linha). O arquivo é limpo automaticamente quando você envia uma nova tela.

```jsonl
{"type":"click","choice":"a","text":"Option A - Simple Layout","timestamp":1706000101}
{"type":"click","choice":"c","text":"Option C - Complex Grid","timestamp":1706000108}
{"type":"click","choice":"b","text":"Option B - Hybrid","timestamp":1706000115}
```

O fluxo completo de eventos mostra o caminho de exploração do usuário — ele pode clicar em várias opções antes de se decidir. O último evento de `choice` é tipicamente a seleção final, mas o padrão de cliques pode revelar hesitação ou preferências sobre as quais vale a pena perguntar.

Se `$STATE_DIR/events` não existir, o usuário não interagiu com o navegador — use apenas o texto do terminal.

## Dicas de Design

- **Ajuste a fidelidade à pergunta** — wireframes para layout, polimento para perguntas de refinamento visual
- **Explique a pergunta em cada página** — "Qual layout parece mais profissional?" e não apenas "Escolha um"
- **Itere antes de avançar** — se o feedback alterar a tela atual, escreva uma nova versão
- **No máximo 2 a 4 opções** por tela
- **Use conteúdo real quando for relevante** — para um portfólio de fotografia, use imagens reais (Unsplash). Conteúdo placeholder mascara problemas de design.
- **Mantenha os mockups simples** — foque no layout e na estrutura, não em um design pixel-perfect

## Nomenclatura de Arquivos

- Use nomes semânticos: `platform.html`, `visual-style.html`, `layout.html`
- Nunca reutilize nomes de arquivo — cada tela deve ser um novo arquivo
- Para iterações: adicione um sufixo de versão como `layout-v2.html`, `layout-v3.html`
- O servidor serve o arquivo mais recente com base na data de modificação

## Limpeza

```bash
bash scripts/stop-server.sh $SESSION_DIR
```

Se a sessão tiver usado `--project-dir`, os arquivos de mockup persistirão em `.superpowers/brainstorm/` para referência futura. Apenas as sessões em `/tmp` são excluídas ao parar o servidor.

## Referência

- Template de frame (referência de CSS): `scripts/frame-template.html`
- Script auxiliar (client-side): `scripts/helper.js`
