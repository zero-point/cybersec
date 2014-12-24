function Random() { 
    var Random = Math.floor(Math.random() * 9); 

    var r_text = new Array ();
    r_text[0] = "Start general...<br/> Start with your broadest ideas before getting to the<br/> specifics, it will make your brainstorm more effective.";
    r_text[1] = "Be curious, not judgmental...<br/> Open up the possibilities and break down your assumptions,<br/> it will help you explore different ideas.";
    r_text[2] = "Take a break...<br/> A good brainstorming session can get pretty lively. Refresh<br/> your mind before starting again. Go easy on the coffee!";
    r_text[3] = "Minimise distractions...<br/> It’s all about focus so limit the distractions around you, it’s<br/> the best way to expand your ideas quicker";
    r_text[4] = "What do your friends think?<br/> Share your brainstorm with friends to get a new perspective<br/> and develop your ideas further in conversation.";
    r_text[5] = "Keep it concise...<br/> Using keywords for your ideas helps you see your<br/> brainstorm in an organised way.";
    r_text[6] = "Breathe...<br/> Fresh air is great fuel for the brain to focus and be more<br/> creative. Why not take a walk before or after this brainstorm.";
    r_text[7] = "Set a time limit...<br/> Whether it be five minutes, fifteen minutes, half an hour we<br/> don’t want you to burn out.";
    r_text[8] = "More than ideas...<br/> Planning a trip or organising an event? See how Brainstorm<br/> can help you in other areas of life. Share your stories with us.";
    document.getElementById("randomDiv").innerHTML = r_text[Random]
    console.log(r_text[Random])
}  

    $(document).ready(function() {

        $('#overlay').fadeIn(300);
        $('#newBrainstorm').css('z-index', '99999');

        Random();
        function zoomhoverin(){document.getElementById("tooltipZoom").style.display='inline';}
        function zoomhoverout(){document.getElementById("tooltipZoom").style.display='none';}
        function centrehoverin(){document.getElementById("tooltipCentre").style.display='inline';}
        function centrehoverout(){document.getElementById("tooltipCentre").style.display='none';}

        $('#zoomBtn').hoverIntent({
            over:zoomhoverin,
            out:zoomhoverout,
            interval:600
        });

        $('#centreBtn').hoverIntent({
            over:centrehoverin,
            out:centrehoverout,
            interval:600
        });

    //      $('#title').editable(function() {
    //          document.getElementById('title').innerHTML;
    //      });

            $('.edit').editable('file:///home/futurenode/workspace/final-brainstorm/brainstorm.html/save.php', {
                indicator : 'Saving...',
                tooltip   : 'Click to edit...'
            });
            
            $('.edit_area').editable('http://zero-point.github.io/brainstorm/save.php', { 
                type      : 'textarea',
                cancel    : 'Cancel',
                submit    : 'OK',
                indicator : '<img src="img/indicator.gif">',
                tooltip   : 'Click to edit...'
            });
        });

var RADIUS = 50;
var CANVAS, MID_X, MID_Y = null;


