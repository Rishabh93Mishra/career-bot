const BASE_URL = "http://127.0.0.1:5000";

// LOGIN
async function login() {
  const email = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const msg = document.getElementById("message");

  const response = await fetch(`${BASE_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });

  const data = await response.json();

  if (data.status === "success") {
    msg.style.color = "green";
    msg.innerHTML = "Login successful!";

    setTimeout(() => {
      document.getElementById("authPage").style.display = "none";
      document.getElementById("mainPage").style.display = "block";
    }, 1000);
  } else {
    msg.style.color = "red";
    msg.innerHTML = "Invalid email or password!";
  }
}

// SIGNUP
async function signup() {
  const name = document.getElementById("signupName").value;
  const email = document.getElementById("signupEmail").value;
  const password = document.getElementById("signupPassword").value;
  const msg = document.getElementById("signupMessage");

  const response = await fetch(`${BASE_URL}/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, email, password })
  });

  msg.style.color = "green";
  msg.innerHTML = "Account created! Redirecting...";

  setTimeout(() => showLogin(), 1500);
}
function loadCourses() {
    fetch("http://127.0.0.1:5000/courses")
    .then(res => res.json())
    .then(data => {
        let container = document.querySelector(".college-list");
        container.innerHTML = "";

        data.forEach(c => {
            container.innerHTML += `
                <div class="college-card">
                    <h3>${c.course_name}</h3>
                    <p>Eligibility: ${c.eligibility}</p>
                    <p>Duration: ${c.duration}</p>
                    <p>Cost: ${c.cost}</p>
                </div>
            `;
        });
    });
}
