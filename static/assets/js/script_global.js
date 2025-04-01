function scaleText() {
    console.log("Scaling text...");
    const containers = document.querySelectorAll('.scaling-container'); 

    containers.forEach(container => {
        const text = container.querySelector('.scaling'); 
        if (!text) return;

        let fontSize = 30; 
        text.style.fontSize = fontSize + 'px';  
        console.log("soirhf")
        console.log("Text width:", text.offsetWidth);
        console.log("Container width:", container.offsetWidth);

        while (text.offsetWidth > container.offsetWidth) {
            console.log(text.offsetWidth)
            console.log(container.offsetWidth)
            fontSize -= 1; 
            text.style.fontSize = fontSize + 'px'; 
        }
    });
}

window.addEventListener('load', scaleText);
window.addEventListener('resize', scaleText);