function getRandomColor() {
        return '#' + (function co(lor){ return (lor += [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f'][Math.floor(Math.random()*16)]) && (lor.length == 6) ?  lor : co(lor); })('');
}

/**
 * HSV to RGB color conversion
 *
 * H runs from 0 to 360 degrees
 * S and V run from 0 to 100
 * 
 * Ported from the excellent java algorithm by Eugene Vishnevsky at:
 * http://www.cs.rit.edu/~ncs/color/t_convert.html
 */
function hsvToRgb(h, s, v) {
        var r, g, b;
        var i;
        var f, p, q, t;
        
        // Make sure our arguments stay in-range
        h = Math.max(0, Math.min(360, h));
        s = Math.max(0, Math.min(100, s));
        v = Math.max(0, Math.min(100, v));
        
        // We accept saturation and value arguments from 0 to 100 because that's
        // how Photoshop represents those values. Internally, however, the
        // saturation and value are calculated from a range of 0 to 1. We make
        // That conversion here.
        s /= 100;
        v /= 100;
        
        if(s == 0) {
                // Achromatic (grey)
                r = g = b = v;
                return [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
        }
        
        h /= 60; // sector 0 to 5
        i = Math.floor(h);
        f = h - i; // factorial part of h
        p = v * (1 - s);
        q = v * (1 - s * f);
        t = v * (1 - s * (1 - f));

        switch(i) {
                case 0:
                        r = v;
                        g = t;
                        b = p;
                        break;
                        
                case 1:
                        r = q;
                        g = v;
                        b = p;
                        break;
                        
                case 2:
                        r = p;
                        g = v;
                        b = t;
                        break;
                        
                case 3:
                        r = p;
                        g = q;
                        b = v;
                        break;
                        
                case 4:
                        r = t;
                        g = p;
                        b = v;
                        break;

                default: // case 5:
                        r = v;
                        g = p;
                        b = q;
        }
        
        return [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
}

$(function() {

CANVAS = new Canvas($("#canvas-container").get(0), $(window).width(), $(window).height()+1);
CANVAS.makeDraggable(); 
//TODO bind on window resize: http://stackoverflow.com/questions/4037212/html-canvas-full-screen
console.log(CANVAS);
MID_X = CANVAS.width/2;
MID_Y = CANVAS.height/2;

window.Sector = Backbone.Model.extend({
        initialize: function() {
                this.set("level", this.get("parent") ? this.get("parent").get("level")+1 : 0);
                this.set({
                        radius: (this.get("level")+0.5) * RADIUS, //TODO make nice
                        children: new (Backbone.Collection.extend({ model : Sector })),
                        offsetAngle: this.get("parent") ? this.get("parent").get("offsetAngle") : 0,
                        angle: this.get("parent") ? this.get("parent").get("angle") : Math.PI*2,
                        view: new SectorView({ model: this })
                });
                this.on("change:offsetAngle change:angle", this.setChildPositions, this);
                this.get("children").on("add", this.setChildPositions, this);
        },

    toggle: function() {
      this.save({done: !this.get("done")});
    },
        
        setLabel: function(label) {
                this.set("label", label);
        },
        
        addChildClockwiseOf: function(childNumber, label) {
                var child = new Sector({ label: label, parent: this });
                this.get("children").add(child); //TODO at correct index
                return child;
        },

        addChildAnticlockwiseOf: function(childNumber, label) {
                return this.addChildClockwiseOf((childNumber-1) % this.get("children").length, label);
        },
        
        addChild: function(label) {
                return this.addChildClockwiseOf(this.get("children").length-1, label);
        },
        
        setChildPositions: function() {
                var childOffsetAngle = this.get("offsetAngle");
                var childAngle = this.get("angle")/this.get("children").length;

                this.get("children").each(function(child) {
                        child.set({
                                angle: childAngle,
                                offsetAngle: childOffsetAngle
                        });
                        childOffsetAngle += childAngle
                });
        },
        
        addClockwise: function() {
                alert("addClockwise");
        },
});

var root = new Sector({
        label: ""
});
});

window.FormPopup = Backbone.View.extend({
        template: _.template($('#popup-template').html()),
        
        events: {
                "dblclick .sector-label" : "edit",
                "keypress .sector-label-edit input" : "setLabel"
                },
        
        render: function() {
                var view = this;

                this.$el.html(this.template(this.model.toJSON()));
                this.$el.modal({
                        backdrop: false
                });
                this.$el.on("hidden", function() {
                        view.remove();
                });

                this.$el.find("form").submit(function() {
                        $(this).find("input:text").each(function() {
                                var label = $(this).val();
                                if (label.length > 0){
                                                view.model.addChild(label);
                                }
                        });
                        view.$el.modal("hide");
                        return false;
                });
        },

        edit: function() {
                this.$el.addClass("edit");
                this.$el.find(".sector-label-edit input").focus();
        },
        
        setLabel: function(e) {
                if (e.keyCode != 13)
                        return;
var newLabel = this.$el.find(".sector-label-edit input").val();
                this.model.set("label", newLabel);
                //document.getElementById('title').innerHTML = newLabel;
                this.$el.find(".sector-label h3").html(newLabel);
                this.$el.removeClass("edit");
        },
});

window.SectorView = Backbone.View.extend({
        initialize: function() {
                this.model.bind("change", this.render, this);
                this.model.bind('destroy', this.remove, this);
                this.setElement(null);
        },
        
        events: {
                "mouseover": "popOut",
                "mouseout": "popIn",
                "dblclick": "showInfo",
    },
        
        render: function() {
                var radius = this.model.get("radius");
                var circle;
                if (this.model.get("level") == 0) {
                        if (this.el != null) return;
                        circle = new Circle(radius, {
                                x: CANVAS.width/2,
                                y: CANVAS.height/2,
                                fill: getRandomColor(),
                        });
                        this.setElement(circle);
                        CANVAS.append(this.el);
                } else {
                        var offsetAngle = this.model.get("offsetAngle");
                        var angle = this.model.get("angle");

                        if (this.el == null) {
                                circle = new Circle(radius, {
                                        x: CANVAS.width/2,
                                        y: CANVAS.height/2,
                                        startAngle: offsetAngle + angle,
					endAngle: offsetAngle + angle,
                                        zIndex: -this.model.get("level"),
                                        includeCenter:true,
                                });
                                this.setElement(circle);
                                CANVAS.append(this.el);
                        }

                        this.el.fill = hsvToRgb((offsetAngle+angle/2)*180/Math.PI, 22, 200); //100-((this.model.get("level")-1)*10)); //TODO make nice
                        this.el.animateTo('startAngle', offsetAngle, 500, 'sine');
                        this.el.animateTo('endAngle', offsetAngle + angle, 500, 'sine');
                        
                        var xx = radius * Math.sin(Math.PI/2 + offsetAngle + angle/2);
                        var yy = -radius * Math.cos(Math.PI/2 + offsetAngle + angle/2);
                        
                        var text = this.el.getElementById("text");
                        if (text == null) {
                                text = new TextNode(Drawable, {
                                        id: "text",
                                        maxWidth:50,
                                        cx: xx,
                                        cy: yy,
                                        fill: "#000",
                                });
                                this.el.append(text);
                        }
                        
                        text.text = this.model.get("label");
                        text.animateTo('cx', xx, 10, 'linear');
                        text.animateTo('cy', yy, 10, 'linear');
                }
        },
        
        popOut: function() {
                this.el.animateTo('scale', 1.1, 100, 'linear');
        },
        
        popIn: function() {
                this.el.animateTo('scale', 1, 100, 'linear');
        },
        showInfo: function() {
                new FormPopup({ model: this.model }).render();
        },
        
});
$(function(){

      $(".editable").keypress(function(e) {
        if (e.which == 13) {
            e.preventDefault();

             if (document.selection) {
                document.selection.createRange().pasteHTML("");
             } else {
                $(this).append("");
             }
        }
    });
});


function func1(){
    var title = document.getElementById("braintitle").value
    if(title=="")   title = "New Brainstorm";
    var root = new Sector({ label: title });
    $("#pbraintitle").text(title);
    document.getElementById("newBrainstorm").style.display="none";
    $('#overlay').fadeOut(300);
    $('#newBrainstorm').css('z-index', '1');
    document.getElementById("zoom").style.display="none";
    document.getElementById("column2").style.display="inline";
}
function func12(){
    title = "New Brainstorm";
    root = new Sector({ label: title });
    $("#pbraintitle").text(title);
    document.getElementById("newBrainstorm").style.display="none";
    $('#overlay').fadeOut(300);
    $('#newBrainstorm').css('z-index', '1');
    document.getElementById("zoom").style.display="none";
    document.getElementById("column2").style.display="inline";
}

function func2(){
    document.getElementById("exitBrainstorm").style.display="none";
    $('#overlay').fadeOut(300);
    $('#exitBrainstorm').css('z-index', '1');
    document.getElementById("zoom").style.display="none";
    document.getElementById("column2").style.display="inline";
}

function newBrain(){

    document.getElementById("exitBrainstorm").style.display='inline';
    $('#overlay').fadeIn(300);
    $('#exitBrainstorm').css('z-index', '99999');
    document.getElementById("zoom").style.display="none";
    document.getElementById("column2").style.display="none";
    //var check = confirm("You are about to leave this brainstorm behind. Make sure you've saved it! And press OK when you're ready!");
    //if (check == false)   return false; else window.location.href = window.location.href;

};

function showit() {
    tooltipCanvas.style.visibility='visible';
}
function hideit() {
    tooltipCanvas.style.visibility='hidden';
}