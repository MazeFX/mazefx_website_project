/**
 * Created by MazeFX on 17-6-2016.
 */
jQuery(function() {

    jQuery('#da-slider').cslider({
        autoplay	: true,
        bgincrement	: 450
    });

});
jQuery(document).ready(function(){
    jQuery('#parallax .parallax-layer')
    .parallax({
      mouseport: jQuery('#parallax')
    });
});