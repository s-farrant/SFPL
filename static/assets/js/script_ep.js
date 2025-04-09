// Hide/Show All/GKP/DEF/MID/FWD in left side menu

document.addEventListener('DOMContentLoaded', function() {

    const allButton = document.getElementById('bar-button-all');
    const gkpButton = document.getElementById('bar-button-gkp');
    const defButton = document.getElementById('bar-button-def');
    const midButton = document.getElementById('bar-button-mid');
    const fwdButton = document.getElementById('bar-button-fwd');
    const all = document.getElementById('side-bar-with-buttons-all');
    const gkp = document.getElementById('side-bar-with-buttons-gkp');
    const def = document.getElementById('side-bar-with-buttons-def');
    const mid = document.getElementById('side-bar-with-buttons-mid');
    const fwd = document.getElementById('side-bar-with-buttons-fwd');

    // Show All
    allButton.addEventListener('click', function() {
            allButton.style.boxShadow = 'inset 0 -1px 0 #963cff';
            gkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
            defButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
            midButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
            fwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
            all.style.display = 'block';
            gkp.style.display = 'none';
            def.style.display = 'none';
            mid.style.display = 'none';
            fwd.style.display = 'none';
    });

    // Show All
    gkpButton.addEventListener('click', function() {
            allButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
            gkpButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
            defButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
            midButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
            fwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
            all.style.display = 'none';
            gkp.style.display = 'block';
            def.style.display = 'none';
            mid.style.display = 'none';
            fwd.style.display = 'none';
    });

    // Show All
    defButton.addEventListener('click', function() {
            allButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
            gkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
            defButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
            midButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
            fwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
            all.style.display = 'none';
            gkp.style.display = 'none';
            def.style.display = 'block';
            mid.style.display = 'none';
            fwd.style.display = 'none';
    });

    // Show All
    midButton.addEventListener('click', function() {
            allButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
            gkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
            defButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
            midButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
            fwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
            all.style.display = 'none';
            gkp.style.display = 'none';
            def.style.display = 'none';
            mid.style.display = 'block';
            fwd.style.display = 'none';
    });

    // Show All
    fwdButton.addEventListener('click', function() {

            allButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
            gkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
            defButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
            midButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
            fwdButton.style.boxShadow = 'inset 0 -1px 0 #963cff';  
            all.style.display = 'none';
            gkp.style.display = 'none';
            def.style.display = 'none';
            mid.style.display = 'none';
            fwd.style.display = 'block';
    });
});

