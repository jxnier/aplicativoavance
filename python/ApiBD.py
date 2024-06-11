from flask import Flask, request, jsonify, redirect, send_file, url_for, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import mysql.connector
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


app = Flask(__name__)
CORS(app)
CORS( resources={r"/publicaciones": {"origins": "http://localhost"}})

app.config["MYSQL_HOST"]="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='proyecto'
mysql = MySQL(app)

####################################################### Registrar paciente #####################################################
@cross_origin()
@app.route('/registrar_paciente', methods=['POST'])
def registrar_paciente():
    try:
        if request.method == 'POST':
            nombre = request.json['nombre']
            correo = request.json['correo'] 
            contraseña = request.json['contraseña']   
            tipo_documento = request.json['tipo_documento'] 
            documento = request.json['documento']  
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO paciente (nombre, tipo_documento, identificacion, correo_institucional, contraseña) VALUES (%s, %s, %s, %s, %s)", (nombre, tipo_documento, documento, correo, contraseña))
            mysql.connection.commit()
            cur.close()
            return jsonify({"mensaje":"Redireccionando","link":"http://localhost/aplicativoavance/html/registrarse.html"})
        else:
            return jsonify({"error": "Método no válido para esta ruta"})
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})



####################################################### Iniciar sesión por rol #######################################################
# Iniciar sesión por rol
@app.route('/iniciar_sesion', methods=['GET', 'POST'])
def inicar_sesion():
    try:
        if request.method == 'POST':
            data = request.json
            correo_institucional = data['correo_institucional']
            contraseña = data['contraseña']
            rol = data['rol']
            if rol == "administrador":
                if correo_institucional == "admin" and contraseña == "admin":
                    return jsonify({"mensaje": "Redireccionando", "link": "http://localhost/aplicativoavance/html/Administrador/0Administrador.html"})
                else:
                    return jsonify({"mensaje": "Credenciales de administrador incorrectas"})
            elif rol == "paciente":
                cursor = mysql.connection.cursor()
                cursor.execute('SELECT nombre FROM paciente WHERE correo_institucional = %s and contraseña = %s', (correo_institucional, contraseña))
                siexiste = cursor.fetchone()
                cursor.close()
                if siexiste != None:
                    nombre_usuario = siexiste[0]  
                    return jsonify({"mensaje": "Redireccionando", "link": "http://localhost/aplicativoavance/html/Paciente/0Paciente.html", "nombre": nombre_usuario})
                else:
                    return jsonify({"mensaje": "Paciente: Correo institucional o contraseña incorrecta"})
            elif rol == "psicologo":
                cursor = mysql.connection.cursor()
                cursor.execute('SELECT nombre FROM psicologo WHERE correo_institucional = %s and contraseña = %s', (correo_institucional, contraseña))
                siexiste = cursor.fetchone()
                cursor.close()
                if siexiste != None:
                    nombre_usuario = siexiste[0]  
                    return jsonify({"mensaje": "Redireccionando", "link": "http://localhost/aplicativoavance/html/Psicologo/0Psicologo.html", "nombre": nombre_usuario})
                else:
                    return jsonify({"mensaje": "Psicólogo: Correo institucional o contraseña incorrecta"})
        else:
            return jsonify({"error": "Método no válido para esta ruta"})
    except Exception as e:
        print(e)
        return jsonify({"información": e})

####################################################### Registrar psicólogo ######################################################
@app.route('/registrar_psicologo', methods=['POST'])
def registrar_psicologo():
    try:
        if request.method == 'POST':
            nombre = request.json['nombre']
            correo_institucional = request.json['correo_institucional'] 
            contraseña = request.json['contraseña']   
            identificacion = request.json['identificacion']  
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO psicologo (nombre, correo_institucional, contraseña, identificacion) VALUES (%s, %s, %s, %s)", (nombre, correo_institucional, contraseña, identificacion))
            mysql.connection.commit()
            cur.close()
            return jsonify({"mensaje": "¡Psicologo(a) registrado exitosamente!"})
        else:
            return jsonify({"error": "Método no válido para esta ruta"})
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

