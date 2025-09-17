// Toggle mobile navigation
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navLinks.classList.toggle('active');
});

// Close mobile nav when clicking on a link
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
    });
});

// Check duplicate functionality
const checkBtn = document.getElementById('check-btn');
const resultDiv = document.getElementById('result');

checkBtn.addEventListener('click', async () => {
    const question1 = document.getElementById('question1').value.trim();
    const question2 = document.getElementById('question2').value.trim();

    if (!question1 || !question2) {
        resultDiv.textContent = 'Please enter both questions!';
        resultDiv.className = 'result duplicate';
        return;
    }

    try {
        // Show loading state
        checkBtn.disabled = true;
        checkBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Checking...';

        // Make API call to backend
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question1: question1,
                question2: question2
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        resultDiv.textContent = `Result: ${data.result}`;
        resultDiv.className = 'result ' + (data.result === 'Duplicate' ? 'duplicate' : 'not-duplicate');

    } catch (error) {
        console.error('Error:', error);
        resultDiv.textContent = 'Error: Could not connect to the server';
        resultDiv.className = 'result duplicate';
    } finally {
        // Reset button state
        checkBtn.disabled = false;
        checkBtn.innerHTML = '<i class="fas fa-check-circle"></i> Check Duplicate';
    }
});