from flask import Flask, request, jsonify, redirect, send_file, url_for, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import os
from werkzeug.utils import secure_filename

#############################################################################################################################
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# from sklearn.naive_bayes import GaussianNB
# from sklearn.metrics import accuracy_score
# from sklearn.model_selection import train_test_split
#############################################################################################################################

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

########################################### Mostrar tabla 'paciente' en datatable ####################################################
@app.route('/tabla', methods=['GET'])
def tabla():
    try:
        if request.method == 'GET':
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM paciente')
            rv = cur.fetchall()
            cur.close()
            payload = []
            content = {}
            for result in rv:
                content = {'nombre': result[1], 'tipo_documento': result[4], 'identificacion': result[5], 'correo_institucional': result[2]}
                payload.append(content)
                content = {}
            return jsonify(payload)
        else:
            return jsonify({"error": "Método no válido para esta ruta"})
    except Exception as e:
        print(e)
        return jsonify({"información":e})


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
                if correo_institucional == "pablo" and contraseña == "pablo":
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

#################################################### Publicar eventos o consejos ######################################################

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

import os

# Configura la carpeta donde se guardarán los archivos subidos
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')  # Obtén la ruta completa al directorio "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)  # Crea el directorio si no existe
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#####subir historial en pdf##############
@app.route('/subir_historial', methods=['POST'])
def subir_historial():
    try:
        if 'pdf' not in request.files:
            return 'No se encontró el archivo'
        archivo = request.files['pdf']

        if archivo.filename == '':
            return 'No se seleccionó ningún archivo'
        if archivo.mimetype != 'application/pdf':
            return 'El archivo debe ser un PDF'

        filename = secure_filename(archivo.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        archivo.save(filepath)

        id_paciente = request.form['id_paciente']  
        cur = mysql.connection.cursor()
        cur.execute("UPDATE paciente SET historial_clinico = %s WHERE id_paciente = %s", (filepath, id_paciente))
        mysql.connection.commit()
        cur.close()

        return 'Historial clínico subido exitosamente'
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})

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
    


    
########################################################### Predecir paciente ####################################################

# @app.route('/prediccion', methods=['POST'])
# def prediccion():
#     try:
#             ### RECIBO JSON
#         ####################################################       
#         ruta_archivo = ('Dataset-Mental-Disorders.csv')
#         df = pd.read_csv(ruta_archivo)
#         df = df.drop(columns=['Patient Number'])
#         labelencoder = LabelEncoder()
#         for column in df.columns:
#             df[column] = labelencoder.fit_transform(df[column])
#         X = df.drop('Expert Diagnose', axis=1)
#         y = df['Expert Diagnose']
#         y = labelencoder.fit_transform(y)
#         X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
#         naive_bayes = GaussianNB()
#         naive_bayes.fit(X_train, y_train)
#         y_pred = naive_bayes.predict(X_test)
#         accuracy = accuracy_score(y_test, y_pred)
#         print("Precisión del modelo de Naive Bayes:", accuracy)

#         ###################################################


#         new_data = {
#             'Sadness': 2,
#             'Exhausted': 1,
#             'Euphoric': 0,
#             'Sleep dissorder': 1,  
#             'Mood Swing': 0,
#             'Suicidal thoughts': 0,
#             'Anorxia': 0,
#             'Authority Respect': 1,
#             'Try-Explanation': 1,
#             'Aggressive Response': 0,
#             'Ignore & Move-On': 0,
#             'Nervous Break-down': 0,
#             'Admit Mistakes': 1,
#             'Overthinking': 1,
#             'Sexual Activity': 1,
#             'Concentration': 1,
#             'Optimisim': 0  
#         }

#         new_data_df = pd.DataFrame(new_data, index=[0])

#         for column in new_data_df.columns:
#             new_data_df[column] = labelencoder.transform([new_data_df[column]])[0]

#         column_order = X_train.columns
#         new_data_df = new_data_df[column_order]
#         prediction = naive_bayes.predict(new_data_df)
#         predicted_disorder_label = labelencoder.inverse_transform(prediction)[0]

#         print("Trastorno mental predicho:", predicted_disorder_label)

#         ######
#     except Exception as e:
#         print(e)
#         return jsonify({"informacion":e})

if __name__=="__main__":
    app.run(port=3000,debug=True)