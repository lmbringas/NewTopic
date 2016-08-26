$(document).ready(function () {
    var colors = ["#ee6e73", "#26a69a", "#7BAABE", "#FF5722", '#5D4037', '#388E3C', '#0288D1', '#6dcb91', '#512DA8', '#7B1FA2']; // ,'#FFEB3B' amarillo
    var changecolor = function () {
        $('.section').each(function (i, e) {
            do {
                var color = colors[Math.floor((Math.random() * colors.length))];
                $(e).css("background-color", color);
            } while ($(e).css("background-color") == $(e).prev().css("background-color"));
        });
    }
    var postOffset = 3;
    $('#fullpage').fullpage({
        menu: '#menu',
        onLeave: function (index, nextIndex, direction) {
            nextIndex=+1;
            if (nextIndex == $('.section').length) {
                $.ajax({
                    type: 'GET',
                    url: '/?offset=' + postOffset,
                    success: function (data) {
                        if (data.length > 0) {
                            alert(data.length);
                            for (var i = 0; i < data.length; i++) {
                                var compile_data;
                                console.log(i);
                                compile_data = " <div class='section fp-section fp-table'><div class='container'><h5 class='titulo'>" + data[i].title + "</h5><p>" + data[i].content + "</p><a class='waves-effect button' href={% url 'blog:post'" + data[i].id + " %}>Ir al articulo</a></div></div>";

                                $('#fullpage').append(compile_data);
                                changecolor();
                            }

                            /* update the offset */
                            postOffset += 5
                        } else {
                            $('#fullpage').append('No articles found');
                        }
                    }
                });
            }
        }
    });
    changecolor();
    $("#btn-floating").click(function (e) {
        $('.dialog-all').addClass("is-visible");
    });
    $('.dialog-all').click(function (e) {
        if ($(e.target).is($('.dialog-all'))) {
            $('.dialog-all').removeClass('is-visible');
        }
    });
    $('#btn-comment').click(function (e) {
        if ($('#comment').val() == "") {
            alert("No tiene nada ");
            return false;
        }
    });
});
