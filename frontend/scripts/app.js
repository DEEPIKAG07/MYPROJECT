document.addEventListener('DOMContentLoaded', () => {
    const grievanceForm = document.getElementById('grievanceForm');
    const trackButton = document.getElementById('trackButton');

    grievanceForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const content = document.getElementById('grievanceContent').value;
        try {
            const response = await submitGrievance(content);
            alert(`Grievance submitted successfully. ID: ${response.id}`);
        } catch (error) {
            alert('Error submitting grievance. Please try again.');
        }
    });

    trackButton.addEventListener('click', async () => {
        const grievanceId = document.getElementById('grievanceId').value;
        try {
            const grievance = await trackGrievance(grievanceId);
            displayGrievanceStatus(grievance);
        } catch (error) {
            alert('Error tracking grievance. Please check the ID and try again.');
        }
    });
});

async function submitGrievance(content) {
    const response = await fetch('/api/grievance', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
        },
        body: JSON.stringify({ content })
    });
    return response.json();
}

async function trackGrievance(id) {
    const response = await fetch(`/api/grievance/${id}`, {
        headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
    });
    return response.json();
}

function displayGrievanceStatus(grievance) {
    const statusDiv = document.getElementById('grievanceStatus');
    statusDiv.innerHTML = `
        <h3>Grievance #${grievance.id}</h3>
        <p>Status: ${grievance.status}</p>
        <p>Category: ${grievance.category}</p>
        <p>Priority: ${grievance.priority}</p>
        <p>Submitted: ${new Date(grievance.created_at).toLocaleString()}</p>
    `;
}
