const API_URL = "http://127.0.0.1:8000";

document.addEventListener("DOMContentLoaded", () => {

    // Flood Prediction Handler
    const floodForm = document.getElementById("floodForm");
    if (floodForm) {
        floodForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const rainfall = parseFloat(document.getElementById("rainfall").value);
            const humidity = parseFloat(document.getElementById("humidity").value);
            const river_level = parseFloat(document.getElementById("river_level").value);
            const resultDiv = document.getElementById("floodResult");
            const outputP = document.getElementById("floodOutput");

            outputP.innerText = "Analyzing...";
            resultDiv.style.display = "block";
            resultDiv.className = "result"; // Reset class

            try {
                const response = await fetch(`${API_URL}/predict/flood`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ rainfall, humidity, river_level })
                });

                if (!response.ok) throw new Error("API Error");

                const data = await response.json();
                outputP.innerHTML = `
                    <strong>Risk Level:</strong> ${data.risk_level}<br>
                    <strong>Probability:</strong> ${(data.probability * 100).toFixed(1)}%<br>
                    <strong>Advice:</strong> ${data.alert}
                `;

                if (data.risk_level === "High") {
                    resultDiv.classList.add("risk-high");
                } else {
                    resultDiv.classList.add("risk-low");
                }

            } catch (error) {
                console.error(error);
                outputP.innerText = "Error connecting to AI engine.";
            }
        });
    }

    // Earthquake Prediction Handler
    const quakeForm = document.getElementById("quakeForm");
    if (quakeForm) {
        quakeForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const magnitude = parseFloat(document.getElementById("magnitude").value);
            const depth = parseFloat(document.getElementById("depth").value);
            const resultDiv = document.getElementById("quakeResult");
            const outputP = document.getElementById("quakeOutput");

            outputP.innerText = "Analyzing...";
            resultDiv.style.display = "block";
            resultDiv.className = "result";

            try {
                const response = await fetch(`${API_URL}/predict/earthquake`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ magnitude, depth })
                });

                if (!response.ok) throw new Error("API Error");

                const data = await response.json();
                outputP.innerHTML = `
                    <strong>Risk Level:</strong> ${data.risk_level}<br>
                    <strong>Probability:</strong> ${(data.probability * 100).toFixed(1)}%<br>
                    <strong>Advice:</strong> ${data.alert}
                `;

                if (data.risk_level === "High") {
                    resultDiv.classList.add("risk-high");
                } else {
                    resultDiv.classList.add("risk-low");
                }

            } catch (error) {
                console.error(error);
                outputP.innerText = "Error connecting to AI engine.";
            }
        });
    }
});
