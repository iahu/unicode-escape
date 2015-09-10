# escape - Sublime Text Plugin

一个类似于 JavaScript (un)escape 的 sublime 插件。
可以把中文等非 ASCII 码转义成unicode_escape 码，也可以反转义unicode_escape成中文字符。

JavaScript (un)escape like tool for sublime. escape non ascii strings to unicode_escape, or unescape unicode_escape code to non ascii strings.

#Installation
Package Control:

search`escape`

Custom install:

1. Download frome (here)[https://github.com/iahu/escape/archive/master.zip].
2. unzip and copy the package to sublime packages fold.
Windows and Linux can find at sublime text menu `Preferences`>`Browse Packages...`
Mac os x as `Sublime Text`>`Preferences`>`Browse Packages...`

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
