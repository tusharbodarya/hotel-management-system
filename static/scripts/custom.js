$(document).ready(function(){
    $('.add-to-selection').on("click", function(){
        let button = $(this)
        let id = button.attr('data-index')

        let hotel_id = $("#h_id").val()
        let room_id = $(".room_id_"+id).val()
        let room_number = $(".room_number_"+id).val()
        let hotel_name = $("#hotel_name").val()
        let room_type = $("#room_type").val()
        let room_price = $("#room_price").val()
        let number_of_beds = $("#number_of_beds").val()
        let room_type_id = $("#room_type_id").val()
        let checkin = $("#checkin").val()
        let checkout = $("#checkout").val()
        let adult = $("#adult").val()
        let children = $("#children").val()

        $.ajax({
            url: '/add_to_selection/',
            data:{
                "id": id,
                "hotel_id": hotel_id,
                "room_id": room_id,
                "room_number": room_number,
                "hotel_name": hotel_name,
                "room_type": room_type,
                "room_price": room_price,
                "number_of_beds": number_of_beds,
                "room_type_id": room_type_id,
                "checkin": checkin,
                "checkout": checkout,
                "adult": adult,
                "children": children,
            },
            dataType: "json",
            beforeSend: function(){
                console.log("Sending Data to server.......");
            },
            success: function(response){
                console.log(response)
            }
        })

    })
})