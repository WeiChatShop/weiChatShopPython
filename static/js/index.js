/**
 * Created by xiaoming on 2015/7/8.
 */
window.onload = buildHtml;
function buildHtml(){
    $.ajax({
        url:"/bookindex",
        dataType:'json',
        cache: false,
        success:function(data){
            var bookList = data;
            if(bookList==null){
                $("#bookshow").append("<span class='glyphicon glyphicon-fire' style='color: rgb(255, 140, 60);'>Sorry ,新书正在火速赶来,敬请期待!</span>")
            }else {
                var com = 0;
                var art=0;
                for(var i=0;i<bookList.length; i++ ){
                    var book = bookList[i].fields;
                    var pk = bookList[i].pk
                    if(book.classify_id==1){
                        if(com==0){
                            $("#computerLi").append('<li data-target="#computerBook" data-slide-to="0" class="active"></li>');
                            $("#computerItem").append('<div class="active item"><a class="image-container" href="/one/'+pk+'"><img src="/static/'+book.path+'"></a>' +
                            '<div class="carousel-caption"><h4>'+book.name+'</h4><p>'+book.describe.substring(0,100)+'...</p></div></div>');
                        }else {
                            $("#computerLi").append('<li data-target="#computerBook" data-slide-to='+com+'></li>');
                            $("#computerItem").append('<div class="item"><a class="image-container" href="/one/'+pk+'"><img src="/static/'+book.path+'"></a>' +
                            '<div class="carousel-caption"><h4>'+book.name+'</h4><p>'+book.describe.substring(0,100)+'...</p></div></div>');
                        }
                        com++;
                    }else if(book.classify_id==2){
                        if(art==0) {
                            $("#artBookLi").append('<li data-target="#artBook" data-slide-to="0" class="active"></li>');
                            $("#artBookItem").append('<div class="active item"><a class="image-container" href="/one/'+pk+'"><img src="/static/'+book.path+'"></a><div class="carousel-caption">' +
                            '<h4>'+book.name+'</h4><p>'+book.describe.substring(0,100)+'...</p></div></div>');
                        }else {
                            $("#artBookLi").append('<li data-target="#artBook" data-slide-to='+art+'></li>');
                            $("#artBookItem").append('<div class="item"><a class="image-container" href="/one/'+pk+'"><img src="/static/'+book.path+'"></a><div class="carousel-caption">' +
                            '<h4>'+book.name+'</h4><p>'+book.describe.substring(0,100)+'...</p></div></div>');
                        }
                        art++;
                    }
                }
            }
            $('#computerBook').carousel({
                interval: 3000
            })
            $('#artBook').carousel({
                interval: 2000
            })
        }
    });
}