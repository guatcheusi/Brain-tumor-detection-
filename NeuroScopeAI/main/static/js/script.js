// script.js
document.addEventListener('DOMContentLoaded', function() {
    var dropArea = document.querySelector('.upload-box');
    var home= document.getElementById('home-presentation');
    var fileInput = document.getElementById('id_image');
    var previewImage = document.querySelector('.preview-image');
    var uploadButton = document.querySelector('.upload-button');

    dropArea.addEventListener('dragover', function(event) {
        event.preventDefault();
        dropArea.classList.add('dragover');
    });

    dropArea.addEventListener('dragleave', function(event) {
        dropArea.classList.remove('dragover');
    });

    dropArea.addEventListener('drop', function(event) {
        event.preventDefault();
        dropArea.classList.remove('dragover');
        var files = event.dataTransfer.files;
        if (files.length > 0) {
            fileInput.files = files;
            handleFiles(files);
        }
        
    });

    dropArea.addEventListener('click', function() {
        fileInput.click();
    });


    
    /*uploadButton.addEventListener('click', function(event) {
        var files = event.target.files;
        fileInput.files = files;
        handleFiles(files);
    });*/


    fileInput.addEventListener('change', function(event) {
        var files = event.target.files;
        if (files.length > 0) {
            fileInput.files = files;
            handleFiles(files);
        }
        
    });

    function handleFiles(files) {
        var file = files[0];
        if (file.type.startsWith('image/')) {
            var reader = new FileReader();
            reader.onload = function(event) {
                uploadButton.type ="submit";
                // Reste du code pour mettre à jour l'aperçu et le bouton (inchangé)
                previewImage.src = event.target.result;
                previewImage.style.display = 'block';
                uploadButton.innerHTML = "Analyser votre IRM";
                uploadButton.style.backgroundColor = "blue";
                
                
            };
            reader.readAsDataURL(file);
        } else {
            uploadButton.type ="button";
            alert('Veuillez sélectionner un fichier image.');
        }
    }
});



