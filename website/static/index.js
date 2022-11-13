function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({noteId: noteId}),
    }).then(res => {
        window.location.href = "/";
    })
}

flashMessages = document.querySelectorAll('.flash-message');
flashMessages.forEach(msg => {
    setTimeout(() => {
        msg.classList.add('hide');
    },3000)
    setTimeout(() => {
        msg.remove()
    }, 3300)
})