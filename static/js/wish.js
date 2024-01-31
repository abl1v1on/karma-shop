$(document).ready(function () {
    const addButton = $('#add_in_wish_list')
    addButton.on('click', function () {
        $.ajax({
            url: '{% url "wish_list:add_item" %}',
            success: function (response) {
                console.log(response)
            },
            error: function (response) {
                console.log(response)
            }
        });
    });
});
