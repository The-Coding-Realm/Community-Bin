//make the attribute parser
var attrParser = function(str){
    //escape ":" and ";"
    var attrs = [["",""]];
    var mode = 0;
    for(var i = 0; i < str.length; i++){
        var attr = attrs.pop();
        var char = str[i];
        if(char === "_"){//escape character
            attr[mode] += str[i+1];
            i++;
            attrs.push(attr);
        }else if(char === ":"){
            mode++;
            attrs.push(attr);
        }else if(char === ";"){
            mode = 0;
            attrs.push(attr);
            attrs.push(["",""]);
        }else{
            attr[mode] += str[i];
            attrs.push(attr);
        }
    }
    attrs = attrs.filter((a)=>{
        if(a[0] === ""){
            return false;
        }
        return true;
    });
    return attrs;
};

var getELEM = function(nname,attrs,inner,style){
    if(typeof nname === "object" && "mtvriiutba" in nname){//it's an ELEM
        return nname;
    }else{
        return new ELEM(nname,attrs,inner,style);
    }
};

//will be a version 2 overhaul, so everything will be different
var ELEM = function(nname,attrs,inner,style){
    if(typeof nname === "string"){
        var e = document.createElement(nname);
        if(attrs){
            attrParser(attrs).map((a)=>{
                e.setAttribute(a[0],a[1]);
            });
        }
        if(inner){
            e.innerHTML = inner;
        }
        if(style){
            e.style = style;
        }
        this.e = e;
    }else{
        this.e = nname;
    }
    this.mtvriiutba = 42;
    
    this.add = function(nname,attrs,inner,style){
        var elem = getELEM(nname,attrs,inner,style);
        this.e.appendChild(elem.e);
        return elem;
    };
    this.attr = function(a,b){
        this.e.setAttribute(a,b);
    };
    this.remove = function(){
        this.e.parentNode.removeChild(this.e);
    };
    var that = this;
    Object.defineProperties(this, {
        "children": {
             "get": ()=>that.e.children,
             "set": ()=>{}
        }
    });
}

var BODY = new ELEM(document.body);