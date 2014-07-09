/// <reference path="../../../Js/jquery-1.4.1-vsdoc.js" />
$(function () {
    /*size控制*/
    function GetSize() {
        //alert(123);
        //        $("#boxTb").width($("body").width())
        //        $("#boxTb").height($("body").height());
        //alert();
        $("#mainTb").height($(document).height() - $("#topTb").height() - $("#footerTb").height() - 4);
        $("#leftTb,#mainFrame").height($("#mainTb").height());
        $("#mainFrame").width($("#mainTb").width() - $("#leftTb").width());
    }
    $(window).resize(function () {
        GetSize();
    });
    GetSize();
    $("a").click(function () {
        //$("#mainFrame").attr("src", $(this).attr("src"));
        //$("#mainFrame").load();
        //return false;
    })

    /*顶部菜单*/
    $("#menu a:first").attr("class", "menuon");
    $("#menu a").click(function () {
        $(this).attr("class", "menuon").blur().parent().siblings().find("a").attr("class", "menuoff");
    });
    /*左边菜单*/
    $(".menu a").click(function () {
        $(".menu a").attr("class", "leftmenuoff");
        $(this).attr("class", "leftmenuon").blur();
        $.dialog.open(
          
            $(this).attr("href"),
            {
                id: $(this).attr("id"),
                title: $(this).text(),
                initFn: function () {
                    this.size(800, 500);
                    this.position('50%', '50%')
                }, noFn: function () { }
            }, false)
        return false;
    });
    $(".m_t td").attr("class", "submenutitleoff").click(function () {
        if ($(this).attr("class") == "submenutitleon") {
            $(this).attr("class", "submenutitleoff");
            $(this).parent().parent().find("tr").eq(1).hide();
        }
        else {
            $(this).attr("class", "submenutitleon");
            $(this).parent().parent().find("tr").eq(1).show();
        }
    });
    /*其它*/
    $("#loginOut").click(function () {
        $.dialog.confirm("确定退出吗？", function () {location.href="Loginout.aspx" }, function () { })
    })
}); 