#################################################### Registrar avance personal ######################################################

@app.route('/registrar_avance_personal', methods=['POST'])
def registrar_avance_personal():
    try:
        if request.method == 'POST':
            contenido = request.json['contenido']
            correo_paciente = request.json['correo_paciente']
            
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT correo_institucional FROM paciente WHERE correo_institucional = %s', (correo_paciente,))
            correo_institucional = cursor.fetchone()
            cursor.close()
            if correo_institucional:
                correo_institucional = correo_institucional[0]
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO avance_personal (correo_institucional, contenido) VALUES (%s, %s)", (correo_institucional, contenido))
                mysql.connection.commit()
                cur.close()
                return jsonify({"mensaje": "Avance personal registrado exitosamente"})
            else:
                return jsonify({"error": "No se encontró ningún paciente con el correo proporcionado"})
        else:
            return jsonify({"error": "Método no válido para esta ruta"})
    except Exception as e:
        print(e)
        return jsonify({"error": "Ocurrió un error al procesar la solicitud"})

#################################################### Mostrar avance personal ######################################################

@app.route('/obtener_avances', methods=['GET'])
def obtener_avances():
    try:
        correo_usuario = request.args.get('correo') 
        cur = mysql.connection.cursor()
        cur.execute("SELECT contenido, fecha_avance, id_avance FROM avance_personal WHERE correo_institucional = %s", (correo_usuario,))
        avances = cur.fetchall()
        cur.close()
        # Convertir la lista de tuplas a una lista de diccionarios
        avances_list = []
        for avance in avances:
            avance_dict = {
                'contenido': avance[0],
                'fecha_avance': avance[1],
                'id_avance': avance[2]
            }
            avances_list.append(avance_dict)

        return jsonify(avances_list)
    except Exception as e:
        return jsonify({'error': str(e)})

#################################################### Eliminar avance personal ######################################################

@app.route('/eliminar_avance', methods=['DELETE'])
def eliminar_avance():
    try:
        if request.method == 'DELETE':
            id_avance = request.args.get('id')
            cursor = mysql.connection.cursor()
            cursor.execute("DELETE FROM avance_personal WHERE id_avance = %s", (id_avance,))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"mensaje": "Avance eliminado exitosamente"})
        else:
            return jsonify({"error": "Método no válido para esta ruta"})
    except Exception as e:
        print(e)
        return jsonify({"error": "Ocurrió un error al procesar la solicitud"})

#################################################### Publicar eventos, consejos y anuncios ######################################################

@app.route('/Publicar', methods=['POST'])
def Publicar():
    try:
        if request.method == 'POST':
            correo_institucional = request.json['correo_institucional']
            titulo = request.json['titulo']
            contenido = request.json['contenido']
            tipo = request.json['tipo']
            cur = mysql.connection.cursor()
            cur.execute("SELECT id_psicologo,nombre FROM psicologo WHERE correo_institucional = %s", (correo_institucional,))
            id_psicologo = cur.fetchone()[0]
            cur.execute("INSERT INTO publicacion (id_psicologo, titulo, contenido, tipo) VALUES (%s, %s, %s, %s)", (id_psicologo, titulo, contenido, tipo))
            mysql.connection.commit()
            cur.close()
            return jsonify({"mensaje": "Publicación creada correctamente"})
        else:
            return jsonify({"error": "Método no válido para esta ruta"})
    except Exception as e:
        print(e)
        return jsonify({"error": "Ocurrió un error al procesar la solicitud"})

#################################################### Mostrar perfil por rol ######################################################

