# escape - Sublime Text Plugin

一个类似于 JavaScript (un)escape 的 sublime 插件。
可以把中文等非 ASCII 码转义成unicode_escape 码，也可以反转义unicode_escape成中文字符。

JavaScript (un)escape like tool for sublime. escape non ascii strings to unicode_escape, or unescape unicode_escape code to non ascii strings.

#Installation
Package Control:

search`escape`

#Usage

Windows:
```json
[
    {"keys": ["ctrl+f11"], "command": "escape"},
    {"keys": ["ctrl+f12"], "command": "unescape"}
]
```

Linux/Mac os x:
```json
[
    {"keys": ["ctrl+escape"], "command": "escape"}
    {"keys": ["ctrl+shift+escape"], "command": "unescape"}
]
```
