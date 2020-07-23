(function() {
    var min_horizontal_move = 30;
    var max_vertical_move = 30;
    var within_ms = 1000;

    var start_xPos;
    var start_yPos;
    var start_time;
    function touch_start(event) {
        start_xPos = event.touches[0].pageX;
        start_yPos = event.touches[0].pageY;
        start_time = new Date();
    }


    function touch_end(event) {
        var end_xPos = event.changedTouches[0].pageX;
        var end_yPos = event.changedTouches[0].pageY;
        var end_time = new Date();
        let move_x = end_xPos - start_xPos;
        let move_y = end_yPos - start_yPos;
        let elapsed_time = end_time - start_time;
        if (Math.abs(move_x) > min_horizontal_move && Math.abs(move_y) < max_vertical_move && elapsed_time < within_ms) {
            if (move_x < 0) {
                //alert("left");
            } else {
                //alert("right");
            }
        }
    }

    var content = document.getElementById("content");
    content.addEventListener('touchstart', touch_start);
    content.addEventListener('touchend', touch_end);

})();

