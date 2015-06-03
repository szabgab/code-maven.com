var templates = {};

function display_template(tmpl, data) {
    console.log('display');

    if (templates[tmpl] === undefined) {
      console.log("need");
      jQuery.get("/try/examples/js/handlerbars_template_" + tmpl + ".htm", function(resp) {
          console.log(resp);
          templates[tmpl] = Handlebars.compile(resp);
          display_template(tmpl, data);
      });
      return;
    }

    var template = templates[tmpl];
    var html    = template(data);
   $("#msg").html(html);
}

$(document).ready(function() {
    $("#show").click(function () {
      console.log('click');
      var name = 'show';
      var data = { time: new Date };
      display_template(name, data);
   });
});
