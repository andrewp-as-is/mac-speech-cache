<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/mac-speech-cache.svg?maxAge=3600)](https://pypi.org/project/mac-speech-cache/)
[![](https://img.shields.io/npm/v/mac-speech-cache.svg?maxAge=3600)](https://www.npmjs.com/package/mac-speech-cache)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/mac-speech-cache/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/mac-speech-cache/actions)

### Installation
```bash
$ [sudo] pip install mac-speech-cache
```

```bash
$ [sudo] npm i -g mac-speech-cache
```

#### How it works
```
~/Library/Caches/speech-cache/<hash>.aiff
```

#### Examples
```bash
# say "$@"
$ afplay "$(speech-cache "$@")"
```

make cache for multiple files and voices:
```bash
$ find . -name "*.txt" | xargs -I{} speech-cache -f {} -v Milena
$ find . -name "*.txt" | xargs -I{} speech-cache -f {} -v Yuri
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>