@app.route('/obtener_perfil', methods=['GET'])
def obtener_perfil():
    try:
        if request.method == 'GET':
            correo_usuario = request.args.get('correo')  
            cur = mysql.connection.cursor()
            cur.execute("SELECT nombre, tipo_documento, identificacion, correo_institucional FROM paciente WHERE correo_institucional = %s", (correo_usuario,))
            perfil_usuario = cur.fetchone()
            cur.close()
            if perfil_usuario:
                perfil_dict = {
                    'nombre': perfil_usuario[0],
                    'tipo_documento': perfil_usuario[1],
                    'identificacion': perfil_usuario[2],
                    'correo_institucional': perfil_usuario[3]
                }
                return jsonify(perfil_dict)
            else:
                return jsonify({'error': 'Usuario no encontrado'})
        else:
            return jsonify({'error': 'Método no válido para esta ruta'})
    except Exception as e:
        return jsonify({'error': str(e)})

##################################################### Mostrar Publicaciones ##########################################################

@app.route('/publicaciones', methods=['GET'])
def obtener_publicaciones():
    try:
        if request.method == 'GET':
            cur = mysql.connection.cursor()
            cur.execute('SELECT p.nombre, pu.titulo, pu.contenido, pu.tipo, pu.fecha_publicacion FROM publicacion pu INNER JOIN psicologo p ON pu.id_psicologo = p.id_psicologo')
            publicaciones = cur.fetchall()
            cur.close()
            
            publicaciones_list = []
            for publicacion in publicaciones:
                publicacion_dict = {
                    "nombre_psicologo": publicacion[0],
                    'titulo': publicacion[1],
                    'contenido': publicacion[2],
                    'tipo': publicacion[3],
                    'fecha': publicacion[4]
                }
                publicaciones_list.append(publicacion_dict)
            return jsonify(publicaciones_list)
        else:
            return jsonify({"error": "Método no válido para esta ruta"})
    except Exception as e:
        print(e)
        return jsonify({"información": e})


##################################################### EVENTOS  ################################################################

@app.route('/obtener_eventos', methods=['GET'])
def obtener_eventos():
    try:
        with mysql.connection.cursor() as cursor:
            sql = "SELECT p.nombre, pu.titulo, pu.contenido, pu.fecha_publicacion FROM publicacion pu INNER JOIN psicologo p ON pu.id_psicologo = p.id_psicologo and pu.tipo = 'evento' "
            cursor.execute(sql)
            eventos = cursor.fetchall()
            
            eventos_list = []
            for eventos in eventos:
                eventos_dict = {
                    'nombre': eventos[0],
                    "titulo": eventos[1],
                    'contenido': eventos[2],
                    'fecha': eventos[3]
                }
                eventos_list.append(eventos_dict)
            return jsonify(eventos_list)
    except Exception as e:
        print("Error al obtener los eventos:", e)
        return jsonify([])  

##################################################### CONSEJOS  ################################################################

@app.route('/obtener_consejos', methods=['GET'])
def obtener_consejos():
    try:
        with mysql.connection.cursor() as cursor:
            sql = "SELECT p.nombre, pu.titulo, pu.contenido, pu.fecha_publicacion FROM publicacion pu INNER JOIN psicologo p ON pu.id_psicologo = p.id_psicologo and pu.tipo = 'consejo' "
            cursor.execute(sql)
            consejos = cursor.fetchall()
            
            consejos_list = []
            for consejos in consejos:
                consejos_dict = {
                    'nombre': consejos[0],
                    "titulo": consejos[1],
                    'contenido': consejos[2],
                    'fecha': consejos[3]
                }
                consejos_list.append(consejos_dict)
            return jsonify(consejos_list)
    except Exception as e:
        print("Error al obtener los consejos:", e)
        return jsonify([])  

##################################################### ANUNCIO  ################################################################

@app.route('/obtener_anuncios', methods=['GET'])
def obtener_anuncios():
    try:
        with mysql.connection.cursor() as cursor:
            sql = "SELECT p.nombre, pu.titulo, pu.contenido, pu.fecha_publicacion FROM publicacion pu INNER JOIN psicologo p ON pu.id_psicologo = p.id_psicologo and pu.tipo = 'anuncio'"
            cursor.execute(sql)
            anuncios = cursor.fetchall()
            
            anuncios_list = []
            for anuncios in anuncios:
                anuncios_dict = {
                    'nombre': anuncios[0],
                    "titulo": anuncios[1],
                    'contenido': anuncios[2],
                    'fecha': anuncios[3]
                }
                anuncios_list.append(anuncios_dict)
            return jsonify(anuncios_list)
    except Exception as e:
        print("Error al obtener los anuncios:", e)
        return jsonify([])  

