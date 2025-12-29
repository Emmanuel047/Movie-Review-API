let token = localStorage.getItem('token') || '';

if (token) {
    document.getElementById('api-tests').style.display = 'block';
}

async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    try {
        const response = await fetch('/api/token/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });
        
        if (response.ok) {
            const data = await response.json();
            token = data.access;
            localStorage.setItem('token', token);
            document.getElementById('api-tests').style.display = 'block';
            alert('✅ Login successful!');
        } else {
            alert('❌ Login failed');
        }
    } catch (error) {
        alert('Error: ' + error.message);
    }
}

async function getReviews() {
    try {
        const response = await fetch('/api/reviews/', {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        const data = await response.json();
        console.log('Reviews:', data);
        alert(`Found ${data.count || 0} reviews`);
    } catch (error) {
        alert('Error: ' + error.message);
    }
}

async function addReview() {
    try {
        const response = await fetch('/api/reviews/', {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}` 
            },
            body: JSON.stringify({
                movie_title: 'Inception',
                review_text: 'Great movie!'
            })
        });
        const data = await response.json();
        alert('✅ Review created! ID: ' + data.id);
    } catch (error) {
        alert('Error: ' + error.message);
    }
}
