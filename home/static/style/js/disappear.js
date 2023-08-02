document.addEventListener("DOMContentLoaded", function() {
    const successDiv = document.querySelector(".success");
    if (successDiv) {
        setTimeout(function() {
            successDiv.classList.add("hide");
        }, 3000); // 3000 milliseconds (3 seconds)
    }
});