
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

function main() {
    console.log("Hello world! I am loaded!");
    $("a.songlink").click(function (ev) {
        console.log(ev.target.href);
        $("#spinner-loading").css('display', 'inline-block');
        $('#song_lyrics').css('display','none');
        $('#song_title').css('display','none');
        console.log("heloow",ev)
        url = ev.target.href.replace("/song/","/lyrics/");

        console.log(url);
        $.ajax({url : ev.target.href,
                dataType:"json",
                success: function(data, textStatus, jqXHR) {
                    $("div.lyrics").html(build_lyrics(data.song));
                }
            });
        ev.preventDefault();
        });
}

$(main);
