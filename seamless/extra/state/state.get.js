const stateName = this.getAttribute('state-name');
const stateNode = document.createTextNode(seamless.state.getState(stateName));
this.appendChild(stateNode);

document.addEventListener(`stateChange:${stateName}`, (event) => {
    stateNode.textContent = event.detail.currentValue;
});