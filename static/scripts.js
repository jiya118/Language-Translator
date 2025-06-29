
async function translateText() {
    const input = document.getElementById("englishText").value;
    const language = document.getElementById("languageSelect").value;
    const outputBox = document.getElementById("output");

    if (!input) {
    outputBox.value = "Please enter text to translate.";
    return;
    }

    outputBox.value = "Translating...";

    try {
    const response = await fetch("/translate", {
        method: "POST",
        headers: {
        "Content-Type": "application/json"
        },
        body: JSON.stringify({ input, language })
    });

    if (!response.ok) {
        const errorText = await response.text(); // helpful for debugging
        console.error("Server responded with error:", errorText);
        throw new Error("Translation failed. Server returned error.");
    }

    const data = await response.json();
    outputBox.value = data.translation || data.error;
    
    } catch (err) {
    outputBox.value = "❌ Translation failed.";
    console.error("Error during translation:", err);
    }
}
