//dirty fucking code, gonna do better next time

var Line = function(points){
    var len = points.length;
    this.get = function(t){
        var rate = len*t;
        var idx = Math.floor(rate);
        var r = rate - idx;
        //ok, now interpolate between idx and idx + 1
        //linear interpolation for now because bicubic is annoying
        return [
            points[idx][0]*(1-r)+points[(idx+1)%len][0]*r,
            points[idx][1]*(1-r)+points[(idx+1)%len][1]*r
        ];
    }
};

var complexMul = function(c1,c2){
    return [c1[0]*c2[0]-c1[1]*c2[1], c1[0]*c2[1]+c1[1]*c2[0]];
};

var complexToExponential = function(c){//converts complex numbers into exponential form
    var magn = Math.sqrt(c[0]*c[0]+c[1]*c[1]);
    var angle = Math.atan2(c[1],c[0]);//y,x
    return [magn,angle];
};

var complexEqual = function(c1,c2){
    if(c1[0] === c2[0] && c1[1] === c2[1]){
        return true;
    }
    return false;
};

var colorOpacity = function(hex,o){
    if(hex.length === 4){
        return hex+(Math.floor(o*15)).toString(16);
    }else if(hex.length === 7){
        return hex+(Math.floor(o*255)).toString(16);
    }else{
        throw new Error("unsupported color type");
    }
}


var generateFourier = function(points,degree){
    //now interpolate the points
    var line = new Line(points);
    var ds = -degree;
    var de = degree;
    //steps is the steps for the number of numerical integration
    var steps = 1000;
    var cs = [];
    
    for(var n = ds; n < de+1; n++){//positive and negative, nicely symmetrical
        var csum = [0,0];//complex sum of the steps
        for(var j = 0; j < steps; j++){
            var t = j/steps;
            var coeffAngle = -2*n*t*Math.PI;//not gonna derive pi this time lol
            var coefficient = [Math.cos(coeffAngle),Math.sin(coeffAngle)];
            var lt = line.get(t);
            //then now multiply lt with coefficent, and then add to the summation
            var muled = complexMul(coefficient,lt);
            //then now incrementing the csum
            csum[0] += muled[0];
            csum[1] += muled[1];
        }
        var cn = [csum[0]/steps,csum[1]/steps];
        cs[n-ds] = complexToExponential(cn);
    }
    return cs;
};



var canvas = document.getElementById("canvas");
var width = window.innerWidth;
var height = window.innerHeight;
canvas.width = width;
canvas.height = height;
var ctx = canvas.getContext("2d");
ctx.fillStyle = "#002";
ctx.fillRect(0,0,width,height);


var drawPoints = function(points,color,targetLen){
    for(var i = 0; i < points.length-1; i++){
        ctx.beginPath();
        ctx.moveTo(points[i][0],points[i][1]);
        ctx.lineTo(points[i+1][0],points[i+1][1]);
        ctx.strokeStyle = colorOpacity(color,(targetLen-(points.length-i)*0.8)/targetLen);
        ctx.stroke();
    }
};

var drawPointsClose = function(points,color){
    ctx.beginPath();
    for(var i = 0; i < points.length; i++){
        ctx.lineTo(points[i][0],points[i][1]);
    }
    ctx.closePath();
    ctx.strokeStyle = color;
    ctx.stroke();
};

var drawTerm = function(term,position,degree,t){//side effect: changes the position
    var r = term[0];
    var phase = term[1];
    //console.log(degree);
    var dx = r*Math.cos(phase+degree*2*Math.PI*t);//tau will make this so much simpler. tau >> pi
    var dy = r*Math.sin(phase+degree*2*Math.PI*t);
    var x = position[0];
    var y = position[1];
    ctx.beginPath();
    ctx.arc(x,y,r,0,6.28);
    ctx.closePath();
    ctx.strokeStyle = "#88f";
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x,y);
    ctx.lineTo(x+dx,y+dy);
    ctx.strokeStyle = "#f88";
    ctx.stroke();//now one iteration ready!!
    position[0] += dx;
    position[1] += dy;
};

var rp;

var truncateTrail = function(trail,n){
    var len = trail.length;
    if(len <= n)return false;
    for(var i = 0; i < n; i++){
        trail[i] = trail[i+(len-n)];
    }
    trail.length = n;
    //truncating
    //wish I had access to linked list in js. Array sucks as queue or something
};

var main = function(){
    var points = [];
    
    var down = false;
    
    
    var handleMouseMove = function(e){
        e.preventDefault();
        //register the mouse movement and draw stuff on the screen
        if(!down)return false;
        points.push([e.clientX+window.scrollX-this.offsetLeft,e.clientY+window.scrollY+this.offsetTop]);
        var current = points.pop();
        var last = points.pop();
        if(complexEqual(current,last)){
            points.push(last);
        }else{
            points.push(last);
            points.push(current);
        }
        ctx.fillStyle = "#002";
        ctx.clearRect(0,0,width,height);
        ctx.fillRect(0,0,width,height);
        drawPointsClose(points,"#4f4");
    };
    
    var handleMouseDown = function(e){
        e.preventDefault();
        down = true;
        points.push([e.clientX+window.scrollX-this.offsetLeft,e.clientY+window.scrollY+this.offsetTop]);
    };
    
    var handleMouseUp = function(e){
        e.preventDefault();
        if(!down)return false;
        down = false;
        document.body.removeEventListener("mousemove",handleMouseMove);
        document.body.removeEventListener("mousedown",handleMouseDown);
        document.body.removeEventListener("mouseup",handleMouseDown);
        //now things are ready
        var degree = 100;
        var sequence = generateFourier(points,degree);//approximate to the 10th degree
        var recentPath = [];
        rp = recentPath;
        var start = 0;
        var period = 10;//10 seconds
        var animate = function(t){
            t /= 1000;//10 seconds to draw the whole thing
            t -= 3;
            if(start === 0)start = t;//t in seconds, not in milliseconds
            var dt = t - start;
            start = t;
            ctx.clearRect(0,0,width,height);
            ctx.fillStyle = "#002";
            ctx.fillRect(0,0,width,height);
            drawPointsClose(points,"#4f48");
            requestAnimationFrame(animate);
            var term = sequence[degree];
            var position = [term[0]*Math.cos(term[1]),term[0]*Math.sin(term[1])];
            for(var i = 1; i < degree+1; i++){
                drawTerm(sequence[degree-i],position,-i,t/period);
                drawTerm(sequence[degree+i],position,+i,t/period);
            }
            recentPath.push(position);
            var desiredLength = 300//Math.floor(period/dt);
            truncateTrail(recentPath,desiredLength);
            drawPoints(recentPath,"#4f4",desiredLength);
        }
        requestAnimationFrame(animate);
    };
    
    document.body.addEventListener("mousemove",handleMouseMove);
    document.body.addEventListener("mousedown",handleMouseDown);
    document.body.addEventListener("mouseup",handleMouseUp);
    
}

main();
