# Quizlet export instructions

TLDR:
 * term/def: `\n+\n`
 * rows: `\n---\n`

## Suggested export plain text separators

Quizlet has an amazing simple plain-text export / import ability. It's amazing because it's so simple, and because it allows the user to dictate the separators, as should be (unlike Apple type companies who force one simple option). What does majorly stink however is that they do not export or import audio and media! Big time stinks. However, if a lot of work was put into the text itself, as is the case for me, this much is still invaluable, including that it allows critical backup when so much hard work was done to make these.

 * Between rows: `\n---\n`
 * Between term and definition: `\n+\n`

Example export output:

```txt
לְאַ֑ט / אַט
+
Gently
subst. gentleness, used only adverbially
with לְ of norm or state
---
לָבֶטַח
+
Securely
---
```

### Regex to alter separators

In the exported plain-text docs, you can use any regex find/replace editor (like in VSCode) to instantly change these separators to something else. Note the importance however of picking separators that never occur in the content itself! (In other words, if you choose a simple comma `,` as a separator, if a comma ever occurs in one of your terms or definitions, this regex will probably not be sufficient)

Replace ROW separator:

Example: just have double lines instead of also 3 dashes:

* FIND: `\n\---\n`
* REPLACE: `\n\n`

Replace TERM / DEFINITION separator:

Example: keep definition / term on same line, separated by tabs with 3 pipes (|):

* FIND: `\n\+\n`
* REPLACE: `\t|||\t`

*Note: obviously in my case, with very frequent terms and definitions, I would not want to do this*



