const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function loadComponent(name) {
  return s.toDOMElement(await s.getComponent(name, {}));
}

const PageStateChange = new Event("pagestatechange");
const spinner = document.createElement("div");
spinner.classList.add("spinner-border");

addEventListener("pagestatechange", () => {
  const path = window.location.pathname;
  const page = routes.find(
    (page) => page.path.replace(/^\//, "") === path.replace(/^\//, "")
  );

  if (!page) {
    return;
  }

  routerContent.innerHTML = "";
  routerContent.prepend(spinner);
  loadComponent(page.name).then((component) => {
    routerContent.removeChild(spinner);
    routerContent.appendChild(component);
  });
});

function navigateTo(to) {
  window.history.pushState({}, "", to);
  dispatchEvent(PageStateChange);
  return false;
}
