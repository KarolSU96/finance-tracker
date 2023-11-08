// Function waits for DOM to be fully loaded before execution
document.addEventListener('DOMContentLoaded', function() {
    // get element containing messages
    const messages = document.querySelector('.messages');

    // check if messages exist
    if (messages) {
        // Display the first message with SweetAlert
        const firstMessage = messages.querySelector('div');
        if (firstMessage) {
            // Use SweetAlert to show notification
            Swal.fire({
                title: firstMessage.textContent,
                icon: firstMessage.classList.contains('success') ? 'success' : 'error',
            });
        }
    }
});