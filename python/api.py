from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app) 

app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyecto'
mysql = MySQL(app)

app.secret_key = "mysecretkey"

#datable
@cross_origin()
@app.route('/tabla', methods=['GET'])
def tabla():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM paciente')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'nombre': result[1], 'tipo_documento': result[2], 'identificacion': result[3], 'correo': result[4]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

#tabla paciente
@app.route('/add_paciente', methods=['POST'])
def add_paciente():
    try:
        if request.method == 'POST':
            nombre = request.json['nombre']
            correo = request.json['correo'] 
            contraseña = request.json['contraseña']   
            tipo_documento = request.json['tipo_documento'] 
            documento = request.json['documento']  
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO paciente (nombre, tipo_documento, identificacion, correo, contraseña) VALUES (%s, %s, %s, %s, %s)", (nombre, tipo_documento, documento, correo, contraseña))
            mysql.connection.commit()
            cur.close()
            return jsonify({"informacion": "Registro exitoso"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": "Error en el servidor"}), 500 # Devuelve un mensaje de error simple y un código de estado HTTP 500

#tabla paciente    
@cross_origin()
@app.route('/getAllById/<int:id>', methods=['GET'])
def getAllById(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM paciente WHERE id_paciente = %s", (id,))
        data = cur.fetchall()
        cur.close()
        return jsonify(data)
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al obtener datos del paciente"})

#getall tabla paciente    
@cross_origin()
@app.route('/getAll', methods=['GET'])
def getAll():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM paciente")
        data = cur.fetchall()
        cur.close()
        return jsonify(data)
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al obtener datos de los pacientes"})

#delete tabla paciente    
@cross_origin()
@app.route('/delete/<id>', methods = ['DELETE'])
def delete_contact(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM paciente WHERE id_paciente = %s', (id,))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro eliminado"}) 
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})    

#put tabla paciente 
@cross_origin()
@app.route('/changePassword/<id>', methods=['PUT'])
def change_password(id):
    try:
        new_password = request.json.get('new_password')
        
        if not new_password:
            return jsonify({"error": "Se requiere una nueva contraseña"})
        cur = mysql.connection.cursor()
        cur.execute("UPDATE paciente SET contraseña = %s WHERE id_paciente = %s", (new_password, id))
        mysql.connection.commit()
        cur.close()

        return jsonify({"message": "Contraseña cambiada exitosamente"})
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al cambiar la contraseña"})

#insertar_avance
@cross_origin()    
@app.route('/insert_avance_personal', methods=['POST'])
def insert_avance_personal():
    try:
        if request.method == 'POST':
            data = request.json
            id_paciente = data['id_paciente']
            fecha_avance = data['fecha_avance']
            contenido = data['contenido']
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT identificacion FROM paciente WHERE identificacion = %s", (id_paciente,))
            usuario_existente = cursor.fetchone()
            
            if not usuario_existente:
                return jsonify({"error": f"El usuario con ID {id_paciente} no existe"})
            
            cursor.execute("INSERT INTO avance_personal (id_paciente, fecha_avance, contenido) VALUES (%s, %s, %s)", (id_paciente,fecha_avance,contenido))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": "Registro exitoso en avance_personal"})
    except Exception as e:
        return jsonify({"error": str(e)})

#buscar avance
@cross_origin()
@app.route('/buscar_avances_personales', methods=['GET'])
def buscar_avances_personales():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM avance_personal")
        avances = cursor.fetchall()
        cursor.close()
        if not avances:
            return jsonify({"message": "No se encontraron avances personales"})
        return jsonify({"avances_personales": avances})
    except Exception as e:
        return jsonify({"error": str(e)})

#buscar por parametro avance
@cross_origin()
@app.route('/buscar_avances/<id_paciente>', methods=['GET'])
def buscar_avances(id_paciente):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM avance_personal WHERE id_paciente = %s", (id_paciente,))
        avances = cursor.fetchall()
        cursor.close()
        
        if not avances:
            return jsonify({"message": f"No se encontraron avances personales para el paciente con identificación {id_paciente}"})
        
        return jsonify({"avances_personales": avances})
    except Exception as e:
        return jsonify({"error": str(e)})

#update avances
@cross_origin()
@app.route('/actualizar_avance_personal/<id_paciente>', methods=['PUT'])
def actualizar_avance_personal(id_paciente):
    try:
        data = request.json
        nuevo_contenido = data['contenido']
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE avance_personal SET contenido = %s WHERE id_paciente = %s", (nuevo_contenido, id_paciente))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": f"Avance personal con ID {id_paciente} actualizado exitosamente"})
    except Exception as e:
        return jsonify({"error": str(e)})

