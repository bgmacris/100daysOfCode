import requests
import os


PATH = os.path.join(os.getcwd(), 'images/')

images_url = [
	'https://pack-yak.intomanga.com/images/manga/One-Piece/chapter/1022/page/2/10185215-1b00-4094-be1e-9e8febb90d40',
	'https://pack-yak.intomanga.com/images/manga/One-Piece/chapter/1022/page/3/ae4e051e-03c9-449d-9245-20ba6223cc4c',
	'https://pack-yak.intomanga.com/images/manga/One-Piece/chapter/1022/page/4/bf9efe3c-5c45-4157-a2df-88c837c38057',
	'https://pack-yak.intomanga.com/images/manga/One-Piece/chapter/1022/page/5/61d28be3-1981-41d7-9f7d-bfd23e571258',
	'https://pack-yak.intomanga.com/images/manga/One-Piece/chapter/1022/page/6/dcb5e63e-9709-465f-ab5e-452252a9a583',
	'https://pack-yak.intomanga.com/images/manga/One-Piece/chapter/1022/page/7/89e1617f-937b-4267-8398-b25a193e8379',
	'https://pack-yak.intomanga.com/images/manga/One-Piece/chapter/1022/page/8/650cf377-52c4-49b4-a1f9-9c33d0c103da',
	'https://pack-yak.intomanga.com/images/manga/One-Piece/chapter/1022/page/9/4cac4eed-dc21-45f6-a2d4-dbb3b0b5ef2c',
	'https://pack-yak.intomanga.com/images/manga/One-Piece/chapter/1022/page/9/4cac4eed-dc21-45f6-a2d4-dbb3b0b5ef2c',
	'https://pack-yak.intomanga.com/images/manga/One-Piece/chapter/1022/page/11/0eacdbf7-80b2-4f76-bdc2-cef04263a3f9',
	'https://pack-yak.intomanga.com/images/manga/One-Piece/chapter/1022/page/12/677bc6c8-fe11-40e7-8ed3-e1c96c81d32e',
	'https://pack-yak.intomanga.com/images/manga/One-Piece/chapter/1022/page/13/8c842ecf-90ca-419d-bec6-70ae57215eff',
	'https://pack-yak.intomanga.com/images/manga/One-Piece/chapter/1022/page/14/5907976c-3690-4a4b-9368-8e4f8ffe2e2f',
	'https://pack-yak.intomanga.com/images/manga/One-Piece/chapter/1022/page/15/226abb7d-caa0-4f68-9676-89ad45b857cd',
	'https://pack-yak.intomanga.com/images/manga/One-Piece/chapter/1022/page/16/d7845cc1-899e-4adf-aac1-8d242bd99c87',
	'https://pack-yak.intomanga.com/images/manga/One-Piece/chapter/1022/page/17/393c49d8-04bd-4c7d-8275-f3609cc3eda2',
]

num = 0
for url in images_url:
	r = requests.get(url, stream=True)
	r.raw.decode_content = True

	with open(f'{PATH}img{num}.jpg', 'wb') as img:
		for data in r.raw:
			img.write(data)
	num = num + 1
