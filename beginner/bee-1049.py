# https://www.beecrowd.com.br/judge/pt/problems/view/1049
keyword1 = str(input())
keyword2 = str(input())
keyword3 = str(input())

vertebrado = {
    "ave": {"carnivoro": "aguia", "onivoro": "pomba"},
    "mamifero": {"onivoro": "homem", "herbivoro": "vaca"}
}

invertebrado = {
    "inseto": {"hematofago": "pulga", "herbivoro": "lagarta"},
    "anelideo": {"hematofago": "sanguessuga", "onivoro": "minhoca"}
}

if(keyword1 == 'vertebrado'):
    for key in vertebrado.keys():
        if(key == keyword2):
            if(keyword3 in vertebrado[key]):
                print(vertebrado[key][keyword3])
                
elif(keyword1 == 'invertebrado'):
    for key in invertebrado.keys():
        if(key == keyword2):
            if(keyword3 in invertebrado[key]):
                print(invertebrado[key][keyword3])