document.getElementById("avatar").addEventListener("click", function() {
    document.getElementById("id_avatar").click();
});

document.getElementById("id_avatar").addEventListener("change", function() {
    if (this.files && this.files.length > 0) {
        let reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById("avatar").src = e.target.result;
        }
        reader.readAsDataURL(this.files[0]);
    }
});