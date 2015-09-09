# encoding=utf-8
import sublime, sublime_plugin, json

class EscapeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel();
		for sel in sels:
			t = self.view.substr(sel);
			self.view.replace(edit, sel, json.dumps(t).strip('"'));

class UnescapeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel();
		for sel in sels:
			t = self.view.substr(sel);
			self.view.replace(edit, sel, json.loads( '["'+t+'"]' )[0] );
