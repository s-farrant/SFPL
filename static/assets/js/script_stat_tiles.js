// TILE1

document.addEventListener('DOMContentLoaded', function() {

    const tile1AllButton = document.getElementById('tile1-all-button');
    const tile1GkpButton = document.getElementById('tile1-gkp-button');
    const tile1DefButton = document.getElementById('tile1-def-button');
    const tile1MidButton = document.getElementById('tile1-mid-button');
    const tile1FwdButton = document.getElementById('tile1-fwd-button');
    const tile1All = document.getElementById('tile1-all');
    const tile1Gkp = document.getElementById('tile1-gkp');
    const tile1Def = document.getElementById('tile1-def');
    const tile1Mid = document.getElementById('tile1-mid');
    const tile1Fwd = document.getElementById('tile1-fwd');

    // Show All
    tile1AllButton.addEventListener('click', function() {
        tile1AllButton.style.boxShadow = 'inset 0 -1px 0 #963cff';
        tile1GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile1DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile1MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile1FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile1All.style.display = 'block';
        tile1Gkp.style.display = 'none';
        tile1Def.style.display = 'none';
        tile1Mid.style.display = 'none';
        tile1Fwd.style.display = 'none';
        scaleText();
    });

    // Show GKP
    tile1GkpButton.addEventListener('click', function() {
        tile1AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile1GkpButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile1DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile1MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile1FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile1All.style.display = 'none';
        tile1Gkp.style.display = 'block';
        tile1Def.style.display = 'none';
        tile1Mid.style.display = 'none';
        tile1Fwd.style.display = 'none';
        scaleText();
    });

    // Show DEF
    tile1DefButton.addEventListener('click', function() {
        tile1AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile1GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile1DefButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile1MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile1FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile1All.style.display = 'none';
        tile1Gkp.style.display = 'none';
        tile1Def.style.display = 'block';
        tile1Mid.style.display = 'none';
        tile1Fwd.style.display = 'none';
        scaleText();
    });

    // Show MID
    tile1MidButton.addEventListener('click', function() {
        tile1AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile1GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile1DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile1MidButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile1FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile1All.style.display = 'none';
        tile1Gkp.style.display = 'none';
        tile1Def.style.display = 'none';
        tile1Mid.style.display = 'block';
        tile1Fwd.style.display = 'none';
        scaleText();
    });

    // Show FWD
    tile1FwdButton.addEventListener('click', function() {
        tile1AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile1GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile1DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile1MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile1FwdButton.style.boxShadow = 'inset 0 -1px 0 #963cff';  
        tile1All.style.display = 'none';
        tile1Gkp.style.display = 'none';
        tile1Def.style.display = 'none';
        tile1Mid.style.display = 'none';
        tile1Fwd.style.display = 'block';
        scaleText();
    });
});

// TILE2

document.addEventListener('DOMContentLoaded', function() {

    const tile2AllButton = document.getElementById('tile2-all-button');
    const tile2GkpButton = document.getElementById('tile2-gkp-button');
    const tile2DefButton = document.getElementById('tile2-def-button');
    const tile2MidButton = document.getElementById('tile2-mid-button');
    const tile2FwdButton = document.getElementById('tile2-fwd-button');
    const tile2All = document.getElementById('tile2-all');
    const tile2Gkp = document.getElementById('tile2-gkp');
    const tile2Def = document.getElementById('tile2-def');
    const tile2Mid = document.getElementById('tile2-mid');
    const tile2Fwd = document.getElementById('tile2-fwd');

    // Show All
    tile2AllButton.addEventListener('click', function() {
        tile2AllButton.style.boxShadow = 'inset 0 -1px 0 #963cff';
        tile2GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile2DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile2MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile2FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile2All.style.display = 'block';
        tile2Gkp.style.display = 'none';
        tile2Def.style.display = 'none';
        tile2Mid.style.display = 'none';
        tile2Fwd.style.display = 'none';
    });

    // Show GKP
    tile2GkpButton.addEventListener('click', function() {
        tile2AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile2GkpButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile2DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile2MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile2FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile2All.style.display = 'none';
        tile2Gkp.style.display = 'block';
        tile2Def.style.display = 'none';
        tile2Mid.style.display = 'none';
        tile2Fwd.style.display = 'none';
        scaleText();
    });

    // Show DEF
    tile2DefButton.addEventListener('click', function() {
        tile2AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile2GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile2DefButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile2MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile2FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile2All.style.display = 'none';
        tile2Gkp.style.display = 'none';
        tile2Def.style.display = 'block';
        tile2Mid.style.display = 'none';
        tile2Fwd.style.display = 'none';
        scaleText();
    });

    // Show MID
    tile2MidButton.addEventListener('click', function() {
        tile2AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile2GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile2DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile2MidButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile2FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile2All.style.display = 'none';
        tile2Gkp.style.display = 'none';
        tile2Def.style.display = 'none';
        tile2Mid.style.display = 'block';
        tile2Fwd.style.display = 'none';
        scaleText();
    });

    // Show FWD
    tile2FwdButton.addEventListener('click', function() {
        tile2AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile2GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile2DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile2MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile2FwdButton.style.boxShadow = 'inset 0 -1px 0 #963cff';  
        tile2All.style.display = 'none';
        tile2Gkp.style.display = 'none';
        tile2Def.style.display = 'none';
        tile2Mid.style.display = 'none';
        tile2Fwd.style.display = 'block';
        scaleText();
    });
});

