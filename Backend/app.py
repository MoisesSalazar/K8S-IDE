from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS
import platform

app = Flask(__name__)
CORS(app)

def get_machine_info():
    return {
        "hostname": platform.node(),
        "system": platform.system(),
        "release": platform.release()
    }

# Método 1: Bienvenida
@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "¡Bienvenido a mi aplicación Flask!"})

# Método 2: Detalles de la computadora
@app.route('/details', methods=['GET'])
def get_details():
    return jsonify(get_machine_info())


# Método 3: Evaluación de código Python
@app.route('/pyeval', methods=['POST'])
def py_eval():
    try:
        data = request.get_json()
        code = data.get("code", "")
        
        # Ejecutar el código en un proceso separado
        subp = subprocess.Popen(['python3'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = subp.communicate(code.encode('utf-8'))
        
        # Capturar la salida y los errores en variables
        output_str = out.decode('utf-8')
        error_str = err.decode('utf-8')
        print(output_str);
        # Crear un diccionario para almacenar el resultado y los errores
        result_dict = {
            "result": output_str,
            "error": error_str,
            "machine_info": get_machine_info()
        }
        return jsonify(result_dict)
    except Exception as e:
        return jsonify({"error": str(e)})

# Método 4: Evaluación de código C++
@app.route('/cpluseval', methods=['POST'])
def cpp_eval():
    try:
        data = request.get_json()
        code = data.get("code", "")
        
        # Crear un archivo temporal para el código C++
        with open("temp.cpp", "w") as cpp_file:
            cpp_file.write(code)
        
        # Compilar el código C++
        compile_command = ["g++", "temp.cpp", "-o", "temp.out"]
        compile_result = subprocess.run(compile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if compile_result.returncode == 0:
            # Ejecutar el programa C++ compilado
            run_command = ["./temp.out"]
            run_result = subprocess.run(run_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Devolver la salida del programa C++
            return jsonify({"result": run_result.stdout, "error": run_result.stderr, "machine_info": get_machine_info()})
        else:
            # Devolver errores de compilación
            return jsonify({"error": compile_result.stderr})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/rubyeval', methods=['POST'])
def ruby_eval():
    try:
        data = request.get_json()
        code = data.get("code", "")
        
        # Ejecutar el código en Ruby en un proceso separado
        subp = subprocess.Popen(['ruby'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = subp.communicate(code.encode('utf-8'))
        
        # Capturar la salida y los errores en variables
        output_str = out.decode('utf-8')
        error_str = err.decode('utf-8')
        
        # Crear un diccionario para almacenar el resultado y los errores
        result_dict = {
            "result": output_str,
            "error": error_str,
            "machine_info": get_machine_info()
        }
        return jsonify(result_dict)
    except Exception as e:
        return jsonify({"error": str(e)})
@app.route('/jseval', methods=['POST'])
def js_eval():
    try:
        data = request.get_json()
        code = data.get("code", "")
        result = subprocess.check_output(['node', '-e', code], text=True)
        
        # Obtener detalles de la máquina
        machine_info = get_machine_info()
        
        return jsonify({"result": result, "machine_info": machine_info})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": "Error de ejecución", "output": e.output, "machine_info": get_machine_info()})
    except Exception as e:
        return jsonify({"error": str(e), "machine_info": get_machine_info()})

@app.route('/phpeval', methods=['POST'])
def php_eval():
    try:
        data = request.get_json()
        code = data.get("code", "")
        
        # Guardar el código PHP en un archivo temporal
        with open("temp.php", "w") as php_file:
            php_file.write(code)
        
        # Ejecutar el código PHP
        php_command = ["php", "temp.php"]
        result = subprocess.check_output(php_command, text=True)
        
        # Obtener detalles de la máquina
        machine_info = get_machine_info()
        
        return jsonify({"result": result, "machine_info": machine_info})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": "Error de ejecución", "output": e.output, "machine_info": get_machine_info()})
    except Exception as e:
        return jsonify({"error": str(e), "machine_info": get_machine_info()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

