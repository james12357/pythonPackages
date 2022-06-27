import io
inp = '''
print("hello world")
'''
v = compile(inp, "", "eval")
a = io.BytesIO(v)
a.getvalue()