########################################################### GROUP BY #####################################################

@app.route('/grafica_tipo_documento', methods=['GET'])
def grafica_tipo_documento():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT tipo_documento, COUNT(*) AS count FROM paciente GROUP BY tipo_documento")
        data = cursor.fetchall()
        cursor.close()
        labels = []
        values = []
        for row in data:
            labels.append(row[0])
            values.append(row[1])
        return jsonify({
            'labels': labels,
            'values': values
        })
    except Exception as e:
        return jsonify({'error': str(e)})
    

@app.route('/tareas_completadas_por_psicologo', methods=['GET'])
def tareas_completadas_por_psicologo():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT ps.nombre AS psicologo, COUNT(t.id_tarea) AS cantidad_tareas_completadas FROM psicologo ps INNER JOIN tarea t ON ps.id_psicologo = t.id_psicologo WHERE t.completada = 1 GROUP BY ps.nombre")
        data = cursor.fetchall()
        cursor.close()
        nombres_psicologos = []
        cantidades = []
        for row in data:
            nombres_psicologos.append(row[0])
            cantidades.append(row[1])
        return jsonify({'nombres_psicologos': nombres_psicologos, 'cantidades': cantidades})
    except Exception as e:
        return jsonify({'error': str(e)})



@app.route('/grafica_predicciones_ia', methods=['GET'])
def grafica_predicciones_ia():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT prediccion_ia, COUNT(*) AS cantidad FROM paciente WHERE prediccion_ia IS NOT NULL GROUP BY prediccion_ia")
        data = cursor.fetchall()
        cursor.close()
        labels = []
        valores = []
        for row in data:
            labels.append(row[0])
            valores.append(row[1])
        return jsonify({'labels': labels, 'valores': valores})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/grafica_tipos_publicaciones', methods=['GET'])
def grafica_tipos_publicaciones():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT tipo, COUNT(*) AS cantidad FROM publicacion GROUP BY tipo")
        data = cursor.fetchall()
        cursor.close()
        labels = []
        valores = []
        for row in data:
            labels.append(row[0])
            valores.append(row[1])
        return jsonify({'labels': labels, 'valores': valores})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/grafica_tareas_psicologos', methods=['GET'])
def grafica_tareas_psicologos():
    try:
        cursor = mysql.connection.cursor()
        # Consulta SQL para obtener datos de tareas completadas
        cursor.execute("SELECT completada, COUNT(*) AS cantidad FROM tarea GROUP BY completada")
        data = cursor.fetchall()

        cursor.close()
        
        # Procesamiento de los datos para la respuesta JSON
        labels = []
        valores = []
        for row in data:
            labels.append(str(row[0]))
            valores.append(row[1])

        return jsonify({'labels': labels, 'valores': valores})

    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/pacientes_por_tipo_documento_y_prediccion_ia', methods=['GET'])
def pacientes_por_tipo_documento_y_prediccion_ia():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT tipo_documento, prediccion_ia, COUNT(*) AS cantidad_pacientes FROM paciente WHERE prediccion_ia IS NOT NULL GROUP BY tipo_documento, prediccion_ia")
        data = cursor.fetchall()
        cursor.close()
        resultados = []
        for row in data:
            resultados.append({'tipo_documento': row[0], 'prediccion_ia': row[1], 'cantidad_pacientes': row[2]})
        return jsonify({'resultados': resultados})
    except Exception as e:
        return jsonify({'error': str(e)})


########################################################## OBTENER PACIENTES ######################################

@app.route('/allpaciente', methods=['GET'])
def allpaciente():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id_paciente, nombre, identificacion FROM paciente")
    pacientes = cursor.fetchall()
    pacientes_dict = [{"id": paciente[0], "nombre": paciente[1], "identificacion": paciente[2]} for paciente in pacientes]
    return jsonify(pacientes_dict)

