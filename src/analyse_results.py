import qsharp

qsharp.init(project_root = '../Grover')

result = qsharp.eval("Grover.Main()")

print(result)