// TILE3

document.addEventListener('DOMContentLoaded', function() {

    const tile3AllButton = document.getElementById('tile3-all-button');
    const tile3GkpButton = document.getElementById('tile3-gkp-button');
    const tile3DefButton = document.getElementById('tile3-def-button');
    const tile3MidButton = document.getElementById('tile3-mid-button');
    const tile3FwdButton = document.getElementById('tile3-fwd-button');
    const tile3All = document.getElementById('tile3-all');
    const tile3Gkp = document.getElementById('tile3-gkp');
    const tile3Def = document.getElementById('tile3-def');
    const tile3Mid = document.getElementById('tile3-mid');
    const tile3Fwd = document.getElementById('tile3-fwd');

    // Show All
    tile3AllButton.addEventListener('click', function() {
        tile3AllButton.style.boxShadow = 'inset 0 -1px 0 #963cff';
        tile3GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile3DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile3MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile3FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile3All.style.display = 'block';
        tile3Gkp.style.display = 'none';
        tile3Def.style.display = 'none';
        tile3Mid.style.display = 'none';
        tile3Fwd.style.display = 'none';
    });

    // Show GKP
    tile3GkpButton.addEventListener('click', function() {
        tile3AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile3GkpButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile3DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile3MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile3FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile3All.style.display = 'none';
        tile3Gkp.style.display = 'block';
        tile3Def.style.display = 'none';
        tile3Mid.style.display = 'none';
        tile3Fwd.style.display = 'none';
        scaleText();
    });

    // Show DEF
    tile3DefButton.addEventListener('click', function() {
        tile3AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile3GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile3DefButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile3MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile3FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile3All.style.display = 'none';
        tile3Gkp.style.display = 'none';
        tile3Def.style.display = 'block';
        tile3Mid.style.display = 'none';
        tile3Fwd.style.display = 'none';
        scaleText();
    });

    // Show MID
    tile3MidButton.addEventListener('click', function() {
        tile3AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile3GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile3DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile3MidButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile3FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile3All.style.display = 'none';
        tile3Gkp.style.display = 'none';
        tile3Def.style.display = 'none';
        tile3Mid.style.display = 'block';
        tile3Fwd.style.display = 'none';
        scaleText();
    });

    // Show FWD
    tile3FwdButton.addEventListener('click', function() {
        tile3AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile3GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile3DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile3MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile3FwdButton.style.boxShadow = 'inset 0 -1px 0 #963cff';  
        tile3All.style.display = 'none';
        tile3Gkp.style.display = 'none';
        tile3Def.style.display = 'none';
        tile3Mid.style.display = 'none';
        tile3Fwd.style.display = 'block';
        scaleText();
    });
});

// TILE4

