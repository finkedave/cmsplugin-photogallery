photogallery

------Overview-----
photogallery is a django-cms plugin that allows you to configure and display a photo gallery or a gallery promotion on a cms page


------Gallery Plugin------
1. Model
A Gallery contains fields title and flier folder. A flier folder should contain images. Even if it has other object types
they WILL NOT be displayed. Only images can be displayed in a gallery. The number of images shown for a gallery is 
defined in settings.py, default is 6. Therefore if any more images are contained in the folder they will not be included.

2. Template
The template that is used to display a Gallery is 'templates/photogallery/photogallery_plugin.html'.
Since multiple galleries can be contained within a page, care must be taken with ids, and javascript.

When called from a promotion page the correct image will be shown in the gallery, along with the title and image description.
The default template also has a scroll_to option. It is defined in settings.py

SCROLL_TO_GALLERY = True
SCROLL_TO_GALLERY_DELAY = 1000

These options enable the page to immediately scroll to the gallery whos promotion was clicked on. The delay option
is a way to smoothly scroll to the gallery letting the user see a glimpse of the rest of the page. Default is a second.
Setting it to 0, the page will almost immediately just appear to load to the position of the gallery

3. Ajax calls
When a different image in a gallery is clicked on. An ajax call is made refreshing the description and title of the image.
Because more then one gallery can be on a page. Care must be taken to index all ids with gallery.

for example
<span id='id_gallery{{gallery.id}}_image_name'>{{selected_image.name|default_if_none:''}}</span><
<span id='id_gallery{{gallery.id}}_image_description'>{{selected_image.description|default_if_none:''}}</span>
This is what the ajax call is requiring that exists on the page. id_gallery1_image_name. Therefore someone could 
browswe two galleries at the same time because the call to instantiate the ajax call is

javascript:refresh_image_data(gallery_id, image_id

4. CSS 


--- Gallery Promotion Plugin ----
1. Model
Promotion model contains a field for a foreign key to the photogallery that it is promotion, a page foreign key
to the page that the gallery resides on. Description and orientation. The orientation can be horizontal or
vertical. This field just tells the plugin with template to use. All fields are required

2. Templates
There are two templates that are used for promotions. 'templates/photogallery/photogallery_promotion_horz_plugin.html'
, 'templates/photogallery/photogallery_promotion_vert_plugin.html'. The one used corresponds to what is selected for 
orientation. A promotion is displayed with links to the page that the gallery resides on. Note if a promotion is created
and points to a page that doesn't contain the gallery, the page will be loaded but the gallery won't be scrolled to and shown.

Like galleries care must be taken when overriding the templates to always index blocks with the prmotion id knowing that more then
one promotion can appear on a page


4. CSS

--- Linking Gallery Promotion Plugin and Gallery Page ----
Since a page have have more then one gallery, and we want a promotion to link to the correct gallery and the gallery
must start with the correct image a way must be used to send the info to the gallery plugin.

We use PROMOTION_LINK_ATTR='photogallery' to send info from one the other. So for each promotion image it has a link
to the corresponding gallery page with a GET argument of ?photogalleryx=y . Where x is the gallery id and y is the index of the image
shown. Therefore when the plugin is called. It searchs for itself in the GET arguments if it finds it on the 
url path. It knows to make the yth+1(0 indexing) element the active image, and scroll down to itself if the SETTING SCROLL_TO_GALLERY
is set. Note while not used in practice you could do
?photogallery2=3&photogallery3=2 . This will select the 2nd element of photogallery2 and 1 element if gallery3. While the scrolling
will be random. Its hard to know which one will be scrolled to.
Note the attr PROMOTION_LINK_ATTR can be changed in settings.py

