# Actividad 08 - Insertando registros a la Base de Datos (Formulario Vr3) · Python (Tkinter)

Programación Avanzada · 3° "N" · LIDTS · UNACH

Formulario de registro (nombre, apellidos, edad, estatura, teléfono y género) que valida cada campo y,
al pulsar **Guardar**, inserta el registro en la tabla `BasePA` de MySQL y lo agrega al archivo
`3NAgoDic26.txt` (en la carpeta desde donde se ejecuta).

## Requisitos
- Python 3.10 o superior
- MySQL Server en `localhost:3306`
- Librería `mysql-connector-python`

## Ejecutar
1. Crea la base de datos y la tabla con `bd/BasePA.sql` (MySQL Workbench o `mysql -u root -p < bd/BasePA.sql`).
2. Instala la librería:

```
pip install -r requirements.txt
```

3. Si tu usuario/contraseña o el nombre de la base son otros, cámbialos en `mysql.connector.connect(...)` dentro de `insertarRegistro`.
4. Ejecuta `_3NLIDTS_DiegoGuerrero_8_py.py` desde Visual Studio (F5) o con `python _3NLIDTS_DiegoGuerrero_8_py.py`.
