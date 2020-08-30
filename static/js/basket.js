window.onload = function(){
    // ajax обработка добавления/удаления товара в корзине
    $('.basket_add').click(function(event){
        var tr = $(this).closest('tr');
        var product_id = $(this).attr('param');

        event.preventDefault();

        $.ajax({
            url: '/basket/add/' + product_id,

            success: function (data) {
                $(tr).find('td[name="quantity"]').html(data['result']['quantity'] + ' шт.');
                $(tr).find('td[name="total"]').html(data['result']['total'] + ' руб.');
                $('#total').html(data['total'] + '&nbsp;руб.');

                $('#alert_message').show();
                $('#alert_message').html(data['result']['message']).fadeIn(400).delay(1000).fadeOut(400);
            },
        });
    });

    $('.basket_remove').click(function(){
        var tr = $(this).closest('tr');
        var product_id = $(this).attr('param');

        $.ajax({
            url: '/basket/remove/' + product_id,

            success: function (data) {
                if (Number(data['result']['total']) > 0) {
                    $(tr).find('td[name="quantity"]').html(data['result']['quantity'] + ' шт.');
                    $(tr).find('td[name="total"]').html(data['result']['total'] + ' руб.');
                }
                else {
                    $(tr).remove();
                }
                $('#total').html(data['total'] + ' руб.');
            },
        });
    });
}