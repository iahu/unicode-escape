## Unicode Escape - Sublime Text Plugin

non_ascii_string <--> Unicode_escape

__note__: Line Ending and Tab are ignored.


e.g.
```html
	&#x4e2d;&#x534e; <!-- <=> 中华 -->
    &#20013;&#33775; <!-- <=> 中華 -->
```

```css
	 font-family: '\5b8b\4f53'; // <=> font-family:'宋体'
```

```js
	var a = '\u6c49\u5b57'; // <=> a = '汉字';
	var b = '\u{0001d306}' // <=> b = '𝌆';
```

##Installation
- Package Control:

	search and install `Unicode Escape`


- Custom install:

	1. Download from [here](https://github.com/iahu/escape/archive/master.zip).
	2. unzip and copy the package to sublime packages fold.
	Windows and Linux can find at sublime text menu `Preferences`>`Browse Packages...`
	Mac os x as `Sublime Text`>`Preferences`>`Browse Packages...`

##Usage

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
    {"keys": ["ctrl+escape"], "command": "escape"},
    {"keys": ["ctrl+shift+escape"], "command": "unescape"}
]
```
