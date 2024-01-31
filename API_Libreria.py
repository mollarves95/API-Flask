from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = '' 
app.config['MYSQL_DB'] = 'libreria' 

mysql = MySQL(app)


# ---------- Rutas POST para Agregar información ----------

# Agregar un Autor
@app.route('/nuevo_autor', methods=['POST'])
def agregarAutor():
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO autores (nombre) VALUES (%s)", (nombre,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'mensaje': 'Autor agregado exitosamente'})

# Agregar un Género
@app.route('/nuevo_genero', methods=['POST'])
def agregarGenero():
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO generos (nombre) VALUES (%s)", (nombre,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'mensaje': 'Género agregado exitosamente'})

# Agregar una Editorial
@app.route('/nueva_editorial', methods=['POST'])
def agregarEditorial():
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO editoriales (nombre) VALUES (%s)", (nombre,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'mensaje': 'Editorial agregada exitosamente'})

# Agregar un Usuario
@app.route('/nuevo_usuario', methods=['POST'])
def agregarUsuario():
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO usuarios (nombre) VALUES (%s)", (nombre,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'mensaje': 'Usuario agregado exitosamente'})

# Agregar un Libro
@app.route('/nuevo_libro', methods=['POST'])
def agregarLibro():
    titulo = request.json['titulo']
    anno_publicacion = request.json['anno_publicacion']
    autor_id = request.json['autor_id']
    genero_id = request.json['genero_id']
    editorial_id = request.json['editorial_id']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO libros (titulo, anno_publicacion, autor_id, genero_id, editorial_id) VALUES (%s, %s, %s, %s, %s)", (titulo, anno_publicacion, autor_id, genero_id, editorial_id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'mensaje': 'Libro agregado exitosamente'})

# Agregar una Reseña
@app.route('/nueva_resenna', methods=['POST'])
def agregarResenna():
    contenido = request.json['contenido']
    libro_id = request.json['libro_id']
    usuario_id = request.json['usuario_id']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO resennas (contenido, libro_id, usuario_id) VALUES (%s, %s, %s)", (contenido, libro_id, usuario_id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'mensaje': 'Reseña agregada exitosamente'})
    

# --------- Rutas GET para Obtener información --------

# Obtener todos los libros 
@app.route('/libros', methods=["GET"])
def obtenerLibros():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM libros")

    libros = cursor.fetchall()

    cursor.close()
    res = jsonify(libros)
    res.headers.add("Access-Control-Allow-Origin","*")
    return res

# Obtener todos los Autores 
@app.route('/autores', methods=["GET"])
def obtenerAutores():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM autores")

    autores = cursor.fetchall()

    cursor.close()
    res = jsonify(autores)
    res.headers.add("Access-Control-Allow-Origin","*")
    return res

# Obtener todos los Géneros 
@app.route('/generos', methods=["GET"])
def obtenerGeneros():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM generos")

    generos = cursor.fetchall()

    cursor.close()
    res = jsonify(generos)
    res.headers.add("Access-Control-Allow-Origin","*")
    return res

# Obtener todas las Editoriales 
@app.route('/editoriales', methods=["GET"])
def obtenerEditoriales():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM editoriales")

    editoriales = cursor.fetchall()

    cursor.close()
    res = jsonify(editoriales)
    res.headers.add("Access-Control-Allow-Origin","*")
    return res

# Obtener todas las Reseñas 
@app.route('/resennas', methods=["GET"])
def obtenerResennas():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM resennas")

    resennas = cursor.fetchall()

    cursor.close()
    res = jsonify(resennas)
    res.headers.add("Access-Control-Allow-Origin","*")
    return res

# Obtener todos los Usuarios 
@app.route('/usuarios', methods=["GET"])
def obtenerUsuarios():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios")

    usuarios = cursor.fetchall()

    cursor.close()
    res = jsonify(usuarios)
    res.headers.add("Access-Control-Allow-Origin","*")
    return res


# --------- Rutas PATCH para Editar información --------

