head = '''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Stack</title>
  </head>
  <script language="javascript">
'''

foot = '''
  </script>
  <body>
    <canvas id="stack_process" width="171" height="221"></canvas>
  </body>
</html>

'''

def concat():
    js = open('../js/functions.js').read()
    arquivo = open('../interface/stack.html', 'w')
    arquivo.writelines(head + js + foot)
    arquivo.close()

concat()
