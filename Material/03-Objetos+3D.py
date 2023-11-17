"""
Objetos 3D:
    - Seta (arraow):
seta = arrow(pos=vector(x,y,z)   # posição da base da seta
            axis=vector(x,y,z)   # posição da ponta da seta
            lenght=float         # tamanho da seta
            color=color.(nome da cor)  # cor da seta
            opacity=float        # determina a opacidade do objeto (0->1)
            shiness=float        # brilho do objeto
            emissive=True/False  # Emissão de luz pelo objeto
            texture=textures.(nome da textura) # Coloca textura no objeto
            make_trail=True/False  # Rastro do objeto
            )

    - Caixa (box):
caixa = box(pos=vector(x,y,z)
            size=vector(lenght, height, width)  # Podemos alterar cada um dos lados da caixa com esta função
            color=color.(nome da cor)
            opacity=float
            shiness=float
            emissive=True/False
            texture=textures.(nome da textura)
            make_trail=True/False
            )

    - Cone (cone):
cone = cone(pos=vector(x,y,z)
            axis=vector(a,b,c)  # Determina a posição da ponta do cone
            radius=float    # valor do raio da base do cone
            lenght=float    # tamanho do objeto
            color=color.(nome da cor)
            opacity=float
            shiness=float
            emissive=True/False
            texture=textures.(nome da textura)
            make_trail=True/False
            )

    - Piramide (pyramid):
piramide = pyramid(pos=vector(x,y,z)
            axis=vector(a,b,c)  # Determina a posição da ponta do cone
            size=vector(lenght, height, width)
            radius=float    # valor do raio da base do cone
            lenght=float    # tamanho do objeto
            color=color.(nome da cor)
            opacity=float
            shiness=float
            emissive=True/False
            texture=textures.(nome da textura)
            make_trail=True/False
            )

    - Cilindro (cylinder):
cilindro = cylinder(pos=vector(x,y,z)   # Posição do começo do cilindro
                    axis=vector(a,b,c)  # Posição da ponta do cilindro
                    radius=float  # Valor do raio do cilindro
                    size=vector(lenght, height, width)
                    color=color.(nome da cor)
                    opacity=float
                    shiness=float
                    emissive=True/False
                    texture=textures.(nome da textura)
                    make_trail=True/False
                    )

    - Elipsoide (ellipsoid):
elipsoide = ellipsoid(pos=vector(x,y,z)  # posição do centro do elipsoide
                    axis=vector(a,b,c)   # tamanho do elipsoide
                    radius=float  # Valor do raio do elipsoide
                    size=vector(lenght, height, width)
                    color=color.(nome da cor)
                    opacity=float
                    shiness=float
                    emissive=True/False
                    texture=textures.(nome da textura)
                    make_trail=True/False
                    )

    - Esfera (sphere):
esfera = sphere(pos=vector(x,y,z)  # posição do centro da esfera
                    radius=float  # Valor do raio da esfera
                    color=color.(nome da cor)
                    opacity=float
                    shiness=float
                    emissive=True/False
                    texture=textures.(nome da textura)
                    make_trail=True/False
                    )

    - Anel (ring):
anel = ring(pos=vector(x,y,z)  # posição do centro do anel
                    axis=vector(a,b,c)   # para onde o anel aponta
                    radius=float  # Valor do raio do anel
                    thickness=float  # espessura do anel
                    color=color.(nome da cor)
                    opacity=float
                    shiness=float
                    emissive=True/False
                    texture=textures.(nome da textura)
                    make_trail=True/False
                    )

    - Hélice (helix):
helice = helix(pos=vector(x,y,z)  # posição do inicio da helice
                    axis=vector(a,b,c)   # posição da ponta da helice
                    radius=float  # Valor do raio da helice
                    thickness=float  # espessura da hélice
                    coils=int  # o número de voltas da hélice
                    color=color.(nome da cor)
                    opacity=float
                    shiness=float
                    emissive=True/False
                    texture=textures.(nome da textura)
                    make_trail=True/False




"""