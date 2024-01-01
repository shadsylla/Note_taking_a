function slopeOfTangentLine(curve, point) {
    // Calculate the slope of the tangent line using the derivative of the curve function
    const dx = 0.0001; // A small change in x
    const x1 = point.x - dx;
    const y1 = curve(x1);
    const x2 = point.x + dx;
    const y2 = curve(x2);
    const slope = (y2 - y1) / (x2 - x1);
    
    return slope;
}
//<!-- Add this canvas element to your HTML file -->
<canvas id="myCanvas"></canvas>

//<!-- Add this script to your JavaScript file -->
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

function renderCurve(curve) {
    // Set the canvas size
    canvas.width = 500;
    canvas.height = 500;

    // Draw the curve
    ctx.beginPath();
    ctx.moveTo(0, curve(0));
    for (let x = 0; x <= canvas.width; x++) {
        const y = curve(x);
        ctx.lineTo(x, y);
    }
    ctx.stroke();
}

// Call the renderCurve function with your curve function as an argument
renderCurve(myCurveFunction);