document.addEventListener('DOMContentLoaded', function() {

    const tile4AllButton = document.getElementById('tile4-all-button');
    const tile4GkpButton = document.getElementById('tile4-gkp-button');
    const tile4DefButton = document.getElementById('tile4-def-button');
    const tile4MidButton = document.getElementById('tile4-mid-button');
    const tile4FwdButton = document.getElementById('tile4-fwd-button');
    const tile4All = document.getElementById('tile4-all');
    const tile4Gkp = document.getElementById('tile4-gkp');
    const tile4Def = document.getElementById('tile4-def');
    const tile4Mid = document.getElementById('tile4-mid');
    const tile4Fwd = document.getElementById('tile4-fwd');

    // Show All
    tile4AllButton.addEventListener('click', function() {
        tile4AllButton.style.boxShadow = 'inset 0 -1px 0 #963cff';
        tile4GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile4DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile4MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile4FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile4All.style.display = 'block';
        tile4Gkp.style.display = 'none';
        tile4Def.style.display = 'none';
        tile4Mid.style.display = 'none';
        tile4Fwd.style.display = 'none';
    });

    // Show GKP
    tile4GkpButton.addEventListener('click', function() {
        tile4AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile4GkpButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile4DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile4MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile4FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile4All.style.display = 'none';
        tile4Gkp.style.display = 'block';
        tile4Def.style.display = 'none';
        tile4Mid.style.display = 'none';
        tile4Fwd.style.display = 'none';
        scaleText();
    });

    // Show DEF
    tile4DefButton.addEventListener('click', function() {
        tile4AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile4GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile4DefButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile4MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile4FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile4All.style.display = 'none';
        tile4Gkp.style.display = 'none';
        tile4Def.style.display = 'block';
        tile4Mid.style.display = 'none';
        tile4Fwd.style.display = 'none';
        scaleText();
    });

    // Show MID
    tile4MidButton.addEventListener('click', function() {
        tile4AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile4GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile4DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile4MidButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile4FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile4All.style.display = 'none';
        tile4Gkp.style.display = 'none';
        tile4Def.style.display = 'none';
        tile4Mid.style.display = 'block';
        tile4Fwd.style.display = 'none';
        scaleText();
    });

    // Show FWD
    tile4FwdButton.addEventListener('click', function() {
        tile4AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile4GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile4DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile4MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile4FwdButton.style.boxShadow = 'inset 0 -1px 0 #963cff';  
        tile4All.style.display = 'none';
        tile4Gkp.style.display = 'none';
        tile4Def.style.display = 'none';
        tile4Mid.style.display = 'none';
        tile4Fwd.style.display = 'block';
        scaleText();
    });
});

// TILE5

document.addEventListener('DOMContentLoaded', function() {

    const tile5AllButton = document.getElementById('tile5-all-button');
    const tile5GkpButton = document.getElementById('tile5-gkp-button');
    const tile5DefButton = document.getElementById('tile5-def-button');
    const tile5MidButton = document.getElementById('tile5-mid-button');
    const tile5FwdButton = document.getElementById('tile5-fwd-button');
    const tile5All = document.getElementById('tile5-all');
    const tile5Gkp = document.getElementById('tile5-gkp');
    const tile5Def = document.getElementById('tile5-def');
    const tile5Mid = document.getElementById('tile5-mid');
    const tile5Fwd = document.getElementById('tile5-fwd');

    // Show All
    tile5AllButton.addEventListener('click', function() {
        tile5AllButton.style.boxShadow = 'inset 0 -1px 0 #963cff';
        tile5GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile5DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile5MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile5FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile5All.style.display = 'block';
        tile5Gkp.style.display = 'none';
        tile5Def.style.display = 'none';
        tile5Mid.style.display = 'none';
        tile5Fwd.style.display = 'none';
    });

    // Show GKP
    tile5GkpButton.addEventListener('click', function() {
        tile5AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile5GkpButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile5DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile5MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile5FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile5All.style.display = 'none';
        tile5Gkp.style.display = 'block';
        tile5Def.style.display = 'none';
        tile5Mid.style.display = 'none';
        tile5Fwd.style.display = 'none';
        scaleText();
    });

    // Show DEF
    tile5DefButton.addEventListener('click', function() {
        tile5AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile5GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile5DefButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile5MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile5FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile5All.style.display = 'none';
        tile5Gkp.style.display = 'none';
        tile5Def.style.display = 'block';
        tile5Mid.style.display = 'none';
        tile5Fwd.style.display = 'none';
        scaleText();
    });

    // Show MID
    tile5MidButton.addEventListener('click', function() {
        tile5AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile5GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile5DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile5MidButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile5FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile5All.style.display = 'none';
        tile5Gkp.style.display = 'none';
        tile5Def.style.display = 'none';
        tile5Mid.style.display = 'block';
        tile5Fwd.style.display = 'none';
        scaleText();
    });

    // Show FWD
    tile5FwdButton.addEventListener('click', function() {
        tile5AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile5GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile5DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile5MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile5FwdButton.style.boxShadow = 'inset 0 -1px 0 #963cff';  
        tile5All.style.display = 'none';
        tile5Gkp.style.display = 'none';
        tile5Def.style.display = 'none';
        tile5Mid.style.display = 'none';
        tile5Fwd.style.display = 'block';
        scaleText();
    });
});

