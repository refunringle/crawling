
function build_lyrics(lyrics) {
    ret = $(`<p>
    <h4> Lyrics for ${lyrics.name} </h4>
    <h5> <small class="text-muted">${lyrics.artist.name}</small> </h5>
</p>
<p style="text-decoration: none">
    <em>${lyrics.lyrics}</em>
</p>`)

    return ret;
}

function click(){
    $(document).ready (function(){
        $('a.songlink').click (function(){
            $('a.songlink').css('color', 'blue');
            $(this).css('color', 'black');
        });
}
)};

function main() {
    $("a.songlink").click(func)
};
function func(ev) {
    ev.preventDefault();
    $("div.lyrics").text("Loading......")
    $.ajax({
        url: ev.target.href,
        dataType: 'json',
        success: function (data, textStatus, jqXHR) {
            $("div.lyrics").html(build_lyrics(data.song));
            var text = ev.target.innerText;
            var parent = ev.target.parentNode;
            $(parent).html(text)
            $(".songname")
                .html(`<a class = "songlink" style="text-decoration: none !important; color: blue;"
                 href="/song/${$(".songname")
                .attr("id")}">${$(".songname").text()}<a/>`);
            $(".songname a").click(func);
            $(".songname").attr("class", "songlinks");
            $(parent).attr("class", "songname");
        }
    })
}
$(main);











// function free(ev) {
//     console.log("Hello world! I am loaded!");
//     $("a.songlink").click(function (ev) {
//         ev.target.style.color = click();

//         console.log(ev.target.href);
//         $("#spinner-loading").css('display', 'inline-block');
//         $('#song_lyrics').css('display','none');
//         $('#song_title').css('display','none');
//         console.log("heloow",ev)
//         url = ev.target.href.replace("/song/","/lyrics/");

//         console.log(url);
//         $.ajax({url : ev.target.href,
//                 dataType:"json",
//                 success: function(data, textStatus, jqXHR) {
//                     $("div.lyrics").html(build_lyrics(data.song));
//                     var text = ev.target.innerText;
//                     console.log(text)
//                     var parent = ev.target.parentNode;
//                     console.log(parent)
//                     $(parent).html(text)
//                     console.log($(parent).html(text))
//                     $(".songname")
//                         .html(`<a class = "songlink" href="/song/${$(".songname")
//                         .attr("id")}">${$(".songname").text()}<a/>`);
//                     $(".songname a").click(myFunc);
//                     $(".songname").attr("class", "songslink");
//                     $(parent).attr("class", "songname");
//                 }
//             });
//         ev.preventDefault();
//         });
// }

// function main() {
//     $("a.songlink").click(free())
// };

// $(main);




// function myFunc(ev) {
//     ev.preventDefault();
//     $("div.lyrics").text("Loading......")
//     $.ajax({
//         url: ev.target.href,
//         dataType: 'json',
//         success: function (data, textStatus, jqXHR) {
//             $("div.lyrics").html(build_lyrics(data.song));
//             var text = ev.target.innerText;
//             var parent = ev.target.parentNode;
//             $(parent).html(text)
//             $(".songname")
//                 .html(`<a class = "songlink" href="/song/${$(".songname")
//                 .attr("id")}">${$(".songname").text()}<a/>`);
//             $(".songname a").click(myFunc);
//             $(".songname").attr("class", "songslink");
//             $(parent).attr("class", "songname");
//         }
//     })
// }
// $(main);