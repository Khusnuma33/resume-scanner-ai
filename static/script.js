// static/js/script.js

// Optional simple alert on upload
document.addEventListener('DOMContentLoaded', function () {
    const uploadForm = document.querySelector('form');
    if (uploadForm) {
        uploadForm.addEventListener('submit', function () {
            alert('Uploading your resume...');
        });
    }
});
