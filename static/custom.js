let socket;
$(document).ready(function () {
    socket = io.connect('http://' + document.domain + ':' + location.port + '/chat');
    socket.on('connect', function () {
        socket.emit('join', {});
    });

    socket.on('message', function (data) {
        console.log(data)
        let tx = GenerateMessageHtml(data)
        $('#chat').append(tx);
        $('.chat-body')[0].scrollTop = $('.chat-body')[0].scrollHeight
    });

    $('#send').click(function (e) {
        text = $('#text').val();
        $('#text').val('');

        if (text) {
            $.ajax({
                url: "message",
                type: "post",
                data: {"msg": text}
            }).success(function (data) {

            });
        }
    });
});

function leave_room() {
    socket.emit('left', {}, function () {
        socket.disconnect();
    });
}

function GenerateMessageHtml(data) {
    let current_user = $("#chat").attr('data-user')
    if (current_user === data.user) {
        return "<li class=\"w-75 float-right\">" + data.msg + "<br><small>" + data.create_at + "</small></li>";
    } else {
        return "<li class=\"w-75\">" + data.msg + "<br><small>" + data.create_at + "</small></li>";
    }
}
