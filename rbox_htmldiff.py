#!/usr/bin/python
"""HTML Diff: http://www.aaronsw.com/2002/diff
Rough code, badly documented. Send me comments and patches."""

__author__ = 'Aaron Swartz <me@aaronsw.com>'
__copyright__ = '(C) 2003 Aaron Swartz. GNU GPL 2 or 3.'
__version__ = '0.22'

import difflib, string

__all__ = ["isTag", "textDiff", "html2list"]


def isTag(x): return x[0] == "<" and x[-1] == ">"

def textDiff(a, b):
	"""Takes in strings a and b and returns a human-readable HTML diff."""

	out = []
	a, b = html2list(a), html2list(b)
	try: # autojunk can cause malformed HTML, but also speeds up processing.
		s = difflib.SequenceMatcher(None, a, b, autojunk=False)
	except TypeError:
		s = difflib.SequenceMatcher(None, a, b)
	for e in s.get_opcodes():
		if e[0] == "replace":
			# @@ need to do something more complicated here
			# call textDiff but not for html, but for some html... ugh
			# gonna cop-out for now
			out.append('<del style="color:#999;">'+''.join(a[e[1]:e[2]]) + '</del><ins style="background:#ffc;text-decoration:none;">'+''.join(b[e[3]:e[4]])+"</ins>")
		elif e[0] == "delete":
			out.append('<del style="color:#999;">'+ ''.join(a[e[1]:e[2]]) + "</del>")
		elif e[0] == "insert":
			out.append('<ins style="background:#ffc;text-decoration:none;">'+''.join(b[e[3]:e[4]]) + "</ins>")
		elif e[0] == "equal":
			out.append(''.join(b[e[3]:e[4]]))
		else:
			raise "Um, something's broken. I didn't expect a '" + `e[0]` + "'."
	return ''.join(out)

def html2list(x, b=0):
	mode = 'char'
	cur = ''
	out = []
	for c in x:
		if mode == 'tag':
			if c == '>': 
				if b: cur += ']'
				else: cur += c
				out.append(cur); cur = ''; mode = 'char'
			else: cur += c
		elif mode == 'char':
			if c == '<': 
				out.append(cur)
				if b: cur = '['
				else: cur = c
				mode = 'tag'
			elif c in string.whitespace: out.append(cur+c); cur = ''
			else: cur += c
	out.append(cur)
	return filter(lambda x: x is not '', out)
