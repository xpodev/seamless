function setSource(id, source) {
  const element = document.getElementById(id);
  if (element) {
    element.setAttribute('seamless:source:init', source);
  }
}

