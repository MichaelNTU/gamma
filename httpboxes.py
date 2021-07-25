#!/usr/bin/env python3
#
import argparse
import http.server
import webbrowser

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type = int, default=8000)
    parser.add_argument('--staticdir', type = str, default="../frontend/dist")
    return parser



def calc_boxes_size(self,width,height,max_area):
    class BoxesCalc(http.server.SimpleHTTPRequestHandler):
        def __init__(self,*args,**kwargs):
            kwargs['directory'] = opts.staticdir
            super().__init__(*args,**kwargs)
    """Returns an array of tuples, describing 
    a list of boxes which will  will tile the widt xheigth
    request, each with an area  less than max_area

    Each tuple is start_col,tile_width,start_row,tile_height
    """
    max_area = 12
    width = [(2.5),(2.5),(2.5),(2.5)] 
    height = [(4.5),(4.5),(4.5),(4.5)]
    Numberofboxes = len(width + height)
    SumWidth = sum(width)
    SumHeight = sum(height)
    U_Width = sum(width)/ max_area
    U_Height = sum(height)/ max_area
    WHsum = SumWidth + SumHeight
    boxUnit = max_area - WHsum
    results = [(0, width),( 0, height)]
    print ('SUM(box_widths) =',SumWidth)
    print ('SUM(box_heights) =',SumHeight)
    print ('box_widths =',U_Width)
    print ('box_heights =',U_Height)
    print ('Combined sum =',SumWidth + SumHeight)
    print ('Number of boxes =',Numberofboxes)
    print ('Max_Area is:',max_area)
    print ('boxUnitis:',boxUnit)
    print ('results:',results)

    # FIXME Actually verify max area, and
    # try to minimize sum(widths) + sum(heights)
    return [(0, width),( 0, height)]
    return calc_boxes_size



def boxescalc(opts):
    class BoxesCalc(http.server.SimpleHTTPRequestHandler):
        def __init__(self,*args,**kwargs):
            kwargs['directory'] = opts.staticdir
            super().__init__(*args,**kwargs)

        def do_GET(self,*args):
            print(self.path,args)
            if self.path.startswith("/calculate/"):
                #self.send_error(404,"Implementation required")
                self.calc_boxes_size(self,5,5,12)
            else:
                super().do_GET(*args)


    return BoxesCalc

def main(opts):
    listen_to = ('',opts.port)
    s = http.server.HTTPServer(listen_to, boxescalc(opts),calc_boxes_size(5,5,5,12))
    print("serving at port", opts.port)
    webbrowser.open('http://localhost:8000/')
    s.serve_forever()
    get_parser()

if __name__ == "__main__":
    p = get_parser()
    opts = p.parse_args()
    main(opts)
