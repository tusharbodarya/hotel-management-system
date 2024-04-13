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
                button.html("<i class='fa fa-spinner fa-spin'></i> Processing")
            },
            success: function(response){
                $(".room-count").text(response.total_selected_items)
                button.html("<i class='fa fa-check'></i> Added to Selection")
                console.log(response)
            }
        })

    })
})

$(document).on("click",".delete-item", function(){
    let hotel_id = $(this).attr("data-item")
    let button = $(this)

    $.ajax({
        url: "/delete_selection/",
        data: {
            "hotel_id": hotel_id,
        },
        dataType: "json",
        beforeSend: function(){
            button.html("<i class='fa fa-spinner fa-spin'></i>")
        },
        success: function(response){
            $(".room-count").text(response.total_selected_item)
            $(".selection-list").html(response.data)
        }
    })
})

function makeAjaxCall(){
    $.ajax({
        url: "/update_room_status/",
        type: "GET",
        success: function(data){
            console.log(data);
        },
        error: function(error){
            console.log(error);
        }
    })
}

// setInterval(makeAjaxCall, 3000);
setInterval(makeAjaxCall, 86400000);