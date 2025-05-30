function updateBookingStatus(bookingId, status) {
    if (!confirm('Are you sure you want to update this booking status?')) {
        return;
    }
    
    fetch(`/accounts/booking/${bookingId}/update-status/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: `status=${status}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Reload the page to show updated status
            location.reload();
        } else {
            alert('Failed to update status: ' + (data.error || 'Unknown error'));
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while updating the status.');
    });
}
