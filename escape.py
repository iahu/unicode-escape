# encoding=utf-8
import sublime, sublime_plugin, re, json

class EscapeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel();
		syntax = getSyntax();
		# if not isSupportSyntax( syntax ):
		# 	print( syntax + ' not support');
		# 	return;
		for sel in sels:
			t = self.view.substr(sel);
			escaped = bytes.decode(t.encode('unicode-escape'));
			escaped = convert_to_lang_style(escaped, syntax);
			escaped = re.sub(r'(?<!\\)\\n', r'\n', escaped);
			escaped = re.sub(r'(?<!\\)\\t', r'\t', escaped);
			escaped = re.sub(r'\\\\', r'\\', escaped);

			self.view.replace( edit, sel, escaped );


class UnescapeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel();
		syntax = getSyntax();
		# if not isSupportSyntax( syntax ):
		# 	print( syntax + ' not support');
		# 	return;
		for sel in sels:
			t = self.view.substr(sel);
			t = convert_to_json_style( t, syntax );
			t = re.sub(r'(\\u[\da-fA-F]{4}|\\x[\da-fA-F]{2}|\\u\{([\da-fA-F]{1,})\})', decode, t)
			t = re.sub(r'\\\\', r'\\', t);
			self.view.replace(edit, sel, t);

# def isSupportSyntax(syntax):
# 	p = re.compile(r'(less|scss|sass|css|stylus|postcss|js|jsx|ts|tsx|html|xml|haml|slim|jade|xml|python)');
# 	return not not re.match(p, syntax );

# ignore bad style strings.
def decode(g):
	if g:
		return _decode(g.group(0));
	return '';

def _decode(s):
	return bytes( s, 'utf-8' ).decode('unicode_escape');

def dec_to_hex(s):
	if s:
		return r'\u' + re.sub( '^0x', '', hex( int(s.group(1), 10) ));
	return '';

def decode_es6(g):
	if g:
		return _decode(r'\U'+ g.group(1).rjust(8, '0'));
	return '';


def getSyntax():
	view = sublime.active_window().active_view();
	pt = view.sel()[0].begin();
	scope = view.scope_name(pt) if hasattr(view,'scope_name') else view.syntax_name(pt);

	inString = re.search(r'\b(string|plain|comment)\b', scope);

	match_text = re.search(r'\btext\.([\w\-]+)\b', scope);
	match_source = re.search(r'\bsource\.([\w\-]+)\b', scope);
	match_css = re.search(r'\b(less|scss|sass|css|stylus|postcss)\b', scope);
	match_html = re.search(r'\b(html|xml|haml|slim|jade)\b', scope);

	syntax = 'text';
	if not inString and match_text:
		syntax = match_text.group(1);
	if inString and match_source:
		print("match_source", match_source.group(1));
		syntax = match_source.group(1);
	elif match_css:
		syntax = match_css.group(0);
	elif match_html:
		syntax = match_html.group(0);

	return syntax;


def convert_to_json_style(unicode_escape, syntax):
	if re.search(r'^(less|scss|sass|css|stylus|postcss)$', syntax):
		return re.sub(r'\\([\da-fA-F]{4})', r'\\u\1', unicode_escape);

	elif re.search(r'^(html|xml|haml|slim|jade)$', syntax):
		# hex style
		unicode_escape = re.sub(r'&#[xX]([\da-fA-F]{1,4});', r'\\u\1', unicode_escape);
		# dec style
		unicode_escape = re.sub(r'&#(\d{1,8});', dec_to_hex, unicode_escape);
		return unicode_escape;

	else:
		# support ES6
		p = r'\\u\{([\da-fA-F]{1,})\}';
		g = re.match(p, unicode_escape);
		if g:
			return re.sub(p, decode_es6, unicode_escape);
		else:
			return unicode_escape;

def convert_to_lang_style(unicode_escape, syntax):
	print(unicode_escape, syntax);
	if re.search(r'(less|scss|sass|css|stylus|postcss)', syntax):
		return re.sub(r'\\u([\da-fA-F]{4})', r'\\\1', unicode_escape);

	elif re.search(r'(html|xml|haml|slim|jade)', syntax):
		return re.sub(r'\\u([\da-fA-F]{1,4})', r'&#x\1;', unicode_escape);

	return re.sub(r'\\U([\da-fA-F]{8})', r'\\u{\1}', unicode_escape);
	# return unicode_escape;
