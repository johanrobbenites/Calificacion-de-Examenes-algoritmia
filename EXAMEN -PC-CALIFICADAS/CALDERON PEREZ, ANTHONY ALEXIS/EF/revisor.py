import subprocess

def run_cpplint(file_path):
    # Ejecuta cpplint para revisar el archivo especificado
    cpplint_cmd = ['cpplint', '--quiet', file_path]
    cpplint_proc = subprocess.Popen(cpplint_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cpplint_output = cpplint_proc.communicate()[0].decode('utf-8')

    # Analiza la salida de cpplint para obtener el número de problemas y los errores
    num_problems = 0
    errores = []
    for line in cpplint_output.split('\n'):
        if line.startswith(file_path):
            num_problems += 1
            errores.append(line)

    # Devuelve un puntaje en una escala del 0 al 20 y la lista de errores
    max_score = 20
    score = max_score - min(num_problems, max_score)
    return score, errores

file_path = 'CALDERON-ANTHONY-P1.cpp'
score, errores = run_cpplint(file_path)
print('El puntaje de estilo del archivo {} es: {}'.format(file_path, score))
print('Los errores encontrados en el archivo {} son:'.format(file_path))
for error in errores:
    print(error)