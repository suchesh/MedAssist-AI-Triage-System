// Patient form + PDF upload + API call
const form = document.getElementById('patientForm');
const pdfInput = document.getElementById('pdfUpload');
const pdfOut = document.getElementById('pdfText');

if (form) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Collect all text/number/textarea fields
    const textFields = {};
    const inputs = form.querySelectorAll("input, textarea");
    inputs.forEach(input => {
      if (input.type !== "file") {
        textFields[input.name] = input.value;
      }
    });

    // Build FormData
    const formData = new FormData();
    formData.append("text_data", JSON.stringify(textFields));

    // Append PDF if uploaded
    if (pdfInput && pdfInput.files.length > 0) {
      formData.append("pdf_file", pdfInput.files[0]);
    }

    try {
      const res = await fetch("/fetch-ai-analysis", {
        method: "POST",
        body: formData
      });

      const result = await res.json();

      pdfOut.hidden = false;
      pdfOut.textContent = JSON.stringify(result, null, 2);
    } catch (err) {
      console.error("Error calling API:", err);
      pdfOut.hidden = false;
      pdfOut.textContent = "Failed to connect to API.";
    }
  });
}