#eliminar avance
@cross_origin()
@app.route('/eliminar_avance_personal/<id_paciente>', methods=['DELETE'])
def eliminar_avance_personal(id_paciente):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM avance_personal WHERE id_paciente = %s", (id_paciente,))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": f"Avance personal con ID {id_paciente} eliminado exitosamente"})
    except Exception as e:
        return jsonify({"error": str(e)})

#insertar cita
@cross_origin()
@app.route('/insertar_cita', methods=['POST'])
def insertar_cita():
    try:
        if request.method == 'POST':
            data = request.json
            id_paciente = data['id_paciente']
            id_psicologo = data['id_psicologo']
            fecha_hora = data['fecha_hora']
            sede = data['sede']
            estado = data['estado']
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT identificacion FROM paciente WHERE identificacion = %s", (id_paciente,))
            paciente_existente = cursor.fetchone()
            if not paciente_existente:
                return jsonify({"error": f"El paciente con ID {id_paciente} no existe"})
            # Verificar si el psicologo existe
            cursor.execute("SELECT identificacion FROM psicologo WHERE identificacion = %s", (id_psicologo,))
            psicologo_existente = cursor.fetchone()
            if not psicologo_existente:
                return jsonify({"error": f"El psicólogo con ID {id_psicologo} no existe"})
            cursor.execute("INSERT INTO cita (id_paciente, id_psicologo, fecha_hora,sede,estado) VALUES (%s, %s, %s, %s, %s)", (id_paciente, id_psicologo, fecha_hora, sede,estado ))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": "Cita registrada exitosamente"})
    except Exception as e:
        return jsonify({"error": str(e)})

#ver citas
@cross_origin()
@app.route('/citas', methods=['GET'])
def citas():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM cita")
        citas = cursor.fetchall()
        cursor.close()
        if not citas:
            return jsonify({"message": "No se encontraron citas"})
        return jsonify({"avances_personales": citas})
    except Exception as e:
        return jsonify({"error": str(e)})

# ver citas por paremetros
@cross_origin()
@app.route('/buscar_citas/<id_paciente>', methods=['GET'])
def buscar_citas(id_paciente):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM cita WHERE id_paciente = %s", (id_paciente,))
        avances = cursor.fetchall()
        cursor.close()
        if not avances:
            return jsonify({"message": f"No se encontraron citas para el paciente con identificación {id_paciente}"})
        return jsonify({"citas": avances})
    except Exception as e:
        return jsonify({"error": str(e)})

#cambiar hora de cita
@cross_origin()
@app.route('/actualizar_hora_cita', methods=['PUT'])
def actualizar_hora_cita():
    try:
        if request.method == 'PUT':
            data = request.json
            id_cita = data['id_cita']
            fecha_hora = data['fecha_hora']
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM cita WHERE id_cita = %s", (id_cita,))
            cita_existente = cursor.fetchone()
            if not cita_existente:
                return jsonify({"error": f"La cita con ID {id_cita} no existe"})
            cursor.execute("UPDATE cita SET fecha_hora = %s WHERE id_cita = %s", (fecha_hora, id_cita))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": "La hora de la cita se ha actualizado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)})

#eliminar cita
@cross_origin()
@app.route('/eliminar_cita/<id_cita>', methods=['DELETE'])
def eliminar_cita(id_cita):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM cita WHERE id_cita = %s", (id_cita,))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": f"cita con ID {id_cita} eliminada exitosamente"})
    except Exception as e:
        return jsonify({"error": str(e)})


#inser historial avance
@cross_origin()
@app.route('/historial_avance', methods=['POST'])
def insertar_historial_avance():
    try:
        if request.method == 'POST':
            data = request.json
            id_paciente = data['id_paciente']
            id_psicologo = data['id_psicologo']
            fecha_historial = data['fecha_historial']
            contenido = data['contenido']
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT identificacion FROM paciente WHERE identificacion = %s", (id_paciente,))
            paciente_existente = cursor.fetchone()
            if not paciente_existente:
                return jsonify({"error": f"El paciente con ID {id_paciente} no existe"})
            cursor.execute("INSERT INTO historial_avance (id_paciente,id_psicologo,fecha_historial, contenido) VALUES (%s, %s, %s,%s)", (id_paciente,id_psicologo,fecha_historial, contenido))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": "Registro de historial de avance exitoso"})
    except Exception as e:
        return jsonify({"error": str(e)})

