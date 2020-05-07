# Hylang support for VSCode
Started with `xuqinghan/vscode-hy`, but as it is just a REGEXP replace of `s/scheme/hy/`, it was impossible to fix.
Current version is *borrowed* from [Clojure syntax](https://github.com/microsoft/vscode/blob/master/extensions/clojure/syntaxes/clojure.tmLanguage.json), but converted into YAML for readability <sup>[citation needed][1]</sup>.

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