########################################################## ASIGNAR TAREA ######################################
@app.route('/registrar_tarea', methods=['POST'])
def registrar_tarea():
    try:
        if request.method == 'POST':
            correo_psico = request.json.get('psicologo_id')
            cur = mysql.connection.cursor()
            cur.execute("SELECT id_psicologo FROM psicologo WHERE correo_institucional = %s", [correo_psico])
            result = cur.fetchone()
            
            if result is not None:
                psicologo_id = result[0]
                
                tarea = request.json
                paciente_id = tarea.get('paciente_id')
                titulo = tarea.get('titulo')
                descripcion = tarea.get('descripcion')
                
                cur.execute("INSERT INTO tarea (id_psicologo, id_paciente, titulo, descripcion) VALUES (%s, %s, %s, %s)", 
                            (psicologo_id, paciente_id, titulo, descripcion))
                mysql.connection.commit()
                cur.close()
                return jsonify({"mensaje": "Tarea registrada exitosamente"})
            else:
                return jsonify({"error": "No se encontró ningún psicólogo con el correo electrónico proporcionado"})
        else:
            return jsonify({"error": "Método no válido para esta ruta"})
    except Exception as e:
        print(e)
        return jsonify({"error": "Ocurrió un error al procesar la solicitud"})

######################################## Ruta para obtener todas las tareas #############################################

@app.route('/mistareas', methods=['GET'])
def mistareas():
    try:
        if request.method == 'GET':
            # Obtener el correo electrónico del usuario desde la solicitud GET
            correo_usuario = request.args.get('usuario')
            # Consultar el ID del usuario basado en su correo electrónico
            cur = mysql.connection.cursor()
            cur.execute("SELECT id_paciente FROM paciente WHERE correo_institucional = %s", (correo_usuario,))
            result = cur.fetchone()
            cur.close()
            # Verificar si se encontró el usuario
            if result is not None:
                usuario_id = result[0]
                # Consultar las tareas asignadas al usuario y el nombre del psicólogo asignado
                cur = mysql.connection.cursor()
                cur.execute("SELECT t.titulo, t.descripcion, p.nombre, t.id_tarea FROM tarea t INNER JOIN psicologo p ON t.id_psicologo = p.id_psicologo WHERE t.id_paciente = %s", (usuario_id,))
                tareas_asignadas = cur.fetchall()
                cur.close()
                # Formatear las tareas como un JSON y devolverlas
                tareas_json = []
                for tarea in tareas_asignadas:
                    tarea_dict = {
                        'titulo': tarea[0],
                        'descripcion': tarea[1],
                        'nombre_psicologo': tarea[2],
                        'id': tarea[3]
                    }
                    tareas_json.append(tarea_dict)
                return jsonify(tareas_json)
            else:
                return jsonify({"error": "No se encontró ningún usuario con el correo electrónico proporcionado"})
        else:
            return jsonify({"error": "Método no válido para esta ruta"})
    except Exception as e:
        print(e)
        return jsonify({"información": str(e)})

############################## MARCAR TAREAS COMO COMPLETADAS ##############################

@app.route('/marcar_como_completada', methods=['POST'])
def marcar_como_completada():
    if request.method == 'POST':
        tarea_id = request.json['tarea_id']  # Suponiendo que obtienes el ID de la tarea del formulario
        completada = True 
        try:
            cur = mysql.connection.cursor()
            cur.execute('UPDATE tarea SET completada = %s WHERE id_tarea = %s', (int(completada), tarea_id))
            mysql.connection.commit()
            cur.close()
            return jsonify({"mensaje": "Tarea marcada como completada exitosamente"})
        except Exception as e:
            print(e)
            return jsonify({"error": "Error al marcar la tarea como completada"})
    else:
        return jsonify({"error": "Método no válido para esta ruta"})

############################## MOSTRAR GRADO DE SALUD Y PDF (HISTORIAL CLINICO)##############################

