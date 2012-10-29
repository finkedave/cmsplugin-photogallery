function get_selected_gallery_attrs(promotion_link_attr)
{
    var reg_ex = new RegExp(".*#("+promotion_link_attr+"\\d+)=(\\d+)");
    matches = reg_ex.exec(window.location.href)
    if(matches!=null)
        return matches
    else
        return null
}
