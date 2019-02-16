$(function(){
    $('html ,body').animate({ scrollTop: 0 }, 10);

    let bannerTop = $("#main .main-banner").offset().top + Number.parseFloat($("#main .main-banner").css("height"));
    let leftNavList = $("#left-nav .l-n-body .l-n-pul-con");//左边a标签
    let mainList = $("#main .main-content .main-content-supermarket");//每一项div
    
    let scrHeight = $(window.screen.height)[0]/2;

    
    $(window).on("scroll",function(){
        //头部
        if($(this).scrollTop()<bannerTop){
            $("#header-top").css("top",-50);
        }else{
            $("#header-top").css("top",0);
        }
        //侧边导航
        if($(this).scrollTop()<bannerTop-190){
            $("#left-nav").css({
                width:0,
                height:0,
                opacity:0
            });
        }else{
            $("#left-nav").css({
                width:36,
                height:370,
                opacity:1
            });
        }

        mainList.each((x,y)=>{
            let changeTop = $(y).offset().top-$(document).scrollTop();
            let cla = "l-n-bgc"+(x+1);
            if(x===7){
                if(changeTop < scrHeight && (-1200)<changeTop){
                    $(leftNavList[x]).addClass(cla);
                    return
                }else{
                    $(leftNavList[x]).removeClass(cla);
                    return
                }
            }
            if(changeTop < scrHeight && (-150)<changeTop){
                $(leftNavList[x]).addClass(cla);
            }else{
                $(leftNavList[x]).removeClass(cla);
            }
        })

    });

    

    $(".go_top").on("click",function(){
        $("html,body").animate({scrollTop:$("#header").offset().top},200);
    });

    //main 点击
    leftNavList.each((x,y)=>{
        $(y).on("click",function(){
            $("html,body").animate({scrollTop:$(mainList[x]).offset().top-60},300);
        });
    });
})