#ver historial avance
@cross_origin()
@app.route('/historial_avances', methods=['GET'])
def historial_avances():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM historial_avance")
        citas = cursor.fetchall()
        cursor.close()
        if not citas:
            return jsonify({"message": "No se encontró historial de avances"})
        return jsonify({"Historial de avances ": citas})
    except Exception as e:
        return jsonify({"error": str(e)})

# ver historial por paremetros
@cross_origin()
@app.route('/historialparametro/<fecha_historial>', methods=['GET'])
def historialparametros(fecha_historial):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM historial_avance WHERE fecha_historial = %s", (fecha_historial,))
        avances = cursor.fetchall()
        cursor.close()
        
        if not avances:
            return jsonify({"message": f"No se encontraró historial para el paciente con fecha de : {fecha_historial}"})
        
        return jsonify({"historial ": avances})
    except Exception as e:
        return jsonify({"error": str(e)})

#actualizar historial avance
@cross_origin()
@app.route('/actualizar_historial', methods=['PUT'])
def actualizar_historial():
    try:
        if request.method == 'PUT':
            data = request.json
            id_historial = data['id_historial']
            contenido = data['contenido']
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM historial_avance WHERE id_historial = %s", (id_historial,))
            cita_existente = cursor.fetchone()
            if not cita_existente:
                return jsonify({"error": f"El historial con ID {id_historial} no existe"})
            cursor.execute("UPDATE historial_avance SET contenido = %s WHERE id_historial = %s", (contenido, id_historial))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": f"El contenido del historial {id_historial} se ha actualizado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)})

#eliminar historial
@cross_origin()
@app.route('/eliminarhistorial/<id_historial>', methods=['DELETE'])
def eliminar_historial(id_historial):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM historial_avance WHERE id_historial = %s", (id_historial,))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": f"historial con ID {id_historial} eliminada exitosamente"})
    except Exception as e:
        return jsonify({"error": str(e)})


#GetAll table notificacion
@cross_origin()
@app.route('/notificacion', methods=['GET'])
def notificacion():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM notificacion")
        notificacion = cursor.fetchall()
        cursor.close()
        if not notificacion:
            return jsonify({"message": "No se encontraron notificaciones"})
        return jsonify({"Notificaciones ": notificacion})
    except Exception as e:
        return jsonify({"error": str(e)})

#GetID table notificacion
@cross_origin()
@app.route('/notificacionid/<id_notificacion>', methods=['GET'])
def notificacionid(id_notificacion):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM notificacion WHERE id_notificacion = %s", (id_notificacion,))
        notificacion = cursor.fetchall()
        cursor.close()
        
        if not notificacion:
            return jsonify({"message": f"No se encontraron notifcaciones con id : {id_notificacion}"})
        
        return jsonify({"Notificación": notificacion})
    except Exception as e:
        return jsonify({"error": str(e)})


#PutID table notificacion
@cross_origin()
@app.route('/actualizar_hora_notificacion/<id_notificacion>', methods=['PUT'])
def actualizar_hora_notificacion(id_notificacion):
    try:
        if request.method == 'PUT':
            data = request.json
            id_notificacion = data['id_notificacion']
            fecha_hora = data['fecha_hora']
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM notificacion WHERE id_notificacion = %s", (id_notificacion,))
            cita_existente = cursor.fetchone()
            if not cita_existente:
                return jsonify({"error": f"La notificacion con ID {id_notificacion} no existe"})
            cursor.execute("UPDATE notificacion SET fecha_hora = %s WHERE id_notificacion = %s", (fecha_hora, id_notificacion))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": "La hora de la notificacion se ha actualizado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)})

