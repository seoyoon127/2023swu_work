var profile_pic = document.querySelector('.profile');

profile_pic.onclick = function(e) {
    profile_pic.setAttribute('src', prompt('이미지 URL을 입력하세요:'));
}

var icon_pic = document.querySelector('.icon');

icon_pic.onclick = function(e) {
    var idname=document.querySelector('#profile_all span');
    idname.innerHTML= prompt('새로운 아이디를 입력하세요.');
}

var introduce=document.getElementById('introduce');
var userName=document.getElementById('userName');
var inform=document.getElementById('inform');
var profile_link=document.getElementById('profile_link');
var changing=false;

profile_button.onclick=function(e){
    if(changing){
        var new_userName=userName.querySelector("input").value;
        var new_inform=inform.querySelector("input").value;
        var new_profile_link=profile_link.querySelector("input").value;

        userName.innerHTML=new_userName;
        inform.innerHTML=new_inform;

        if(new_profile_link.startsWith('http')){
            new_profile_link="<a href=\'"+new_profile_link+"\'>"+new_profile_link+'</a>';
        }
        profile_link.innerHTML=new_profile_link;
        e.target.textContent='프로필 편집';
        changing=false;
    }
    else{
        var new_userName=userName.textContent;
        var new_inform=inform.textContent;
        var new_profile_link=profile_link.textContent;

        userName.innerHTML = '<input value="' + new_userName + '" class=\'jsClass\'>';
        inform.innerHTML = '<input value="' + new_inform + '"class=\'jsClass\'>';
        profile_link.innerHTML = '<input value="' + new_profile_link + '"class=\'jsClass\'>';

        e.target.textContent='프로필 편집 완료';
        changing=true;
    }
    }