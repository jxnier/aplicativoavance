let tu = JSON.parse(localStorage.getItem('tu'));
if (tu && tu.rol) {
    if (tu.rol === "psicologo") {
        console.log("Bienvenido, psicólogo(a). Acceso permitido.");
    } else {
        localStorage.removeItem('tu');
        window.location.href = '../registrarse.html';
        alert("No ha iniciado sesión como Psicólogo(a). \nIngrese nuevamente.");
    }
} else {
    window.location.href = '../registrarse.html';
    alert("No has iniciado sesión. Acceso denegado.");
}

const cerrarsesion = () =>{
    localStorage.removeItem("tu")
    window.location="../../index.html";
}