from PIL import Image, ImageDraw, ImageFont

def antirobo(path,fontPath,texto,fSize=100):
    
    img = Image.open(path).convert("RGBA")

    with img as base:
        h = base.size[0]
        v = base.size[1]
        txt = Image.new("RGBA", (h*2,v*2), (255,255,255,0))
        fnt = ImageFont.truetype(fontPath,fSize)
        draw = ImageDraw.Draw(txt)
        
        
        for i in range(int(h/100)):
            for j in range(int(v/100)):
                draw.text((10+i*600,10+j*250),texto, font=fnt ,fill=(0,0,0,40))
       
        txt = txt.rotate(10).crop((h/1.5,v/10,h+h/1.5,v+v/10))
        
        out = Image.alpha_composite(base,txt)
        return out
        
    
def wmark(path,markpath, alfa=0.7):

    mark = Image.open(markpath).convert("RGBA")
    
    img = Image.open(path).convert("RGBA")

    canal_alfa = mark.split()[3]

   
    canal_alfa = canal_alfa.point(lambda i: int(i * alfa))

   
    nmark = Image.merge('RGBA', mark.split()[:3] + (canal_alfa,))

    img.alpha_composite(nmark, (int(img.size[0]/2 - nmark.size[0]/2),img.size[1]-nmark.size[1]))
    return img
    
    

