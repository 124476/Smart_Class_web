document.addEventListener("DOMContentLoaded", () => {
  const themeToggleButtons = document.querySelectorAll("[data-bs-theme-value]");
  const body = document.body;

  themeToggleButtons.forEach(button => {
    button.addEventListener("click", () => {
      const themeValue = button.getAttribute("data-bs-theme-value");
      body.setAttribute("data-bs-theme", themeValue);
      localStorage.setItem("theme", themeValue);
    });
  });

  const savedTheme = localStorage.getItem("theme") || "light";
  body.setAttribute("data-bs-theme", savedTheme);
});