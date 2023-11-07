function showNotification(message) {
    alert(message);
}

document.addEventListener("DOMConentLoaded", function() {
    if (planAdded === "true") {
        showNotification("Plan added successfully!")
    }
})