#-*-coding:utf-8-*-
import requests
import re 
import os 

html_data = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="baidu-site-verification" content="cNhJHKEzsD" />
<meta property="qc:admins" content="27354635321361636375" />
<link rel="canonical" href="https://music.163.com/playlist?id=319135616">
<meta name="applicable-device" content="pc">
<link rel="alternate" media="only screen and (max-width: 640px)" href="https://music.163.com/m/playlist?id=319135616">
<meta name="mobile-agent" content="format=html5;url=https://music.163.com/m/playlist?id=319135616">
<title>吃个早茶饼喜欢的音乐 - 歌单 - 网易云音乐</title>
<meta name="keywords" content="吃个早茶饼喜欢的音乐，吃个早茶饼" />
<meta name="description" content="歌单：吃个早茶饼喜欢的音乐。创建者：吃个早茶饼。" />
<script type="application/ld+json">
{
"@context": "https://ziyuan.baidu.com/contexts/cambrian.jsonld",
"@id": "http://music.163.com/playlist?id=319135616",
"appid": "1582028769404989",
"title": "吃个早茶饼喜欢的音乐",
"images": ["http://p1.music.126.net/8xYnBPl89VLi8pqaJJOqXg==/18964376556038798.jpg"],
"description": "歌单：吃个早茶饼喜欢的音乐。创建者：吃个早茶饼。",
"pubDate": "2016-03-17T12:57:22"
}
</script>
<script type="text/javascript">
var GDownloadLink="";
var GDevice = "phone";
var GFrom="";
var GClient="";
var GPlatform="other";
var GRef = '';
var GInApp = false;
var GMobile = false;
var GAbroad = false;
var GUser={};
var GAllowRejectComment = false;
var GEnc = true;
var GEnvType = "online";
var GWebpSupport = "1";
window.NEJ_CONF = {p_csrf:{cookie:'__csrf',param:'csrf_token'}};
//线上环境参数配置
window.MUSIC_CONFIG = {
pushHost:'web.push.126.net',
pushPort:'6003',
pushKey:'3b97981848064bbabeaaf2fb1eab7368'
};
GUtil = {
getBase:function(){
return location.protocol+'//'+location.hostname;
},
getPathAndHash:function(_url){//获取URL path 之后的所有内容,并将/#/替换成/m/使之成为path的一部分
if(!_url) return '';
var _reg0 = /^https?:\/\/.*?\//i,
_reg1 = /\/?#\/?/i;
return _url.replace(_reg0,'/').replace(_reg1,'/m/');
},
composeRefer:function(_url,_ref){//对所有的页面请求都加上ref参数表示被嵌套的来源
if(!_ref) return _url;
var _hi = _url.indexOf('#'),
_si = _url.indexOf('?');
if(_si>0&&(_si<_hi||_hi<0)){
return _url.substring(0,_si+1)+'ref='+_ref+'&'+_url.substring(_si+1);
}else if(_hi>0&&(_si<0||_si>_hi)){
return _url.substring(0,_hi)+'?ref='+_ref+_url.substring(_hi);
}else{
return _url+'?ref='+_ref;
}
}
};(function(){
var _ua = window.navigator.userAgent,
_isMobile = /(mobile|mobi|wap|iphone)/i.test(_ua),
_isAndroid = /android/i.test(_ua),
_isIpad = /(ipad)/i.test(_ua),
_igList = [/^\/xiami$/,/^\/live$/],//不需要以单页面打开的列表，比如某些活动页面
_pn = location.pathname,
_idx = _pn.lastIndexOf('/'),
_pReg = /\s*(\w+)\s*=\s*(\d+)\s*/,
_redirect2mobile = function() {
var _type,_murl,
_id = 0,
_hash = location.hash,
_mReg = /^#\/?m?\/(share|song|playlist|djradio|dj|program|album|mv|artist|topic|radio|zysf|drqp|qp|activity|store|user|event|video|discover\/toplist)(\/(\d+))?/,
_base = location.protocol+'//'+location.hostname,
_sindex = _hash.lastIndexOf('?'),
_search = _sindex>-1?_hash.substring(_sindex+1):'',
_match = _mReg.exec(_hash);
// 无hash || 不匹配 || 匹配但是商品之外不带参数 || 匹配且是排行榜
if (!_hash.length || !_match || (_match[1] != 'store' && !_search) || /share|discover\/toplist/.test(_match[1])) {
// 有hash && (没有参数 || 排行榜)
if ((!_search || /share|discover\/toplist/.test(_match[1])) && _hash.length) {
location.href = _base + '/' + _hash.replace('#', 'm');
} else {
location.href = _base + '/m/';
}
return;
}
_type = _match[1];
_id = _match[3];
if (_type == 'dj') _type = 'program';
if (_type == 'store') {
_murl = /^#\/store\/(product|concert)\/detail/.test(_hash) ? _hash.replace('#/store', '/store/m') : '/store/m/product/index';
} else {
_murl = '/' + _type + '?' + (_id ? 'id=' + _id + '&': '') + _search;
}
location.href = _base + _murl;
};
if(_isMobile || _isAndroid || _isIpad){
_redirect2mobile();
return;
}
if(!_pn||_pn=='/') return;
for(var i in _igList){
if(_igList[i].test(_pn)) return;
}
if(top==self){
location.href = '/#'+GUtil.getPathAndHash(location.href);
return;
}
//搜索引擎过来的内容页连接
if(top==self&&/^\/static\/(song|playlist|album|artist)/i.test(_pn)){
location.href = '/#'+_pn.substring(0,_idx).replace('/static/','/')+'?id='+_pn.substring(_idx+1);
}
})();
(function(){
var _addEvent = function(_node,_type,_cb){
if(_node.addEventListener){
_node.addEventListener(_type,_cb);
}else if(_node.attachEvent){
_node.attachEvent('on'+_type,_cb);
}
},
_onAnchorClick = function(_event){//截获所有<a>标签的点击事件，自定义页面的跳转
_event = _event||window.event;
var _el = _event.target||_event.srcElement,
_base = location.protocol+'//'+location.host;
while(_el&&_el!=document){
if(_el.tagName&&_el.tagName.toLowerCase()=='a'){
//fix ie6下有时javascript:;不能阻止默认事件的bug.
if(_el.href.indexOf('javascript:')>=0){
!!_event.preventDefault
? _event.preventDefault()
: _event.returnValue = !1;
return;
}
if(_event.button==2) return;//ff 右键会触发click事件
//商城有独立地顶栏了，排除掉。但会员、数字专辑、单曲的商品、订单页仍保持主站frame，
//这些url往往是通过/vip2, /payfee这样的地址跳转的，也没有问题，如果真的有，URL用#配置就好了
var _path = _el.href.replace(/^https?:\/\/.*?\//i, '/').split(/[?#]/)[0];
if(_path.indexOf('/store/')==0) return;
if(_path.indexOf('/m/at/')==0) return;
//新窗口打开的链接、云音乐单页面形式的链接、站外的链接不做拦截处理。
if(_el.target=='_blank'
||_el.target=='blank'
||_isNotSameHost(_el.href)
||_el.href==_base
||_el.href.indexOf(_base+'/#')>=0) return;
!!_event.preventDefault
? _event.preventDefault()
: _event.returnValue = !1;
location.dispatch2(_el.href);
break;
}else{
_el = _el.parentNode;
}
}
},
_isNotSameHost = function(_href){
var _same = true;
if(_href.charAt(0)!='/'){
var _index = _href.indexOf('//'+location.hostname);
if(_index > 0){
var _index2 = _href.indexOf('?');
if(_index2 > 0 && _index2 < _index){
_same = false;
}
}else{
_same = false;
}
}
return !_same;
};
_addEvent(document,'click',_onAnchorClick);
//扩展一个js中直接使用的页面跳转的方法，以拦截js中的页面跳转行为
location.dispatch2 = function(_url,_replace){
var delegate = false;
try{
delegate = !!top.GDispatcher;
}catch(e){
delegate = false;
}
if(delegate){
top.GDispatcher.dispatch(_url,_replace);
}else{
_url = GUtil.composeRefer(_url,GRef);
//邮箱音乐盒中，每次链接的跳转都要将proxy.html的地址合并到hash中
if(GRef&&GRef=='mail'){
var _hindex,_sindex,
_reg = /(https?:\/\/.+\/proxy.html)/,
_hreg = /#(.*?)$/,
_href = decodeURIComponent(location.href);
if(!_reg.test(decodeURIComponent(_url))&&_reg.test(_href)){
_hindex = _url.indexOf('#');
_sindex = _url.lastIndexOf('?');
if(_hindex>0){
_url = _url+(_sindex>_hindex?'&':'?')+'proxy='+encodeURIComponent(RegExp.$1);
}else{
_url = _url+'#proxy='+encodeURIComponent(RegExp.$1);
}
}
}
if(_replace){
location.replace(_url);
}else{
location.href = _url;
}
}
};
})();(function(){
if(window.addEventListener){
window.addEventListener('scroll', onScroll)
}else{
window.attachEvent('onscroll', onScroll)
}
try{
top.scrollTopbar(0);
}catch(e){
}
function onScroll(){
try{
top.scrollTopbar(Math.max(document.body.scrollTop, document.documentElement.scrollTop));
}catch(e){
//ignore
}
};
})();</script>
<base href="//music.163.com/" target="_top">
<link rel="shortcut icon" href="//s1.music.126.net/music.ico?v1" />
<link href="//s2.music.126.net/web/s/core.css?a448caf6c3ffc14adc6bfa960ae97855" type="text/css" rel="stylesheet"/><link href="//s2.music.126.net/web/s/pt_frame.css?ffd1572ccdecf55728531020c67a7389" type="text/css" rel="stylesheet"/>
</head>
<body>
<div data-module="discover" data-sub="other" id="g_top" class="m-top">&nbsp;</div>
<div id="g_nav" class="m-subnav">&nbsp;</div>
<script>
try{
top.matchNav("discover", "other");
}catch(e){
}
</script>
<div id="m-playlist" class="g-bd4 f-cb">
<div class="g-mn4">
<div class="g-mn4c">
<div class="g-wrap6">
<div class="m-info f-cb" id="auto-id-Mt2ToAb4W4VIExnM">
<div class="cover u-cover u-cover-dj">
<img src="http://p3.music.126.net/8xYnBPl89VLi8pqaJJOqXg==/18964376556038798.jpg?param=200y200" class="j-img" data-src="http://p3.music.126.net/8xYnBPl89VLi8pqaJJOqXg==/18964376556038798.jpg" data-key="OmbJA"/>
<span class="msk"></span>
</div>
<div class="cnt">
<div class="cntc">
<div class="hd f-cb">
<i class="f-fl u-icn u-icn-13"></i>
<div class="tit">
<h2 class="f-ff2 f-brk">吃个早茶饼喜欢的音乐</h2>
</div>
</div>
<div class="user f-cb">
<a class="face" href="/user/home?id=254672398"><img src="http://p1.music.126.net/4NTr7krypDRZh8Pk1PwvCg==/3295236359974156.jpg?param=40y40"></a>
<span class="name">
<a href="/user/home?id=254672398" class="s-fc7">吃个早茶饼</a>
</span>
<span class="time s-fc4">2016-03-17&nbsp;创建</span>
</div>
<div id="content-operation" class="btns f-cb" data-rid="319135616" data-type="13" data-special="5" >
<a data-res-action="play"
data-res-id="319135616"
data-res-type="13"
href="javascript:;" class="u-btn2 u-btn2-2 u-btni-addply f-fl" hidefocus="true" title="播放"><i><em class="ply"></em>播放</i></a>
<a data-res-action="addto"
data-res-id="319135616"
data-res-type="13"
href="javascript:;" class="u-btni u-btni-add" hidefocus="true" title="添加到播放列表"></a>
<a data-res-id="319135616"
data-res-type="13"
data-count="0"
data-res-action="fav"
class="u-btni u-btni-fav " href="javascript:;">
<i>收藏</i>
</a>
<a data-res-id="319135616"
data-res-type="13"
data-count="0"
data-res-action="share"
data-res-name="吃个早茶饼喜欢的音乐"
data-res-author="吃个早茶饼"
data-res-authors=""
data-res-pic="http://p1.music.126.net/8xYnBPl89VLi8pqaJJOqXg==/18964376556038798.jpg"
class="u-btni u-btni-share " href="javascript:;"><i>分享</i></a>
<a data-res-id="319135616"
data-res-type="13"
data-res-action="download"
class="u-btni u-btni-dl " href="javascript:;"><i>下载</i></a>
<a data-res-action="comment" href="javascript:;" class="u-btni u-btni-cmmt "><i>(<span id="cnt_comment_count">1</span>)</i></a>
</div>
</div>
</div>
</div>
<div class="n-songtb">
<div class="u-title u-title-1 f-cb">
<h3>
<span class="f-ff2">歌曲列表</span>
</h3>
<span class="sub s-fc3"><span id="playlist-track-count">98</span>首歌</span>
<div class="more s-fc3">播放：<strong id="play-count" class="s-fc6">798</strong>次</div>
<div class="out out-list s-fc3">
<i class="u-icn u-icn-95 f-fl"></i>
<a data-action="outchain" data-href="/outchain/0/319135616/" class="des s-fc7">生成外链播放器</a>
</div>
</div>
<div id="song-list-pre-cache" data-key="track_playlist-319135616" data-simple="1" data-pvnamed="1">
<div class="u-load s-fc4"><i class="icn"></i> 加载中...</div>
<ul class="f-hide"><li><a href="/song?id=480769052">俗人言</a></li><li><a href="/song?id=28234970">想把我唱给你听</a></li><li><a href="/song?id=5253801">Free Loop</a></li><li><a href="/song?id=2864538">Happy Birthday</a></li><li><a href="/song?id=22703777">Lil' Goldfish</a></li><li><a href="/song?id=449578813">行歌</a></li><li><a href="/song?id=31654492">声律启蒙</a></li><li><a href="/song?id=456185374">别送我</a></li><li><a href="/song?id=470057375">至此流年各天涯</a></li><li><a href="/song?id=448184048">化身孤岛的鲸</a></li><li><a href="/song?id=1210496">What Are Words</a></li><li><a href="/song?id=28953033">Shake It Off</a></li><li><a href="/song?id=36703311">我在里贾纳晚上十点的阳光下</a></li><li><a href="/song?id=475072295">清白之年</a></li><li><a href="/song?id=30394673">午餐</a></li><li><a href="/song?id=36308916">Monody</a></li><li><a href="/song?id=417250673">父亲写的散文诗(时光版)</a></li><li><a href="/song?id=28167426">温柔 (Live)</a></li><li><a href="/song?id=18578526">A Penny For The Band</a></li><li><a href="/song?id=186139">安静</a></li><li><a href="/song?id=30431367">走马</a></li><li><a href="/song?id=463840571">好在</a></li><li><a href="/song?id=448144319">今年勇</a></li><li><a href="/song?id=465677131">深夜书店</a></li><li><a href="/song?id=31445772">理想三旬</a></li><li><a href="/song?id=38592976">Dream It Possible</a></li><li><a href="/song?id=27646786">活着</a></li><li><a href="/song?id=1491585">Traveling Light</a></li><li><a href="/song?id=29535531">历历万乡</a></li><li><a href="/song?id=480353">いつも何度でも</a></li><li><a href="/song?id=22712173">Refrain</a></li><li><a href="/song?id=27678693">再遇见</a></li><li><a href="/song?id=28285912">爱呀</a></li><li><a href="/song?id=26505369">Talk</a></li><li><a href="/song?id=357126">Tassel</a></li><li><a href="/song?id=26060065">Counting Stars</a></li><li><a href="/song?id=28747425">Tell Me If You Wanna Go Home</a></li><li><a href="/song?id=186016">晴天</a></li><li><a href="/song?id=254328">原来你也在这里</a></li><li><a href="/song?id=149297">夜的钢琴曲五</a></li><li><a href="/song?id=37239018">Everglow</a></li><li><a href="/song?id=29567192">少年锦时</a></li><li><a href="/song?id=16439857">When You Say Nothing At All</a></li><li><a href="/song?id=16607998">The Show</a></li><li><a href="/song?id=19711382">New Soul</a></li><li><a href="/song?id=30706076">Goodbye</a></li><li><a href="/song?id=1697653">You Are Not Alone</a></li><li><a href="/song?id=254039">偶阵雨</a></li><li><a href="/song?id=408814900">借我</a></li><li><a href="/song?id=415086030">我从崖边跌落</a></li><li><a href="/song?id=20707713">You Raise Me Up</a></li><li><a href="/song?id=408307811">恋曲1990（Cover 罗大佑）</a></li><li><a href="/song?id=29999506">莫失莫忘</a></li><li><a href="/song?id=28996630">Tomorrow With You</a></li><li><a href="/song?id=1674192">More Than I Can Say</a></li><li><a href="/song?id=36990266">Faded</a></li><li><a href="/song?id=3986326">Fix You</a></li><li><a href="/song?id=2533578">You Are My Sunshine</a></li><li><a href="/song?id=368727">明天，你好</a></li><li><a href="/song?id=280120">梦一场</a></li><li><a href="/song?id=1494060">Your Man</a></li><li><a href="/song?id=28661564">Maps</a></li><li><a href="/song?id=4083399">Far Away From Home</a></li><li><a href="/song?id=139730">安静的午后</a></li><li><a href="/song?id=413831772">小幸运钢琴版(Pianoboy_COVER)</a></li><li><a href="/song?id=308353">钟无艳</a></li><li><a href="/song?id=405253305">写给你的歌</a></li><li><a href="/song?id=32957955">逝年</a></li><li><a href="/song?id=411754937">夕阳下的歌</a></li><li><a href="/song?id=39635939">旧时光</a></li><li><a href="/song?id=41633177">我们在世上流浪</a></li><li><a href="/song?id=410042507">这场名叫人生的旅途</a></li><li><a href="/song?id=33378164">Let Her Go (DOAN Remix)</a></li><li><a href="/song?id=3950116">Big Big World</a></li><li><a href="/song?id=25657282">Marry You</a></li><li><a href="/song?id=29535483">Immortals (End Credit Version) ["From "Big Hero 6”]</a></li><li><a href="/song?id=27901416">哆啦a梦</a></li><li><a href="/song?id=32166628">Summertime</a></li><li><a href="/song?id=496549">Chiru (Saisei no Uta)</a></li><li><a href="/song?id=247634">想起</a></li><li><a href="/song?id=247498">那年的情书</a></li><li><a href="/song?id=229401">到不了</a></li><li><a href="/song?id=22844535">Moon Flow</a></li><li><a href="/song?id=34033985">La Vida Seguirá</a></li><li><a href="/song?id=407764471">漂洋过海来看你 唯美钢琴版</a></li><li><a href="/song?id=392367">经过</a></li><li><a href="/song?id=110359">练习(Live) - live</a></li><li><a href="/song?id=223960">爱过</a></li><li><a href="/song?id=223638">多么想念你</a></li><li><a href="/song?id=223972">街角的祝福</a></li><li><a href="/song?id=223794">小小</a></li><li><a href="/song?id=224000">怎样</a></li><li><a href="/song?id=223636">光着我的脚丫子</a></li><li><a href="/song?id=1606099">Lost Without You</a></li><li><a href="/song?id=27863779">Staring At You</a></li><li><a href="/song?id=16574705">Better in Time (Single Mix)</a></li><li><a href="/song?id=32648199">Sound of Your Heart</a></li><li><a href="/song?id=37653063">Please Don't Go</a></li></ul>
<textarea style="display:none;">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
</textarea>
</div>
</div>
<div class="n-cmt" id="comment-box" data-tid=A_PL_0_319135616 data-count=1 data-uid=254672398></div>
</div>
</div>
</div>
<div class="g-sd4">
<div class="g-wrap7">
<div id="j-music-ad" class="m-sidead f-hide" data-has-music-ad="0">
<div class="j-flag f-hide"></div>
<div class="f-hide j-flag">
<ins class="adsbydm" inner-prod="adbid" inner-width="200" inner-height="220" inner-src="http://iad.g.163.com/wa/ad?site=netease&affiliate=music&cat=detail&type=logo200x220&location=1" check-src="http://iad.g.163.com/wa/ad_check?site=netease&affiliate=music&cat=detail&type=logo200x220&location=1"></ins>
</div>
</div>
<h3 class="u-hd3">
<span class="f-fl">热门歌单</span>
</h3>
<ul class="m-rctlist f-cb">
<li>
<div class="cver u-cover u-cover-3">
<a href="/playlist?id=2073888683" title="我很想念你，你有没有想起我"
data-res-id="2073888683"
data-res-type="13"
data-res-action="log"
data-res-data="recommendclick|0||playlist-playlist-recommend|319135616"
><img src="http://p1.music.126.net/8PfVKd_95-VhU8LvIc2r2Q==/109951163118307140.jpg?param=50y50">
</a>
</div>
<div class="info">
<p class="f-thide">
<a class="sname f-fs1 s-fc0" href="/playlist?id=2073888683" title="我很想念你，你有没有想起我"
data-res-id="2073888683"
data-res-type="13"
data-res-action="log"
data-res-data="recommendclick|0||playlist-playlist-recommend|319135616"
>我很想念你，你有没有想起我</a>
</p>
<p><span class="by s-fc4">by</span><a class="nm nm f-thide s-fc3" href="/user/home?id=103780233" title="雾与晨的杂货店">雾与晨的杂货店</a>
<sup class="u-icn u-icn-1 "></sup>
</div>
</li>
<li>
<div class="cver u-cover u-cover-3">
<a href="/playlist?id=978161852" title="ღ 你 是 我 心 甘 情 愿 的 劫 ღ"
data-res-id="978161852"
data-res-type="13"
data-res-action="log"
data-res-data="recommendclick|1||playlist-playlist-recommend|319135616"
><img src="http://p1.music.126.net/HO2GUd7BoVU-TgPJPyRVgQ==/109951163133237645.jpg?param=50y50">
</a>
</div>
<div class="info">
<p class="f-thide">
<a class="sname f-fs1 s-fc0" href="/playlist?id=978161852" title="ღ 你 是 我 心 甘 情 愿 的 劫 ღ"
data-res-id="978161852"
data-res-type="13"
data-res-action="log"
data-res-data="recommendclick|1||playlist-playlist-recommend|319135616"
>ღ 你 是 我 心 甘 情 愿 的 劫 ღ</a>
</p>
<p><span class="by s-fc4">by</span><a class="nm nm f-thide s-fc3" href="/user/home?id=107044126" title="Spyromun_">Spyromun_</a>
<sup class="u-icn u-icn-84 "></sup>
</div>
</li>
<li>
<div class="cver u-cover u-cover-3">
<a href="/playlist?id=2027700851" title="『日系』这封信寄给不会陪伴我的你"
data-res-id="2027700851"
data-res-type="13"
data-res-action="log"
data-res-data="recommendclick|2||playlist-playlist-recommend|319135616"
><img src="http://p1.music.126.net/QiaiXaFIZEmhan8PNMmEKQ==/109951163107237272.jpg?param=50y50">
</a>
</div>
<div class="info">
<p class="f-thide">
<a class="sname f-fs1 s-fc0" href="/playlist?id=2027700851" title="『日系』这封信寄给不会陪伴我的你"
data-res-id="2027700851"
data-res-type="13"
data-res-action="log"
data-res-data="recommendclick|2||playlist-playlist-recommend|319135616"
>『日系』这封信寄给不会陪伴我的你</a>
</p>
<p><span class="by s-fc4">by</span><a class="nm nm f-thide s-fc3" href="/user/home?id=98315791" title="原风Fay">原风Fay</a>
</div>
</li>
<li>
<div class="cver u-cover u-cover-3">
<a href="/playlist?id=946036828" title="说唱告白│我是北方的红色 你是南方的斑马"
data-res-id="946036828"
data-res-type="13"
data-res-action="log"
data-res-data="recommendclick|3||playlist-playlist-recommend|319135616"
><img src="http://p1.music.126.net/lTF_2QTV7JWceRFE__z3Pg==/19062233091128058.jpg?param=50y50">
</a>
</div>
<div class="info">
<p class="f-thide">
<a class="sname f-fs1 s-fc0" href="/playlist?id=946036828" title="说唱告白│我是北方的红色 你是南方的斑马"
data-res-id="946036828"
data-res-type="13"
data-res-action="log"
data-res-data="recommendclick|3||playlist-playlist-recommend|319135616"
>说唱告白│我是北方的红色 你是南方的斑马</a>
</p>
<p><span class="by s-fc4">by</span><a class="nm nm f-thide s-fc3" href="/user/home?id=17711631" title="-KooTo-">-KooTo-</a>
<sup class="u-icn u-icn-84 "></sup>
</div>
</li>
<li>
<div class="cver u-cover u-cover-3">
<a href="/playlist?id=2087725103" title="【超级碗2018】贾老板的中场盛事"
data-res-id="2087725103"
data-res-type="13"
data-res-action="log"
data-res-data="recommendclick|4||playlist-playlist-recommend|319135616"
><img src="http://p1.music.126.net/55o6hXrDVlQCgSbk5Tnyiw==/109951163132914367.jpg?param=50y50">
</a>
</div>
<div class="info">
<p class="f-thide">
<a class="sname f-fs1 s-fc0" href="/playlist?id=2087725103" title="【超级碗2018】贾老板的中场盛事"
data-res-id="2087725103"
data-res-type="13"
data-res-action="log"
data-res-data="recommendclick|4||playlist-playlist-recommend|319135616"
>【超级碗2018】贾老板的中场盛事</a>
</p>
<p><span class="by s-fc4">by</span><a class="nm nm f-thide s-fc3" href="/user/home?id=37316751" title="KFM981">KFM981</a>
<sup class="u-icn u-icn-1 "></sup>
</div>
</li>
</ul>
<div class="m-multi" >
<h3 class="u-hd3">
<span class="f-fl">网易云音乐多端下载</span>
</h3>
<ul class="bg f-cb">
<li><a data-res-action="bilog" data-log-action="downloadapp" data-log-json='{"type":"iPhone","source":"detail"}' href="https://itunes.apple.com/app/id590338362" class="ios" hidefocus="true" target="_blank">iPhone</a></li>
<li><a data-res-action="bilog" data-log-action="downloadapp" data-log-json='{"type":"pc","source":"detail"}' href="http://music.163.com/api/pc/download/latest" class="pc" hidefocus="true" target="_blank">PC</a></li>
<li><a data-res-action="bilog" data-log-action="downloadapp" data-log-json='{"type":"android","source":"detail"}' href="http://music.163.com/api/android/download/latest2" class="aos" hidefocus="true" target="_blank">Android</a></li>
</ul>
<p class="s-fc4">同步歌单，随时畅听320k好音乐</p>
</div>
</div>
</div>
</div>
<div class="g-ft ">
<div class="m-ft">
<div class="wrap f-cb">
<div class="copy">
<p>
<a href="//music.163.com/about" target="_blank" class="s-fc4">关于网易</a><span class="line">|</span>
<a href="//help.163.com/" target="_blank" class="s-fc4">客户服务</a><span class="line">|</span>
<a href="//music.163.com/html/web2/service.html" target="_blank" class="s-fc4">服务条款</a><span class="line">|</span>
<a href="//sitemap.163.com/" target="_blank" class="s-fc4">网站导航</a><span class="line">|</span>
<a id="g_feedback" href="#" class="s-fc4" onclick="nm.x.feedback();return false;" hidefocus="true">意见反馈</a>
</p>
<p class="s-fc3">
<span class="sep">网易公司版权所有©1997-2018</span>杭州乐读科技有限公司运营：<a href="http://p1.music.126.net/-DB9zs1FAJq8vg7HOb-yOQ==/3250156395654666.jpg" target="_blank" class="s-fc3">浙网文[2015] 0415-135号</a>
</p>
</div>
<ul class="enter f-fr">
<li>
<a class="logo logo-musician f-tid" href="//music.163.com/recruit" target="_blank">独立音乐人</a>
</li>
<li>
<a class="logo logo-topic f-tid" href="//music.163.com/topic/recruit" target="_blank">音乐专栏</a>
</li>
<li>
<a class="logo logo-midea f-tid" href="//music.163.com/topic/selfmedia" target="_blank">自媒体</a>
</li>
<li>
<a class="logo logo-reward f-tid" href="//music.163.com/web/reward" target="_blank">赞赏</a>
</li>
</ul>
</div>
</div>
</div>
<a title="回到顶部" class="m-back" href="#" id="g_backtop" hidefocus="true" style="display:none;">回到顶部</a>
<div id="template-box" style="display:none;"> <textarea name="ntp" id="m-wgt-selector" style="display:none;"><div class="u-slt f-pr"><span class="curr f-thide"></span><i class="btn"></i><ul></ul></div>
</textarea>
<textarea name="jst" id="m-wgt-selector-list" style="display:none;">{list data as x}<li class="f-thide"><a href="#" data-value="${x.v}" title="${x.t}">${x.t}</a></li>{/list}
</textarea>
<textarea name="ntp" id="m-wgt-create" style="display:none;"><div class="lyct m-crgd f-cb f-tc">
<p>歌单名：<input type="text" class="u-txt j-flag"></p>
<div class="u-err f-vhide j-flag"><i class="u-icn u-icn-25"></i>错误提示</div>
<p class="tip s-fc4">可通过“收藏”将音乐添加到新歌单中</p>
<div class="btn">
<a href="javascript:;" class="u-btn2 u-btn2-2 u-btn2-w2 j-flag" hidefocus="true"><i>新 建</i></a>
<a href="javascript:;" class="u-btn2 u-btn2-1 u-btn2-w2 j-flag" hidefocus="true"><i>取 消</i></a>
</div>
</div>
</textarea>
<textarea name="ntp" id="m-wgt-comment" style="display:none;"><div class="u-title u-title-1">
<h3><span class="f-ff2">评论</span></h3><span class="sub s-fc3">共<span class="j-flag">0</span>条评论</span>
</div>
<div class="m-cmmt">
<div class="iptarea">
<div class="head"><img src="http://s4.music.126.net/style/web2/img/default/default_avatar.jpg?param=50y50"></div>
<div class="j-flag"></div>
</div>
<div class="cmmts j-flag"></div>
<div class="j-flag"></div>
</div>
</textarea>
<textarea name="ntp" id="m-wgt-comment2" style="display:none;"><div class="m-dynamic">
<div class="dbox dbox-cmt">
<span class="darr"><i class="bd">◆</i><i class="bg">◆</i></span>
<div class="m-cmmt m-cmmt-s">
<div class="iptarea j-flag">
</div>
<div class="cmmts">
<div class="j-flag"></div>
<div class="dmore dmore-cmt f-cb">
<div class="dhas s-fc3">后面还有<span class="j-flag">0</span>条评论，<a data-type="viewmore" class="s-fc3 f-ff1" href="javascript:void(0)">查看更多&gt;</a></div>
<a data-type="cc" class="dtoggle" href="javascript:void(0)">收起<i data-type="cc" class="u-icn u-icn-61"></i></a>
</div>
</div>
</div>
</div>
</div>
</textarea>
<textarea name="ntp" id="m-wgt-comment3" style="display:none;"><div class="dcmt">
<p><span class="f-fw1">评论</span> (<span class="j-flag"></span>)</p>
<div class="m-cmmt m-cmmt-s">
<div class="iptarea j-flag">
</div>
<div class="cmmts j-flag">
</div>
<div class="j-flag">
</div>
</div>
</div>
</textarea>
<textarea name="jst" id="m-wgt-comment-item" style="display:none;"> {list beg..end as y}
{var x=xlist[y]}
{if !!x}
<div id="${x.commentId|seed}" class="itm" data-id="${x.commentId}">
<div class="head">
<a href="/user/home?id=${x.user.userId}"><img src="${x.user.avatarUrl}?param=50y50"></a>
</div>
<div class="cntwrap">
<div class="">
<div class="cnt f-brk">
<a href="/user/home?id=${x.user.userId}" class="s-fc7">${escape(x.user.nickname)}</a>
${getAuthIcon(x.user)}
{if !!x.beRepliedUser}
&nbsp;回复&nbsp;<a href="/user/home?id=${x.beRepliedUser.userId}" class="s-fc7">${escape(x.beRepliedUser.nickname)}</a>
${getAuthIcon(x.beRepliedUser)}
{/if}
：${getRichText(escape(x.content),'s-fc7')}
</div>
</div>
{if x.beReplied&&x.beReplied.length}
{var replied = x.beReplied[0]}
<div class="que f-brk f-pr s-fc3">
<span class="darr"><i class="bd">◆</i><i class="bg">◆</i></span>
{if replied&&replied.content&&replied.status!=-5}
<a class="s-fc7" href="/user/home?id=${replied.user.userId}">${replied.user.nickname}${getAuthIcon(replied.user)}</a>：${getRichText(escape(replied.content),'s-fc7')}
{else}
该评论已删除
{/if}
</div>
{/if}
<div class="rp">
<div class="time s-fc4">${timeformat(x.time)}</div>
{if x.topCommentId}<span class="top">音乐人置顶</span>{/if}
{if canTop()&&GUser&&GUser.userId&&(GUser.userId==x.user.userId)}
<span class="dlt">{if x.topCommentId}<a href="javascript:void(0)" class="s-fc3" data-id="${x.commentId}" data-tid="${x.topCommentId}" data-type="canceltop">解除置顶</a>{else}<a href="javascript:void(0)" class="s-fc3" data-id="${x.commentId}" data-type="gotop">置顶评论</a>{/if}<span class="sep">|</span></span>
{/if}
{if GUser&&GUser.userId&&(GUser.userId==x.user.userId||GUser.userId==resUserId)}
<span class="dlt"><a href="javascript:void(0)" class="s-fc3" data-id="${x.commentId}" {if x.topCommentId}data-tid="${x.topCommentId}" {/if}data-type="delete">删除</a><span class="sep">|</span></span>
{/if}
{if GAllowRejectComment}
{if hot||!x.isRemoveHotComment}
<span class="dlt"><a href="javascript:void(0)" class="s-fc3" data-id="${x.commentId}" data-type="reject">移除精彩评论</a><span class="sep">|</span></span>
{else}
<span class="s-fc3">已移除精彩评论</span><span class="sep">|</span>
{/if}
{/if}
{if !x.topCommentId}<a data-id="${x.commentId}" data-type="{if !x.liked}like{else}unlike{/if}" href="javascript:void(0)"><i class="zan u-icn2 u-icn2-{if x.liked}13{else}12{/if}"></i>{if x.likedCount} (${getPlayCount(x.likedCount)}){/if}</a>
<span class="sep">|</span>{/if}
<a href="javascript:void(0)" class="s-fc3" data-id="${x.commentId}" data-type="reply">回复</a>
</div>
</div>
</div>
{/if}
{/list}
</textarea>
<textarea name="jst" id="m-wgt-comment-item-2" style="display:none;"> {list beg..end as y}
{var x=xlist[y]}
<div class="itm" data-id="${x.commentId}">
<div class="head">
<a href="/user/home?id=${x.user.userId}"><img src="${x.user.avatarUrl}?param=50y50"></a>
</div>
<div class="cntwrap">
<div class="cnt2 f-brk">
<a href="/user/home?id=${x.user.userId}" class="s-fc7">${escape(x.user.nickname)}</a>
${getAuthIcon(x.user)}
{if !!x.beRepliedUser}
&nbsp;回复&nbsp;<a href="/user/home?id=${x.beRepliedUser.userId}" class="s-fc7">${escape(x.beRepliedUser.nickname)}</a>
${getAuthIcon(x.beRepliedUser)}
{/if}
：${getRichText(escape(x.content),'s-fc7')}
</div>
{if x.beReplied&&x.beReplied.length}
{var replied = x.beReplied[0]}
<div class="que f-brk f-pr s-fc3">
<span class="darr"><i class="bd">◆</i><i class="bg">◆</i></span>
{if replied&&replied.content}
<a class="s-fc7" href="/user/home?id=${replied.user.userId}">${replied.user.nickname}${getAuthIcon(replied.user)}</a>：${getRichText(escape(replied.content),'s-fc7')}
{else}
该评论已删除
{/if}
</div>
{/if}
<div class="rp">
<div class="time s-fc4">${timeformat(x.time)}</div>
{if GUser&&GUser.userId&&(GUser.userId==x.user.userId||GUser.userId==resUserId)}
<span class="dlt">
<a href="javascript:void(0)" class="s-fc3" data-id="${x.commentId}" data-type="delete">删除</a><span class="sep">|</span>
</span>
{/if}
<a data-id="${x.commentId}" data-type="{if !x.liked}like{else}unlike{/if}" href="javascript:void(0)"><i class="zan u-icn2 u-icn2-{if x.liked}13{else}12{/if}"></i>{if x.likedCount} (${getPlayCount(x.likedCount)}){/if}</a>
<span class="sep">|</span>
<a href="javascript:void(0)" class="s-fc3" data-id="${x.commentId}" data-type="reply">回复</a>
</div>
</div>
</div>
{/list}
</textarea>
<textarea name="jst" id="m-wgt-input-1" style="display:none;"> <div class="m-cmmtipt f-cb f-pr">
<div class="u-txtwrap holder-parent f-pr">
<textarea class="u-txt area j-flag" data-type="" placeholder="${placeholder}"><&#47;textarea>
</div>
<div class="btns f-cb f-pr">
<i class="icn u-icn u-icn-36 j-flag"></i><i class="icn u-icn u-icn-41 j-flag"></i>
<a href="javascript:void(0)" class="btn u-btn u-btn-1 j-flag">评论</a>
<span class="zs s-fc4 j-flag">110/120</span>
</div>
<div class="corr u-arr"><em class="arrline">◆</em><span class="arrclr">◆</span></div>
</div>
</textarea>
<textarea name="jst" id="m-wgt-input-2" style="display:none;"> <div class="rept m-quk m-quk-1 f-pr">
<div class="iner">
<div class="corr u-arr u-arr-1"><em class="arrline">◆</em><span class="arrclr">◆</span></div>
<div class="m-cmmtipt m-cmmtipt-1 f-cb f-pr">
<div class="u-txtwrap holder-parent f-pr j-wrap">
<textarea class="u-txt area j-flag" placeholder="${placeholder}"><&#47;textarea>
</div>
<div class="btns f-cb f-pr">
<i class="icn u-icn u-icn-36 j-flag"></i><i class="icn u-icn u-icn-41 j-flag"></i>
<a href="javascript:void(0)" class="btn u-btn u-btn-1 j-flag">回复</a>
<span class="zs s-fc4 j-flag">110/120</span>
</div>
</div>
</div>
</div>
</textarea>
<textarea name="jst" id="m-wgt-input-3" style="display:none;"> <div class="m-cmmtipt f-cb f-pr">
<div class="u-txtwrap holder-parent f-pr">
<textarea class="u-txt area j-flag" placeholder="${placeholder}"><&#47;textarea>
</div>
<div class="btns f-cb f-pr">
<i class="icn u-icn u-icn-36 j-flag"></i><i class="icn u-icn u-icn-41 j-flag"></i>
<a class="btn u-btn u-btn-1 j-flag" href="javascript:void(0)">回复</a>
<span class="zs s-fc4 j-flag">110/120</span>
</div>
</div>
</textarea>
<textarea name="jst" id="m-wgt-input-4" style="display:none;"> <div class="m-cmmtipt f-cb f-pr">
<div class="u-txtwrap f-pr">
<textarea class="u-txt area j-flag"><&#47;textarea>
</div>
<div class="btns f-cb f-pr">
<i class="icn u-icn u-icn-36 j-flag"></i><i class="icn u-icn u-icn-41 j-flag" style="display:none;"></i>
<a class="f-fr u-btn u-btn-1 j-flag" href="javascript:void(0)">发送</a><span class="zs s-fc4 j-flag">110/120</span>
</div>
</div>
</textarea>
<textarea name="jst" id="m-wgt-input-5" style="display:none;"> <div class="m-cmmtipt f-cb f-pr">
<div class="u-txtwrap holder-parent f-pr">
<textarea class="u-txt area j-flag" placeholder="${placeholder}"><&#47;textarea>
</div>
<div class="btns f-cb f-pr">
<i class="icn u-icn u-icn-36 j-flag"></i><i class="icn u-icn u-icn-41 j-flag"></i>
<a class="btn u-btn u-btn-1 j-flag" href="javascript:void(0)">评论</a>
<span class="zs s-fc4 j-flag">110/120</span>
</div>
</div>
</textarea>
<textarea name="jst" id="m-wgt-input-6" style="display:none;"> <div class="m-cmmtipt f-cb f-pr">
<div class="u-txtwrap holder-parent f-pr">
<textarea class="u-txt area j-flag" placeholder="${placeholder}"><&#47;textarea>
</div>
<div class="btns f-cb f-pr">
<i class="icn u-icn u-icn-36 j-flag"></i><i class="icn u-icn u-icn-41 j-flag"></i>
<a class="btn u-btn u-btn-1 j-flag" href="javascript:void(0)">发送</a>
<span class="zs s-fc4 j-flag">110/120</span>
</div>
</div>
</textarea>
<textarea name="ntp" id="m-wgt-subscribe" style="display:none;"><div class="lyct lyct-1 m-favgd f-cb">
<div class="tit j-flag"><i class="u-icn u-icn-33"></i>新歌单</div>
<div class="j-flag">
<div class="u-load s-fc4"><i class="icn"></i> 加载中...</div>
</div>
</div>
</textarea>
<textarea name="jst" id="m-wgt-subscribe-item" style="display:none;"><ul>
{list beg..end as y}
{var x=xlist[y]}
<li data-id="${x.id}" class="xtag {if x.trackCount+size>10000}dis{/if}">
<div class="item f-cb">
<div class="left">
<a href="javascript:void(0)" class="avatar" target="_blank">
<img alt="" src="${x.coverImgUrl}?param=40y40">
{if x.highQuality}<i class="u-jp u-icn2 u-icn2-jp5"></i>{/if}
</a>
</div>
<p class="name f-thide"><a class="s-fc0" href="javascript:void(0)" target="_blank">${escape(cutStr(x.name,40))}</a></p>
<p class="s-fc3">${x.trackCount}首</p>
{if x.trackCount+size>10000}<p class="limit">歌单已满</p>{/if}
</div>
</li>
{/list}
</ul>
</textarea>
<textarea name="ntp" id="m-wgt-forward" style="display:none;"><div class="lyct lyct-1 f-cb">
<div class="m-lyshare">
<div class="u-txtwrap f-pr">
<label style="display: block;" class="j-flag">说点什么</label>
<textarea class="u-txt area j-flag" text = ><&#47;textarea>
</div>
<div class="oper f-cb j-flag">
<div class="face f-fl f-pr">
<i class="u-icn u-icn-36 f-fl j-flag"></i>
<i class="u-icn u-icn-41 j-flag"></i>
</div>
<span class="zs f-fr s-fc3 j-flag">140</span>
</div>
<div class="btnwrap">
<a class="u-btn2 u-btn2-2 u-btn2-w2 j-flag" hidefocus="true" href="#"><i>转发</i></a>
<a class="u-btn2 u-btn2-1 u-btn2-w2 j-flag" hidefocus="true" href="#"><i>取消</i></a>
</div>
<div class="j-flag u-err"><i class="u-icn u-icn-25"></i><span></span></div>
</div>
</div>
</textarea>
<textarea name="ntp" id="m-import-ok" style="display:none;"><div class="lyct f-cb f-tc">
<p class="f-fs3 f-ff2"><i class="u-icn u-icn-76"></i>&nbsp;&nbsp;歌曲同步完成</p>
<div class="lybtn">
<a href="javascript:;" class="u-btn2 u-btn2-2 j-flag" hidefocus="true"><i>查看我的音乐</i></a>
</div>
</div>
</textarea>
<textarea name="jst" id="m-wgt-atlist" style="display:none;"> <div class="u-atlist">
{if suggests.length == 0}
<p>轻敲空格完成输入</p>
{else}
<p>选择最近@的人或直接输入</p>
{/if}
<div class="lst">
{list suggests as suggest}
<a href="javascript:;" data-index=${suggest_index} class="f-thide j-sgt">${suggest.nickname}</a>
{/list}
</div>
</div>
</textarea>
<textarea name="jst" id="m-wgt-receiverInput" style="display:none;"> <div class="ct f-pr">
<div class="u-txtwrap f-pr">
<div class="u-txt txtwrap j-flag">
{if receiver}
<div class="blk s-fc3 j-receiver">${receiver.nickname}<a href="#" class="cls" title="删除">&times;</a></div>
{/if}
<span class="holder-parent j-flag" style="float:left">
<input type="text" class="txt j-flag" />
<label class="holder j-flag">选择或输入好友昵称</label>
</span>
</div>
</div>
<ul class="full j-flag" style="_height:182px;display:none">
{list users as user}
<li class="j-item" data-userId=${user.userId} data-username=${user.nickname} data-index=${user_index}><a href="#"><img src=${user.avatarUrl}>${user.nickname}</a></li>
{/list}
</ul>
<div class="j-flag" style="position:absolute;left: -1000px;width:auto;"></div>
</div>
</textarea>
<textarea name="jst" id="m-wgt-receiverList" style="display:none;"> {list users as user}
<li class="j-item" data-userId=${user.userId} data-username=${user.nickname} data-index=${user_index}><a href="#"><img src=${user.avatarUrl}>${user.nickname}</a></li>
{/list}
</textarea>
<textarea name="ntp" id="m-wgt-sharewin" style="display:none;"><div class="lyct lyct-1 f-cb">
<div class="m-lyshare">
<ul class="m-tabs1 j-flag">
<li><a href="#"><em>分享给大家</em></a></li>
<li><a href="#"><em>私信分享</em></a></li>
</ul>
<div class="u-err j-flag" style="display:none">最多选择10位好友</div>
<div class="j-flag"></div>
<div class="j-slogan"></div>
<div class="u-txtwrap f-pr">
<textarea class="u-txt area j-flag" placeholder="说点什么吧" data-action="txt"><&#47;textarea>
<div class="info f-pr j-flag" data-action="search"></div>
</div>
<div class="oper f-cb">
<div class="face f-fl f-pr">
<i class="u-icn u-icn-36 f-fl j-flag" data-action="emot"></i>
<i class="u-icn u-icn-41 f-fl j-flag" data-action="at"></i>
<i class="u-icn u-icn-97 j-flag f-pr" data-action="upload" data-default></i>
</div>
<span class="f-fr s-fc4 j-flag">140/140</span>
</div>
<div class="f-cb j-flag"></div>
<div class="f-cb">
<div class="btnwrap f-fl">
<a class="u-btn2 u-btn2-2 u-btn2-w2 j-flag" hidefocus="true" href="javascript:;" data-action="share"><i>分享</i></a>
<a class="u-btn2 u-btn2-1 u-btn2-w2 j-flag" hidefocus="true" href="javascript:;" data-action="close"><i>取消</i></a>
</div>
<div class="f-cb j-flag f-fr">
<div class="share f-fr">
<span class="f-fl s-fc3">同时分享到：</span>
<ul class="u-logo u-logo-s f-cb">
<li><a class="u-slg u-slg-sn j-t" data-action="sns" data-type="2" hidefocus="true" href="//music.163.com/api/sns/authorize?snsType=2&clientType=web2&callbackType=Binding&forcelogin=true" title="新浪微博"></a></li>
<li><a class="u-slg u-slg-db j-t" data-action="sns" data-type="3" hidefocus="true" href="//music.163.com/api/sns/authorize?snsType=3&clientType=web2&callbackType=Binding&forcelogin=true" title="豆瓣网"></a></li>
</ul>
</div>
</div>
</div>
<div class="u-err j-flag"><i class="u-icn u-icn-25"></i><span></span></div>
</div>
</div>
</textarea>
<textarea name="jst" id="m-search-suggest" style="display:none;">{macro listArtists(artists)}
{list artists as art}
${art.name|mark}&nbsp;
{/list}
{/macro}
<div class="m-schlist">
<p class="note s-fc3"><a class="s-fc3 xtag" href="/search/#/?s=${keyword}&type=1002">搜“${keyword|cutStr}” 相关用户</a> &gt;</p>
<div class="rap">
{list result.order as index}
{var lst=result[index]}
{if !!lst&&!!lst.length}
<div class="itm f-cb">
{if index=="songs"}
<h3 class="hd"><i class="icn u-icn u-icn-26"></i><em class="f-fl">单曲</em></h3>
<ul class="{if index_index%2!=0}odd{/if} f-cb">
{list lst as song}
<li><a class="s-fc0 f-thide xtag" href="/song?id=${song.id}">${song.name|mark}-${listArtists(song.artists)}</a></li>
{/list}
</ul>
{elseif index=="artists"}
<h3 class="hd"><i class="icn u-icn u-icn-27"></i><em class="f-fl">歌手</em></h3>
<ul class="{if index_index%2!=0}odd{/if} f-cb">
{list lst as artist}
<li><a class="s-fc0 f-thide xtag" href="/artist?id=${artist.id}">${artist.name|mark}</a></li>
{/list}
</ul>
{elseif index=="albums"}
<h3 class="hd"><i class="icn u-icn u-icn-28"></i><em class="f-fl">专辑</em></h3>
<ul class="{if index_index%2!=0}odd{/if} f-cb">
{list lst as album}
<li><a class="s-fc0 f-thide xtag" href="/album?id=${album.id}">${album.name|mark}{if album.artist}-${album.artist.name|mark}{/if}</a></li>
{/list}
</ul>
{elseif index=="playlists"}
<h3 class="hd"><i class="icn u-icn u-icn-29"></i><em class="f-fl">歌单</em></h3>
<ul class="{if index_index%2!=0}odd{/if} f-cb">
{list lst as playlist}
<li><a class="s-fc0 f-thide xtag" href="/playlist?id=${playlist.id}">${playlist.name|mark}</a></li>
{/list}
</ul>
{elseif index=="mvs"}
<h3 class="hd"><i class="icn u-icn u-icn-96"></i><em class="f-fl">视频</em></h3>
<ul class="{if index_index%2!=0}odd{/if} f-cb">
{list lst as mv}
<li><a class="s-fc0 f-thide xtag" href="/mv?id=${mv.id}">MV:${mv.name|mark}{if mv.artistName}-${mv.artistName|mark}{/if}</a></li>
{/list}
</ul>
{/if}
</div>
{/if}
{/list}
</div>
</div>
</textarea>
<textarea name="jst" id="m-xwgt-share-infobar" style="display:none;"><i class="highlight"></i><div class="text f-fl f-fs1"><p class="f-thide">${info|escape}</p></div>
{if canChange}<i class="f-fr icn u-icn2 u-icn2-arr"></i>{/if}
</textarea>
<textarea name="jst" id="m-xwgt-share-videobar" style="display:none;"><div class="text">
<div class="cvr f-fl f-pr" style="background-image:url(${picUrl}?imageView&thumbnail=107x60),url(${picUrl}?imageView&thumbnail=107y60&blur=30x15)">
</div>
<h3 class="f-thide f-fs1">${title}</h3>
<i class="f-fr icn u-icn2 u-icn2-arr"></i>
</div>
</textarea>
<textarea name="ntp" id="m-xwgt-share-upload" style="display:none;"> <div class="f-pr choose f-cb">
<ul class="pics f-pr f-cb j-flag"><li class="f-pr add j-flag u-icn2 u-icn2-addimg" title="添加新图片"></li></ul>
<div class="f-pa tip s-fc6 j-flag"></div>
</div>
</textarea>
<textarea name="jst" id="m-xwgt-share-upload-preview" style="display:none;"> <li class="pic f-pr{if fail} z-fail{/if}">
{if !fail}
<i class="f-img icn"></i>
{else}
<div class="mask f-blk f-pa"></div><div class="f-blk f-pa error">${fail}</div>
{/if}
<span class="del f-pa u-icn2 u-icn2-delimg" title="删除"></span>
</li>
</textarea>
<textarea name="jst" id="m-xwgt-share-upload-preview-img" style="display:none;">{if !fail}
<img class="f-img" src="${url}?imageView&thumbnail=80y80" draggable=false>
{else}
<div class="mask f-blk f-pa"></div><div class="f-blk f-pa error">${fail}</div>
{/if}
</textarea>
<textarea name="ntp" id="ntp-alert" style="display:none;"><div class="lyct f-cb f-tc">
<p class="f-fs1">
<i class="u-icn u-icn-89 j-flag"></i>
<span class="f-fw1">&nbsp;&nbsp;&nbsp;<span class="j-flag"></span></span>
</p>
<p class="mesg j-flag">&nbsp;</p>
<div class="lybtn">
<a href="javascript:;" class="u-btn2 u-btn2-2 u-btn2-w2 j-flag" hidefocus="true"><i>知道了</i></a>
</div>
</div>
</textarea>
<textarea name="ntp" id="m-layer-commwin" style="display:none;"><div class="lyct f-tc">
<p class="j-t"><i class="u-icn u-icn-90"></i></p>
<p class="j-t msg1"></p>
</div>
<div class="j-t lsbtn f-tc">
<a href="javascript:;" class="u-btn2 u-btn2-2 u-btn2-w2" hidefocus="true"><i>上传节目</i></a>
</div>
</textarea>
<textarea name="ntp" id="m-layer-delwin" style="display:none;"><div class="lyct lyct-1 f-cb">
<div class="n-log2 n-log2-4">
<p class="js-tip u-tip-2"></p>
<div class="lybtn f-tc">
<a href="javascript:;" class="u-btn2 u-btn2-2" hidefocus="true" data-action="ok"><i>删除</i></a>
<a href="javascript:;" class="u-btn2 u-btn2-1" hidefocus="true" data-action="cancel"><i>取消</i></a>
</div>
</div>
</div>
</textarea>
<textarea name="jst" id="m-layer-commwin-btn" style="display:none;">{list buttons as item}
<a hidefocus="true" class="u-btn2 ${item.klass} {if item.style}${item.style}{else}u-btn2-w2{/if}" href="#" {if !!item.action}data-action="${item.action}"{/if}><i>${item.text}</i></a>
{/list}
</textarea>
<textarea name="ntp" id="m-layer-outershare" style="display:none;"><div class="lyct lyct-1">
<ul class="n-outshr f-cb">
<li>
<a href="#" data-action="wxfrd" class="logo wxfrd"></a>
<a href="#" data-action="wxfrd" class="wd">微信</a>
</li>
<!--
<li>
<a href="#" data-action="wxevt" class="logo wxevt"></a>
<a href="#" data-action="wxevt" class="wd">微信朋友圈</a>
</li>
-->
<li>
<a href="#" data-action="yxfrd" class="logo yxfrd"></a>
<a href="#" data-action="yxfrd" class="wd">易信</a>
</li>
<!--
<li>
<a href="#" data-action="yxevt" class="logo yxevt"></a>
<a href="#" data-action="yxevt" class="wd">易信朋友圈</a>
</li>
-->
<li>
<a href="#" data-action="qzone" class="logo qzone"></a>
<a href="#" data-action="qzone" class="wd">QQ空间</a>
</li>
<li>
<a href="#" data-action="lofte" class="logo lofte"></a>
<a href="#" data-action="lofte" class="wd">LOFTER</a>
</li>
</ul>
</div>
</textarea>
<textarea name="ntp" id="m-layer-tip" style="display:none;"><div class="lyct f-cb f-tc">
<div class="f-fs1 j-flag">message</div>
<div class="lybtn">
<a hidefocus="true" class="u-btn2 u-btn2-2 u-btn2-w2 j-flag" href="javascript:;"><i>知道了</i></a>
</div>
</div>
</textarea>
<textarea name="ntp" id="m-outshare-layer" style="display:none;"><div class="lyct lyct-1 f-cb">
<ul class="m-shareto f-cb j-flag">
<li class="fst" data-action="sn" data-type="2">
<a href="#" class="logo logo-sn"></a>
<a href="#" class="wd s-fc3">新浪微博</a>
</li>
<li data-action="tx" data-type="6" style="display:none;">
<a href="#" class="logo logo-tc"></a>
<a href="#" class="wd s-fc3">腾讯微博</a>
</li>
<li data-action="db" data-type="3">
<a href="#" class="logo logo-db"></a>
<a href="#" class="wd s-fc3">豆瓣</a>
</li>
</ul>
</div>
</div>
</textarea>
<textarea name="ntp" id="m-sharesingle-layer" style="display:none;"><div class="lyct lyct-1 f-cb">
<div class="m-lyshare">
<div class="u-txtwrap f-pr">
<textarea data-action="txt" class="u-txt area j-flag"><&#47;textarea>
</div>
<div class="oper f-cb">
<div class="face f-fl f-pr j-flag">
<i data-action="emt" class="u-icn u-icn-36 f-fl"></i>
</div>
<span class="zs f-fr s-fc3 j-flag">140</span>
</div>
<div class="btnwrap">
<a data-action="ok" class="u-btn2 u-btn2-2 u-btn2-w2 j-flag" hidefocus="true" href="#"><i>分享</i></a>
<a data-action="cc" class="u-btn2 u-btn2-1 u-btn2-w2" hidefocus="true" href="#"><i>取消</i></a>
</div>
<div class="u-err f-hide j-flag"><i class="u-icn u-icn-25"></i></div>
</div>
</div>
</textarea>
<textarea name="jst" id="m-popup-info" style="display:none;"><div class="lyct f-tc">
<div class="f-cb m-tipinfo">
<i class="u-icn2 u-icn2-11 f-fl"></i>
<div class="f-fr f-pr f-fs1 tip">${tip}</div>
</div>
</div>
<div class="lsbtn f-tc">
<a data-action="ok" href="javascript:void(0)" class="u-btn2 u-btn2-2 u-btn2-2-h {if oktext.length<=2}u-btn2-w2{/if}" hidefocus="true"><i>${oktext}</i></a>
<a data-action="cc" href="javascript:void(0)" hidefocus="true" class="u-btn2 u-btn2-1 u-btn2-1-h {if cctext.length<=2}u-btn2-w2{/if}"><i>${cctext}</i></a>
</div>
</textarea>
<textarea name="jst" id="m-popup-song-buy" style="display:none;"><div class="lyct m-songpay f-tc">
<div class="f-cb m-tipinfo">
<i class="u-icn2 u-icn2-11 f-fl"></i>
<div class="f-fr f-pr f-fs1 tip">${tip}</div>
</div>
<div class="f-pr f-tc">
<a data-action="ok" href="javascript:void(0)" class="u-btn2 u-btn2-2 {if oktext.length<=2}u-btn2-w2{/if}" hidefocus="true"><i>${oktext}</i></a>
{if showSongText}<a data-action="song" class="song s-fc4" href="javascript:void(0)">${songTxt}</a>{/if}
</div>
</div>
</textarea>
<textarea name="jst" id="m-popup-alert" style="display:none;"><div class="lyct f-tc">
<p><i class="${icon}"></i></p>
<p class="msg1"><span class="f-fs1 s-fc1">${tip}</span></p>
</div>
<div class="lsbtn f-tc">
{if typeof(oktext) != 'undefined'}<a data-action="ok" href="javascript:void(0)" class="u-btn2 u-btn2-2 u-btn2-2-h {if oktext.length<=2}u-btn2-w2{/if}" hidefocus="true"><i>${oktext}</i></a>{/if}
{if typeof(cctext) != 'undefined'}<a data-action="cc" href="javascript:void(0)" class="u-btn2 u-btn2-1 u-btn2-1-h {if cctext.length<=2}u-btn2-w2{/if}" hidefocus="true"><i>${cctext}</i></a>{/if}
</div>
</textarea>
<textarea name="txt" id="m-donate-tip" style="display:none;"><p>该资源为公益歌曲<p>
<p>捐赠任意金额（2~4999元）即可无限畅听下载</p>
</textarea>
<textarea name="ntp" id="m-simple-share-layer" style="display:none;"> <div class="lyct lyct-1">
<ul class="n-outshr f-cb">
<li data-type="xlwb">
<a href="javascript:;" class="logo xlwb"></a>
<a href="javascript:;" class="wd">新浪微博</a>
</li>
<li data-type="wx">
<a href="javascript:;" class="logo wxfrd"></a>
<a href="javascript:;" class="wd">微信</a>
</li>
<li data-type="yx">
<a href="javascript:;" class="logo yxfrd"></a>
<a href="javascript:;" class="wd">易信好友</a>
</li>
<li data-type="qzone">
<a href="javascript:;" class="logo qzone"></a>
<a href="javascript:;" class="wd">QQ空间</a>
</li>
<li data-type="lofter" style="display:none;">
<a href="javascript:;" class="logo lofte"></a>
<a href="javascript:;" class="wd">LOFTER</a>
</li>
<li data-type="db" style="display:none;">
<a href="javascript:;" class="logo db"></a>
<a href="javascript:;" class="wd">豆瓣</a>
</li>
</ul>
</div>
</textarea>
<textarea name="txt" id="m-report-point" style="display:none;"><div class="zcnt">
<div class="lyct f-cb f-tc">
<p class="f-fs2">悬赏1积分让大家来帮你补歌词，是否继续？</p>
<p style="padding-top: 10px;">若30天内歌词未补充，积分将退还给您</p>
<div class="lybtn">
<a href="javascript:;" data-action="ok" class="u-btn2 u-btn2-2 u-btn2-w2" hidefocus="true"><i>继续求</i></a>
<a href="javascript:;" data-action="cc" class="u-btn2 u-btn2-1 u-btn2-w2" hidefocus="true"><i>取消</i></a>
</div>
</div>
</div>
</textarea>
<textarea name="txt" id="txt-mobilestatus" style="display:none;"><div class="box f-cb">
<div data-action="invalid" class="item z-first f-fl">
<div class="icon"></div>
<p>原手机号已停用</p>
<p class="s-fc3">(使用其他方式验证)</p>
</div>
<div data-action="valid" class="item f-fr">
<div class="icon"></div>
<p>原手机号仍能使用</p>
<p class="s-fc3">(使用手机验证码验证)</p>
</div>
</div>
</textarea>
<textarea name="ntp" id="m-question" style="display:none;"><div class="m-question">
<div>请填写以下安全问题的答案</div>
<div class="qa j-flag f-cb">
<label class="f-fl">问题：</label>
</div>
<div class="qa f-cb">
<label class="f-fl">回答：</label>
<input type="text" class="u-txt txt f-fl j-flag">
</div>
<div class="u-err f-hide j-flag"><i class="u-icn u-icn-25"></i>帐号或密码错误</div>
<div class="btnwrap">
<a data-action="back" class="u-btn2 u-btn2-1 u-btn2-w2" hidefocus="true" href="javascript:void(0)"><i>上一步</i></a>
<a data-action="next" class="u-btn2 u-btn2-2 u-btn2-w2" hidefocus="true" href="javascript:void(0)"><i>下一步</i></a>
</div>
</div>
</textarea>
<textarea name="ntp" id="g-select" style="display:none;"><div class="u-slt f-ib">
<span class="curr f-thide">－请选择－</span>
<i class="btn"></i>
<ul class="f-hide">
</ul>
</div>
</textarea>
<textarea name="ntp" id="ntp-linuxlinks" style="display:none;"><div class="lyct lyct-1">
<div class="dc f-cb">
<ul class="links">
<li class="link f-cb">
<a href="" class="right" target="_blank" hidefocus="true" title="Linux版下载">deepin15（64位）</a>
<a href="" class="right" target="_blank" hidefocus="true" title="Linux版下载">ubuntu16.04（64位）</a>
</li>
</ul>
</div>
</div>
</textarea>
<textarea name="ntp" id="ntp-pcRedirect" style="display:none;"><div class="lyct lyct-1">
<div class="pcdld f-cb">
<img src="../../../style/web2/img/down/uwpWindown.png" alt="网易云音乐-UWP版">
<p class="txt">您的系统为Windows 10，推荐下载UWP版</p>
<div class="choose">
<a class="u-btn2 u-btn2-2" data-res-action="bilog" data-log-action="downloadapp" data-log-json='{"type":"pc","source":"downloadapp"}' href="https://www.microsoft.com/store/apps/9nblggh6g0jf" onclick="g_stat('uwp',true,event);_gaq.push(['_trackEvent','download','uwp','download']);" hidefocus="true" title="UWP版下载" target="_blank"><i>下载UWP版本</i></a>
<a class="link" data-res-action="bilog" data-log-action="downloadapp" data-log-json='{"type":"pc","source":"downloadapp"}' href="http://music.163.com/api/pc/download/latest" onclick="g_stat('pc',true,event);_gaq.push(['_trackEvent','download','pc','download']);" hidefocus="true" title="PC版下载" target="_blank"><i>继续下载PC版本</i></a>
</div>
</div>
</div>
</textarea>
<textarea name="jst" id="g-select-item" style="display:none;">{list options as o}
<li class="f-thide" data-index="${o_index}"><a href="javascript:;">${o|filter}</a></li>
{/list}
</textarea>
<textarea name="ntp" id="m-download-layer" style="display:none;"><h3 class="f-tc">使用云音乐客户端</h3>
<h4 class="f-tc s-fc3">即可无限下载高品质音乐</h4>
<div class="f-cb wrap">
<div class="left">
<div data-action="download" data-src="http://music.163.com/api/osx/download/latest" class="btn btn-mac"><i></i>Mac版<span class="ver j-flag">V1.9.1</span></div>
<div data-action="download" data-src="http://music.163.com/api/pc/download/latest" class="btn f-hide"><i></i>PC版<span class="ver j-flag">V1.9.1</span></div>
<div data-action="orpheus" class="btn btn-installed j-flag">已安装PC版</div>
</div>
<div class="right">
<div class="qtcode"></div>
<div class="s-fc3 f-tc">扫描下载手机版</div>
</div>
</div>
</textarea>
<textarea name="ntp" id="m-programtips-layer" style="display:none;"><div class="f-tc wrap ">
<p class="f-fs1 s-fc1 wrap-p">该节目为付费内容，扫描下方二维码，使用最新的安卓或iPhone版本购买后即可畅享</p>
<div class="f-tc wrap-d">
<span class="qtcode j-flag"></span>
</div>
</div>
</textarea>
<textarea name="jst" id="com-artists-title" style="display:none;">{var title=""}
{if artists && artists.length}
{list artists as x}
{if x}
{var title = title + x.name}
{if x_index < x_length - 1}
{var title = title + " / "}
{/if}
{/if}
{/list}
{/if}
${escape(title)}
</textarea>
<textarea name="jst" id="com-mv-artists" style="display:none;">{if artists && artists.length}
<span class="${boxClazz}" title="${comJST('com-artists-title', artists)}">
{list artists as x}
{if !!x}
{if !!x.id}
<a href="/artist?id=${x.id}" class="${clazz}">${mark(escape(x.name))}</a>
{else}
<span class="${clazz}">${mark(escape(x.name))}</span>
{/if}
{if x_index < x_length - 1}&nbsp;/&nbsp;{/if}
{/if}
{/list}
</span>
{/if}
</textarea>
<textarea name="jst" id="com-album-artists" style="display:none;">${comJST('com-mv-artists', artists, clazz, mark, boxClazz)}
</textarea>
<textarea name="jst" id="com-user-type" style="display:none;">{if x.userType==4}${before}<sup class="${clazz2} u-icn2 u-icn2-music2 ${clazz}"></sup>${after}{elseif x.authStatus==1}${before}<sup class="u-icn u-icn-1 ${clazz}"></sup>${after}{elseif (x.expertTags && x.expertTags.length>0) || !isEmptyObject(x.experts)}${before}<sup class="u-icn u-icn-84 ${clazz}"></sup>${after}{/if}
</textarea>
<textarea name="ntp" id="ntp-portrait" style="display:none;"><div class="m-emts z-show">
<div class="j-flag emtwrap f-cb"></div>
<div class="page">
<a href="#" hidefocus="true" class="j-flag u-btn u-btn-prv"></a><em class="j-flag s-fc3">1/2</em><a href="#" hidefocus="true" class="j-flag u-btn u-btn-nxt"></a>
</div>
</div>
</textarea>
<textarea name="jst" id="jst-portrait" style="display:none;">{list plist as item}
<span title="${item.key}" class="emtitm"><img data-text="${item.key}" data-url="${item.key|purl}" class="f-alpha" src="${item.key|purl}"></span>
{/list}
</textarea>
<textarea name="ntp" id="m-wgt-song-box" style="display:none;"><div class="j-flag"></div>
<div class="j-flag"></div>
</textarea>
<textarea name="jst" id="m-wgt-song-list" style="display:none;"><table class="m-table {if type=='rank'}m-table-rank{/if}">
<thead>
<tr>
<th class="first {if type=='rank'}wrk{else}w1{/if}"><div class="wp">&nbsp;</div></th>
<th><div class="wp af0"></div></th>
<th class="w2"><div class="wp af1"></div></th>
<th class="w3"><div class="wp af2"></div></th>
<th class="w4"><div class="wp af3"></div></th>
</tr>
</thead>
<tbody>
{list beg..end as y}
{var x=xlist[y]}
<tr id="${x.id|seed}" class="{if y%2==0}even{/if} {if disable(x)}js-dis{/if}">
<td class="left">
<div class="hd {if type=='rank'}rank{/if}">
<span data-res-id="${x.id}" data-res-type="18" data-res-action="play" {if from}data-res-from="${from.fid}" data-res-data="${from.fdata}"{/if} class="ply {if isPlaying(x)}ply-z-slt{/if}">&nbsp;</span>
<span class="num">${y+1}</span>
{if type=='rank'}
<div class="rk rk-1">
{if x.lastRank>=0}
{if y-x.lastRank>0}
<span class="ico u-icn u-icn-74 s-fc10">${y-x.lastRank}</span>
{elseif y-x.lastRank==0}
<span class="ico u-icn u-icn-72 s-fc4">0</span>
{else}
<span class="ico u-icn u-icn-73 s-fc9">${x.lastRank-y}</span>
{/if}
{else}
<span class="u-icn u-icn-75"></span>
{/if}
</div>
{/if}
</div>
</td>
<td class="">
<div class="f-cb">
<div class="tt">
<div class="ttc">
<span class="txt">
{var alia=songAlia(x)}
<a href="/song?id=${x.id}"><b title="${x.name|escape}{if alia} - (${alia|escape}){/if}">${soil(x.name)}</b></a>{if alia}<span title="${alia|escape}" class="s-fc8"> - (${soil(alia)})</span>{/if}
{if x.mvid>0}
<span data-res-id="${x.id}" data-res-action="mv" title="播放mv" class="mv">MV</span>
{/if}
</span>
</div>
</div>
</div>
</td>
<td class=" s-fc3">
<span class="u-dur {if canDel}candel{/if}">${dur2time(x.duration/1000)}{if x.ftype==2}<i title="歌曲来自第三方网站" class="migu u-icn2 u-icn2-14"></i>{/if}</span>
<div class="opt hshow">
<a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true"
data-res-type="18"
data-res-id="${x.id}"
data-res-action="addto"
{if from}data-res-from="${from.fid}" data-res-data="${from.fdata}"{/if}></a>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="share" data-res-name="${x.name}" data-res-author="{list x.artists as art}${art.name}{if art_index<x.artists.length-1}/{/if}{/list}" {if x.album}data-res-pic="${x.album.picUrl}"{/if} class="icn icn-share" title="分享">分享</span>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
{if canDel}
<span data-res-id="${x.id}" data-res-type="18" data-res-action="delete" class="icn icn-del" title="删除">删除</span>
{/if}
</div>
</td>
<td class="">
<div class="text" title="{list x.artists as art}${art.name}{if art_index<x.artists.length-1}/{/if}{/list}">
${getArtistName(x.artists, '', '', false, false, true)}
</div>
</td>
{if type=='dayRcmd'}
<td class="hascls">
<div class="f-pr">
<div class="text">{if x.album}<a href="/album?id=${x.album.id}" title="${x.album.name}">${x.album.name}</a>{/if}</div>
<a href="javascript:;" data-res-action="dislike" data-res-id="${x.id}" data-res-alg="${x.alg}" class="cls u-icn u-icn-80 f-tid icn-dislike" title="不感兴趣">不感兴趣</a>
</div>
</td>
{else}
<td class="">
<div class="text">
{if x.album}
<a href="/album?id=${x.album.id}" title="${x.album.name|escape}">${soil(x.album.name)}</a>
{/if}
</div>
</td>
{/if}
</tr>
{/list}
</tbody>
</table>
</textarea>
<textarea name="jst" id="m-wgt-album-list" style="display:none;"><table class="m-table {if type=='rank'}m-table-rank{/if}">
<thead>
<tr>
<th class="first {if type=='rank'}wrk{else}w1{/if}"><div class="wp">&nbsp;</div></th>
<th><div class="wp">歌曲标题</div></th>
<th class="w2-1"><div class="wp">时长</div></th>
<th class="w4"><div class="wp">歌手</div></th>
</tr>
</thead>
<tbody>
{list beg..end as y}
{var x=xlist[y]}
<tr id="${x.id|seed}" class="{if y%2==0}even{/if} {if disable(x)}js-dis{/if}">
<td class="left">
<div class="hd {if type=='rank'}rank{/if}">
<span data-res-id="${x.id}" data-res-type="18" data-res-action="play" {if from}data-res-from="${from.fid}" data-res-data="${from.fdata}"{/if} class="ply {if isPlaying(x)}ply-z-slt{/if}">&nbsp;</span>
<span class="num">${y+1}</span>
{if type=='rank'}
<div class="rk rk-1">
{if x.lastRank>=0}
{if y-x.lastRank>0}
<span class="ico u-icn u-icn-74 s-fc10">${y-x.lastRank}</span>
{elseif y-x.lastRank==0}
<span class="ico u-icn u-icn-72 s-fc4">0</span>
{else}
<span class="ico u-icn u-icn-73 s-fc9">${x.lastRank-y}</span>
{/if}
{else}
<span class="u-icn u-icn-75"></span>
{/if}
</div>
{/if}
</div>
</td>
<td class="">
<div class="f-cb">
<div class="tt">
<div class="ttc">
<span class="txt">
{var alia=songAlia(x)}
<a href="/song?id=${x.id}"><b title="${x.name|escape}{if alia} - (${alia|escape}){/if}">${soil(x.name)}</b></a>{if alia}<span title="${alia|escape}" class="s-fc8"> - (${soil(alia)})</span>{/if}
{if x.mvid>0}
<span data-res-id="${x.id}" data-res-action="mv" title="播放mv" class="mv">MV</span>
{/if}
</span>
</div>
</div>
</div>
</td>
<td class=" s-fc3">
<span class="u-dur {if canDel}candel{/if}">${dur2time(x.duration/1000)}{if x.ftype==2}<i title="歌曲来自第三方网站" class="migu u-icn2 u-icn2-14"></i>{/if}</span>
<div class="opt hshow">
<a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true"
data-res-type="18"
data-res-id="${x.id}"
data-res-action="addto"
{if from}data-res-from="${from.fid}" data-res-data="${from.fdata}"{/if}></a>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="share" data-res-name="${x.name}" data-res-author="{list x.artists as art}${art.name}{if art_index<x.artists.length-1}/{/if}{/list}" {if x.album}data-res-pic="${x.album.picUrl}"{/if} class="icn icn-share" title="分享">分享</span>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
{if canDel}
<span data-res-id="${x.id}" data-res-type="18" data-res-action="delete" class="icn icn-del" title="删除">删除</span>
{/if}
</div>
</td>
<td class="">
<div class="text" title="{list x.artists as art}${art.name}{if art_index<x.artists.length-1}/{/if}{/list}">
${getArtistName(x.artists, '', '/', false, true, true)}
</div>
</td>
</tr>
{/list}
</tbody>
</table>
</textarea>
<textarea name="jst" id="m-wgt-song-top50-list" style="display:none;"><table class="m-table m-table-1 m-table-4">
<tbody>
{list beg..end as y}
{var x=xlist[y]}
<tr id="${x.id|seed}" class="{if y%2==0}even{/if} {if disable(x)}js-dis{/if}">
<td class="w1">
<div class="hd">
<span data-res-id="${x.id}" data-res-type="18" data-res-action="play" {if from}data-res-from="${from.fid}" data-res-data="${from.fdata}"{/if} class="ply {if isPlaying(x)}ply-z-slt{/if}">&nbsp;</span>
<span class="num">${y+1}</span>
</div>
</td>
<td class="">
<div class="f-cb">
<div class="tt">
<div class="ttc">
<span class="txt">
{var alia=songAlia(x)}
<a href="/song?id=${x.id}"><b title="${x.name|escape}{if alia} - (${alia|escape}){/if}">${soil(x.name)}</b></a>{if alia}<span title="${alia|escape}" class="s-fc8"> - (${soil(alia)})</span>{/if}
{if x.mvid>0}
<span data-res-id="${x.id}" data-res-action="mv" title="播放mv" class="mv">MV</span>
{/if}
</span>
</div>
</div>
</div>
</td>
<td class="w2-1 s-fc3">
<span class="u-dur {if canDel}candel{/if}">${dur2time(x.duration/1000)}{if x.ftype==2}<i title="歌曲来自第三方网站" class="migu u-icn2 u-icn2-14"></i>{/if}</span>
<div class="opt hshow">
<a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true"
data-res-type="18"
data-res-id="${x.id}"
data-res-action="addto"
{if from}data-res-from="${from.fid}" data-res-data="${from.fdata}"{/if}></a>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="share" data-res-name="${x.name}" data-res-author="{list x.artists as art}${art.name}{if art_index<x.artists.length-1}/{/if}{/list}" {if x.album}data-res-pic="${x.album.picUrl}"{/if} class="icn icn-share" title="分享">分享</span>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
{if canDel}
<span data-res-id="${x.id}" data-res-type="18" data-res-action="delete" class="icn icn-del" title="删除">删除</span>
{/if}
</div>
</td>
<td class="w4">
<div class="text">
{if x.album}
{var transName = x.album.tns && x.album.tns.length > 0 ? x.album.tns[0] : ''}
<a href="/album?id=${x.album.id}" title="${x.album.name|escape}{if transName} - (${transName|escape}){/if}">${soil(x.album.name)}</a>
{if transName}
<span title="${transName|escape}" class="s-fc8"> - (${transName|escape})</span>
{/if}
{/if}
</div>
</td>
</tr>
{/list}
</tbody>
</table>
</textarea>
<textarea name="jst" id="m-wgt-song-rank-list" style="display:none;"><table class="m-table m-table-rank">
<thead>
<tr>
<th class="first w1"></th>
<th><div class="wp">标题</div></th>
<th class="w2-1"><div class="wp">时长</div></th>
<th class="w3"><div class="wp">歌手</div></th>
</tr>
</thead>
<tbody>
{list beg..end as y}
{var x=xlist[y]}
<tr id="${x.id|seed}" class="{if y%2==0}even{/if} {if disable(x)}js-dis{/if}">
{if y<3}
<td>
<div class="hd">
<span class="num">${y+1}</span>
<div class="rk ">
{if x.lastRank>=0}
{if y-x.lastRank>0}
<span class="ico u-icn u-icn-74 s-fc10">${y-x.lastRank}</span>
{elseif y-x.lastRank==0}
<span class="ico u-icn u-icn-72 s-fc4">0</span>
{else}
<span class="ico u-icn u-icn-73 s-fc9">${x.lastRank-y}</span>
{/if}
{else}
<span class="u-icn u-icn-75"></span>
{/if}
</div>
</div>
</td>
<td class="rank">
<div class="f-cb">
<div class="tt">
<a href="/song?id=${x.id}">{if x.album}<img class="rpic" src="${x.album.picUrl}?param=50y50&quality=100">{/if}</a>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="play" {if from}data-res-from="${from.fid}" data-res-data="${from.fdata}"{/if} class="ply {if isPlaying(x)}ply-z-slt{/if}">&nbsp;</span>
<div class="ttc">
<span class="txt">
{var alia=songAlia(x)}
<a href="/song?id=${x.id}"><b title="${x.name|escape}{if alia} - (${alia|escape}){/if}">${soil(x.name)}</b></a>{if alia}<span title="${alia|escape}" class="s-fc8"> - (${soil(alia)})</span>{/if}
{if x.mvid>0}
<span data-res-id="${x.id}" data-res-action="mv" title="播放mv" class="mv">MV</span>
{/if}
</span>
</div>
</div>
</div>
</td>
{else}
<td>
<div class="hd">
<span class="num">${y+1}</span>
<div class="rk ">
{if x.lastRank>=0}
{if y-x.lastRank>0}
<span class="ico u-icn u-icn-74 s-fc10">${y-x.lastRank}</span>
{elseif y-x.lastRank==0}
<span class="ico u-icn u-icn-72 s-fc4">0</span>
{else}
<span class="ico u-icn u-icn-73 s-fc9">${x.lastRank-y}</span>
{/if}
{else}
<span class="u-icn u-icn-75"></span>
{/if}
</div>
</div>
</td>
<td class="">
<div class="f-cb">
<div class="tt">
<span data-res-id="${x.id}" data-res-type="18" data-res-action="play" {if from}data-res-from="${from.fid}" data-res-data="${from.fdata}"{/if} class="ply {if isPlaying(x)}ply-z-slt{/if}">&nbsp;</span>
<div class="ttc">
<span class="txt">
{var alia=songAlia(x)}
<a href="/song?id=${x.id}"><b title="${x.name|escape}{if alia} - (${alia|escape}){/if}">${soil(x.name)}</b></a>{if alia}<span title="${alia|escape}" class="s-fc8"> - (${soil(alia)})</span>{/if}
{if x.mvid>0}
<span data-res-id="${x.id}" data-res-action="mv" title="播放mv" class="mv">MV</span>
{/if}
</span>
</div>
</div>
</div>
</td>
{/if}
<td class=" s-fc3">
<span class="u-dur {if canDel}candel{/if}">${dur2time(x.duration/1000)}{if x.ftype==2}<i title="歌曲来自第三方网站" class="migu u-icn2 u-icn2-14"></i>{/if}</span>
<div class="opt hshow">
<a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true"
data-res-type="18"
data-res-id="${x.id}"
data-res-action="addto"
{if from}data-res-from="${from.fid}" data-res-data="${from.fdata}"{/if}></a>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="share" data-res-name="${x.name}" data-res-author="{list x.artists as art}${art.name}{if art_index<x.artists.length-1}/{/if}{/list}" {if x.album}data-res-pic="${x.album.picUrl}"{/if} class="icn icn-share" title="分享">分享</span>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
{if canDel}
<span data-res-id="${x.id}" data-res-type="18" data-res-action="delete" class="icn icn-del" title="删除">删除</span>
{/if}
</div>
</td>
<td class="">
<div class="text" title="{list x.artists as art}${art.name}{if art_index<x.artists.length-1}/{/if}{/list}">
${getArtistName(x.artists, '', '', false, false, true)}
</div>
</td>
</tr>
{/list}
</tbody>
</table>
</textarea>
<textarea name="jst" id="m-wgt-song-pgm-list" style="display:none;"><table class="m-table m-table-prog">
<tbody id="song-list">
{list beg..end as y}
{var x=xlist[y]}
<tr id="${x.id|seed}" class="{if y%2!=0}even{/if} {if disable(x)}js-dis{/if}">
<td class="first col1">
<div class="hd">
<span data-res-id="${x.id}" data-res-type="18" data-res-action="play" {if from}data-res-from="${from.fid}" data-res-data="${from.fdata}"{/if} class="ply {if isPlaying(x)}ply-z-slt{/if}">&nbsp;</span>
<span class="num">${y+1}</span>
</div>
</td>
<td class="col2">
<div class="f-cb">
<div class="tt">
<div class="ttc">
<span class="txt">
{var alia=songAlia(x)}
<a href="/song?id=${x.id}"><b title="${x.name|escape}{if alia} - (${alia|escape}){/if}">${soil(x.name)}</b></a>{if alia}<span title="${alia|escape}" class="s-fc8"> - (${soil(alia)})</span>{/if}
{if x.mvid>0}
<span data-res-id="${x.id}" data-res-action="mv" title="播放mv" class="mv">MV</span>
{/if}
</span>
</div>
</div>
</div>
</td>
<td class="col3 s-fc3">
<span class="u-dur {if canDel}candel{/if}">${dur2time(x.duration/1000)}{if x.ftype==2}<i title="歌曲来自第三方网站" class="migu u-icn2 u-icn2-14"></i>{/if}</span>
<div class="opt hshow">
<a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true"
data-res-type="18"
data-res-id="${x.id}"
data-res-action="addto"
{if from}data-res-from="${from.fid}" data-res-data="${from.fdata}"{/if}></a>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="share" data-res-name="${x.name}" data-res-author="{list x.artists as art}${art.name}{if art_index<x.artists.length-1}/{/if}{/list}" {if x.album}data-res-pic="${x.album.picUrl}"{/if} class="icn icn-share" title="分享">分享</span>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
{if canDel}
<span data-res-id="${x.id}" data-res-type="18" data-res-action="delete" class="icn icn-del" title="删除">删除</span>
{/if}
</div>
</td>
<td class="col4">
<div class="text" title="{list x.artists as art}${art.name}{if art_index<x.artists.length-1}/{/if}{/list}">
${getArtistName(x.artists, '', '', false, false, true)}
</div>
</td>
<td class="col5">
<div class="text">
{if x.album}
<a href="/album?id=${x.album.id}" title="${x.album.name|escape}">${soil(x.album.name)}</a>
{/if}
</div>
</td>
</tr>
{/list}
</tbody>
</table>
</textarea>
<textarea name="jst" id="m-wgt-song-listen" style="display:none;"> <ul>
{list beg..end as y}
{var x=xlist[y]}
{if extData&&extData.limit&&y>=extData.limit}
{break}
{/if}
{var from=getFrom()}
<li id="${x.id|seed}" {if y%2 !=0 }class='even'{/if}>
<div class="hd ">
<span data-res-id="${x.id}" data-res-type="18" data-res-action="play" {if from}data-res-from="${from.fid}" data-res-data="${from.fdata}"{/if} class="ply {if isPlaying(x)}ply-z-slt{/if}">&nbsp;</span>
<span class="num">${y+1}.</span>
</div>
<div class="song">
<div class="tt">
<div class="ttc">
<span class="txt"><a href="/song?id=${x.id}"><b title="${x.name}">${x.name}</b></a>
<span class='ar s-fc8'> <em>-</em>
${getArtistName(x.artists, 's-fc8')}
</span>
</span>
</div>
</div>
<div class="opt">
<a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="${x.id}" data-res-action="addto" {if from}data-res-from="${from.fid}" data-res-data="${from.fdata}"{/if}></a>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="subscribe" class="icn icn-fav" title="收藏"></span>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="share" data-res-name="${x.name}" data-res-author="{list x.artists as art}${art.name}{if art_index<x.artists.length-1}/{/if}{/list}" class="icn icn-share" title="分享">分享</span>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载">下载</span>
</div>
</div>
<div class="tops">
<span class="bg" style='width:${x.score*100/x.max}%;'></span>
{if extData.showCount&&x.playCount}<span class="times f-ff2">${x.playCount}次</span>{/if}
</div>
</li>
{/list}
</ul>
{if extData&&extData.limit&&xlist.length>extData.limit}
<div class="more">
<a href="/user/songs/rank?id=${hostId}" >查看更多&gt;</a>
</div>
{/if}
</textarea>
<textarea name="jst" id="m-wgt-purchased-song-list" style="display:none;"> {list beg..end as y}
{var x=xlist[y]}
<tr id="${x.id|seed}" class="{if y%2==1}even{/if} {if disable(x)}js-dis{/if}">
<td class="left">
<div class="hd {if type=='rank'}rank{/if}">
<span data-res-id="${x.id}" data-res-type="18" data-res-action="play" {if from}data-res-from="${from.fid}" data-res-data="${from.fdata}"{/if} class="ply {if isPlaying(x)}ply-z-slt{/if}">&nbsp;</span>
<span class="num">${y+1}</span>
{if type=='rank'}
<div class="rk rk-1">
{if x.lastRank>=0}
{if y-x.lastRank>0}
<span class="ico u-icn u-icn-74 s-fc10">${y-x.lastRank}</span>
{elseif y-x.lastRank==0}
<span class="ico u-icn u-icn-72 s-fc4">0</span>
{else}
<span class="ico u-icn u-icn-73 s-fc9">${x.lastRank-y}</span>
{/if}
{else}
<span class="u-icn u-icn-75"></span>
{/if}
</div>
{/if}
</div>
</td>
<td class="u-hasopt">
<div class="f-cb">
<div class="tt">
<div class="ttc">
<span class="txt">
{var alia=songAlia(x)}
<a href="/song?id=${x.id}"><b title="${x.name|escape}{if alia} - (${alia|escape}){/if}">${soil(x.name)}</b></a>{if alia}<span title="${alia|escape}" class="s-fc8"> - (${soil(alia)})</span>{/if}
{if x.mvid>0}
<span data-res-id="${x.id}" data-res-action="mv" title="播放mv" class="mv">MV</span>
{/if}
</span>
</div>
</div>
<div class="opt hshow">
<a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true"
data-res-type="18"
data-res-id="${x.id}"
data-res-action="addto"
{if from}data-res-from="${from.fid}" data-res-data="${from.fdata}"{/if}></a>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="share" data-res-name="${x.name}" data-res-author="{list x.artists as art}${art.name}{if art_index<x.artists.length-1}/{/if}{/list}" {if x.album}data-res-pic="${x.album.picUrl}"{/if} class="icn icn-share" title="分享">分享</span>
<span data-res-id="${x.id}" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
{if canDel}
<span data-res-id="${x.id}" data-res-type="18" data-res-action="delete" class="icn icn-del" title="删除">删除</span>
{/if}
</div>
</div>
</td>
<td class="">
<div class="text" title="{list x.artists as art}${art.name}{if art_index<x.artists.length-1}/{/if}{/list}">
${getArtistName(x.artists, '', '', false, false, true)}
</div>
</td>
<td class="">
<div class="text">
{if x.album}
<a href="/album?id=${x.album.id}" title="${x.album.name|escape}">${soil(x.album.name)}</a>
{/if}
</div>
</td>
<td class="s-fc3">${formatTime(x.paidTime)}</td>
</tr>
{/list}
</textarea>
<textarea name="ntp" id="m-msg-private-send" style="display:none;"><div class="lyct lyct-1 f-cb">
<div class="m-lyshare m-plshare">
<div class="u-err j-flag" style="display: none;">最多选择10位好友</div>
<div class="item item-1 f-cb">
<label>发 给：</label>
<div class="ct f-pr j-flag">
</div>
</div>
<div class="item f-cb">
<label>内 容：</label>
<div class="ct j-flag">
</div>
</div>
</div>
</div>
</textarea>
</div>
<script src="//s3.music.126.net/web/s/core.js?2adf840caa7109e74a8a7a6d3329ab86" type="text/javascript"></script><script src="//s3.music.126.net/web/s/pt_playlist_index.js?d5e7d99da6d6b32e5482182672ee35a8" type="text/javascript"></script>
<script defer="defer" src="//img3.126.net/kaola/dsp1f/js/ntes-ad-cloud.min.js?v=1.0"></script>
</body>
<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-38766552-1'],['_setLocalGifPath', '/UA-38766552-1/__utm.gif'],['_setLocalRemoteServerMode']);
_gaq.push(['_trackPageview']);
(function() {
var ga = document.createElement('script');
ga.type = 'text/javascript';
ga.async = true;
ga.src = '//wr.da.netease.com/ga.js';
var s = document.getElementsByTagName('script')[0];
s.parentNode.insertBefore(ga, s);
})();//fix ipad下的一个bug
if (navigator.userAgent.indexOf('iPad') != -1) {
iframeHeight = Math.max(
Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
Math.max(document.body.clientHeight, document.documentElement.clientHeight)
);
top.document.body.style.height = iframeHeight + 20 + 'px';
}</script>
</html>
'''


#print user_id
re_music = re.compile("song\?id=(\d*?)\"")

music_list = re_music.findall(html_data)
print music_list

