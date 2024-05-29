// Mostrar/Ocultar contraseña al hacer click en el icono de visibilidad
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