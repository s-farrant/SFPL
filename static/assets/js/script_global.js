function scaleText() {
    const containers = document.querySelectorAll('.scaling-container'); 

    containers.forEach(container => {
        const text = container.querySelector('.scaling'); 
        if (!text) return;

        let fontSize = 30; 
        text.style.fontSize = fontSize + 'px';  

        while (text.offsetWidth > container.offsetWidth) {
            fontSize -= 1; 
            text.style.fontSize = fontSize + 'px'; 
        }
    });
}

window.addEventListener('load', scaleText);
window.addEventListener('resize', scaleText);


function scaleText2() {
    const containers = document.querySelectorAll('.scaling-container2'); 

    containers.forEach(container => {
        const text = container.querySelector('.scaling2'); 
        if (!text) return;

        let fontSize = 20; 
        text.style.fontSize = fontSize + 'px';  

        while (text.offsetWidth > container.offsetWidth) {
            fontSize -= 1; 
            text.style.fontSize = fontSize + 'px'; 
        }
    });
}

window.addEventListener('load', scaleText2);
window.addEventListener('resize', scaleText2);