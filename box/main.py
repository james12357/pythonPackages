import io
inp = '''
print("hello world")
'''
v = compile(inp, "", "exec")
a = io.BytesIO(v)
a.getvalue()


