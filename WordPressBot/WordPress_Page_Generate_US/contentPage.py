import random
def content(titleSummary,heading,heading_summary,SubHeading,SubHeading_summary,graphData,graphLine):
    graphName = 'Pie Chart Analysis'
    option1= graphData[0][0]
    value1= graphData[0][1]
    option2= graphData[1][0]
    value2=graphData[1][1]
    option3= graphData[2][0]
    value3= graphData[2][1]
    Bargraph='App Vs Web User 2023'
    length = len(SubHeading) - 1
    hidcolumn = ''
    idnum=0
    def randomnumber(idnum):
        minimum = pow(10, 9)
        maximum = pow(10, 10) - 1
        n=0
        while(n<=idnum):
            n= random.randint(minimum, maximum)
        return n    
    for i in range(1,length):
        idnum=randomnumber(idnum)
        hidcolumn += "[vc_tta_section title=\"" + SubHeading[i] + "\" tab_id=\"" + str(idnum) + "945-11809e1e-ed7b\"][vc_column_text]"+ SubHeading_summary[i] +"[/vc_column_text][/vc_tta_section]"

    dataUS1 = "[vc_row][vc_column][vc_custom_heading source=\"post_title\" font_container=\"tag:h3|text_align:left|line_height:40px\" use_theme_fonts=\"yes\" el_class=\"text-transform\"][vc_column_text]" + titleSummary + "[/vc_column_text][vc_single_image source=\"featured_image\" img_size=\"full\"][vc_column_text]\n"
    dataUS2 = "<blockquote>" + heading + "</blockquote>\n"
    dataUS3 = "[/vc_column_text][vc_column_text]" + heading_summary + "[/vc_column_text][/vc_column][/vc_row][vc_row][vc_column width=\"1/2\" css=\".vc_custom_1494235812995{margin-bottom: 25px !important;}\"][vc_custom_heading text=\"" + SubHeading[0] + "\" font_container=\"tag:h4|text_align:left\" use_theme_fonts=\"yes\" el_class=\"text-transform\" css=\".vc_custom_1526913962867{margin-bottom: 26px !important;}\"][vc_column_text css=\".vc_custom_1494235286024{margin-bottom: 34px !important;}\"]" + SubHeading_summary[0] + "[/vc_column_text][/vc_column][vc_column width=\"1/2\"][vc_custom_heading text=\"" + graphName + "\" font_container=\"tag:h4|text_align:left\" use_theme_fonts=\"yes\" el_class=\"text-transform\" css=\".vc_custom_1526913973482{margin-bottom: 24px !important;}\"][vc_round_chart stroke_width=\"2\" values=\"%5B%7B%22title%22%3A%22" + option1 + "%22%2C%22value%22%3A%22" + value1 + "%22%2C%22color%22%3A%22turquoise%22%7D%2C%7B%22title%22%3A%22" + option2 + "%22%2C%22value%22%3A%22" + value2 + "%22%2C%22color%22%3A%22pink%22%7D%2C%7B%22title%22%3A%22" + option3 + "%22%2C%22value%22%3A%22" + value3 + "%22%2C%22color%22%3A%22mulled-wine%22%7D%5D\" el_class=\"small_chart\" css=\".vc_custom_1494234342834{margin-bottom: 2px !important;}\"][vc_column_text el_class=\"stm-effects_opacity\"]" + graphLine + "[/vc_column_text][/vc_column][/vc_row][vc_row css=\".vc_custom_1494240191005{margin-bottom: 60px !important;}\"][vc_column][vc_tta_accordion c_icon=\"triangle\" active_section=\"1\" ac_style=\"style_2\"]"+ hidcolumn +"[/vc_tta_accordion][/vc_column][/vc_row][vc_row][vc_column width=\"1/2\" css=\".vc_custom_1494235812995{margin-bottom: 25px !important;}\"][vc_custom_heading text=\""+ Bargraph+"\" font_container=\"tag:h4|text_align:left\" use_theme_fonts=\"yes\" el_class=\"text-transform\" css=\".vc_custom_1526913981011{margin-bottom: 31px !important;}\"][stm_charts design=\"bar\" x_values=\"JAN; FEB; MAR; APR; MAY; JUN;\" values=\"%5B%7B%22title%22%3A%22WEB%22%2C%22y_values%22%3A%2210%3B%2015%3B%2020%3B%2025%3B%2027%3B%2025%3B%20%22%2C%22color%22%3A%22%23fe6c61%22%7D%2C%7B%22title%22%3A%22APP%22%2C%22y_values%22%3A%2225%3B%2018%3B%2016%3B%2017%3B%2020%3B%2035%3B%22%2C%22color%22%3A%22%235472d2%22%7D%5D\" width=\"400\" height=\"320\"][/vc_column][vc_column width=\"1/2\"][vc_custom_heading text=\"" + SubHeading[-1] + "\" font_container=\"tag:h4|text_align:left\" use_theme_fonts=\"yes\" el_class=\"text-transform\" css=\".vc_custom_1526913986851{margin-bottom: 36px !important;}\"][vc_column_text css=\".vc_custom_1494240118978{margin-bottom: 30px !important;}\"]"+ SubHeading_summary[-1]+" [/vc_column_text][/vc_column][/vc_row]"

    fullcontent = dataUS1+dataUS2+dataUS3
    # print(fullcontent)
    return fullcontent