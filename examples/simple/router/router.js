async function loadComponent(name) {
  return s.toDOMElement(await s.getComponent(name, {}));
}

const PageStateChange = new Event("pagestatechange");
const spinner = document.createElement("div");
spinner.classList.add("spinner-border");

window.addEventListener("pagestatechange", () => {
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

this.navigateTo = function(to) {
  window.history.pushState({}, "", to);
  window.dispatchEvent(PageStateChange);
  return false;
}
