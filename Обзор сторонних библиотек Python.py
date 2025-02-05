from pprint import pprint

from PIL import Image
import requests

Image.effect_mandelbrot((512, 512), (-3, -2.5, 2, 2.5), 100).show()


with Image.open("pic1.png") as im:
    rotate = im.rotate(45)
    rotate.show()
    rotate.save("pic2.png")

with Image.open("pic1.png") as im:
    im = im.convert("L")
    im.show()


r = requests.get('https://id.vk.com/auth?scheme=space_gray&action=eyJuYW1lIjoibXVsdGlfYWNjb3VudF9mbG93IiwicGFyYW1zIjp7ImZsb3dfbmFtZSI6ImFkZF90b19zd2l0Y2hlciIsInVzZXJfaWQiOjMyNTQ3MjYxOH19&uuid=gyvqwa&response_type=silent_token&v=1.3.0&app_id=7913379&redirect_uri=https%3A%2F%2Fvk.com%2F%3Fto%3DL2ZlZWQ-')

print(r.url)
print(r.status_code)
print(r.history)
r1 = requests.get('https://vk.com/')
pprint(r1.content)