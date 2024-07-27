seamless.loadComponent = async function (name) {
  return seamless.instance.toDOMElement(await seamless.instance.getComponent(name, {}));
}

const parent = this.parentElement;
const PageStateChange = new Event("pageLocationChange");

window.addEventListener("pageLocationChange", () => {
  const path = window.location.pathname;
  const page = routes.find(
    (page) => page.path.replace(/^\//, "") === path.replace(/^\//, "")
  );

  if (!page) {
    return;
  }

  while (parent.firstChild) {
    parent.removeChild(parent.firstChild);
  }

  seamless.loadComponent(page.name).then((component) => {
    parent.appendChild(component);
  });
});

seamless.navigateTo = function (to) {
  window.history.pushState({}, "", to);
  window.dispatchEvent(PageStateChange);
  return false;
}

window.dispatchEvent(PageStateChange);
