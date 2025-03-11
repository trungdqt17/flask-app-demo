async function deleteBook(bookId) {
    if (confirm('Are you sure you want to delete this book?')) {
        try {
            const response = await fetch(`/books/${bookId}`, {
                method: 'DELETE'
            });
            if (response.ok) {
                const result = await response.json();
                alert(result.message);
                // Remove the row from the table
                document.querySelector(`tr[data-book-id="${bookId}"]`).remove();
            } else {
                const error = await response.json();
                alert(error.error || 'Failed to delete book');
            }
        } catch (error) {
            alert('Error deleting book');
        }
    }
}
