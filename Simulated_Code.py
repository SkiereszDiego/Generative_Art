w, h = 1000, 1000

#especifica o quanto longo tu quer a sequencia de linhas
code_start = h/20
code_end = h -h/20
#separação entre as linhas
lines_of_code = 30  
line_sep = (code_end - code_start)/lines_of_code

#São as configurações do canvas, onde vai serlido apenas uma vez
def setup():
    size(w, h)
    background(30, 30, 30) #Um pouco mais escuro que o preto

#Basic Line
    strokeWeight(12)#seria a espessura da linha
    strokeCap(ROUND)
    stroke(0, 255, 255)
    
    '''
    caso queira fazer um teste
    #Especificar onde começa a linha
    line(200, 500, 800, 500) #(x,y height, width)
    '''
    '''
    line_y começa a linha incrementando a espessura da linha para desenhar, porem cada linha
     irá ter um numero aleatorio de segmentos e cada segmento ira ter um comprimento aleatorio.
    '''
    line_y = code_start
    line_x = 50
    indent = 0
    stroke(random(60, 200), random(60,200), random(60, 200))
    for i in range(lines_of_code):
        #esse if gera quebra de linhas
        if (not(random(1) < .2 and indent is 0)):
        
            line_x = 50 +(indent * 50) #reinicia a posição da linha no eixo X
            line_segments = random(2, 8) # ele gera um valor em float
            
            '''
            #criando cores aleatorias para cada linha
                stroke(random(60, 200), random(60,200), random(60, 200))
            '''
            
            for j in range(int(line_segments)):
                
                if (random(1) < .3):
                #Gera cores aleatorias para cada segmento
                    stroke(random(60, 200), random(60,200), random(60, 200))
                
                segment_length = random(10, 80) #baseado no pixel
                                    
                line(line_x,line_y,line_x + segment_length,line_y)
                #Para não começar sempre no mesmo ponto, depois de desenhar a linha...
                
                line_x += segment_length +20
                
                #depois de escrita a primeira linha, vai gerar uma identação
            
            if (random(1) < .2 and indent < 5):
                indent += 1
            elif (random(1) < .3 and indent > 0):
                indent -= 1
        
        line_y += line_sep
        