// TILE6

document.addEventListener('DOMContentLoaded', function() {

    const tile6AllButton = document.getElementById('tile6-all-button');
    const tile6GkpButton = document.getElementById('tile6-gkp-button');
    const tile6DefButton = document.getElementById('tile6-def-button');
    const tile6MidButton = document.getElementById('tile6-mid-button');
    const tile6FwdButton = document.getElementById('tile6-fwd-button');
    const tile6All = document.getElementById('tile6-all');
    const tile6Gkp = document.getElementById('tile6-gkp');
    const tile6Def = document.getElementById('tile6-def');
    const tile6Mid = document.getElementById('tile6-mid');
    const tile6Fwd = document.getElementById('tile6-fwd');

    // Show All
    tile6AllButton.addEventListener('click', function() {
        tile6AllButton.style.boxShadow = 'inset 0 -1px 0 #963cff';
        tile6GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile6DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile6MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile6FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile6All.style.display = 'block';
        tile6Gkp.style.display = 'none';
        tile6Def.style.display = 'none';
        tile6Mid.style.display = 'none';
        tile6Fwd.style.display = 'none';
    });

    // Show GKP
    tile6GkpButton.addEventListener('click', function() {
        tile6AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile6GkpButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile6DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile6MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile6FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile6All.style.display = 'none';
        tile6Gkp.style.display = 'block';
        tile6Def.style.display = 'none';
        tile6Mid.style.display = 'none';
        tile6Fwd.style.display = 'none';
        scaleText();
    });

    // Show DEF
    tile6DefButton.addEventListener('click', function() {
        tile6AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile6GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile6DefButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile6MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile6FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile6All.style.display = 'none';
        tile6Gkp.style.display = 'none';
        tile6Def.style.display = 'block';
        tile6Mid.style.display = 'none';
        tile6Fwd.style.display = 'none';
        scaleText();
    });

    // Show MID
    tile6MidButton.addEventListener('click', function() {
        tile6AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile6GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile6DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile6MidButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile6FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile6All.style.display = 'none';
        tile6Gkp.style.display = 'none';
        tile6Def.style.display = 'none';
        tile6Mid.style.display = 'block';
        tile6Fwd.style.display = 'none';
        scaleText();
    });

    // Show FWD
    tile6FwdButton.addEventListener('click', function() {
        tile6AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile6GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile6DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile6MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile6FwdButton.style.boxShadow = 'inset 0 -1px 0 #963cff';  
        tile6All.style.display = 'none';
        tile6Gkp.style.display = 'none';
        tile6Def.style.display = 'none';
        tile6Mid.style.display = 'none';
        tile6Fwd.style.display = 'block';
        scaleText();
    });
});

// TILE7

