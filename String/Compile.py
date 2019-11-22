"""
compile(source,filename,mode, flags=0,dont_inherit=False,optimize=-1)
AST = Abstract Syntax Trees

"""

codeInString = 'a = 5\nb = 6\nsum = a + b\nprint("sum = ",sum)'
codeObject = compile(codeInString,'sumstring','exec')
exec(codeObject)
