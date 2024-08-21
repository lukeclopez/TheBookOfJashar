function redirectToPage() {
  // Get the current path relative to your project
  const currentPath = window.location.pathname;
  const cityName = currentPath.split("/").slice(-1)[0];

  // Build the new path with the "/pages" directory
  const newPath = "../pages/cities/" + cityName; // "./pages/cities/adullam.html"

  console.log(newPath);
  // Redirect to the new path
  window.location.href = newPath;
}

window.onload = function () {
  redirectToPage();
};