document.addEventListener('DOMContentLoaded', function() {

    const tile7AllButton = document.getElementById('tile7-all-button');
    const tile7GkpButton = document.getElementById('tile7-gkp-button');
    const tile7DefButton = document.getElementById('tile7-def-button');
    const tile7MidButton = document.getElementById('tile7-mid-button');
    const tile7FwdButton = document.getElementById('tile7-fwd-button');
    const tile7All = document.getElementById('tile7-all');
    const tile7Gkp = document.getElementById('tile7-gkp');
    const tile7Def = document.getElementById('tile7-def');
    const tile7Mid = document.getElementById('tile7-mid');
    const tile7Fwd = document.getElementById('tile7-fwd');

    // Show All
    tile7AllButton.addEventListener('click', function() {
        tile7AllButton.style.boxShadow = 'inset 0 -1px 0 #963cff';
        tile7GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile7DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile7MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile7FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile7All.style.display = 'block';
        tile7Gkp.style.display = 'none';
        tile7Def.style.display = 'none';
        tile7Mid.style.display = 'none';
        tile7Fwd.style.display = 'none';
    });

    // Show GKP
    tile7GkpButton.addEventListener('click', function() {
        tile7AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile7GkpButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile7DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile7MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile7FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile7All.style.display = 'none';
        tile7Gkp.style.display = 'block';
        tile7Def.style.display = 'none';
        tile7Mid.style.display = 'none';
        tile7Fwd.style.display = 'none';
        scaleText();
    });

    // Show DEF
    tile7DefButton.addEventListener('click', function() {
        tile7AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile7GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile7DefButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile7MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile7FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile7All.style.display = 'none';
        tile7Gkp.style.display = 'none';
        tile7Def.style.display = 'block';
        tile7Mid.style.display = 'none';
        tile7Fwd.style.display = 'none';
        scaleText();
    });

    // Show MID
    tile7MidButton.addEventListener('click', function() {
        tile7AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile7GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile7DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile7MidButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile7FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile7All.style.display = 'none';
        tile7Gkp.style.display = 'none';
        tile7Def.style.display = 'none';
        tile7Mid.style.display = 'block';
        tile7Fwd.style.display = 'none';
        scaleText();
    });

    // Show FWD
    tile7FwdButton.addEventListener('click', function() {
        tile7AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile7GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile7DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile7MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile7FwdButton.style.boxShadow = 'inset 0 -1px 0 #963cff';  
        tile7All.style.display = 'none';
        tile7Gkp.style.display = 'none';
        tile7Def.style.display = 'none';
        tile7Mid.style.display = 'none';
        tile7Fwd.style.display = 'block';
        scaleText();
    });
});

// TILE8

document.addEventListener('DOMContentLoaded', function() {

    const tile8AllButton = document.getElementById('tile8-all-button');
    const tile8GkpButton = document.getElementById('tile8-gkp-button');
    const tile8DefButton = document.getElementById('tile8-def-button');
    const tile8MidButton = document.getElementById('tile8-mid-button');
    const tile8FwdButton = document.getElementById('tile8-fwd-button');
    const tile8All = document.getElementById('tile8-all');
    const tile8Gkp = document.getElementById('tile8-gkp');
    const tile8Def = document.getElementById('tile8-def');
    const tile8Mid = document.getElementById('tile8-mid');
    const tile8Fwd = document.getElementById('tile8-fwd');

    // Show All
    tile8AllButton.addEventListener('click', function() {
        tile8AllButton.style.boxShadow = 'inset 0 -1px 0 #963cff';
        tile8GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile8DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile8MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile8FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile8All.style.display = 'block';
        tile8Gkp.style.display = 'none';
        tile8Def.style.display = 'none';
        tile8Mid.style.display = 'none';
        tile8Fwd.style.display = 'none';
    });

    // Show GKP
    tile8GkpButton.addEventListener('click', function() {
        tile8AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile8GkpButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile8DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile8MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile8FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile8All.style.display = 'none';
        tile8Gkp.style.display = 'block';
        tile8Def.style.display = 'none';
        tile8Mid.style.display = 'none';
        tile8Fwd.style.display = 'none';
        scaleText();
    });

    // Show DEF
    tile8DefButton.addEventListener('click', function() {
        tile8AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile8GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile8DefButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile8MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile8FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile8All.style.display = 'none';
        tile8Gkp.style.display = 'none';
        tile8Def.style.display = 'block';
        tile8Mid.style.display = 'none';
        tile8Fwd.style.display = 'none';
        scaleText();
    });

    // Show MID
    tile8MidButton.addEventListener('click', function() {
        tile8AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile8GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile8DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile8MidButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile8FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile8All.style.display = 'none';
        tile8Gkp.style.display = 'none';
        tile8Def.style.display = 'none';
        tile8Mid.style.display = 'block';
        tile8Fwd.style.display = 'none';
        scaleText();
    });

    // Show FWD
    tile8FwdButton.addEventListener('click', function() {
        tile8AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile8GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile8DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile8MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile8FwdButton.style.boxShadow = 'inset 0 -1px 0 #963cff';  
        tile8All.style.display = 'none';
        tile8Gkp.style.display = 'none';
        tile8Def.style.display = 'none';
        tile8Mid.style.display = 'none';
        tile8Fwd.style.display = 'block';
        scaleText();
    });
});

