/**
 * Created by xiaoming on 2015/7/9.
 */
window.onload = classifyHtml;
function classifyHtml(){
    var classify = getParam();
    $.ajax({
        url:"/classify/"+classify,
        dataType:'json',
        success:function(data){
            var bookClassList = new Array();
            if(data==null){
                $("#classify_page").append("sorry ,新书正在努力上架中,敬请期待!");
            }else if(data.status==0){
                $("#classify_page").append(data.message);
            }else{
                bookClassList = data.data;
                    var classStyle='';
                    if(bookClassList[0][5]==1){
                        classStyle='class="glyphicon glyphicon-phone"'
                    }else if(bookClassList[0][5]==2){
                        classStyle = 'class="glyphicon glyphicon-book"';
                    }
                    $("#classify_page").append('<div id="classifyName" style="padding-top:10px;padding-bottom: 10px">'+
                    '<a '+classStyle+' id="title">'+bookClassList[0][6]+'</a></div>');
                for(var i = 0; i<bookClassList.length; i++){
                    book = bookClassList[i];
                    $("#classify_page").append('<div class="classbox">');
                    if(book[4].hot==1){
                        $("#classify_page").append('<div class="hot">' +
                        '<span class="glyphicon glyphicon-fire" style="color: rgb(255, 140, 60);">本周推荐图书</span></div>')
                    }
                    $("#classify_page").append('<div class="titleName"><span class="glyphicon glyphicon-star" style="color: #71F53C;">' +
                   '</span><a href="/one/'+book[0]+'">'+book[1]+'</a></div>');
                    $("#classify_page").append('<div class="describe">'+book[2]+'</div>');
                    $("#classify_page").append('<div><a class="image-container" href="/one/'+book[0]+'"><img src="/static/'+book[3]+'"></a></div>');
                    $("#classify_page").append('</div>');
                }
            }
        }
    });
}

function getParam(){
    var u=document.location.href;
    var arr=u.split("?");
    for(var i=0;i<=arr.length;i++){
        if(arr[i].indexOf('type')>=0){
            return arr[i].split("=")[1];
        }
    }
}