seamless.loadComponent = async function (name) {
  return seamless.instance.toDOMElement(await seamless.instance.getComponent(name, {}));
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

  this.innerHTML = "";
  this.prepend(spinner);
  seamless.loadComponent(page.name).then((component) => {
    this.removeChild(spinner);
    this.appendChild(component);
  });
});

seamless.navigateTo = function(to) {
  window.history.pushState({}, "", to);
  window.dispatchEvent(PageStateChange);
  return false;
}

seamless.navigateTo(window.location.pathname);