// TILE9

document.addEventListener('DOMContentLoaded', function() {

    const tile9AllButton = document.getElementById('tile9-all-button');
    const tile9GkpButton = document.getElementById('tile9-gkp-button');
    const tile9DefButton = document.getElementById('tile9-def-button');
    const tile9MidButton = document.getElementById('tile9-mid-button');
    const tile9FwdButton = document.getElementById('tile9-fwd-button');
    const tile9All = document.getElementById('tile9-all');
    const tile9Gkp = document.getElementById('tile9-gkp');
    const tile9Def = document.getElementById('tile9-def');
    const tile9Mid = document.getElementById('tile9-mid');
    const tile9Fwd = document.getElementById('tile9-fwd');

    // Show All
    tile9AllButton.addEventListener('click', function() {
        tile9AllButton.style.boxShadow = 'inset 0 -1px 0 #963cff';
        tile9GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile9DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile9MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile9FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile9All.style.display = 'block';
        tile9Gkp.style.display = 'none';
        tile9Def.style.display = 'none';
        tile9Mid.style.display = 'none';
        tile9Fwd.style.display = 'none';
    });

    // Show GKP
    tile9GkpButton.addEventListener('click', function() {
        tile9AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile9GkpButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile9DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile9MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile9FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile9All.style.display = 'none';
        tile9Gkp.style.display = 'block';
        tile9Def.style.display = 'none';
        tile9Mid.style.display = 'none';
        tile9Fwd.style.display = 'none';
        scaleText();
    });

    // Show DEF
    tile9DefButton.addEventListener('click', function() {
        tile9AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile9GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile9DefButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile9MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile9FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile9All.style.display = 'none';
        tile9Gkp.style.display = 'none';
        tile9Def.style.display = 'block';
        tile9Mid.style.display = 'none';
        tile9Fwd.style.display = 'none';
        scaleText();
    });

    // Show MID
    tile9MidButton.addEventListener('click', function() {
        tile9AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile9GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile9DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile9MidButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile9FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile9All.style.display = 'none';
        tile9Gkp.style.display = 'none';
        tile9Def.style.display = 'none';
        tile9Mid.style.display = 'block';
        tile9Fwd.style.display = 'none';
        scaleText();
    });

    // Show FWD
    tile9FwdButton.addEventListener('click', function() {
        tile9AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile9GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile9DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile9MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile9FwdButton.style.boxShadow = 'inset 0 -1px 0 #963cff';  
        tile9All.style.display = 'none';
        tile9Gkp.style.display = 'none';
        tile9Def.style.display = 'none';
        tile9Mid.style.display = 'none';
        tile9Fwd.style.display = 'block';
        scaleText();
    });
});

// TILE10

