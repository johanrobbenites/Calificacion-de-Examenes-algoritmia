document.getElementById('ejecutar').addEventListener('click', function() {
    fetch('/execute')
        .then(response => response.text())
        .then(result => {
            document.getElementById('resultado').textContent = result;
        });
});