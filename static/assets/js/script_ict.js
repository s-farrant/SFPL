// INFLUENCE

document.addEventListener('DOMContentLoaded', function() {

    const influenceAllButton = document.getElementById('influence-all-button');
    const influenceGkpButton = document.getElementById('influence-gkp-button');
    const influenceDefButton = document.getElementById('influence-def-button');
    const influenceMidButton = document.getElementById('influence-mid-button');
    const influenceFwdButton = document.getElementById('influence-fwd-button');
    const influenceAll = document.getElementById('influence-all');
    const influenceGkp = document.getElementById('influence-gkp');
    const influenceDef = document.getElementById('influence-def');
    const influenceMid = document.getElementById('influence-mid');
    const influenceFwd = document.getElementById('influence-fwd');

    // Show All
    influenceAllButton.addEventListener('click', function() {
        influenceAllButton.style.boxShadow = 'inset 0 -1px 0 #963cff';
        influenceGkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        influenceDefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        influenceMidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        influenceFwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        influenceAll.style.display = 'block';
        influenceGkp.style.display = 'none';
        influenceDef.style.display = 'none';
        influenceMid.style.display = 'none';
        influenceFwd.style.display = 'none';
        scaleText();
    });

    // Show GKP
    influenceGkpButton.addEventListener('click', function() {
        influenceAllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        influenceGkpButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        influenceDefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        influenceMidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        influenceFwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        influenceAll.style.display = 'none';
        influenceGkp.style.display = 'block';
        influenceDef.style.display = 'none';
        influenceMid.style.display = 'none';
        influenceFwd.style.display = 'none';
        scaleText();
    });

    // Show DEF
    influenceDefButton.addEventListener('click', function() {
        influenceAllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        influenceGkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        influenceDefButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        influenceMidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        influenceFwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        influenceAll.style.display = 'none';
        influenceGkp.style.display = 'none';
        influenceDef.style.display = 'block';
        influenceMid.style.display = 'none';
        influenceFwd.style.display = 'none';
        scaleText();
    });

    // Show MID
    influenceMidButton.addEventListener('click', function() {
        influenceAllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        influenceGkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        influenceDefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        influenceMidButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        influenceFwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        influenceAll.style.display = 'none';
        influenceGkp.style.display = 'none';
        influenceDef.style.display = 'none';
        influenceMid.style.display = 'block';
        influenceFwd.style.display = 'none';
        scaleText();
    });

    // Show FWD
    influenceFwdButton.addEventListener('click', function() {
        influenceAllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        influenceGkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        influenceDefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        influenceMidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        influenceFwdButton.style.boxShadow = 'inset 0 -1px 0 #963cff';  
        influenceAll.style.display = 'none';
        influenceGkp.style.display = 'none';
        influenceDef.style.display = 'none';
        influenceMid.style.display = 'none';
        influenceFwd.style.display = 'block';
        scaleText();
    });
});

// CREATIVITY

document.addEventListener('DOMContentLoaded', function() {

    const creativityAllButton = document.getElementById('creativity-all-button');
    const creativityGkpButton = document.getElementById('creativity-gkp-button');
    const creativityDefButton = document.getElementById('creativity-def-button');
    const creativityMidButton = document.getElementById('creativity-mid-button');
    const creativityFwdButton = document.getElementById('creativity-fwd-button');
    const creativityAll = document.getElementById('creativity-all');
    const creativityGkp = document.getElementById('creativity-gkp');
    const creativityDef = document.getElementById('creativity-def');
    const creativityMid = document.getElementById('creativity-mid');
    const creativityFwd = document.getElementById('creativity-fwd');

    // Show All
    creativityAllButton.addEventListener('click', function() {
        creativityAllButton.style.boxShadow = 'inset 0 -1px 0 #963cff';
        creativityGkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        creativityDefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        creativityMidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        creativityFwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        creativityAll.style.display = 'block';
        creativityGkp.style.display = 'none';
        creativityDef.style.display = 'none';
        creativityMid.style.display = 'none';
        creativityFwd.style.display = 'none';
    });

    // Show GKP
    creativityGkpButton.addEventListener('click', function() {
        creativityAllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        creativityGkpButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        creativityDefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        creativityMidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        creativityFwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        creativityAll.style.display = 'none';
        creativityGkp.style.display = 'block';
        creativityDef.style.display = 'none';
        creativityMid.style.display = 'none';
        creativityFwd.style.display = 'none';
        scaleText();
    });

    // Show DEF
    creativityDefButton.addEventListener('click', function() {
        creativityAllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        creativityGkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        creativityDefButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        creativityMidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        creativityFwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        creativityAll.style.display = 'none';
        creativityGkp.style.display = 'none';
        creativityDef.style.display = 'block';
        creativityMid.style.display = 'none';
        creativityFwd.style.display = 'none';
        scaleText();
    });

    // Show MID
    creativityMidButton.addEventListener('click', function() {
        creativityAllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        creativityGkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        creativityDefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        creativityMidButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        creativityFwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        creativityAll.style.display = 'none';
        creativityGkp.style.display = 'none';
        creativityDef.style.display = 'none';
        creativityMid.style.display = 'block';
        creativityFwd.style.display = 'none';
        scaleText();
    });

    // Show FWD
    creativityFwdButton.addEventListener('click', function() {
        creativityAllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        creativityGkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        creativityDefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        creativityMidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        creativityFwdButton.style.boxShadow = 'inset 0 -1px 0 #963cff';  
        creativityAll.style.display = 'none';
        creativityGkp.style.display = 'none';
        creativityDef.style.display = 'none';
        creativityMid.style.display = 'none';
        creativityFwd.style.display = 'block';
        scaleText();
    });
});

