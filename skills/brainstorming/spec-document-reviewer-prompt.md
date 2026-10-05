# Template de Prompt para Revisor de Documento de Especificação

Use este template ao disparar um subagent revisor de documento de especificação.

**Objetivo:** Verificar se a spec está completa, consistente e pronta para o planejamento da implementação.

**Disparar após:** O documento de especificação for gravado em docs/superpowers/specs/

```
Subagent (general-purpose):
  description: "Revisar documento de especificação"
  prompt: |
    Você é um revisor de documento de especificação. Verifique se esta spec está completa e pronta para o planejamento.

    **Spec a revisar:** [SPEC_FILE_PATH]

    ## O que Verificar

    | Categoria | O que Procurar |
    |-----------|----------------|
    | Completude | TODOs, placeholders, "TBD", seções incompletas |
    | Consistência | Contradições internas, requisitos conflitantes |
    | Clareza | Requisitos ambíguos o suficiente para fazer alguém construir a coisa errada |
    | Escopo | Focado o suficiente para um único plano — sem cobrir múltiplos subsistemas independentes |
    | YAGNI | Recursos não solicitados, over-engineering |

    ## Calibração

    **Aponte apenas problemas que causariam problemas reais durante o planejamento da implementação.**
    Uma seção ausente, uma contradição ou um requisito tão ambíguo que possa ser
    interpretado de duas maneiras diferentes — esses são problemas. Pequenas melhorias de redação,
    preferências estilísticas e "seções menos detalhadas que outras" não são.

    Aprove, a menos que haja lacunas graves que levariam a um plano falho.

    ## Formato de Saída

    ## Revisão da Spec

    **Status:** Aprovado | Problemas Encontrados

    **Problemas (se houver):**
    - [Seção X]: [problema específico] - [por que isso importa para o planejamento]

    **Recomendações (consultivas, não bloqueiam a aprovação):**
    - [sugestões de melhoria]
```

**O revisor retorna:** Status, Problemas (se houver), Recomendações
