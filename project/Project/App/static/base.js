 /* NOTE : Use web server to view HTML files as real-time update will not work if you directly open the HTML file in the browser. */
 (function(d, m) {
     var kommunicateSettings = {
         "appId": "a6f13994ce9205491944ea2f00ae9abf",
         "popupWidget": true,
         "automaticChatOpenOnNavigation": true
     };
     var s = document.createElement("script");
     s.type = "text/javascript";
     s.async = true;
     s.src = "https://widget.kommunicate.io/v2/kommunicate.app";
     var h = document.getElementsByTagName("head")[0];
     h.appendChild(s);
     window.kommunicate = m;
     m._globals = kommunicateSettings;
 })(document, window.kommunicate || {});


 const userName = document.querySelector('.user-name');
 const memberOption = document.querySelector('.member-option')

 userName.addEventListener('click', function(event) {
     if (memberOption.style.display == "none") {
         memberOption.style.display = "flex";
         setTimeout(function() {
             memberOption.style.top = "70px";
         }, 10);

     } else {
         memberOption.style.top = "40px";
         setTimeout(function() {
             memberOption.style.display = "none";
         }, 10);
     }
 });