@app.route('/psico', methods=['GET'])
def psico():
    try:
        if request.method == 'GET':
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM paciente')
            rv = cur.fetchall()
            cur.close()
            payload = []
            content = {}
            for result in rv:
                content = {'nombre': result[1], 'tipo_documento': result[4], 'identificacion': result[5], 'correo_institucional': result[2], 'grado_salud': result[7]}
                payload.append(content)
                content = {}
            return jsonify(payload)
        else:
            return jsonify({"error": "Método no válido para esta ruta"})
    except Exception as e:
        print(e)
        return jsonify({"información":e})

########################################### MOSTRAR CITAS DISPONIBLES POR FECHA ##################################################

@app.route('/buscar-citas', methods=['GET'])
def buscar_citas():
    try:
        if request.method == 'GET':
            fecha = request.args.get('fecha')  # Acceder al parámetro de la URL
            cursor = mysql.cursor()
            cursor.execute('''
                SELECT p.nombre, c.fecha, c.hora, c.sede
                FROM cita c
                INNER JOIN psicologo p ON c.id_psicologo = p.id_psicologo
                WHERE c.fecha = %s
            ''', (fecha,))
            citas = cursor.fetchall()
            cursor.close()
            citas_dict = []
            for cita in citas:
                cita_dict = {
                    'nombre_psicologo': cita[0],
                    'fecha': cita[1],
                    'hora': cita[2],
                    'sede': cita[3]
                }
                citas_dict.append(cita_dict)
            print("si se envia")
            return jsonify(citas_dict)
        else:
            return jsonify({"error": "Método no válido para esta ruta"})
    except Exception as e:
        # Manejo del error
        print("no se envia")
        return jsonify({'error': str(e)})

########################################################### Predecir paciente ####################################################



# Cargar y preparar los datos
ruta_archivo = "C:/xampp/htdocs/aplicativoavance/python/Dataset-Mental-Disorders.csv"
df = pd.read_csv(ruta_archivo)
df = df.drop(columns=['Patient Number'])

labelencoder = LabelEncoder()
for column in df.columns:
    df[column] = labelencoder.fit_transform(df[column])

X = df.drop('Expert Diagnose', axis=1)
y = df['Expert Diagnose']
y = labelencoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

# Entrenar el modelo de Naive Bayes
naive_bayes = GaussianNB()
naive_bayes.fit(X_train, y_train)


@app.route('/prediccion', methods=['POST'])
def prediccion():

    print("Nombres de características utilizadas durante el entrenamiento:")
    print(X_train.columns)
    data = request.get_json()

    # Crear un dataframe con los datos del formulario
    new_data_df = pd.DataFrame(data, index=[0])
    column_order = X_train.columns
    new_data_df = new_data_df[column_order]

    # Hacer la predicción
    prediction = naive_bayes.predict(new_data_df)
    predicted_disorder_label = labelencoder.inverse_transform(prediction)[0]

    # Mapeo de números a etiquetas de trastornos mentales
    diagnose_mapping = {
        0: 'Bipolar Type-1',
        1: 'Bipolar Type-2',
        2: 'Depresion',
        3: 'Normal'
    }

    return jsonify({'predicted_disorder': diagnose_mapping[predicted_disorder_label]})

@app.route('/actualizar_prediccion', methods=['POST'])
def actualizar_prediccion():
    data = request.json

    # Extraer el correo del paciente y la predicción de los datos enviados
    correo_paciente = data.get('correo_paciente')
    prediccion_ia = data.get('prediccion_ia')

    # Actualizar la predicción en la base de datos
    update_query = "UPDATE paciente SET prediccion_ia = %s WHERE correo_institucional = %s"
    cursor = mysql.connection.cursor()
    cursor.execute(update_query, (prediccion_ia, correo_paciente))
    mysql.connection.commit()  
    return jsonify({'mensaje': 'Predicción actualizada correctamente'}), 200


if __name__=="__main__":
    app.run(port=3000,debug=True)