# Hylang support for VSCode
Syntax file *borrowed* from VSCode's Clojure built-in, but converted into YAML for readability<sup>[citation needed]</sup>.
Colors for tokens are as similar to Python as possible.

# Done
- using JSON instead of XML
- using YAML instead of JSON
- sensible colors & paren matching
- fixed single-quote pairing
- lists, sets and dictionaries
- function definitions
- fixed paren matching
- octals and hexes

# TODO
- **convert YAML on npm install**
- sieve through built-in and non-built-in symbols
- consistent hy/hylang naming around the project
- separate rules for classes, lambdas, macros and imports
- format & bracket string (https://docs.hylang.org/en/stable/language/syntax.html#string-literals)
- function variadic args & metadata
- some special symbols like #_, #* etc.
- for, lfor, gfor syntax help
- special highlight for regexes
- built-in exceptions highlight