document.addEventListener('DOMContentLoaded', function() {

    const tile10AllButton = document.getElementById('tile10-all-button');
    const tile10GkpButton = document.getElementById('tile10-gkp-button');
    const tile10DefButton = document.getElementById('tile10-def-button');
    const tile10MidButton = document.getElementById('tile10-mid-button');
    const tile10FwdButton = document.getElementById('tile10-fwd-button');
    const tile10All = document.getElementById('tile10-all');
    const tile10Gkp = document.getElementById('tile10-gkp');
    const tile10Def = document.getElementById('tile10-def');
    const tile10Mid = document.getElementById('tile10-mid');
    const tile10Fwd = document.getElementById('tile10-fwd');

    // Show All
    tile10AllButton.addEventListener('click', function() {
        tile10AllButton.style.boxShadow = 'inset 0 -1px 0 #963cff';
        tile10GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile10DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile10MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile10FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile10All.style.display = 'block';
        tile10Gkp.style.display = 'none';
        tile10Def.style.display = 'none';
        tile10Mid.style.display = 'none';
        tile10Fwd.style.display = 'none';
    });

    // Show GKP
    tile10GkpButton.addEventListener('click', function() {
        tile10AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile10GkpButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile10DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile10MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile10FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile10All.style.display = 'none';
        tile10Gkp.style.display = 'block';
        tile10Def.style.display = 'none';
        tile10Mid.style.display = 'none';
        tile10Fwd.style.display = 'none';
        scaleText();
    });

    // Show DEF
    tile10DefButton.addEventListener('click', function() {
        tile10AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile10GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile10DefButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile10MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile10FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile10All.style.display = 'none';
        tile10Gkp.style.display = 'none';
        tile10Def.style.display = 'block';
        tile10Mid.style.display = 'none';
        tile10Fwd.style.display = 'none';
        scaleText();
    });

    // Show MID
    tile10MidButton.addEventListener('click', function() {
        tile10AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile10GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile10DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile10MidButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile10FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile10All.style.display = 'none';
        tile10Gkp.style.display = 'none';
        tile10Def.style.display = 'none';
        tile10Mid.style.display = 'block';
        tile10Fwd.style.display = 'none';
        scaleText();
    });

    // Show FWD
    tile10FwdButton.addEventListener('click', function() {
        tile10AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile10GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile10DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile10MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile10FwdButton.style.boxShadow = 'inset 0 -1px 0 #963cff';  
        tile10All.style.display = 'none';
        tile10Gkp.style.display = 'none';
        tile10Def.style.display = 'none';
        tile10Mid.style.display = 'none';
        tile10Fwd.style.display = 'block';
        scaleText();
    });
});

// TILE11

document.addEventListener('DOMContentLoaded', function() {

    const tile11AllButton = document.getElementById('tile11-all-button');
    const tile11GkpButton = document.getElementById('tile11-gkp-button');
    const tile11DefButton = document.getElementById('tile11-def-button');
    const tile11MidButton = document.getElementById('tile11-mid-button');
    const tile11FwdButton = document.getElementById('tile11-fwd-button');
    const tile11All = document.getElementById('tile11-all');
    const tile11Gkp = document.getElementById('tile11-gkp');
    const tile11Def = document.getElementById('tile11-def');
    const tile11Mid = document.getElementById('tile11-mid');
    const tile11Fwd = document.getElementById('tile11-fwd');

    // Show All
    tile11AllButton.addEventListener('click', function() {
        tile11AllButton.style.boxShadow = 'inset 0 -1px 0 #963cff';
        tile11GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile11DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile11MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile11FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile11All.style.display = 'block';
        tile11Gkp.style.display = 'none';
        tile11Def.style.display = 'none';
        tile11Mid.style.display = 'none';
        tile11Fwd.style.display = 'none';
    });

    // Show GKP
    tile11GkpButton.addEventListener('click', function() {
        tile11AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile11GkpButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile11DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile11MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile11FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile11All.style.display = 'none';
        tile11Gkp.style.display = 'block';
        tile11Def.style.display = 'none';
        tile11Mid.style.display = 'none';
        tile11Fwd.style.display = 'none';
        scaleText();
    });

    // Show DEF
    tile11DefButton.addEventListener('click', function() {
        tile11AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile11GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile11DefButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile11MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile11FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile11All.style.display = 'none';
        tile11Gkp.style.display = 'none';
        tile11Def.style.display = 'block';
        tile11Mid.style.display = 'none';
        tile11Fwd.style.display = 'none';
        scaleText();
    });

    // Show MID
    tile11MidButton.addEventListener('click', function() {
        tile11AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile11GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile11DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile11MidButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        tile11FwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        tile11All.style.display = 'none';
        tile11Gkp.style.display = 'none';
        tile11Def.style.display = 'none';
        tile11Mid.style.display = 'block';
        tile11Fwd.style.display = 'none';
        scaleText();
    });

    // Show FWD
    tile11FwdButton.addEventListener('click', function() {
        tile11AllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        tile11GkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile11DefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile11MidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        tile11FwdButton.style.boxShadow = 'inset 0 -1px 0 #963cff';  
        tile11All.style.display = 'none';
        tile11Gkp.style.display = 'none';
        tile11Def.style.display = 'none';
        tile11Mid.style.display = 'none';
        tile11Fwd.style.display = 'block';
        scaleText();
    });
});
