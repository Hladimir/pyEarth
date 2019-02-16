//今日疯抢转换
(function(){
    let aRobLi = document.querySelectorAll(".super-b-right-t .super-b-right-t-act .rob li"),
        aDiv = document.querySelectorAll(".super-b-right-t-act .rob li .right-t-act-c"),
        index = 0;
    ;
    for(let i=0,len=aRobLi.length;i<len;i++){
        aRobLi[i].onmouseenter = function () {
            setTimeout(function () {
                if(aRobLi[i].classList.contains("show")){
                    return;
                }
                aRobLi[i].classList.add("show");
                aRobLi[index].classList.remove("show");

                aDiv[i].classList.add("show");
                aDiv[index].classList.remove("show");
                index = i;
            },200);
        }
    }

})();

//banner轮播切换
(function () {
    let aBanLi = document.querySelectorAll(".main-banner .main-nav-list li"),
        aBanBgc = document.querySelectorAll(".main-banner .main-b-bgc"),
        aCon = document.querySelectorAll(".main-banner .main-b-bgc .main-b-con"),
        index = 0,
        len = aBanLi.length
    ;
    
    for(let i=0;i<len;i++){
        //轮播点击切换
        aBanLi[i].onmouseenter = function () {
            clearInterval(timer);
            timer = setInterval(time,6000);
            setTimeout(function () {
                if(aBanLi[i].classList.contains("show")){
                    return;
                }
                aBanLi[i].classList.add("show");
                aBanLi[index].classList.remove("show");

                aBanBgc[i].classList.add("show");
                aBanBgc[index].classList.remove("show");
                index=i;
            },200);
        }
    }
    //轮播自动播放
    function time(){
        aBanLi[index].classList.remove("show");
        aBanBgc[index].classList.remove("show");
        index++;
        if(index>=len){
            index=0;
        }
        aBanLi[index].classList.add("show");
        aBanBgc[index].classList.add("show");
    }
    var timer = setInterval(time,6000);
})();

