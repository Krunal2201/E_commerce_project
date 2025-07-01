document.querySelectorAll('input').forEach((item) => {
    item.addEventListener("focus", function() {
        item.previousElementSibling.className = 'label-selected';
    })
    item.addEventListener("blur", function() {
        if (item.value === '') {
            item.previousElementSibling.className = '';
        }
    })
})
document.getElementById('registerLink').addEventListener("click", function() {
    if(window.innerWidth < 600){
        document.getElementById("singUp").style.display = "block";
        document.getElementById("login").style.display = "none";
    } else {
        document.getElementById("overlay").style.transform = 'translate(100%, -25px)';
    }
});

document.getElementById('loginLink').addEventListener("click", function() {
    if(window.innerWidth < 600) {
        document.getElementById("signUp").style.display = "block";
        document.getElementById("login").style.display = "none";
    } else {
        document.getElementById("overlay").style.transform = 'translate(0, -25px)';
    }
});
document.getElementById('password1').addEventListener('click', function () {
      const passwordField = document.getElementById('password');
      const passwordIcon = document.getElementById('passwordIcon');
      if (passwordField.type === 'password') {
        passwordField.type = 'text';
        passwordIcon.classList.replace('bi-eye', 'bi-eye-slash');
      } else {
        passwordField.type = 'password';
        passwordIcon.classList.replace('bi-eye-slash', 'bi-eye');
      }
    });