// THREAT

document.addEventListener('DOMContentLoaded', function() {

    const threatAllButton = document.getElementById('threat-all-button');
    const threatGkpButton = document.getElementById('threat-gkp-button');
    const threatDefButton = document.getElementById('threat-def-button');
    const threatMidButton = document.getElementById('threat-mid-button');
    const threatFwdButton = document.getElementById('threat-fwd-button');
    const threatAll = document.getElementById('threat-all');
    const threatGkp = document.getElementById('threat-gkp');
    const threatDef = document.getElementById('threat-def');
    const threatMid = document.getElementById('threat-mid');
    const threatFwd = document.getElementById('threat-fwd');

    // Show All
    threatAllButton.addEventListener('click', function() {
        threatAllButton.style.boxShadow = 'inset 0 -1px 0 #963cff';
        threatGkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        threatDefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        threatMidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        threatFwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        threatAll.style.display = 'block';
        threatGkp.style.display = 'none';
        threatDef.style.display = 'none';
        threatMid.style.display = 'none';
        threatFwd.style.display = 'none';
    });

    // Show GKP
    threatGkpButton.addEventListener('click', function() {
        threatAllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        threatGkpButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        threatDefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        threatMidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        threatFwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        threatAll.style.display = 'none';
        threatGkp.style.display = 'block';
        threatDef.style.display = 'none';
        threatMid.style.display = 'none';
        threatFwd.style.display = 'none';
        scaleText();
    });

    // Show DEF
    threatDefButton.addEventListener('click', function() {
        threatAllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        threatGkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        threatDefButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        threatMidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        threatFwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        threatAll.style.display = 'none';
        threatGkp.style.display = 'none';
        threatDef.style.display = 'block';
        threatMid.style.display = 'none';
        threatFwd.style.display = 'none';
        scaleText();
    });

    // Show MID
    threatMidButton.addEventListener('click', function() {
        threatAllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        threatGkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        threatDefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        threatMidButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        threatFwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        threatAll.style.display = 'none';
        threatGkp.style.display = 'none';
        threatDef.style.display = 'none';
        threatMid.style.display = 'block';
        threatFwd.style.display = 'none';
        scaleText();
    });

    // Show FWD
    threatFwdButton.addEventListener('click', function() {
        threatAllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        threatGkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        threatDefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        threatMidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        threatFwdButton.style.boxShadow = 'inset 0 -1px 0 #963cff';  
        threatAll.style.display = 'none';
        threatGkp.style.display = 'none';
        threatDef.style.display = 'none';
        threatMid.style.display = 'none';
        threatFwd.style.display = 'block';
        scaleText();
    });
});

// ICT

document.addEventListener('DOMContentLoaded', function() {

    const ictAllButton = document.getElementById('ict-all-button');
    const ictGkpButton = document.getElementById('ict-gkp-button');
    const ictDefButton = document.getElementById('ict-def-button');
    const ictMidButton = document.getElementById('ict-mid-button');
    const ictFwdButton = document.getElementById('ict-fwd-button');
    const ictAll = document.getElementById('ict-all');
    const ictGkp = document.getElementById('ict-gkp');
    const ictDef = document.getElementById('ict-def');
    const ictMid = document.getElementById('ict-mid');
    const ictFwd = document.getElementById('ict-fwd');

    // Show All
    ictAllButton.addEventListener('click', function() {
        ictAllButton.style.boxShadow = 'inset 0 -1px 0 #963cff';
        ictGkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        ictDefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        ictMidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        ictFwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        ictAll.style.display = 'block';
        ictGkp.style.display = 'none';
        ictDef.style.display = 'none';
        ictMid.style.display = 'none';
        ictFwd.style.display = 'none';
    });

    // Show GKP
    ictGkpButton.addEventListener('click', function() {
        ictAllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        ictGkpButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        ictDefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        ictMidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        ictFwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        ictAll.style.display = 'none';
        ictGkp.style.display = 'block';
        ictDef.style.display = 'none';
        ictMid.style.display = 'none';
        ictFwd.style.display = 'none';
        scaleText();
    });

    // Show DEF
    ictDefButton.addEventListener('click', function() {
        ictAllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        ictGkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        ictDefButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        ictMidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        ictFwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        ictAll.style.display = 'none';
        ictGkp.style.display = 'none';
        ictDef.style.display = 'block';
        ictMid.style.display = 'none';
        ictFwd.style.display = 'none';
        scaleText();
    });

    // Show MID
    ictMidButton.addEventListener('click', function() {
        ictAllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        ictGkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        ictDefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        ictMidButton.style.boxShadow = 'inset 0 -1px 0 #963cff'; 
        ictFwdButton.style.boxShadow = 'inset 0 -0px 0 #963cff';  
        ictAll.style.display = 'none';
        ictGkp.style.display = 'none';
        ictDef.style.display = 'none';
        ictMid.style.display = 'block';
        ictFwd.style.display = 'none';
        scaleText();
    });

    // Show FWD
    ictFwdButton.addEventListener('click', function() {
        ictAllButton.style.boxShadow = 'inset 0 -0px 0 #963cff';
        ictGkpButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        ictDefButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        ictMidButton.style.boxShadow = 'inset 0 -0px 0 #963cff'; 
        ictFwdButton.style.boxShadow = 'inset 0 -1px 0 #963cff';  
        ictAll.style.display = 'none';
        ictGkp.style.display = 'none';
        ictDef.style.display = 'none';
        ictMid.style.display = 'none';
        ictFwd.style.display = 'block';
        scaleText();
    });
});


