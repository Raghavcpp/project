import imagecode as IC
HEADER_TITLE = 'The standard Lorem Ipsum passage, used since the 1500s'
HEADER_CONTENT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
"""

INTRO_TITLE = 'Section 1.10.33 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC'
INTRO_CONTENT = """xncvjbgsghjxfhgxcyfgchgh bchgjkdfjcjkfgjkhb gnmhbgh
jhbcnjgbhdgnmb fhugsbdzje gklfizghsgxklcf
xzgbhjcvzxczcghvdfsghiwfajkcjkzvxbvjbv"""
service_mapping = {
    'android development': IC.Android_Development,
    'mobile app development': IC.Mobile_App_Development,
    'ios app development': IC.IOS_App_Development,
    'hybrid app development': IC.Hybrid_App_Development,
    'education app development': IC.Education_App_Development,
    'entertainment music app': IC.Entertainment_Music_App,
    'entertainment & music app': IC.Entertainment_Music_App,
    'food ordering app': IC.Food_Ordering_App,
    'healthcare app': IC.Healthcare_App,
    'iot in healthcare': IC.IoT_in_Healthcare,
    'cab taxi solutions': IC.Cab_Taxi_Solutions,
    'cab & taxi solutions': IC.Cab_Taxi_Solutions,
    'manufacturing solution': IC.Manufacturing_Solution,
    'web development': IC.Web_Development,
    'e-commerce': IC.E_Commerce,
    'e commerce': IC.E_Commerce,
    'digital marketing': IC.Digital_Marketing,
    'advertising solution': IC.Advertising_Solution,
    'native app development': IC.Native_App_Development,
    'custom app development': IC.Custom_App_Development
}
services=[]
STEP_VARIABLE = [IC.Web_Development, IC.Native_App_Development, IC.Android_Development, IC.Digital_Marketing, IC.IOS_App_Development, IC.Custom_App_Development]

for i, service_name in enumerate(services):
    service_lower = service_name.lower()
    if service_lower in service_mapping:
        STEP_VARIABLE[i] = service_mapping[service_lower]

OTHER_SERVICES = '<p> [vc_row full_width="stretch_row" css=".vc_custom_1672119069502{margin-top: 0px !important;margin-bottom: 30px !important;padding-top: 10px !important;padding-bottom: 0px !important;}"][vc_column][vc_custom_heading text="Other Services You May Like" font_container="tag:h3|font_size:35px|text_align:center|line_height:45px" use_theme_fonts="yes" el_class="font-weight-bold" css=".vc_custom_1672123736225{margin-bottom: 50px !important;}"][/vc_column][vc_column css_animation="none" width="1/3" css=".vc_custom_1579590363406{margin-top: 0px !important;margin-bottom: 30px !important;padding-top: 0px !important;padding-bottom: 0px !important;}" el_class="slide-up-hover-effect"]' + STEP_VARIABLE[0] + '[/vc_column][vc_column css_animation="none" width="1/3" css=".vc_custom_1579590169080{margin-top: 0px !important;margin-bottom: 30px !important;padding-top: 0px !important;padding-bottom: 0px !important;}" el_class="slide-up-hover-effect"]' + STEP_VARIABLE[1] + '[/vc_column][vc_column css_animation="none" width="1/3" css=".vc_custom_1579590180904{margin-top: 0px !important;margin-bottom: 30px !important;padding-top: 0px !important;padding-bottom: 0px !important;}" el_class="slide-up-hover-effect"]' + STEP_VARIABLE[2] + '[/vc_column][/vc_row][vc_row full_width="stretch_row" css=".vc_custom_1671607297462{margin-top: 0px !important;margin-bottom: 50px !important;padding-top: 0px !important;padding-bottom: 0px !important;}"][vc_column css_animation="none" width="1/3" css=".vc_custom_1579590363406{margin-top: 0px !important;margin-bottom: 30px !important;padding-top: 0px !important;padding-bottom: 0px !important;}" el_class="slide-up-hover-effect"]' + STEP_VARIABLE[3] + '[/vc_column][vc_column css_animation="none" width="1/3" css=".vc_custom_1579590169080{margin-top: 0px !important;margin-bottom: 30px !important;padding-top: 0px !important;padding-bottom: 0px !important;}" el_class="slide-up-hover-effect"]' + STEP_VARIABLE[4] + '[/vc_column][vc_column css_animation="none" width="1/3" css=".vc_custom_1579590180904{margin-top: 0px !important;margin-bottom: 30px !important;padding-top: 0px !important;padding-bottom: 0px !important;}" el_class="slide-up-hover-effect"]' + STEP_VARIABLE[5] + '[/vc_column][/vc_row]</p>'




HEADER = '<p>[vc_row full_width="stretch_row" css=".vc_custom_1670068129337{background-image: url(https://www.ajath.ae/wp-content/uploads/2023/09/Untitled-design-1-scaled.jpg) !important;}"][vc_column][vc_row_inner][vc_column_inner width="1/2"][vc_custom_heading text="' + HEADER_TITLE + '" font_container="tag:h1|font_size:30px|text_align:left|color:%23ffffff|line_height:50px" use_theme_fonts="yes" css=".vc_custom_1669805607379{padding-top: 110px !important;}"][vc_column_text]</p><p style="color: #fff; padding-top: 20px; font-size: 16px;"><span style="font-weight: 400;">' + HEADER_CONTENT + '</span></p><p>[/vc_column_text][/vc_column_inner][vc_column_inner width="1/2" css=".vc_custom_1668410431339{margin-bottom: 60px !important;}"][rt_cf7_style submit_background_color="#04aef1" submit_hover_color="#f2f2f2" submit_text_hover_color="#04aef1" radiant_submit_border_style="solid" contact_form_form_row_margin_top="5px" contact_form_form_row_margin_right="5px" contact_form_form_row_margin_bottom="15px" contact_form_form_row_margin_left="5px" radiant_submit_border_color="#04aef1" radius_top="3px" radius_right="3px" radius_bottom="3px" radius_left="3px" padding_top="6px" padding_right="10px" padding_bottom="6px" padding_left="10px" radiant_border_style="solid" radiant_border_color="#cccccc" radiant_border_top="2px" radiant_border_right="2px" radiant_border_bottom="2px" radiant_border_left="2px" radiant_focus_style="solid" radiant_focus_color="#0883ea" radiant_focus_top="2px" radiant_focus_right="2px" radiant_focus_bottom="2px" radiant_focus_left="2px"][contact-form-7 id="3578"][/rt_cf7_style][/vc_column_inner][/vc_row_inner][/vc_column][/vc_row]'

GET_IN_TOUCH = '[lea_button_style title="Get In Touch" align="center" font_color="#ffffff" use_theme_fonts="yes" background_hover_color="#ffffff" border_hover_color="#0883ea" font_hover_color="#0883ea" link="url:https%3A%2F%2Fwww.ajath.ae%2Fcontact-dubai%2F" button_font_size="15px" button_line_height="26px" animation="fadeIn" extra_class="font-weight-medium" button_design_css=".vc_custom_1672132528921{margin-top: 10px !important;margin-bottom: 10px !important;border-top-width: 2px !important;border-right-width: 2px !important;border-bottom-width: 2px !important;border-left-width: 2px !important;padding-top: 11px !important;padding-right: 35px !important;padding-bottom: 11px !important;padding-left: 35px !important;background-color: #0883ea !important;border-left-color: #0883ea !important;border-left-style: solid !important;border-right-color: #0883ea !important;border-right-style: solid !important;border-top-color: #0883ea !important;border-top-style: solid !important;border-bottom-color: #0883ea !important;border-bottom-style: solid !important;border-radius: 4px !important;}"]'

INTRO = '[vc_row][vc_column width="1/2" css=".vc_custom_1671598463419{margin-top: 70px !important;}"][vc_single_image image="5841" img_size="full" css=".vc_custom_1671598421004{padding-top: 18px !important;}"][/vc_column][vc_column width="1/2"][vc_row_inner][vc_column_inner][vc_custom_heading text="' + INTRO_TITLE + '" font_container="tag:h1|font_size:30px|text_align:left|color:%23181616|line_height:46px" use_theme_fonts="yes" el_class="font-weight-bold" css=".vc_custom_1670068166136{margin-top: 60px !important;margin-bottom: 40px !important;}"][vc_column_text css=".vc_custom_1671602164424{margin-top: 0px !important;margin-bottom: 0px !important;}"]</p>' + INTRO_CONTENT + '[/vc_column_text][/vc_column_inner][/vc_row_inner][/vc_column][/vc_row][vc_row][vc_column css=".vc_custom_1671598386595{padding-top: 25px !important;}"][vc_column_text]</p>'


print(HEADER)
print(INTRO)
print(GET_IN_TOUCH)
print(OTHER_SERVICES)