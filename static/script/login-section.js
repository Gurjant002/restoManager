/**
 * Este script muestra u oculta la contraseña al hacer clic en el icono de visibilidad.
 *
 * Al cargar la página, se añaden dos eventos de clic a los elementos con los id 'verContraseña1' y 'verContraseña2'.
 * Al hacer clic en estos elementos, se verifica el tipo de entrada de la contraseña correspondiente.
 * Si el tipo de entrada es 'password', se cambia a 'text' y se cambia la clase del icono correspondiente.
 * Si el tipo de entrada es 'text', se cambia a 'password' y se cambia la clase del icono correspondiente.
 */
document.addEventListener('DOMContentLoaded', function() {
  const mostrarContraseña1 = document.getElementById('verContraseña1');
  const mostrarContraseña2 = document.getElementById('verContraseña2');
  const contraseña1 = document.getElementById('contraseña1');
  const contraseña2 = document.getElementById('contraseña2');

  mostrarContraseña1.addEventListener('click', function() {
      if (contraseña1.type === 'password') {
          contraseña1.type = 'text';
          mostrarContraseña1.classList.remove('fa-eye');
          mostrarContraseña1.classList.add('fa-eye-slash');
      } else {
          contraseña1.type = 'password';
          mostrarContraseña1.classList.remove('fa-eye-slash');
          mostrarContraseña1.classList.add('fa-eye');
      }
  });

  mostrarContraseña2.addEventListener('click', function() {
      if (contraseña2.type === 'password') {
          contraseña2.type = 'text';
          mostrarContraseña2.classList.remove('fa-eye');
          mostrarContraseña2.classList.add('fa-eye-slash');
      } else {
          contraseña2.type = 'password';
          mostrarContraseña2.classList.remove('fa-eye-slash');
          mostrarContraseña2.classList.add('fa-eye');
      }
  });
});
