const tdp = (num) => num < 10 ? `0${num}` : num;

const setClock = () => {
    const date = new Date();
    const hours = date.getHours();
    const minutes = date.getMinutes();
    const seconds = date.getSeconds();
    const time = `${tdp(hours)}:${tdp(minutes)}:${tdp(seconds)}`;
    this.textContent = time;
    setInterval(setClock, 1000);
}

setClock();
