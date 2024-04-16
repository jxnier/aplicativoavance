let tu = JSON.parse(localStorage.getItem('tu'));
if (tu && tu.rol) {
    if (tu.rol === "paciente") {
        console.log("Bienvenido, paciente. Acceso permitido.");
    } else {
        localStorage.removeItem('tu');
        window.location.href = '../registrarse.html';
        alert("No ha iniciado sesión como Paciente. \nIngrese nuevamente.");
    }
} else {
    window.location.href = '../registrarse.html';
    alert("No has iniciado sesión. Acceso denegado.");
}

const cerrarsesion = () => {
    localStorage.removeItem("tu")
    window.location = "../../index.html";
}