# Editar un libro
@app.route("/libros/<book_id>", methods=["PATCH"])
def actualizar_libro(book_id):
    
    titulo = request.json["titulo"]
    anno_publicacion = request.json['anno_publicacion']
    autor_id = request.json['autor_id']
    genero_id = request.json['genero_id']
    editorial_id = request.json['editorial_id']

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE libros SET titulo = %s, anno_publicacion = %s, autor_id = %s, genero_id = %s, editorial_id = %s WHERE id = %s", (titulo, anno_publicacion, autor_id, genero_id, editorial_id, book_id))

    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':'El Libro se actualizó correctamente'})

# Editar un Autor
@app.route("/autores/<authors_id>", methods=["PATCH"])
def actualizar_autor(authors_id):
    
    nombre = request.json["nombre"]

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE autores SET nombre = %s WHERE id = %s", (nombre, authors_id))

    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':'El Autor se actualizó correctamente'})

# Editar un Género
@app.route("/generos/<gender_id>", methods=["PATCH"])
def actualizar_genero(gender_id):
    
    nombre = request.json["nombre"]

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE generos SET nombre = %s WHERE id = %s", (nombre, gender_id))

    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':'El Género se actualizó correctamente'})

# Editar una Editorial
@app.route("/editoriales/<edit_id>", methods=["PATCH"])
def actualizar_editorial(edit_id):
    
    nombre = request.json["nombre"]

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE editoriales SET nombre = %s WHERE id = %s", (nombre, edit_id))

    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':'La Editorial se actualizó correctamente'})

# Editar una Reseña
@app.route("/resennas/<rese_id>", methods=["PATCH"])
def actualizar_resenna(rese_id):
    
    contenido = request.json['contenido']
    libro_id = request.json['libro_id']
    usuario_id = request.json['usuario_id']

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE resennas SET contenido = %s, libro_id = %s, usuario_id = %s WHERE id = %s", (contenido, libro_id, usuario_id, rese_id))

    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':'La Reseña se actualizó correctamente'})

# Editar un Usuario
@app.route("/usuarios/<user_id>", methods=["PATCH"])
def actualizar_usuario(user_id):
    
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE usuarios SET nombre = %s WHERE id = %s", (nombre, user_id))

    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':'El Usuario se actualizó correctamente'})


# --------- Rutas DELETE para Eliminar información --------

# Eliminar un libro
@app.route("/libros/<book_id>", methods=["DELETE"])
def eliminar_libro(book_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM libros WHERE id = %s", (book_id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':'El Libro se eliminó correctamente'})

# Eliminar un Autor
@app.route("/autores/<authors_id>", methods=["DELETE"])
def eliminar_autor(authors_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM autores WHERE id = %s", (authors_id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':'El Autor se eliminó correctamente'})

# Eliminar un Género
@app.route("/generos/<gender_id>", methods=["DELETE"])
def eliminar_genero(gender_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM generos WHERE id = %s", (gender_id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':'El Género se eliminó correctamente'})

# Eliminar una Editorial
@app.route("/editoriales/<edit_id>", methods=["DELETE"])
def eliminar_editorial(edit_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM editoriales WHERE id = %s", (edit_id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':'La Editorial se eliminó correctamente'})

# Eliminar una Reseña
@app.route("/resennas/<rese_id>", methods=["DELETE"])
def eliminar_resenna(rese_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM resennas WHERE id = %s", (rese_id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':'La Reseña se eliminó correctamente'})

# Eliminar un Usuario
@app.route("/usuarios/<user_id>", methods=["DELETE"])
def eliminar_usuario(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (user_id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':'El Usuario se eliminó correctamente'})



# --------- Ruta aplicando JOIN para Obtener toda la información relacionada a un Libro --------

@app.route('/books', methods=["GET"])
def obtener_informacion_libros():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT libros.id, libros.titulo, autores.nombre, generos.nombre, editoriales.nombre FROM libros JOIN autores ON autor_id = autores.id JOIN generos ON genero_id = generos.id JOIN editoriales ON editorial_id = editoriales.id")

    books = cursor.fetchall()

    cursor.close()
    res = jsonify(books)
    res.headers.add("Access-Control-Allow-Origin","*")
    return res

    

if __name__ == '__main__':
    app.run(debug=True, port=8080)


