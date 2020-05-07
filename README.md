# Hylang support for VSCode
Based on `sjhuangx/vscode-scheme` and `xuqinghan/vscode-hy`, but is much more than just a REGEXP replace of `scheme -> hy`.
Also a bit modernized and fixed where possible (WIP).

# Done
- using .json instead of .xml
- fixed single-quote pairing
- json from more readable [citation needed] yaml
- lists, sets and dictionaries
- remove non-built-in symbols
- functions
- illegal parenthesis
- octals and hexes

# TODO
- **build process for npm install**
- separate rules for classes, lambdas, macros and imports
- format & bracket string (https://docs.hylang.org/en/stable/language/syntax.html#string-literals)
- function definition variadic args & metadata
- some special symbols like #_, #* etc.
- for, lfor, gfor syntax help
- special highlight for regexes
