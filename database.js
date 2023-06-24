const sqlite3 = require('sqlite3').verbose();

// Conectar a la base de datos
const dbPath = 'C:\Users\Usuario\Desktop\DBTic\DBTic\DBTic.db'; // Reemplaza con la ruta correcta a tu base de datos
const db = new sqlite3.Database(dbPath);

// Consulta para obtener los datos de la tabla Ambito_Financiero
const query = 'SELECT * FROM Ambito_Financiero';

// Ejecutar la consulta
db.all(query, (err, rows) => {
  if (err) {
    console.error(err);
    return;
  }

  // Procesar los resultados
  rows.forEach((row) => {
    // Haz lo que necesites con los datos (por ejemplo, mostrarlos en la interfaz de la aplicación)
    console.log(row.ID, row.Fecha, row.Titulo);
  });

  // Cerrar la conexión a la base de datos
  db.close();
});