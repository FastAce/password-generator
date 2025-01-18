document.getElementById("generate").addEventListener("click", () => {
  const length = document.getElementById("length").value;
  const includeLetters = document.getElementById("letters").checked;
  const includeNumbers = document.getElementById("numbers").checked;
  const includeSymbols = document.getElementById("symbols").checked;

  const password = generatePassword(length, includeLetters, includeNumbers, includeSymbols);
  document.getElementById("result").innerText = password;
});

function generatePassword(length, includeLetters, includeNumbers, includeSymbols) {
  const letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const numbers = "0123456789";
  const symbols = "!@#$%^&*()_+[]{}|;:',.<>?";
  let chars = "";

  if (includeLetters) chars += letters;
  if (includeNumbers) chars += numbers;
  if (includeSymbols) chars += symbols;

  if (chars.length === 0) return "Error: Select at least one option.";

  let password = "";
  for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * chars.length);
    password += chars[randomIndex];
  }
  return password;
}

