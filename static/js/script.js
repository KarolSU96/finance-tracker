document.addEventListener('DOMContentLoaded', function() {

    const messages = document.querySelector('.messages')


    if (messages) {
        // Display the first message with SweetAlert
        const firstMessage = messages.querySelector('div');
        if (firstMessage) {
            Swal.fire({
                title: firstMessage.textContent,
                icon: firstMessage.classList.contains('success') ? 'success' : 'error',
            });
        }
    }
})