#Post table notificacion
@cross_origin()
@app.route('/notificacionpost', methods=['POST'])
def notificacionpost():
    try:
        if request.method == 'POST':
            data = request.json
            id_paciente = data['id_paciente']
            tipo = data['tipo']
            correo_institucional = data['correo_institucional']
            mensaje = data['mensaje']
            fecha_hora = data['fecha_hora']
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT identificacion FROM paciente WHERE identificacion = %s", (id_paciente,))
            paciente_existente = cursor.fetchone()
            if not paciente_existente:
                return jsonify({"error": f"El paciente con ID {id_paciente} no existe"})
            cursor.execute("INSERT INTO notificacion (id_paciente,tipo,correo_institucional,mensaje,fecha_hora) VALUES (%s, %s, %s, %s, %s)", (id_paciente,tipo,correo_institucional,mensaje,fecha_hora))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": "Registro de notificacion exitoso"})
    except Exception as e:
        return jsonify({"error": str(e)})

#Delete table notificacion
@cross_origin()
@app.route('/eliminar_notificacion/<id_notificacion>', methods=['DELETE'])
def eliminar_notificacion(id_notificacion):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM notificacion WHERE id_notificacion = %s", (id_notificacion,))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": f"Notificacion con ID {id_notificacion} eliminada exitosamente"})
    except Exception as e:
        return jsonify({"error": str(e)})

#GetAll table psicologo
@cross_origin()
@app.route('/psicologoall', methods=['GET'])
def psicologoall():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM psicologo")
        psicologoall = cursor.fetchall()
        cursor.close()
        if not psicologoall:
            return jsonify({"message": "No se encontraron psicologos"})
        return jsonify({"Psicologos ": psicologoall})
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al obtener datos de los psicologos"})

#GetID table psicologo
@cross_origin()
@app.route('/psicologoid/<identificacion>', methods=['GET'])
def psicologoid(identificacion):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM psicologo WHERE identificacion = %s", (identificacion,))
        psicologo = cursor.fetchall()
        cursor.close()
        if not psicologo:
            return jsonify({"message": f"No se encontro psicologo con identificacion : {identificacion}"})
        return jsonify({"Psicologo": psicologo})
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al obtener datos del psicologo"})

#PutID table psicologo
@cross_origin()
@app.route('/cambiartelefono/<identificacion>', methods=['PUT'])
def cambiartelefono(identificacion):
    try:
        if request.method == 'PUT':
            nuevo_telefono = request.json.get('nuevo_telefono')
            if not nuevo_telefono:
                return jsonify({"error": "Se requiere un nuevo telefono"})
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM psicologo WHERE identificacion = %s", (identificacion,))
            psychologist = cursor.fetchone()
            if not psychologist:
                cursor.close()
                return jsonify({"error": "No se encontró un psicólogo con la identificación proporcionada"})
            cursor.execute("UPDATE psicologo SET telefono = %s WHERE identificacion = %s", (nuevo_telefono, identificacion))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": "Telefono cambiado exitosamente"})
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al cambiar el telefono"})

#Post table psicologo
@cross_origin()
@app.route('/psicologopost', methods=['POST'])
def psicologopost():
    try:
        if request.method == 'POST':
            data = request.json
            nombre = data['nombre']
            correo_institucional = data['correo_institucional']
            contraseña = data['contraseña']
            disponibilidad_horaria = data['disponibilidad_horaria']
            telefono = data['telefono']
            identificacion = data['identificacion']
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT identificacion FROM psicologo WHERE identificacion = %s", (identificacion))
            psicologo_existente = cursor.fetchone()
            if not psicologo_existente:
                return jsonify({"error": f"El psicologo con identificación {identificacion} ya existe"})
            cursor.execute("INSERT INTO psicologo (nombre, correo_institucional, contraseña, disponibilidad_horaria, telefono, identificacion) VALUES (%s, %s, %s, %s, %s, %s)", (nombre,correo_institucional, contraseña, disponibilidad_horaria,telefono,identificacion ))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": "Registro de psicologo exitoso"})
    except Exception as e:
        return jsonify({"error": str(e)})

#Delete table psicologo 
@cross_origin()
@app.route('/DeletePsicologo/<identificacion>', methods=['DELETE'])
def DeletePsicologo(identificacion):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM psicologo WHERE identificacion = %s", (identificacion))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": f"Psicólogo con identificacion {identificacion} eliminado exitosamente"})
    except Exception as e:
        return jsonify({"error": str(e)})


#GetAll publicacion

# if __name__ == "__main__":
#     app.run(port=3000,debug=True)