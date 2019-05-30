$(function () {
    $(".schedule_type").each(function () {
        var st_time = $("#time").val();
        var stp_pk = $(this).attr("id");
        $.ajax({
            url:"/schedule/scheduletype_get",
            type:"post",
            data:{
                "st_time":st_time,
                "stp_pk":stp_pk,
            },
            success:function (e) {
                if(e == "y"){
                    $("#" + stp_pk).attr("checked","checked");
                }
            }
        })
    });

    $(".schedule_type").on("change",function () {
        var st_time = $("#time").val();
        var stp_pk = $(this).attr("id");
        var stp_status = $("#" + stp_pk).prop("checked");
        if(stp_status == true){
            stp_action = "add"
        }else if(stp_status == false){
            stp_action = "del"
        }
        $.ajax({
            url:"/schedule/scheduletime_add",
            type:"post",
            data:{
                "st_time":st_time,
                "stp_pk":stp_pk,
                "stp_action":stp_action,
            },
            success:function (e) {
            }
        })
    })
});