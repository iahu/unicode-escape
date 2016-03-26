# encoding=utf-8
import sublime, sublime_plugin, re

class EscapeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel();
		for sel in sels:
			t = self.view.substr(sel);
			escaped = bytes.decode(t.encode('unicode-escape'));

			self.view.replace(edit, sel, escaped.replace('\\n', '\n').replace('\\t', '\t') );

class UnescapeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel();
		for sel in sels:
			t = self.view.substr(sel).lower();

			self.view.replace(edit, sel, bytes( t, 'utf-8' ).decode('unicode_escape') );
