# encoding=utf-8
import sublime, sublime_plugin, re

class EscapeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel();
		syntax = getSyntax();
		if not isSupportSyntax( syntax ):
			return;
		for sel in sels:
			t = self.view.substr(sel);
			escaped = bytes.decode(t.encode('unicode-escape'));
			escaped = convert_to_lang_style(escaped, syntax);
			escaped = escaped.replace(r'\n', '\n').replace(r'\t', '\t');

			self.view.replace( edit, sel, escaped );

class UnescapeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel();
		syntax = getSyntax();
		if not isSupportSyntax( syntax ):
			return;
		for sel in sels:
			t = self.view.substr(sel);
			t = convert_to_json_style( t, syntax );
			self.view.replace(edit, sel, re.sub(r'(\\u[\da-f]{4})', decode, t));

def isSupportSyntax(syntax):
	return not not re.match('''less|scss|sass|css|stylus|postcss|
		js|jsx|
		html|xml|haml|slim|jade|xml|
		python''', syntax );

# ignore bad style strings.
def decode(s):
	if s:
		return bytes( s.group(0), 'utf-8' ).decode('unicode_escape');
	return '';

def getSyntax():
	view = sublime.active_window().active_view();
	pt = view.sel()[0].begin();
	scope = view.scope_name(pt) if hasattr(view,'scope_name') else view.syntax_name(pt);

	inString = re.search(r'\b(string|comment)\b', scope);

	match_text = re.search(r'\btext\.([\w\-]+)\b', scope);
	match_source = re.search(r'\bsource\.([\w\-]+)\b', scope);
	match_css = re.search(r'\b(less|scss|sass|css|stylus|postcss)\b', scope);
	match_html = re.search(r'\b(html|xml|haml|slim|jade)\b', scope);

	syntax = 'html';
	if not inString and match_text:
		syntax = match_text.group(1);
	if inString and match_source:
		syntax = match_source.group(1);
	elif match_css:
		syntax = match_css.group(0);
	elif match_html:
		syntax = match_html.group(0);

	return syntax;

def convert_to_json_style(unicode_escape, syntax):
	if re.search(r'^(js|jsx|python)$', syntax):
		return unicode_escape;

	elif re.search(r'^(less|scss|sass|css|stylus|postcss)$', syntax):
		return re.sub(r'\\([\da-fA-F]{4})', r'\\u\1', unicode_escape);

	elif re.search(r'^(html|xml|haml|slim|jade|xml)$', syntax):
		# hex style
		unicode_escape = re.sub(r'&#x([\da-f]{1,4});', r'\\u\1', unicode_escape);
		# dec style
		unicode_escape = re.sub(r'&#(\d{1,8});', dec_to_hex, unicode_escape);
		return unicode_escape;

	return unicode_escape;

def convert_to_lang_style(unicode_escape, syntax):
	if re.search(r'(js|jsx)', syntax):
		return unicode_escape;

	elif re.search(r'(less|scss|sass|css|stylus|postcss)', syntax):
		return re.sub(r'\\u([\da-fA-F]{4})', r'\\\1', unicode_escape);

	elif re.search(r'(html|xml|haml|slim|jade|xml)', syntax):
		return re.sub(r'\\u([\da-f]{1,4})', r'&#x\1;', unicode_escape);

	return unicode_escape;


def dec_to_hex(s):
	if s:
		return r'\u' + re.sub( '^0x', '', hex( int(s.group(1), 10) ));
	return '';